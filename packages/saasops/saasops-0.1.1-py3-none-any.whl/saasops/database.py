import os
from sqlalchemy import text
import pandas as pd
import duckdb

# Database functions

# FIXME: The database add functions need to address use of PRIMARY KEY and AUTOINCREMENT or whatever works in DuckDB


def connect_database(console):
    """
    Connect to a DuckDB database file specified in an environment variable.

    Args:
        console (Console): Rich console object

    Returns:
        connection: DuckDB connection object
    """

    # Read database prefix from environment variable
    db_prefix = os.environ.get("DB_NAME", "testdb")

    # Construct the full database filename
    db_filename = f"data/{db_prefix}.duckdb"

    # Connect to the DuckDB file
    con = duckdb.connect(database=db_filename)

    # Print success status
    console.print(f"INFO: Connected to database {db_prefix}.", style="bold green")

    return con


def fetch_data_from_db(engine, table_name):
    """
    Fetch data from a database table and return a Pandas DataFrame.

    Args:
        engine (SQLAlchemy engine object): SQLAlchemy engine object
        table_name (str): Name of the table to fetch data from

    Returns:
        Pandas DataFrame: DataFrame containing the data from the table
    """

    # Create a new DataFrame from a database table
    with engine.begin() as conn:
        query = text(f"SELECT * FROM {table_name}")
        df = pd.read_sql(query, conn)
    return df


# Customer functions


def add_customer(con, name, city, state):
    # Prepare the query and parameters
    query = """INSERT INTO Customers (CustomerID, Name, City, State) VALUES (nextval('Customers_id_seq'), ?, ?, ?);"""
    params = (name, city, state)

    # Execute the query
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows added."
    else:
        return f"Row added. Customer {name} was successfully added."


def delete_customer(con, customer_id):
    query = """DELETE FROM Customers WHERE CustomerID = ?;"""
    params = (customer_id,)
    result = con.execute(query, params)

    if result.rowcount == 0:
        return "No rows deleted. The specified CustomerID may not exist."
    else:
        return f"1 row(s) deleted. Customer with CustomerID {customer_id} was successfully deleted."


def update_customer(con, customer_id, field, value):
    query = f"""UPDATE Customers SET {field} = ? WHERE CustomerID = ?;"""
    params = (value, customer_id)
    result = con.execute(query, params)

    if result.rowcount == 0:
        return "No rows updated. The specified CustomerID may not exist."
    else:
        return f"1 row(s) updated. Customer with CustomerID {customer_id} was successfully updated."


# Contract functions


def add_contract(
    con,
    customer_id,
    reference,
    contract_date,
    term_start_date,
    term_end_date,
    total_value,
    renewal_id=None,
    merge_id=None,
):
    # Prepare the query and parameters
    query = """INSERT INTO Contracts (ContractID, CustomerID, RenewalFromContractID, MergesToContractID, Reference, ContractDate, TermStartDate, TermEndDate, TotalValue) VALUES (nextval('Contracts_id_seq'), ?, ?, ?, ?, ?, ?, ?, ?) RETURNING ContractID;"""
    params = (
        customer_id,
        renewal_id,
        merge_id,
        reference,
        contract_date,
        term_start_date,
        term_end_date,
        total_value,
    )
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows added."
    else:
        return f"Row added. ContractID {result.fetchone()[0]} was successfully added."


def delete_contract(con, contract_id):
    # Prepare the query and parameters
    query = """DELETE FROM Contracts WHERE ContractID = ?;"""
    params = (contract_id,)
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows deleted. The specified ContractID may not exist."
    else:
        return f"1 row(s) deleted. Contract with ContractID {contract_id} was successfully deleted."


def update_contract(con, contract_id, field, value):
    # Prepare the query and parameters
    query = f"""UPDATE Contracts SET {field} = ? WHERE ContractID = ?;"""
    params = (value, contract_id)
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows updated. The specified ContractID may not exist."
    else:
        return f"1 row(s) updated. Contract with ContractID {contract_id} was successfully updated."
\

# Segment functions


