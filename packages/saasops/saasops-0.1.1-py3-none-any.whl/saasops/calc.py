from saasops.classes import SegmentData, SegmentContext, ARRMetricsCalculator, ARRTable
from datetime import date, timedelta, datetime
import pandas as pd


# ARR Calculation Functions


def customer_arr_tbl(
    date, con, customer=None, contract=None, ignore_zeros=False, tree_detail=False
):
    """
    Returns a DataFrame with the ARR for each customer at the specified date.

    Args:
        date (str or date): The date for which to calculate ARR.
        con: The database connection object.
        customer (str): The customer ID to filter by.
        contract (str): The contract ID to filter by.
        ignore_zeros (bool): If True, exclude customers with zero ARR.
        tree_detail (bool): If True, include detailed tree structure in the output.

    Returns:
        DataFrame: A DataFrame with the ARR for each customer at the specified date.
    """
    # Convert the date to a pandas Timestamp
    date_as_timestamp = pd.to_datetime(date)

    # Build the ARR table instance (which now uses a DataFrame)
    arr_table = build_arr_table(con, customer=customer, contract=contract)
    # arr_table.print_table()

    # print(f"ARR Table: {arr_table.data.shape[0]} rows")
    # print(f"ARR Table Columns: {arr_table.data.columns}")
    # print(f"ARR Table Data Types: {arr_table.data.dtypes}")
    # print(f"ARR Table Data: {arr_table.data}")

    # COmmenting out the following code as suspect not needed...

    active_segments = arr_table.data[
        (arr_table.data["ARRStartDate"] <= date_as_timestamp)
        & (arr_table.data["ARREndDate"] >= date_as_timestamp)
    ]
    # print(active_segments)

    # has_renewal = active_segments["ContractID"].isin(
    #     active_segments["RenewalFromContractID"].dropna()
    # )
    # active_segments = active_segments[~has_renewal]
 
    # # need to filter active segments to exclude segments that are part of a merge
    # # build True/False based on a given contract having MergesToContractID set (not the merged-to contract ID)
    # is_merged = active_segments["MergesToContractID"].notna()
    # # filter out segments that are merged
    # active_segments = active_segments[~is_merged]

    # Sum ARR per customer
    df = active_segments.groupby("CustomerName")["ARR"].sum().reset_index()
    df.rename(columns={"ARR": "TotalARR"}, inplace=True)
    df.set_index("CustomerName", inplace=True)

    if ignore_zeros:
        df = df[df["TotalARR"] != 0]

    # Add a total ARR sum as last row
    df.loc["Total"] = df.sum()

    return df


def customer_arr_df(start_date, end_date, con, timeframe="M", ignore_zeros=True):
    """
    Returns a DataFrame with the ARR for each customer in each period between start_date and end_date.

    Args:
        start_date (str or date): The start date for the period.
        end_date (str or date): The end date for the period.
        con: The database connection object.
        timeframe (str): The timeframe for grouping the data ('M' for month, 'Q' for quarter).
        ignore_zeros (bool): If True, exclude customers with zero ARR.

    Returns:
        DataFrame: A DataFrame with the ARR for each customer in each period between start_date and end_date.
    """
    final_df = pd.DataFrame()

    current_date = start_date
    while current_date <= end_date:
        period_start, period_end = calculate_timeframe(current_date, timeframe)
        period_end_timestamp = pd.to_datetime(period_end.strftime("%Y-%m-%d"))

        # Build temp table in database of ARR data
        arr_table = build_arr_table(con)
        # print(f"ARR Table: {arr_table.data.shape[0]} rows")
        # print(f"ARR Table Data: {arr_table.data}")

        # Filter active segments for the period
        if not arr_table.data.empty:
            active_segments = arr_table.data[
                (arr_table.data["ARRStartDate"] <= period_end_timestamp)
                & (arr_table.data["ARREndDate"] >= period_end_timestamp)
            ]
            has_renewal = active_segments["ContractID"].isin(
                active_segments["RenewalFromContractID"].dropna()
            )
            active_segments = active_segments[~has_renewal]

            # print("Period Start:", period_start)
            # print("Period End:", period_end)
            # print(active_segments)

            # Sum ARR per customer for the period
            if not active_segments.empty:
                df = active_segments.groupby("CustomerName")["ARR"].sum().reset_index()
                df.set_index("CustomerName", inplace=True)

                if ignore_zeros:
                    df = df[df["ARR"] != 0]

                # Format column name based on the timeframe
                column_name = format_column_name(period_end, timeframe)
                df.rename(columns={"ARR": column_name}, inplace=True)

                # Join the dataframes
                if final_df.empty:
                    final_df = df
                else:
                    final_df = final_df.join(df, how="outer")

            else:
                # Handle the case where active_segments is empty after filtering
                if final_df.empty:
                    # Initialize final_df with the correct column if it's the first iteration
                    final_df = pd.DataFrame(
                        columns=[format_column_name(period_end, timeframe)]
                    )
                else:
                    # If final_df is not empty but no active segments in this period, ensure the column is added
                    final_df[format_column_name(period_end, timeframe)] = 0

        current_date = (period_end + pd.Timedelta(days=1)).date()

    final_df.fillna(0, inplace=True)  # Replace NaN with 0

    # Add a row that sums ARR per period
    if not final_df.empty:
        final_df.loc["Total ARR"] = final_df.sum()

    return final_df


