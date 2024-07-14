import saasops.database as database
import saasops.display as display
import saasops.calc as calc
import saasops.check as check

# import saasops.database, display, export, calc
from typer import Typer
import typer
from rich.console import Console
from datetime import datetime
from typing import Optional
import os
import logging

logging.basicConfig(level=logging.ERROR)

# Main Application TODOs
# TODO: add Items/Products as a table, and link to Segments and Invoices (would need to update Description/Type in Segments to be a FK to Items/Products)
# TODO: add retail pricing and discounts to Segments? - would need to somewhere track the retail value and then actual discounted value
# TODO: with items/products, would then want to report out on ARR etc. filtered by item/product
# TODO: build a better front-end for data entry with pull down from table joins etc. - this should be quite easy

app = Typer(name="saasops")

customer_app = Typer(name="customer", help="Manage customers")
contract_app = Typer(name="contract", help="Manage contracts")
segment_app = Typer(name="segment", help="Manage segments")
invoice_app = Typer(name="invoice", help="Manage invoices")
invoicesegment_app = Typer(name="invoicesegment", help="Map invoices to segments")
calc_app = Typer(name="calc", help="Calculate output data and metrics")
export_app = Typer(name="export", help="Export data to various file type")
check_app = Typer(name="check", help="Check data for issues and consistency")

app.add_typer(customer_app, name="customer")
app.add_typer(contract_app, name="contract")
app.add_typer(segment_app, name="segment")
app.add_typer(invoice_app, name="invoice")
app.add_typer(invoicesegment_app, name="invoicesegment")
app.add_typer(calc_app, name="calc")
app.add_typer(export_app, name="export")
app.add_typer(check_app, name="check")

# Database selection commands


@app.command("set_db")
def set_db(db_name: str):
    """
    Set the database to use.
    """
    os.environ["DB_NAME"] = db_name
    typer.echo(f"Database set to: {db_name}")


@app.command("get_db")
def get_db():
    """
    Get the current database in use.
    """
    db_name = os.environ.get("DB_NAME", "testdb")
    typer.echo(f"Current database: {db_name}")


# Customer commands


@customer_app.command("list")
def listcust():
    """
    List all customers.
    """
    console = Console()
    con = database.connect_database(console)
    display.print_customers(con, console)


@customer_app.command("add")
def custadd(name: str, city: str, state: str):
    """
    Add a new customer.
    """
    console = Console()
    engine = database.connect_database(console)
    database.add_customer(engine, name, city, state)
    console.print(f"INFO: Customer {name} added.", style="bold green")


@customer_app.command("del")
def custdel(customer_id: int):
    """
    Delete a customer.
    """
    console = Console()
    engine = database.connect_database(console)
    database.delete_customer(engine, customer_id)
    console.print(f"INFO: Customer ID {customer_id} deleted.", style="bold green")


@customer_app.command("update")
def custupd(customer_id: int, field: str, value: str):
    """
    Update a customer record with new value.
    """
    console = Console()
    engine = database.connect_database(console)
    database.update_customer(engine, customer_id, field, value)
    console.print(f"INFO: Customer ID {customer_id} updated.", style="bold green")

# Contract commands


@contract_app.command("list")
def listcont(sort_column: Optional[str] = None):
    """
    List all contracts.
    """
    console = Console()
    con = database.connect_database(console)
    display.print_contracts(con, console, sort_column)


@contract_app.command("add")
def contadd(customer_id: int, reference: str, contract_date: str, term_start_date: str, term_end_date: str, total_value: int, renewal_id: Optional[int]=None, merge_id: Optional[int]=None):
    """
    Add a new contract.
    """
    console = Console()
    engine = database.connect_database(console)
    database.add_contract(engine, customer_id, reference, contract_date, term_start_date, term_end_date, total_value, renewal_id, merge_id)
    console.print(f"INFO: Contract {reference} added.", style="bold green")


@contract_app.command("del")
def contdel(contract_id: int):
    """
    Delete a contract.
    """
    console = Console()
    engine = database.connect_database(console)
    database.delete_contract(engine, contract_id)
    console.print(f"INFO: Contract ID {contract_id} deleted.", style="bold green")


