import pandas as pd

from services.query_service import (
    get_registered_sales,
    get_registered_regional_sales,
    get_registered_smb_sales,
    get_registered_enterprise_sales
)

# =========================================
# REGION CONFIG
# =========================================

REGION_LOADER = {
    "commercial": get_registered_sales,
    "regional": get_registered_regional_sales
}

# =========================================
# DIVISION CONFIG
# COMMERCIAL ONLY
# =========================================

DIVISION_LOADER = {
    "commercial_smb": get_registered_smb_sales,
    "commercial_enterprise": get_registered_enterprise_sales
}

# =========================================
# METRIC MAPPING
# =========================================

METRIC_COLUMN = {
    "jan": "Jan %",
    "feb": "Feb %",
    "mar": "Mar %",
    "apr": "Apr %",
    "may": "May %",
    "jun": "Jun %",
    "jul": "Jul %",
    "aug": "Aug %",
    "sep": "Sep %",
    "oct": "Oct %",
    "nov": "Nov %",
    "dec": "Dec %",
    "ytd": "YTD %",
    "q1": "Ach Q1 %",
    "q2": "Ach Q2 %",
    "q3": "Ach Q3 %",
    "q4": "Ach Q4 %"
}


# =========================================
# PREPARE DATA
# =========================================

def prepare_ranking_data(
    metric="ytd",
    region="commercial",
    smb=False,
    enterprise=False
):

    metric = metric.lower()
    region = region.lower()

    # =========================================
    # VALIDATION
    # =========================================
    if metric not in METRIC_COLUMN:
        raise ValueError(
            f"Metric '{metric}' not valid"
        )

    if region not in REGION_LOADER:
        raise ValueError(
            f"Region '{region}' not valid"
        )

    # =========================================
    # REGIONAL VALIDATION
    # =========================================
    if region == "regional" and (smb or enterprise):
        raise ValueError(
            "Regional does not support SMB or Enterprise division"
        )

    # =========================================
    # LOAD DATA
    # =========================================

    # SMB
    if smb:

        df = DIVISION_LOADER[
            "commercial_smb"
        ]()

    # ENTERPRISE
    elif enterprise:

        df = DIVISION_LOADER[
            "commercial_enterprise"
        ]()

    # ALL
    else:

        df = REGION_LOADER[region]()

    # =========================================
    # METRIC COLUMN
    # =========================================
    metric_column = METRIC_COLUMN[metric]

    # =========================================
    # CLEAN NUMERIC
    # =========================================
    df = df.copy()

    df[metric_column] = pd.to_numeric(
        df[metric_column],
        errors="coerce"
    )

    df = df[
        df[metric_column].notna()
    ]

    # =========================================
    # ACHIEVEMENT
    # =========================================
    df["Achievement"] = (
        df[metric_column]
        .round(2)
    )

    return df


# =========================================
# TOP SALES
# =========================================

def get_top_sales(
    metric="ytd",
    region="commercial",
    limit=10,
    smb=False,
    enterprise=False
):

    df = prepare_ranking_data(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    df = (
        df
        .sort_values(
            by="Achievement",
            ascending=False
        )
        .head(limit)
    )

    # =========================================
    # SALES TYPE
    # =========================================
    if smb:

        ranking_group = "SMB SALES"

    elif enterprise:

        ranking_group = "ENTERPRISE SALES"

    else:

        ranking_group = "ALL SALES"

    data = []

    for i, row in enumerate(
        df.to_dict(orient="records"),
        start=1
    ):

        data.append({
            "rank": i,
            "name": row["Name"],
            "teritory": row["Teritory"],
            "achievement": f'{row["Achievement"]:.2f}%',
            "status": row["Status"]
        })

    return {
        "region": region.upper(),
        "metric": metric.upper(),
        "ranking_type": "TOP PERFORMER",
        "sales_type": ranking_group,
        "total_data": len(data),
        "data": data
    }


# =========================================
# BOTTOM SALES
# =========================================

def get_bottom_sales(
    metric="ytd",
    region="commercial",
    limit=10,
    smb=False,
    enterprise=False
):

    df = prepare_ranking_data(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    df = (
        df
        .sort_values(
            by="Achievement",
            ascending=True
        )
        .head(limit)
    )

    # =========================================
    # SALES TYPE
    # =========================================
    if smb:

        ranking_group = "SMB SALES"

    elif enterprise:

        ranking_group = "ENTERPRISE SALES"

    else:

        ranking_group = "ALL SALES"

    data = []

    for i, row in enumerate(
        df.to_dict(orient="records"),
        start=1
    ):

        data.append({
            "rank": i,
            "name": row["Name"],
            "teritory": row["Teritory"],
            "achievement": f'{row["Achievement"]:.2f}%',
            "status": row["Status"]
        })

    return {
        "region": region.upper(),
        "metric": metric.upper(),
        "ranking_type": "UNDERPERFORM",
        "sales_type": ranking_group,
        "total_data": len(data),
        "data": data
    }