def new_arr_by_timeframe(date, con, timeframe="M", ignore_zeros=False):
    """
    Returns a DataFrame with the total new ARR for each customer in the specified timeframe.

    Args:
        date (str or date): The date for which to calculate the new ARR.
        con: The database connection object.
        timeframe (str): The timeframe for grouping the data ('M' for month, 'Q' for quarter).
        ignore_zeros (bool): If True, exclude customers with zero ARR.

    Returns:
        DataFrame: A DataFrame with the total new ARR for each customer in the specified timeframe.
    """
    start_date, end_date = calculate_timeframe(date, timeframe)
    start_timestamp = pd.to_datetime(start_date)
    end_timestamp = pd.to_datetime(end_date)

    # Build the ARR table instance (which now uses a DataFrame)
    arr_table = build_arr_table(con)

    # Filter for segments with ARR start date within the specified period
    new_segments = arr_table.data[
        (arr_table.data["ARRStartDate"] >= start_timestamp)
        & (arr_table.data["ARRStartDate"] <= end_timestamp)
    ]

    # Exclude segments that are renewals
    new_segments = new_segments[new_segments["RenewalFromContractID"].isna()]

    # Sum new ARR per customer
    df = new_segments.groupby("CustomerName")["ARR"].sum().reset_index()
    df.rename(columns={"ARR": "TotalNewARR"}, inplace=True)
    df.set_index("CustomerName", inplace=True)

    if ignore_zeros:
        df = df[df["TotalNewARR"] != 0]

    # Add a total ARR sum as last row
    df.loc["Total"] = df.sum()

    return df


def build_arr_change_df(
    start_date, end_date, con, freq="M", format_type=None, customer=None, contract=None, print_metrics=False
):
    arr_table = build_arr_table(con, customer=customer, contract=contract)
    metrics_dfs = {"New": pd.DataFrame(), "Expansion": pd.DataFrame(), "Contraction": pd.DataFrame(), "Churn": pd.DataFrame()}

    periods = generate_periods(start_date, end_date, freq)
    # columns = [f"{start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}" for start, end in periods]
    columns = [format_column_name(start, freq) for start, end in periods]
    df = pd.DataFrame(
        index=[
            "Beginning ARR",
            "New",
            "Expansion",
            "Contraction",
            "Churn",
            "Ending ARR",
        ],
        columns=columns,
    )

    # Calculate previous ending ARR, this will be used as the beginning ARR for the first period
    # Have to calculate this before the loop, because it will be used as the beginning ARR for the first period
    # But it is effectively the execution of the loop but for prior period
    # use the customer_arr_tbl function to calculate the ARR for the previous period
    previous_start, previous_end = periods[0]
    previous_end = previous_start - timedelta(days=1)
    # The customer ARR table has a Total row at the bottom of column TotalARR, so we can use that to get the previous ending ARR
    previous_ending_arr = customer_arr_tbl(
        previous_end, con, customer=customer, contract=contract
    ).loc["Total", "TotalARR"]

    # Set beginning ARR for the first period
    df.at["Beginning ARR", columns[0]] = previous_ending_arr

    carry_forward_churn = []

    for i, (start, end) in enumerate(periods):
        arr_calculator = ARRMetricsCalculator(arr_table, start, end)

        # Set the beginning ARR for the period
        beginning_arr = previous_ending_arr

        carry_forward_churn = arr_calculator.calculate_arr_changes(carry_forward_churn)

        # Calculate the ending ARR for the period, by adding New + Expansion and subtracting Contraction + Churn
        calculated_ending_arr = (
            beginning_arr
            + arr_calculator.metrics["New"]
            + arr_calculator.metrics["Expansion"]
            - arr_calculator.metrics["Contraction"]
            - arr_calculator.metrics["Churn"]
        )

        # Populate the DataFrame for each period
        df.at["Beginning ARR", columns[i]] = beginning_arr
        df.at["New", columns[i]] = arr_calculator.metrics["New"]
        df.at["Expansion", columns[i]] = arr_calculator.metrics["Expansion"]
        df.at["Contraction", columns[i]] = arr_calculator.metrics["Contraction"]
        df.at["Churn", columns[i]] = arr_calculator.metrics["Churn"]
        df.at["Ending ARR", columns[i]] = calculated_ending_arr

        previous_ending_arr = calculated_ending_arr

        # Concat the self.metrics_dfs values to the function metrics_dfs
        for key in metrics_dfs:
            metrics_dfs[key] = pd.concat([metrics_dfs[key], arr_calculator.metrics_dfs[key]], axis=0, ignore_index=True)

        arr_calculator.reset_metrics()

    # If print_metrics is True, print the metrics DataFrames
    # Use print from the Rich library and print as tables
    # Add in a section title line with the key and then skip if the dataframe is empty
    if print_metrics:
        from rich import print

        for key, df_m in metrics_dfs.items():
            if not df_m.empty:
                # print key as a title
                print(f"[bold]Contracts: {key}[/bold]")
                print(df_m)

    return df


