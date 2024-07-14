import saasops.classes as classes
from collections import defaultdict

# TODO: Need a check on contracts that verifies contracts exist for renewal and merges to (as not a FK)

def check_segment_data(con, console, customer=None, contract=None):
    """ """

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

    classes.SegmentData.add_rule(classes.valid_segment_start_end_dates)
    classes.SegmentData.add_rule(classes.valid_segment_length)
    classes.SegmentData.add_rule(classes.valid_arr_override_date)

    console.print(
        f"INFO: Checking {len(rows)} segments for consistency...",
        style="bold green"
    )

    for row in rows:
        segment_data = classes.SegmentData(*row, console=console)
        segment_data.check_consistency()

    return rows


def check_contract_data(con, console, customer=None, contract=None):
    """ """

    # Retrieve contract and segment data from the database
    query = """
    SELECT c.ContractID, c.CustomerID, c.RenewalFromContractID, c.MergesToContractID, c.Reference, c.ContractDate,
           c.TermStartDate, c.TermEndDate, c.TotalValue, s.SegmentID, s.SegmentStartDate,
           s.SegmentEndDate, s.SegmentValue
    FROM Contracts c
    LEFT JOIN Segments s ON c.ContractID = s.ContractID
    JOIN Customers cu ON c.CustomerID = cu.CustomerID
    """

    conditions = []
    if customer:
        conditions.append(f"cu.CustomerID = '{customer}'")
    if contract:
        conditions.append(f"c.ContractID = '{contract}'")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    result = con.execute(query)
    rows = result.fetchall()

    contracts = defaultdict(lambda: None)
    for row in rows:
        contract_id = row[0]
        if contracts[contract_id] is None:
            # Create a new Contract object if it doesn't exist
            contracts[contract_id] = classes.Contract(
                contract_id=row[0],
                customer_id=row[1],
                renewal_from_contract_id=row[2],
                merges_to_contract_id=row[3],
                reference=row[4],
                contract_date=row[5],
                term_start_date=row[6],
                term_end_date=row[7],
                total_value=row[8],
                console=console
            )
        # Check if there is segment data in this row (i.e., if SegmentID is not None)
        if row[9] is not None:
            segment = {
                'segment_id': row[9],
                'segment_start_date': row[10],
                'segment_end_date': row[11],
                'segment_value': row[12]
            }
            contracts[contract_id].segments.append(segment)

    classes.Contract.add_rule(classes.contract_value_matches_aggregate_segment_value)

    console.print(
        f"INFO: Checking {len(contracts)} contracts for consistency...",
        style="bold green"
    )

    for contract in contracts.values():
        contract.check_consistency()

    return contracts