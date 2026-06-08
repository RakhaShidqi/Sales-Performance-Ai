
import pandas as pd

from services.excel_service import (
    load_sales_data,
    load_regional_data,
    load_database_data
)

# =========================================
# NORMALIZER
# =========================================

def normalize_percentage(value):

    if pd.isna(value):
        return 0.0

    value = (
        str(value)
        .replace("%", "")
        .replace(" ", "")
        .strip()
    )

    value = value.replace(",", ".")

    try:
        value = float(value)
    except:
        return 0.0

    # =========================================
    # EXCEL FRACTION NORMALIZATION
    #
    # 0.0431 -> 4.31
    # 0.9559 -> 95.59
    # 1.0143 -> 101.43
    # =========================================
    if value <= 10:
        value = value * 100

    return round(value, 6)


# =========================================
# FORMAT PERCENTAGE
# =========================================

def format_percentage(value):

    if pd.isna(value):
        return "0%"

    try:
        value = float(value)
        return f"{round(value, 2)}%"
    except:
        return "0%"
    
def format_vs_gap(value):

    if pd.isna(value):
        return "0%"

    try:
        value = float(value)

        return f"{round(value * 100, 2)}%"

    except:
        return "0%"


# =========================================
# COMMON CLEANER
# =========================================

def _prepare_dataframe(df):

    df = df.copy()

    # =========================================
    # ACTIVE ONLY
    # =========================================
    df = df[
        (df["Name"].notna()) &
        (df["Status"] == "Active")
    ]

    # =========================================
    # REMOVE INVALID NAME
    # =========================================
    excluded_keywords = [
        "VACANT",
        "TOTAL",
        "TEAM"
    ]

    df = df[
        ~df["Name"]
        .astype(str)
        .str.upper()
        .str.contains(
            "|".join(excluded_keywords),
            na=False
        )
    ]

    # =========================================
    # DATE FORMAT
    # =========================================
    df["Join Date"] = pd.to_datetime(
        df["Join Date"],
        errors="coerce"
    )

    # =========================================
    # NORMALIZE PERCENTAGE
    # =========================================
    percentage_columns = [
        "Jan %",
        "Feb %",
        "Mar %",
        "Apr %",
        "May %",
        "Jun %",
        "Jul %",
        "Aug %",
        "Sep %",
        "Oct %",
        "Nov %",
        "Des %",
        "YTD %",
        "Ach Q1 %",
        "Ach Q2 %",
        "Ach Q3 %",
        "Ach Q4 %",
        "GP Margin (%)",
        "Noted"
    ]

    for col in percentage_columns:

        if col in df.columns:

            df[col] = df[col].apply(
                normalize_percentage
            )

    return df


# =========================================
# SALES
#
# No != 1
# =========================================

def _clean_sales(df):

    df = _prepare_dataframe(df)

    df = df[
        (df["No"].notna()) &
        (df["No"] != 1)
    ]

    return df


# =========================================
# HEAD SALES
#
# No == 1
# exclude VP
# exclude SMB BAG
# =========================================

def _clean_headsales(df):

    df = _prepare_dataframe(df)

    # =========================================
    # HEAD SALES ONLY
    # =========================================
    df = df[
        (df["No"] == 1)
    ]

    # =========================================
    # EXCLUDE VP
    # =========================================
    df = df[
        ~df["Teritory"]
        .astype(str)
        .str.upper()
        .isin([
            "VP OF COMMERCIAL",
            "VP OF REGIONAL"
        ])
    ]

    # =========================================
    # EXCLUDE UNIT HEAD
    # SMB BAG*
    # =========================================
    df = df[
        ~df["Teritory"]
        .astype(str)
        .str.upper()
        .str.startswith("SMB BAG")
    ]

    return df


# =========================================
# UNIT HEAD
#
# No == 1
# Teritory startswith SMB BAG
# =========================================

def _clean_unit_head(df):

    df = _prepare_dataframe(df)

    # =========================================
    # UNIT HEAD ONLY
    # =========================================
    df = df[
        (df["No"] == 1)
    ]

    # =========================================
    # SMB BAG ONLY
    # =========================================
    df = df[
        df["Teritory"]
        .astype(str)
        .str.upper()
        .str.startswith("SMB BAG")
    ]

    return df