@contract_app.command("update")
def contupd(contract_id: int, field: str, value: str):
    """
    Update a contract record with new value.
    """
    console = Console()
    engine = database.connect_database(console)
    if field == 'renewalfromcontractid' and value.lower() == 'none':
        value = None
    database.update_contract(engine, contract_id, field, value)
    console.print(f"INFO: Contract ID {contract_id} updated.", style="bold green")


# @contract_app.command("print")
# def prntcont(contract_id: int):
#     """
#     Print details of a contract.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     display.print_contract(engine, contract_id, console)

# @contract_app.command("reconcile")
# def reconcont(contract_id: int):
#     """
#     Reconcile a contract with linked segment details.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     display.print_contract_details(engine, contract_id, console)

# @contract_app.command("unlinked")
# def unlinkedcont():
#     """
#     List all contracts with no linked segments.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     display.print_contracts_without_segments(engine, console)

# Segment commands


@segment_app.command("list")
def listseg(sort_column: Optional[str] = None, exportfile: Optional[str] = None):
    """
    List all segments.
    """
    console = Console()
    con = database.connect_database(console)
    df = display.print_segments(con, console, sort_column)

    # Check if exportfile argument is provided
    if exportfile:
        # Ensure the exports directory exists
        exports_dir = "exports"
        os.makedirs(exports_dir, exist_ok=True)

        # Define the full path for the CSV file
        filepath = os.path.join(exports_dir, f"{exportfile}.csv")

        # Export the DataFrame to CSV
        df.to_csv(filepath, index=True)

        # Optionally, print a message to the console indicating the export was successful
        console.print(f"Segments list data exported to {filepath}", style="green")


# @segment_app.command("print")
# def prntseg(segment_id: int):
#     """
#     Print details of a segment.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     display.print_segment(engine, segment_id, console)

@segment_app.command("add")
def segadd(contract_id: int, segment_start_date: str, segment_end_date: str, title: str, type: str, segment_value: int):
    """
    Add a new segment.
    """
    console = Console()
    engine = database.connect_database(console)
    database.add_segment(engine, contract_id, segment_start_date, segment_end_date, title, type, segment_value)
    console.print(f"INFO: Segment {title} added.", style="bold green")

@segment_app.command("del")
def segdel(segment_id: int):
    """
    Delete a segment.
    """
    console = Console()
    engine = database.connect_database(console)
    database.delete_segment(engine, segment_id)
    console.print(f"INFO: Segment ID {segment_id} deleted.", style="bold green")

@segment_app.command("update")
def segupd(segment_id: int, field: str, value: str):
    """
    Update a segment record with new value.
    """
    console = Console()
    engine = database.connect_database(console)
    database.update_segment(engine, segment_id, field, value)
    console.print(f"INFO: Segment ID {segment_id} updated.", style="bold green")

# Invoice commands

# @invoice_app.command("list")
# def listinv(sort_column: Optional[str]=None):
#     """
#     List all invoices.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     display.print_invoices(engine, console, sort_column)

# @invoice_app.command("add")
# def invadd(number: str, date: str, dayspayable: int, amount: int):
#     """
#     Add a new invoice.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     print(database.add_invoice(engine, number, date, dayspayable, amount))

# @invoice_app.command("del")
# def invdel(invoice_id: int):
#     """
#     Delete an invoice.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     print(database.delete_invoice(engine, invoice_id))

# Invoice Segment commands

# @invoicesegment_app.command("add")
# def addinvseg(invoice_id: int, segment_id: int):
#     """
#     Add a new invoice segment mapping.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     print(database.add_invoice_to_segment_mapping(engine, invoice_id, segment_id))

# @invoicesegment_app.command("del")
# def delinvseg(invoice_segment_id: int):
#     """
#     Delete an invoice segment mapping.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     print(database.delete_invoice_to_segment_mapping(engine, invoice_segment_id))

# Calculation commands


@calc_app.command("bkingsdf")
def bkingsdf(
    start_date: str,
    end_date: str,
    customer: Optional[int] = None,
    contract: Optional[int] = None,
    timeframe: Optional[str] = "M",
    format_type: Optional[str] = "dollar",
    ignoreoverrides: Optional[bool] = False,
):
    """
    Print bookings dataframe.
    """
    console = Console()
    con = database.connect_database(console)
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    df = calc.customer_bkings_df(start_date, end_date, con, timeframe)
    df_title = display.generate_title(
        "Bookings by Customer",
        start_date,
        end_date,
        timeframe,
        format_type,
        customer,
        contract,
    )
    display.print_combined_table(df, df_title, console, format_type)