def build_arr_table(con, customer=None, contract=None):
    """
    Builds an ARRTable instance from the database.

    Args:
        con: The database connection object.
        customer (str): The customer ID to filter by.
        contract (str): The contract ID to filter by.

    Returns:
        ARRTable: An instance of the ARRTable class containing the ARR data.
    """

    # Retrieve segment data from the database
    query = """
    SELECT cu.CustomerID, cu.Name, s.ContractID, s.SegmentID, c.ContractDate, c.RenewalFromContractID, c.MergesToContractID, 
           s.SegmentStartDate, s.SegmentEndDate, s.ARROverrideStartDate, s.ARROverrideNote,
           s.Title, s.Type, s.SegmentValue
    FROM Segments s
    JOIN Contracts c ON s.ContractID = c.ContractID
    JOIN Customers cu ON c.CustomerID = cu.CustomerID
    """

    # Apply filters within the SQL query if parameters are provided
    conditions = []
    if customer:
        conditions.append(f"cu.CustomerID = '{customer}'")
    if contract:
        conditions.append(f"c.ContractID = '{contract}'")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    result = con.execute(query)
    rows = result.fetchall()

    arr_table = ARRTable()

    for row in rows:
        segment_data = SegmentData(*row)
        context = SegmentContext(segment_data)
        context.calculate_arr()
        arr_table.add_row(segment_data, context)

    # print("ARRTable before updates:")
    # arr_table.print_table()

    arr_table.update_for_renewal_contracts()
    arr_table.update_for_merged_contracts()
    
    # print("ARRTable after updates:")
    # arr_table.print_table()

    return arr_table


def delete_arr_table(con):
    """
    Deletes the ARRTable from the database.
    """

    delete_table_query = "DROP TABLE IF EXISTS ARRTable;"
    con.execute(delete_table_query)
    print("ARRTable deleted.")
    return


# Bookings calculation functions


def customer_bkings_tbl(date, con, timeframe="M", ignore_zeros=True, tree_detail=False):
    # Calculate the start and end dates for the given timeframe
    start_date, end_date = calculate_timeframe(date, timeframe)

    # Query contracts table to get all contracts that were signed in the given timeframe
    query = f"""
    SELECT cu.Name AS CustomerName, SUM(c.TotalValue) AS TotalNewBookings
    FROM Contracts c
    JOIN Customers cu ON c.CustomerID = cu.CustomerID
    WHERE c.ContractDate BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY cu.Name;
    """

    cursor = con.execute(query)
    df = cursor.fetchdf()

    df.set_index("CustomerName", inplace=True)

    if ignore_zeros:
        df = df[df["TotalNewBookings"] != 0]

    return df


