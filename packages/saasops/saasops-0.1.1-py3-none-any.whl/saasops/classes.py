from enum import Enum
import pandas as pd
import warnings
from rich.console import Console


class MessageStyle(Enum):
    """
    Enum class to define the message styles for the logger

    Attributes:
    -----------
    INFO : str
        Blue color for information messages
    SUCCESS : str
        Green color for success messages
    ERROR : str
        Red color for error messages
    """

    INFO = "blue"
    SUCCESS = "green"
    ERROR = "red"


class Customer:
    """
    Class to store customer data from the customer table in the database.
    """

    def __init__(self, customer_id, name, city, state):
        self.customer_id = customer_id
        self.name = name
        self.city = city
        self.state = state


class Contract:
    """
    Class to store contract data from the contract table in the database.
    """

    # Initialize the rules list as a class variable
    rules = []

    def __init__(
        self,
        contract_id,
        customer_id,
        renewal_from_contract_id,
        merges_to_contract_id,
        reference,
        contract_date,
        term_start_date,
        term_end_date,
        total_value,
        console=None,
    ):
        self.contract_id = contract_id
        self.customer_id = customer_id
        self.renewal_from_contract_id = renewal_from_contract_id
        self.merges_to_contract_id = merges_to_contract_id
        self.reference = reference
        self.contract_date = contract_date
        self.term_start_date = term_start_date
        self.term_end_date = term_end_date
        self.total_value = total_value
        self.segments = []
        self.console = console if console else Console()

    @classmethod
    def add_rule(cls, rule):
        """
        Add a new validation rule to the contract class.

        Parameters:
        -----------
        rule : function
            A function that takes a Contract object and checks for a specific condition.
        """
        cls.rules.append(rule)

    def check_consistency(self):
        """
        Check the consistency of the contract (inc segment) data according to the set rules.

        Returns:
        --------
        None
        """
        for rule_index, rule in enumerate(self.rules):
            rule(self)


def contract_value_matches_aggregate_segment_value(contract):
    """
    Rule to check if the sum of segment values matches the total value of the contract.

    Parameters:
    -----------
    contract : Contract
        The contract instance to validate.

    Returns:
    --------
    None

    """

    # Adjust to use dictionary key access
    total_segments_value = sum(segment['segment_value'] for segment in contract.segments)
    if total_segments_value != contract.total_value:
        contract.console.print(
            f"ERROR: Total value of segments does not match contract value for contract ID {contract.contract_id}",
            style="bold red",
        )