def _clean_database_data(df):

    df = df.copy()

    # hanya data yang memiliki division
    if "Division" in df.columns:
        df = df[
            df["Division"].notna()
        ]

    # format tanggal
    if "Created date" in df.columns:
        df["Created date"] = pd.to_datetime(
            df["Created date"],
            errors="coerce"
        )

    # normalize percentage
    for col in [
        "GP Margin (%)",
        "Noted"
    ]:
        if col in df.columns:
            df[col] = df[col].apply(
                normalize_percentage
            )

    return df

# =========================================
# SALES LOADERS
# =========================================

def get_registered_sales():

    return _clean_sales(
        load_sales_data()
    )


def get_registered_regional_sales():

    return _clean_sales(
        load_regional_data()
    )

# =========================================
# SMB SALES
#
# No != 1
# Teritory startswith SMB
# =========================================

def get_registered_smb_sales():

    df = get_registered_sales()

    df = df[
        df["Teritory"]
        .astype(str)
        .str.upper()
        .str.startswith("SMB")
    ]

    return df


# =========================================
# ENTERPRISE SALES
#
# No != 1
# exclude SMB
# =========================================

def get_registered_enterprise_sales():

    df = get_registered_sales()

    df = df[
        ~df["Teritory"]
        .astype(str)
        .str.upper()
        .str.startswith("SMB")
    ]

    return df

# =========================================
# HEAD SALES LOADERS
# =========================================

def get_registered_headsales_commercial():

    return _clean_headsales(
        load_sales_data()
    )


def get_registered_headsales_regional():

    return _clean_headsales(
        load_regional_data()
    )


# =========================================
# UNIT HEAD LOADERS
# =========================================

def get_registered_unit_head_commercial():

    return _clean_unit_head(
        load_sales_data()
    )


def get_registered_unit_head_regional():

    return _clean_unit_head(
        load_regional_data()
    )


# =========================================
# Database Loaders
# =========================================

def get_registered_database():
    return _clean_database_data(
        load_database_data()
    )

# =========================================
# RESPONSE FORMATTER
# =========================================

def to_response(df):

    df = df.copy()

    # =========================================
    # FORMAT DATE
    # =========================================
    if "Join Date" in df.columns:

        df["Join Date"] = pd.to_datetime(
            df["Join Date"],
            errors="coerce"
        ).dt.strftime("%d %b %Y")
        
    if "Created date" in df.columns:
        df["Created date"] = pd.to_datetime(
            df["Created date"],
            errors="coerce"
        ).dt.strftime("%d %b %Y")

    # =========================================
    # FORMAT PERCENTAGE
    # =========================================
    percentage_columns = [
        "Achievement",
        "Jan %",
        "Feb %",
        "Mar %",
        "Apr %",
        "May %",
        "Jun %",
        "Jul %",
        "Aug %",
        "Sep %",
        "Oct %",
        "Nov %",
        "Des %",
        "YTD %",
        "Ach Q1 %",
        "Ach Q2 %",
        "Ach Q3 %",
        "Ach Q4 %",
        "VS Gap",
        "GP Margin (%)",
        "Noted"
    ]

    for col in percentage_columns:

        if col not in df.columns:
            continue

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

        if col == "VS Gap":
            df[col] = df[col].apply(
                format_vs_gap
            )
        else:
            df[col] = df[col].apply(
                format_percentage
            )

    # =========================================
    # REPLACE NAN
    # =========================================
    df = df.fillna("")

    return df.to_dict(
        orient="records"
    )


# =========================================
# SALES WITH YTD
# =========================================

def get_sales_with_ytd(
    region="commercial",
    headsales=False,
    unit_head=False
):

    # =========================================
    # REGIONAL
    # =========================================
    if region == "regional":

        if unit_head:
            df = get_registered_unit_head_regional()

        elif headsales:
            df = get_registered_headsales_regional()

        else:
            df = get_registered_regional_sales()

    # =========================================
    # COMMERCIAL
    # =========================================
    else:

        if unit_head:
            df = get_registered_unit_head_commercial()

        elif headsales:
            df = get_registered_headsales_commercial()

        else:
            df = get_registered_sales()

    return to_response(df)

