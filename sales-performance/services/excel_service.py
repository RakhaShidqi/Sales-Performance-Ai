import warnings
import pandas as pd

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="openpyxl"
)

EXCEL_FILE = "data/Achievement Report 2026.xlsx"


# =========================================
# SHEETS CONFIG
# =========================================

SAME_SCHEMA_SHEETS = [
    "Commercial",
    "Regional"
]

DATABASE_SHEET = "Database"


# =========================================
# SALES BASE SCHEMA
# =========================================

BASE_COLUMNS = [

    "No",
    "Name",
    "Join Date",
    "Teritory",
    "Status",
    "JAN",
    "Jan %",
    "FEB",
    "Feb %",
    "MAR",
    "Mar %",
    "APR",
    "Apr %",
    "MAY",
    "May %",
    "JUN",
    "Jun %",
    "JUL",
    "Jul %",
    "AUG",
    "Aug %",
    "SEP",
    "Sep %",
    "OCT",
    "Oct %",
    "NOV",
    "Nov %",
    "DEC",
    "Dec %",
    "Total YTD",
    "YTD %",
    "Ach Q1",
    "Ach Q1 %",
    "Ach Q2",
    "Ach Q2 %",
    "Ach Q3",
    "Ach Q3 %",
    "Ach Q4",
    "Ach Q4 %",
    "Total PO",
    "Gap Ach YTD",
    "Leads on Progress",
    "VS Gap",
]


# =========================================
# DATABASE CUSTOM SCHEMA (DEFINE HERE)
# =========================================

DATABASE_COLUMNS = [
    # contoh kamu bebas isi sesuai Excel Database sheet
    # ganti sesuai kebutuhan real kamu

    "Division",
    "Type WO",
    "Ticket ID",
    "Created date",
    "Tanggal Submit Dokumen",
    "Applicants Name",
    "Teritory",
    "Customer ID",
    "Customer Name",
    "Service",
    "Contract Duration (Month)",
    "No. Form",
    "No. WO/SO",
    "No Quotation",
    "OTC",
    "MRC",
    "Industry",
    "Program",
    "No Inv",
    "Payment Status",
    "Ach Periode",
    "Transaction",
    "Product Category",
    "Service Description",
    "Upgrade",
    "Price Before",
    "Price After",
    "Instalation Address",
    "Kontrak 24",
    "Transaction2",
    "Monthly Revenue",
    "GP/Bulan (Rp)",
    "GP/Tahun (Rp)",
    "GP Margin (%)",
    "Noted",
    "GP OTC Recurring",
    "Focus Account",
    "Division2",
    "Carryover",
    "Prorate NY",
    "By Calc Apps",
    "Jmlh PO",
    "Revenue/Tahun" 
]


# =========================================
# GET SHEET NAMES
# =========================================

def get_sheet_names():
    return pd.ExcelFile(EXCEL_FILE).sheet_names


# =========================================
# GET SHEET COLUMNS
# =========================================

def get_sheet_columns(sheet_name, header_index=1):

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name=sheet_name,
        header=header_index
    )

    return df.columns.tolist()


# =========================================
# CORE LOADER
# =========================================

def load_sheet_data(
    sheet_name,
    header_index=1,
    required_columns=None,
    drop_empty_name=True
):

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name=sheet_name,
        header=header_index
    )

    # =========================================
    # APPLY SCHEMA IF PROVIDED
    # =========================================

    if required_columns:

        available_columns = [
            col for col in required_columns
            if col in df.columns
        ]

        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            print(f"\n[WARNING] {sheet_name} missing columns:")
            for col in missing_columns:
                print(f"- {col}")

        df = df[available_columns]

    # =========================================
    # CLEAN NAME (ONLY FOR SALES SHEETS)
    # =========================================

    if drop_empty_name and "Name" in df.columns:
        df = df[df["Name"].notna()]

    df = df.reset_index(drop=True)

    return df


# =========================================
# SALES SHEET LOADER
# =========================================

def load_sales_data():

    return load_sheet_data(
        sheet_name="Commercial",
        header_index=1,
        required_columns=BASE_COLUMNS
    )


def load_regional_data():

    return load_sheet_data(
        sheet_name="Regional",
        header_index=1,
        required_columns=BASE_COLUMNS
    )

def load_all_sales_data():

    result = {}

    for sheet in SAME_SCHEMA_SHEETS:

        result[sheet] = load_sheet_data(
            sheet_name=sheet,
            header_index=1,
            required_columns=BASE_COLUMNS
        )

    return result


# =========================================
# DATABASE LOADER (CUSTOM SCHEMA)
# =========================================

def load_database_data():
    return load_sheet_data(
        sheet_name="Database",
        header_index=1,
        required_columns=DATABASE_COLUMNS
    )

def load_all_database_data():

    result = {}

    for sheet in DATABASE_SHEET:

        result[sheet] = load_sheet_data(
            sheet_name=sheet,
            header_index=1,
            required_columns=DATABASE_COLUMNS
        )

    return result


# =========================================
# GENERIC ACCESS
# =========================================

def load_single_sheet(sheet_name):

    if sheet_name == DATABASE_SHEET:
        return load_database_data()

    return load_sheet_data(
        sheet_name=sheet_name,
        header_index=1,
        required_columns=BASE_COLUMNS
    )


# =========================================
# DEBUG
# =========================================

if __name__ == "__main__":

    print("\n=== SHEETS ===")
    print(get_sheet_names())

    print("\n=== COMMERCIAL ===")
    print(load_sales_data().head())

    print("\n=== REGIONAL ===")
    print(load_regional_data().head())

    print("\n=== DATABASE ===")
    print(load_database_data().head())