class SegmentData:
    """
    Class to store native data for a segment. The combined data is sourced from the segment, contract and customer tables in the database.
    """

    # Initialize the rules list as a class variable
    rules = []

    def __init__(
        self,
        customer_id,
        customer_name,
        contract_id,
        segment_id,
        contract_date,
        renewal_from_contract_id,
        merges_to_contract_id,
        segment_start_date,
        segment_end_date,
        arr_override_start_date,
        arr_override_note,
        title,
        type,
        segment_value,
        console=None,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.contract_id = contract_id
        self.segment_id = segment_id
        self.contract_date = contract_date
        self.renewal_from_contract_id = renewal_from_contract_id
        self.merges_to_contract_id = merges_to_contract_id
        self.segment_start_date = segment_start_date
        self.segment_end_date = segment_end_date
        self.arr_override_start_date = arr_override_start_date
        self.arr_override_note = arr_override_note
        self.title = title
        self.type = type
        self.segment_value = segment_value
        self.console = console if console else Console()

    @classmethod
    def add_rule(cls, rule):
        """
        Add a new rule to the set of rules.

        Parameters:
        -----------
        rule : function
            A function that takes a SegmentData object and checks for consistency.
        """
        cls.rules.append(rule)

    def check_consistency(self):
        """
        Check the consistency of the segment data according to the set rules.

        Returns:
        --------
        None
        """
        for rule_index, rule in enumerate(self.rules):
            rule(self)


# TODO: Add further segment data consistency checks


def valid_segment_start_end_dates(segment_data):
    """
    Rule function to check if segment start date is later than segment end date .
    """
    if segment_data.segment_start_date > segment_data.segment_end_date:
        segment_data.console.print(
            f"ERROR: Segment start date later than segment end date in segment ID {segment_data.segment_id}",
            style="bold red",
        )


def valid_segment_length(segment_data):
    """
    Rule function to check if segment length is near a round number of months.
    """
    contract_length_months = (
        segment_data.segment_end_date - segment_data.segment_start_date
    ).days / 30.42

    diff_to_month = abs(contract_length_months - round(contract_length_months))

    if (diff_to_month) > 0.05:
        segment_data.console.print(
            f"ISSUE: Segment length diverges from near-number-of-months -- difference {round(diff_to_month,3)} -- in segment ID {segment_data.segment_id}",
            style="bold yellow",
        )


def valid_arr_override_date(segment_data):
    """
    Rule function to check if ARR override date is between the contract date and segment start date.
    """
    if segment_data.arr_override_start_date:
        if not (
            segment_data.contract_date
            <= segment_data.arr_override_start_date
            <= segment_data.segment_start_date
        ):
            segment_data.console.print(
                f"ISSUE: ARR override date outside of contract date and segment start date in segment ID {segment_data.segment_id}",
                style="bold yellow",
            )


class SegmentContext:
    """
    Class to manage the context for ARR calculations for a segment. The context items are additional data derived from the native data in the SegmentData class.

    Attributes:
    -----------
    segment_data : SegmentData
        Data for the segment
    arr_start_date : datetime
        ARR start date for the segment
    arr_end_date : datetime
        ARR end date for the segment
    arr : float
        Calculated ARR for the segment
    length_variance_alert : bool
        Flag to indicate if there is a length variance alert

    Methods:
    --------
    calculate_arr()
        Calculate ARR for the segment
    """

    def __init__(self, segment_data):
        self.segment_data = segment_data
        self.contract_length_months = None
        self.arr_start_date = None
        self.arr_end_date = None
        self.arr = None
        self.length_variance_alert = False

    def calculate_arr(self):
        """
        Calculate ARR for the segment based on the segment type

        The method uses decision tables to determine the ARR start date and calculate ARR

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        """
        # Only proceed if segment type is 'Subscription'
        if self.segment_data.type == "Subscription":
            arr_start_decision_table = ARRStartDateDecisionTable()
            arr_calculation_table = ARRCalculationDecisionTable()

            arr_start_decision_table.add_rule(has_arr_override, set_arr_to_override)
            arr_start_decision_table.add_rule(
                booked_before_segment_start, set_arr_to_booked_date
            )
            arr_start_decision_table.add_rule(
                segment_start_before_booked, set_arr_to_segment_start
            )

            evaluated_date = arr_start_decision_table.evaluate(self)
            if evaluated_date:
                self.arr_start_date = evaluated_date

            # Set the ARR end date to the segment end date for time being
            self.arr_end_date = self.segment_data.segment_end_date

            arr_calculation_table.evaluate(self)

        else:
            # If not a 'Subscription' type, set ARR to None or 0 as appropriate
            # TODO: Do we need to set any of the other data items given the non-subscription data type?
            self.arr = (
                0  # Or None, depending on how you want to handle non-subscription types
            )


class ARRStartDateDecisionTable:
    """
    Decision table to determine the ARR start date based on segment context

    Attributes:
    -----------
    rules : list
        List of rules containing conditions and actions
    """

    def __init__(self):
        self.rules = []

    def add_rule(self, condition, action):
        """
        Add a new rule to the decision table
        """
        self.rules.append((condition, action))

    def evaluate(self, segment_context):
        """
        Evaluate the decision table based on the segment context
        """
        for condition, action in self.rules:
            if condition(segment_context):
                return action(segment_context)


# Condition functions


def has_arr_override(segment_context):
    return segment_context.segment_data.arr_override_start_date is not None


def booked_before_segment_start(segment_context):
    return (
        segment_context.segment_data.contract_date
        < segment_context.segment_data.segment_start_date
    )


def segment_start_before_booked(segment_context):
    return (
        segment_context.segment_data.segment_start_date
        <= segment_context.segment_data.contract_date
    )


def is_contract_renewal_and_dates_mismatch(segment_context):
    # Check if the contract is a renewal and the date condition is met
    renewing_contract = ...  # Logic to get the renewing contract details
    if (
        renewing_contract
        and (renewing_contract.term_start_date - segment_context.arr_end_date).days > 1
    ):
        return True
    return False


# Action functions


def set_arr_to_override(segment_context):
    return segment_context.segment_data.arr_override_start_date


def set_arr_to_booked_date(segment_context):
    return segment_context.segment_data.contract_date


def set_arr_to_segment_start(segment_context):
    return segment_context.segment_data.segment_start_date


class ARRCalculationDecisionTable:
    """
    Decision table to calculate ARR based on segment context

    Attributes:
    -----------
    None

    Methods:
    --------
    evaluate(segment_context)
        Evaluate the decision table based on the segment context

    """

    def __init__(self):
        pass

    def evaluate(self, segment_context):
        """
        Evaluate the decision table based on the segment context

        Parameters:
        -----------
        segment_context : SegmentContext
            Context for ARR calculation for the segment

        Returns:
        --------
        None
        """
        if segment_context.arr_start_date is not None:
            # Corrected to use segment_data
            segment_context.contract_length_months = round(
                (
                    segment_context.segment_data.segment_end_date
                    - segment_context.segment_data.segment_start_date
                ).days
                / 30.42
            )

            if segment_context.contract_length_months > 0:
                segment_context.arr = (
                    segment_context.segment_data.segment_value
                    / segment_context.contract_length_months
                ) * 12
                segment_context.length_variance_alert = (
                    segment_context.contract_length_months % 1
                ) > 0.2
            else:
                segment_context.arr = 0
                segment_context.length_variance_alert = False

        segment_context.arr_end_date = segment_context.segment_data.segment_end_date


class ARRMetricsCalculator:
    """
    Class to calculate ARR changes for a given period

    Attributes:
    -----------
    arr_table : ARRTable
        ARR data for segments
    start_period : datetime
        Start date of the period
    end_period : datetime
        End date of the period
    metrics : dict
        Dictionary to store the calculated metrics

    Methods:
    --------
    calculate_arr_changes(carry_forward_churn=None)
        Calculate ARR changes for the period
    reset_metrics()
        Reset the metrics to zero
    """

    def __init__(self, arr_table, start_period, end_period):
        self.arr_table = arr_table
        self.start_period = start_period
        self.end_period = end_period
        self.metrics = {"New": 0, "Expansion": 0, "Contraction": 0, "Churn": 0}
        self.metrics_dfs = {"New": pd.DataFrame(), "Expansion": pd.DataFrame(), "Contraction": pd.DataFrame(), "Churn": pd.DataFrame()}

    def calculate_arr_changes(self, carry_forward_churn=None):
        """
        Calculate ARR changes for the period

        Parameters:
        -----------
        carry_forward_churn : list
            List of contract IDs to carry forward churn calculation

        Returns:
        --------
        list
            List of contract IDs to carry forward churn calculation for the next period
        """

        # TODO: Needs updated once merged contracts are implemented, to correctly assign ARR changes to Expansion/Contraction etc.

        # Initialize carry_forward_churn if not provided
        if carry_forward_churn is None:
            carry_forward_churn = []

        # Filter data for the current period
        df = self.arr_table.data
        period_data = df[
            (df["ARRStartDate"] <= self.end_period)
            & (df["ARREndDate"] >= self.start_period)
        ]

        # Additionally, consider contracts from the carry_forward_churn list
        for contract_id in carry_forward_churn:
            contract_data = df[df["ContractID"] == contract_id]
            period_data = pd.concat([period_data, contract_data])

        next_period_carry_forward = []

        # print(f"Calculating ARR changes for {len(period_data)} contracts")
        # print(f"Period start: {self.start_period}, Period end: {self.end_period}")
        # print(period_data[['ContractID', 'ARRStartDate', 'ARREndDate', 'ARR', 'RenewalFromContractID']])

        # So now we have the list of contracts that were active during the period
        # In the sequence, the tests are:
        # If a contract has an ARRStart Date in the period and is not a renewal, it is a new contract
        # If a contract has an ARRStartDate in the period and is a renewal, then:
        # If the ARR is higher than the previous ARR, it is an expansion
        # If the ARR is lower than the previous ARR, it is a contraction
        # If a contract has an ARREndDate in the period, and there is no renewal, it is churn

        for index, row in period_data.iterrows():
            # Handle new and renewal contracts
            if row["ARRStartDate"] >= self.start_period:
                if not row["RenewalFromContractID"]:
                    self.metrics["New"] += row["ARR"]
                    self.metrics_dfs["New"] = pd.concat([self.metrics_dfs["New"], pd.DataFrame([row])], ignore_index=True)
                else:
                    renewed_contract_id = row["RenewalFromContractID"]
                    renewed_contract = df[df["ContractID"] == renewed_contract_id]
                    # TODO: Should throw a warning here if >1 renewal contracts i.e. rows in this df
                    if not renewed_contract.empty:
                        prior_arr = renewed_contract.iloc[0]["ARR"]
                        if row["ARR"] > prior_arr:
                            self.metrics["Expansion"] += row["ARR"] - prior_arr
                            self.metrics_dfs["Expansion"] = pd.concat([self.metrics_dfs["Expansion"], pd.DataFrame([row])], ignore_index=True)
                        elif row["ARR"] < prior_arr:
                            self.metrics["Contraction"] += prior_arr - row["ARR"]
                            self.metrics_dfs["Contraction"] = pd.concat([self.metrics_dfs["Contraction"], pd.DataFrame([row])], ignore_index=True)

            # Adjusted churn condition to accurately account for renewals
            if row["ARREndDate"] <= self.end_period:
                if row["ContractID"] in carry_forward_churn:
                    # Process previously identified potential churn
                    self.metrics["Churn"] += row["ARR"]
                    self.metrics_dfs["Churn"] = pd.concat([self.metrics_dfs["Churn"], pd.DataFrame([row])], ignore_index=True)
                    carry_forward_churn.remove(row["ContractID"])
                else:
                    # Check for renewals before marking as churn
                    next_contract_start = df[
                        df["RenewalFromContractID"] == row["ContractID"]
                    ]["ARRStartDate"].min()
                    if pd.isnull(next_contract_start) or next_contract_start > row[
                        "ARREndDate"
                    ] + pd.Timedelta(days=1):
                        if row["ARREndDate"] == self.end_period:
                            # Potential churn carried forward if ending on the last day without immediate renewal
                            next_period_carry_forward.append(row["ContractID"])
                        else:
                            # Mark as churn if no immediate renewal and not carried forward
                            self.metrics["Churn"] += row["ARR"]
                            self.metrics_dfs["Churn"] = pd.concat([self.metrics_dfs["Churn"], pd.DataFrame([row])], ignore_index=True)

        # Return the list of contracts to carry forward for churn calculation in the next period
        return next_period_carry_forward

    def reset_metrics(self):
        """
        Reset the metrics to zero
        """
        self.metrics = {key: 0 for key in self.metrics}
        self.metrics_dfs = {key: pd.DataFrame() for key in self.metrics_dfs}


class ARRTable:
    """
    Class to manage ARR data for segments

    Attributes:
    -----------

    data : pd.DataFrame
        DataFrame to store ARR data for segments

    Methods:
    --------

    add_row(segment_data, context)
        Add a new row to the ARR data DataFrame

    update_renewed_segment_arr_end_date(segment_id, new_arr_end_date)
        Update the ARR end date for a renewed segment

    update_for_renewal_contracts()
        Update the ARR end date for segments that are renewed
    """

    def __init__(self):
        # Define the dtypes for your DataFrame columns
        dtypes = {
            "SegmentID": "object",
            "ContractID": "object",
            "RenewalFromContractID": "object",
            "MergesToContractID": "object",
            "CustomerName": "object",
            "ARRStartDate": "datetime64[ns]",
            "ARREndDate": "datetime64[ns]",
            "ARR": "float",
        }
        # Initialize self.data as an empty DataFrame with these dtypes
        self.data = pd.DataFrame(
            {col: pd.Series(dtype=typ) for col, typ in dtypes.items()}
        )

    def add_row(self, segment_data, context):
        new_row = {
            "SegmentID": segment_data.segment_id,
            "ContractID": segment_data.contract_id,
            "RenewalFromContractID": segment_data.renewal_from_contract_id,
            "MergesToContractID": segment_data.merges_to_contract_id,
            "CustomerName": segment_data.customer_name,
            "ARRStartDate": pd.to_datetime(context.arr_start_date),
            "ARREndDate": pd.to_datetime(context.arr_end_date),
            "ARR": context.arr,
        }
        # Convert new_row dict to DataFrame with a single row, aligning with self.data's columns
        new_row_df = pd.DataFrame([new_row], columns=self.data.columns)

        # Suppress FutureWarning for DataFrame concatenation
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=FutureWarning)
            self.data = pd.concat([self.data, new_row_df], ignore_index=True)

    def update_renewed_segment_arr_end_date(self, segment_id, new_arr_end_date):
        self.data.loc[self.data["SegmentID"] == segment_id, "ARREndDate"] = (
            pd.to_datetime(new_arr_end_date)
        )

    # TODO: Add in a update_for_merged_contracts method to handle contract merges
    # Think it's the same principle as below, with ARR end date of merged contracts brought forward to match ARR start date of merging contract
    # So there's no duplication of ARR reported at the end of a given period
    # And then the ARR change function can report on the changes in the period

    def update_for_renewal_contracts(self):
        '''
        Update the ARR end date for segments that are renewed
        '''
        # Iterate over each row in the DataFrame
        for index, row in self.data.iterrows():
            if row["RenewalFromContractID"]:
                renewing_segment_id = row["SegmentID"]
                # Find the corresponding row for the renewal
                renewing_rows = self.data[self.data["SegmentID"] == renewing_segment_id]
                # print("Renewing rows")
                # print(renewing_rows)
                if not renewing_rows.empty:
                    renewing_arr_start_date = renewing_rows.iloc[0]["ARRStartDate"]
                    # Find the corresponding renewed contract's end date
                    renewed_rows = self.data[
                        self.data["ContractID"] == row["RenewalFromContractID"]
                    ]
                    if not renewed_rows.empty:
                        renewed_arr_end_date = renewed_rows.iloc[0]["ARREndDate"]
                        if (renewing_arr_start_date - renewed_arr_end_date).days > 1:
                            new_arr_end_date = renewing_arr_start_date - pd.Timedelta(
                                days=1
                            )
                            # TODO: Should have some warning message here if setting a new ARR end date to be more than say 30 days than previous
                            # Now fix the ARR end date for the renewed segment
                            # Use the RenewalFromContractID to find the segments (with that contract ID) for which to update ARR End Date
                            self.data.loc[
                                self.data["ContractID"] == row["RenewalFromContractID"],
                                "ARREndDate",
                            ] = new_arr_end_date


    def update_for_merged_contracts(self):
        '''
        Update the ARR end date for segments that are merged
        '''
        # Iterate over each row in the DataFrame
        for index, row in self.data.iterrows():
            if row["MergesToContractID"]:
                # If here, then the contract is merged to another contract
                merged_segment_id = row["SegmentID"]
                
                # This is the contract being merged to another contract
                merging_rows = self.data[self.data["SegmentID"] == merged_segment_id]
                
                if not merging_rows.empty:
                    # if that dataframe is not empty, then find the corresponding contract to which that one is merged
                    merged_rows = self.data[
                        self.data["ContractID"] == row["MergesToContractID"]
                    ]

                    # Not needed?
                    # merging_arr_end_date = merging_rows.iloc[0]["ARREndDate"]

                    if not merged_rows.empty:
                        # and if that dataframe is not empty, find its ARR Start date
                        # and then update the ARR End Date for the merged segment

                        merged_arr_start_date = merged_rows.iloc[0]["ARRStartDate"]
                        
                        # TODO: Need some kind of warning if setting the date to be later than previous (and maybe with >30 days or something)
                        # Now we just set the ARR End Date for the merged segment to be the day before the ARR Start Date of the merging segment
                        new_arr_end_date = merged_arr_start_date - pd.Timedelta(days=1)

                        self.data.loc[
                            self.data["SegmentID"] == merged_segment_id,
                            "ARREndDate",
                        ] = new_arr_end_date
                        
                        
                        
                        

    def print_table(self):
        print(self.data)