# =========================================
# FILTER SALES BY TERRITORY
# =========================================

def get_sales_by_territory(
    keyword,
    region="commercial"
):

    # =========================================
    # LOAD DATA
    # =========================================
    if region == "regional":
        df = get_registered_regional_sales()
    else:
        df = get_registered_sales()

    # =========================================
    # FILTER TERRITORY
    # =========================================
    result = df[
        df["Teritory"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]

    return to_response (result)

# =========================================
# SEARCH SALES NAME
# =========================================

def search_sales_name(
    keyword,
    region="commercial"
):

    # =========================================
    # LOAD DATA
    # =========================================
    if region == "regional":
        df = get_registered_regional_sales()
    else:
        df = get_registered_sales()

    # =========================================
    # SEARCH NAME
    # =========================================
    result = df[
        df["Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]

    return to_response (result)


# =========================================
# SEARCH SALES METRIC
# =========================================

def search_sales_metric(
    keyword,
    column_name,
    region="commercial"
):

    # =========================================
    # LOAD DATA
    # =========================================
    if region == "regional":
        df = get_registered_regional_sales()
    else:
        df = get_registered_sales()

    # =========================================
    # SEARCH NAME
    # =========================================
    result = df[
        df["Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]

    # =========================================
    # RETURN SELECTED COLUMN
    # =========================================
    columns = [
        col for col in [
            "Name",
            "Teritory",
            column_name
        ]
        if col in result.columns
    ]
    print(result[["Name", "VS Gap"]])
    
    return to_response(
        result[columns]
    )

# =========================================
# SEARCH TOTAL PO
# =========================================

def search_sales_total_po(
    keyword,
    region="commercial"
):
    return search_sales_metric(
        keyword,
        "Total PO",
        region
    )

# =========================================
# SEARCH GAP ACH YTD
# =========================================

def search_sales_gap_ach_ytd(
    keyword,
    region="commercial"
):
    return search_sales_metric(
        keyword,
        "Gap Ach YTD",
        region
    )

# =========================================
# SEARCH LEADS ON PROGRESS
# =========================================

def search_sales_leads_on_progress(
    keyword,
    region="commercial"
):
    return search_sales_metric(
        keyword,
        "Leads on Progress",
        region
    )
    
# =========================================
# SEARCH VS GAP
# =========================================

def search_sales_vs_gap(
    keyword,
    region="commercial"
):
    return search_sales_metric(
        keyword,
        "VS Gap",
        region
    )

# =========================================
# FILTER SALES BY STATUS
# =========================================

def get_sales_by_status(
    status,
    region="commercial"
):

    # =========================================
    # LOAD DATA
    # =========================================
    if region == "regional":
        df = get_registered_regional_sales()
    else:
        df = get_registered_sales()

    # =========================================
    # FILTER STATUS
    # =========================================
    result = df[
        df["Status"]
        .astype(str)
        .str.lower()
        == status.lower()
    ]

    return to_response (result)

# =========================================
# SEARCH DATABASE SALES NAME
# =========================================

def search_sales_name_database(keyword):

    df = get_registered_database()

    result = df[
        df["Customer Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]

    return to_response(result)

# ==========================================
# SEARCH DATABASE APPLICANTS NAME
# ==========================================

def search_applicant_name(keyword):

    df = get_registered_database()

    result = df[
        df["Applicants Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]

    return to_response(result)

# ============================================
# SEARCH DATABASE BY DIVISION
# ============================================


def search_division(keyword):
    
    df = get_registered_database()
    
    result = df [
        df["Division"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]
    
    return to_response(result)

# ===========================================
# SEARCH DATABASE BY TERITORY
# ===========================================
def search_teritory_name(keyword):
    
    df = get_registered_database()
    
    result = df [
        df["Teritory"]
        .astype(str)
        .str.lower()
        .str.contains(
            keyword.lower(),
            na=False
        )
    ]
    
    return to_response(result)