@calc_app.command("arrdf")
def arrdf(
    start_date: str,
    end_date: str,
    customer: Optional[int] = None,
    contract: Optional[int] = None,
    timeframe: Optional[str] = "M",
    format_type: Optional[str] = "dollar",
    ignoreoverrides: Optional[bool] = False,
):
    """
    Print ARR dataframe.
    """
    console = Console()
    con = database.connect_database(console)
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    df = calc.customer_arr_df(start_date, end_date, con, timeframe)
    df_title = display.generate_title(
        "Period End ARR by Customer",
        start_date,
        end_date,
        timeframe,
        format_type,
        customer,
        contract,
    )
    display.print_combined_table(df, df_title, console, format_type)


# @calc_app.command("revtbl")
# def revdf(
#         start_date: str,
#         end_date: str,
#         type: str,
#         customer: Optional[int]=None,
#         contract: Optional[int]=None,
#         frequency: Optional[str]='M'
# ):
#     """
#     Print revenue dataframe.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
#     df = calc.populate_revenue_df(start_date, end_date, type, engine, customer, contract, frequency)
#     _, last_day_start = calendar.monthrange(start_date.year, start_date.month)
#     _, last_day_end = calendar.monthrange(end_date.year, end_date.month)
#     if type == 'mid':
#         start_date = start_date.replace(day=15)
#         end_date = end_date.replace(day=15)
#     elif type == 'end':
#         start_date = start_date.replace(day=last_day_start)
#         end_date = end_date.replace(day=last_day_end)
#     df_title = f'Revenue, {start_date} to {end_date}, type: {type}-month'
#     if customer:
#         df_title += f', customer: {customer}'
#     if contract:
#         df_title += f', contract: {contract}'
#     display.print_combined_table(df, df_title, console, "Revenue")

# @calc_app.command("metricstbl")
# def metricsdf(
#         start_date: str,
#         end_date: str,
#         customer: Optional[int]=None,
#         contract: Optional[int]=None,
#         frequency: Optional[str]='M'
# ):
#     """
#     Print metrics dataframe.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
#     df = calc.populate_metrics_df(start_date, end_date, engine, customer, contract, frequency)
#     df_title = f'Metrics, {start_date} to {end_date}, frequency: {frequency}'
#     if customer:
#         df_title += f', customer: {customer}'
#     if contract:
#         df_title += f', contract: {contract}'

#     display.print_combined_table(df, df_title, console, "MRR Metrics")


@calc_app.command("bkings")
def bkingstbl(
    date: str,
    ignore_zeros: bool = typer.Option(
        False, "--ignore_zeros", help="Ignore customers with zero bookings."
    ),
    timeframe: Optional[str] = "M",
):
    """
    Print bookings table for specific date.
    """
    console = Console()
    con = database.connect_database(console)

    # Determine table title based on the provided frequency
    title_date_str = calc.get_timeframe_title(date, timeframe)

    df = calc.customer_bkings_tbl(date, con, timeframe)

    display.print_combined_table(df, f"Bookings for {title_date_str}", console)


@calc_app.command("arr")
def arrtbl(
    date: str,
    # ignoreoverrides: Optional[bool]=False,
    customer: Optional[int] = None,
    contract: Optional[int] = None,
    ignore_zeros: bool = typer.Option(
        False, "--ignore_zeros", help="Ignore customers with zero ARR."
    ),
    tree_detail: Optional[bool] = False,
):
    """
    Print ARR table for specific date.
    """
    console = Console()
    con = database.connect_database(console)
    date = datetime.strptime(date, "%Y-%m-%d").date()

    # Dynamically build the title based on provided arguments
    title_parts = [f"ARR at {date}"]
    if customer:
        title_parts.append(f"Customer: {customer}")
    if contract:
        title_parts.append(f"Contract: {contract}")
    title = " | ".join(title_parts)  # Combine parts into a single string

    df = calc.customer_arr_tbl(date, con, customer, contract, ignore_zeros, tree_detail)
    display.print_combined_table(df, title, console)


# @calc_app.command("carr")
# def carrdf(date: str,
#            ignore_zeros: bool = typer.Option(False, "--ignore_zeros", help="Ignore customers with zero CARR."),
#            tree_detail: Optional[bool]=False):
#     """
#     Print CARR table for specific date.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     date = datetime.strptime(date, '%Y-%m-%d').date()
#     df = calc.customer_carr_df(date, engine, ignore_zeros, tree_detail)
#     display.print_combined_table(df, f'CARR at {date}', console)