def add_segment(
    con, contract_id, segment_start_date, segment_end_date, title, type, segment_value
):
    
    # Prepare the query and parameters
    query = """INSERT INTO Segments (SegmentID, ContractID, SegmentStartDate, SegmentEndDate, Title, Type, SegmentValue) VALUES (nextval('Segments_id_seq'), ?, ?, ?, ?, ?, ?) RETURNING SegmentID;"""
    params = (
        contract_id,
        segment_start_date,
        segment_end_date,
        title,
        type,
        segment_value,
    )
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows added."
    else:
        return f"Row added. SegmentID {result.fetchone()[0]} was successfully added."


def delete_segment(con, segment_id):
    # Prepare the query and parameters
    query = """DELETE FROM Segments WHERE SegmentID = ?;"""
    params = (segment_id,)
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows deleted. The specified SegmentID may not exist."
    else:
        return f"1 row(s) deleted. Segment with SegmentID {segment_id} was successfully deleted."


def update_segment(con, segment_id, field, value):
    # Prepare the query and parameters
    query = f"""UPDATE Segments SET {field} = ? WHERE SegmentID = ?;"""
    params = (value, segment_id)
    result = con.execute(query, params)

    # Check if the query was successful
    if result.rowcount == 0:
        return "No rows updated. The specified SegmentID may not exist."    
    else:
        return f"1 row(s) updated. Segment with SegmentID {segment_id} was successfully updated."


# Invoice functions


def add_invoice(con, number, date, dayspayable, amount):
    query = text(
        """INSERT INTO Invoices (Number, Date, DaysPayable, Amount) VALUES (:Number, :Date, :DaysPayable, :Amount) RETURNING InvoiceID;"""
    )
    params = {
        "Number": number,
        "Date": date,
        "DaysPayable": dayspayable,
        "Amount": amount,
    }
    result = con.execute(query, params)
    if result.rowcount == 0:
        return "No rows added."
    else:
        return f"{result.rowcount} row(s) added. InvoiceID {result.fetchone()[0]} was successfully added."


def delete_invoice(con, invoice_id):
    query = text("""DELETE FROM Invoices WHERE InvoiceID = :InvoiceID;""")
    params = {"InvoiceID": invoice_id}
    result = con.execute(query, params)
    if result.rowcount == 0:
        return "No rows deleted. The specified InvoiceID may not exist."
    else:
        return f"{result.rowcount} row(s) deleted. Invoice with InvoiceID {invoice_id} was successfully deleted."


def update_invoice(con, invoice_id, field, value):
    query = text(
        f"""UPDATE Invoices SET {field} = :Value WHERE InvoiceID = :InvoiceID;"""
    )
    params = {"InvoiceID": invoice_id, "Value": value}
    result = con.execute(query, params)
    if result.rowcount == 0:
        return "No rows updated. The specified InvoiceID may not exist."
    else:
        return f"{result.rowcount} row(s) updated. Invoice with InvoiceID {invoice_id} was successfully updated."


# Invoice-Segment functions


def add_invoice_to_segment_mapping(con, invoice_id, segment_id):
    query = text(
        """INSERT INTO InvoiceSegmentMapping (InvoiceID, SegmentID) VALUES (:InvoiceID, :SegmentID);"""
    )
    params = {"InvoiceID": invoice_id, "SegmentID": segment_id}
    result = con.execute(query, params)
    if result.rowcount == 0:
        return "No rows added."
    else:
        return f"{result.rowcount} row(s) added. InvoiceID {invoice_id} was successfully added to SegmentID {segment_id}."


def delete_invoice_to_segment_mapping(con, invoicesegment_id):
    query = text(
        """DELETE FROM InvoiceSegmentMapping WHERE InvoiceSegmentID = :InvoiceSegmentID;"""
    )
    params = {"InvoiceSegmentID": invoicesegment_id}
    result = con.execute(query, params)
    if result.rowcount == 0:
        return "No rows deleted. The specified InvoiceSegmentID may not exist."
    else:
        return f"{result.rowcount} row(s) deleted. InvoiceSegmentID {invoicesegment_id} was successfully deleted."