def customer_bkings_df(start_date, end_date, con, timeframe="M", ignore_zeros=True):
    # Create an empty DataFrame for the final results
    final_df = pd.DataFrame()

    current_date = start_date
    while current_date <= end_date:
        # Calculate the start and end dates for the current period
        period_start, period_end = calculate_timeframe(current_date, timeframe)

        # Format period_start and period_end as date strings without time components
        # This is necessary for the SQL query with the DuckDB database
        period_start_str = period_start.strftime("%Y-%m-%d")
        period_end_str = period_end.strftime("%Y-%m-%d")

        # Query to get data for the current period
        query = f"""
        SELECT cu.Name AS CustomerName, SUM(c.TotalValue) AS TotalNewBookings
        FROM Contracts c
        JOIN Customers cu ON c.CustomerID = cu.CustomerID
        WHERE c.ContractDate BETWEEN '{period_start_str}' AND '{period_end_str}'
        GROUP BY cu.Name;
        """

        cursor = con.execute(query)
        df = cursor.fetchdf()
        df.set_index("CustomerName", inplace=True)

        print(period_start, period_end)
        print(df)

        if ignore_zeros:
            df = df[df["TotalNewBookings"] != 0]

        # Format column name based on the timeframe
        column_name = format_column_name(period_start, timeframe)
        df.rename(columns={"TotalNewBookings": column_name}, inplace=True)

        final_df = final_df.join(df, how="outer")

        current_date = (period_end + pd.Timedelta(days=1)).date()

    final_df.fillna(0, inplace=True)  # Replace NaN with 0

    return final_df


# Date & text helper functions


def calculate_timeframe(date, timeframe):
    date_datetime = pd.Timestamp(date)

    if timeframe == "M":
        start_date = date_datetime.replace(day=1)
        end_date = start_date + pd.offsets.MonthEnd(1)
    elif timeframe == "Q":
        quarter_mapping = {1: (1, 3), 2: (4, 6), 3: (7, 9), 4: (10, 12)}
        q = (date_datetime.month - 1) // 3 + 1
        start_month, end_month = quarter_mapping[q]
        start_date = date_datetime.replace(month=start_month, day=1)
        end_date = date_datetime.replace(month=end_month).replace(
            day=1
        ) + pd.offsets.MonthEnd(1)
    else:
        raise ValueError(
            "Invalid timeframe. It should be either 'M' for month or 'Q' for quarter"
        )

    return start_date, end_date


def get_timeframe_title(date_input, timeframe):
    """
    Generates a title for the table based on the date and timeframe.

    Args:
        date_input (str or date): The date for which to generate the title.
        timeframe (str): The timeframe ('M' for month, 'Q' for quarter, etc.).

    Returns:
        str: A string representing the title for the table.
    """
    # Check if date_input is a string and convert to date if necessary
    if isinstance(date_input, str):
        date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
    elif isinstance(date_input, date):  # Corrected usage of date type
        date_obj = date_input
    else:
        raise ValueError("Date must be a string or a datetime.date object")

    # Format the date based on the timeframe
    if timeframe == "M":
        return date_obj.strftime("%B %Y")  # e.g., "January 2023"
    elif timeframe == "Q":
        quarter = (date_obj.month - 1) // 3 + 1
        return f"Q{quarter} {date_obj.year}"
    else:
        # Handle other timeframe formats or raise an error for unsupported ones
        raise ValueError("Unsupported timeframe specified")


def format_column_name(period_start, timeframe):
    if timeframe == "M":
        # Monthly: Format as "Jan 2024", "Feb 2024", etc.
        return period_start.strftime("%b %Y")
    elif timeframe == "Q":
        # Quarterly: Format as "Q1 2024", "Q2 2024", etc.
        quarter = (period_start.month - 1) // 3 + 1
        return f"Q{quarter} {period_start.year}"
    else:
        raise ValueError("Invalid timeframe. Use 'M' for monthly or 'Q' for quarterly.")


def generate_periods(start_date, end_date, freq="M"):
    """
    Generate periods between start_date and end_date with given frequency ('M' for months, 'Q' for quarters).
    """
    # Adjust the start date to the first day of the month or quarter
    if freq == "M":
        adjusted_start_date = start_date - pd.offsets.MonthBegin(n=1)
    elif freq == "Q":
        adjusted_start_date = start_date - pd.offsets.QuarterBegin(startingMonth=1, n=1)
    else:
        raise ValueError("Frequency must be 'M' for months or 'Q' for quarters.")

    # Generate the periods
    periods = pd.date_range(start=adjusted_start_date, end=end_date, freq=freq)

    return [
        (start + timedelta(days=1), start + timedelta(days=(end - start).days))
        for start, end in zip(periods, periods[1:])
    ]