@calc_app.command("arrnew")
def arrnewtf(date: str, timeframe: Optional[str] = "M"):
    """
    Print New ARR table for month or quarter.
    """
    console = Console()
    con = database.connect_database(console)

    # Determine table title based on the provided frequency
    title_date_str = calc.get_timeframe_title(date, timeframe)

    df = calc.new_arr_by_timeframe(date, con, timeframe)

    display.print_combined_table(df, f"New ARR for {title_date_str}", console)


@calc_app.command("arrchange")
def arrchangedf(
    start_date: str,
    end_date: str,
    customer: Optional[int] = None,
    contract: Optional[int] = None,
    timeframe: Optional[str] = "M",
    format_type: Optional[str] = None,
    exportfile: Optional[str] = None,
    print_metrics: Optional[bool] = False,
):
    """
    Print ARR Change table for month or quarter.
    """

    console = Console()
    con = database.connect_database(console)

    # Parse the input start and end dates
    start_date_parsed = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_parsed = datetime.strptime(end_date, "%Y-%m-%d").date()

    # Calculate the ARR change dataframe
    df = calc.build_arr_change_df(
        start_date_parsed,
        end_date_parsed,
        con,
        timeframe,
        format_type,
        customer,
        contract,
        print_metrics
    )

    df_title = display.generate_title(
        "ARR Change",
        start_date_parsed,
        end_date_parsed,
        timeframe,
        format_type=format_type,
        customer=customer,
        contract=contract,
    )

    display.print_combined_table(df, df_title, console)

    # Check if exportfile argument is provided
    if exportfile:
        # Ensure the exports directory exists
        exports_dir = "exports"
        os.makedirs(exports_dir, exist_ok=True)

        # Define the full path for the CSV file
        filepath = os.path.join(exports_dir, f"{exportfile}.csv")

        # Export the DataFrame to CSV
        df.to_csv(filepath, index=True)  # Index is included in the export

        # Optionally, print a message to the console indicating the export was successful
        console.print(f"ARR Change data exported to {filepath}", style="green")


# @calc_app.command("arrmetrics")
# def arrmetricsdf(start_date: str, end_date: str, customer: Optional[int]=None, contract: Optional[int]=None, frequency: Optional[str]='M', ignoreoverrides: Optional[bool]=False):
#     """
#     Print ARR metrics dataframe.
#     """
#     console = Console()
#     engine = database.connect_database(console)

#     start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

#     df = calc.populate_arr_metrics_df(start_date, end_date, engine, customer, contract, frequency, ignoreoverrides)
#     df_title = f'ARR Metrics, {start_date} to {end_date}, frequency: {frequency}'

#     display.print_combined_table(df, df_title, console, True, "ARR Metrics")


# Export commands

# @export_app.command("all")
# def exportall(start_date: str, end_date: str):
#     """
#     Export all chart data to PowerPoint presentation and Excel workbook.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
#     export.export_data_to_pptx(engine, start_date, end_date)
#     export.export_data_to_xlsx(engine, start_date, end_date)

# @export_app.command("charts")
# def exportcharts(
#         start_date: str,
#         end_date: str,
#         customer: Optional[int]=None,
#         contract: Optional[int]=None,
#         show_gridlines: bool = typer.Option(False, "--show-gridlines", help="Show gridlines on charts"),
#         frequency: Optional[str]='M',
#         ignoreoverrides: Optional[bool]=False
# ):
#     """
#     Export all charts to image files.
#     """
#     console = Console()
#     engine = database.connect_database(console)
#     start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
#     export.export_chart_images(engine, start_date, end_date, customer, contract, show_gridlines, frequency, ignoreoverrides)


# Check commands
@check_app.command("segments")
def checksegments():
    """
    Check segments for consistency.
    """
    console = Console()
    con = database.connect_database(console)
    check.check_segment_data(con, console)
    console.print("INFO: Segment data consistency check complete.", style="bold green")


@check_app.command("contracts")
def checkcontracts():
    """
    Check segments for consistency.
    """
    console = Console()
    con = database.connect_database(console)
    check.check_contract_data(con, console)
    console.print("INFO: Segment data consistency check complete.", style="bold green")

