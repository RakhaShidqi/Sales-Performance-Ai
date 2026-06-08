import pandas as pd

from services.query_service import (
    to_response,
    get_registered_sales,
    get_registered_smb_sales,
    get_registered_enterprise_sales,
    get_registered_regional_sales,
    get_registered_headsales_commercial,
    get_registered_headsales_regional,
    get_registered_unit_head_commercial
)
from services.analytics_service import (

    # =========================================
    # SALES ACHIEVEMENT
    # =========================================
    get_minimum_achievement_jan_commercial,
    get_minimum_achievement_feb_commercial,
    get_minimum_achievement_mar_commercial,
    get_minimum_achievement_apr_commercial,
    get_minimum_achievement_may_commercial,
    get_minimum_achievement_jun_commercial,
    get_minimum_achievement_jul_commercial,
    get_minimum_achievement_aug_commercial,
    get_minimum_achievement_sep_commercial,
    get_minimum_achievement_oct_commercial,
    get_minimum_achievement_nov_commercial,
    get_minimum_achievement_dec_commercial,
    
    get_minimum_achievement_ytd_commercial,
    get_minimum_achievement_q1_commercial,
    get_minimum_achievement_q2_commercial,
    get_minimum_achievement_q3_commercial,
    get_minimum_achievement_q4_commercial,

    get_minimum_achievement_jan_regional,
    get_minimum_achievement_feb_regional,
    get_minimum_achievement_mar_regional,
    get_minimum_achievement_apr_regional,
    get_minimum_achievement_may_regional,
    get_minimum_achievement_jun_regional,
    get_minimum_achievement_jul_regional,
    get_minimum_achievement_aug_regional,
    get_minimum_achievement_sep_regional,
    get_minimum_achievement_oct_regional,
    get_minimum_achievement_nov_regional,
    get_minimum_achievement_dec_regional,
    
    get_minimum_achievement_ytd_regional,
    get_minimum_achievement_q1_regional,
    get_minimum_achievement_q2_regional,
    get_minimum_achievement_q3_regional,
    get_minimum_achievement_q4_regional,

    # =========================================
    # HEAD SALES ACHIEVEMENT
    # =========================================
    
    get_minimum_achievement_headsales_jan_commercial,
    get_minimum_achievement_headsales_feb_commercial,
    get_minimum_achievement_headsales_mar_commercial,
    get_minimum_achievement_headsales_apr_commercial,
    get_minimum_achievement_headsales_may_commercial,
    get_minimum_achievement_headsales_jun_commercial,
    get_minimum_achievement_headsales_jul_commercial,
    get_minimum_achievement_headsales_aug_commercial,
    get_minimum_achievement_headsales_sep_commercial,
    get_minimum_achievement_headsales_oct_commercial,
    get_minimum_achievement_headsales_nov_commercial,
    get_minimum_achievement_headsales_dec_commercial,
    
    get_minimum_achievement_headsales_ytd_commercial,
    get_minimum_achievement_headsales_q1_commercial,
    get_minimum_achievement_headsales_q2_commercial,
    get_minimum_achievement_headsales_q3_commercial,
    get_minimum_achievement_headsales_q4_commercial,


    get_minimum_achievement_headsales_jan_regional,
    get_minimum_achievement_headsales_feb_regional,
    get_minimum_achievement_headsales_mar_regional,
    get_minimum_achievement_headsales_apr_regional,
    get_minimum_achievement_headsales_may_regional,
    get_minimum_achievement_headsales_jun_regional,
    get_minimum_achievement_headsales_jul_regional,
    get_minimum_achievement_headsales_aug_regional,
    get_minimum_achievement_headsales_sep_regional,
    get_minimum_achievement_headsales_oct_regional,
    get_minimum_achievement_headsales_nov_regional,
    get_minimum_achievement_headsales_dec_regional,
    
    get_minimum_achievement_headsales_ytd_regional,
    get_minimum_achievement_headsales_q1_regional,
    get_minimum_achievement_headsales_q2_regional,
    get_minimum_achievement_headsales_q3_regional,
    get_minimum_achievement_headsales_q4_regional,
    
    # =============================================
    # UNIT HEAD ACHIEVEMENT
    # =============================================
    
    get_minimum_achievement_unit_head_jan_commercial,
    get_minimum_achievement_unit_head_feb_commercial,
    get_minimum_achievement_unit_head_mar_commercial,
    get_minimum_achievement_unit_head_apr_commercial,
    get_minimum_achievement_unit_head_may_commercial,
    get_minimum_achievement_unit_head_jun_commercial,
    get_minimum_achievement_unit_head_jul_commercial,
    get_minimum_achievement_unit_head_aug_commercial,
    get_minimum_achievement_unit_head_sep_commercial,
    get_minimum_achievement_unit_head_oct_commercial,
    get_minimum_achievement_unit_head_nov_commercial,
    get_minimum_achievement_unit_head_dec_commercial,
    
    get_minimum_achievement_unit_head_ytd_commercial,
    get_minimum_achievement_unit_head_q1_commercial,
    get_minimum_achievement_unit_head_q2_commercial,
    get_minimum_achievement_unit_head_q3_commercial,
    get_minimum_achievement_unit_head_q4_commercial
)

# =========================================
# COLUMN PERCENT MAP
# =========================================

COLUMN_PERCENT_MAP = {
    "jan": "Jan %", 
    "feb": "Feb %",
    "mar":"Mar %",
    "apr":"Apr %",
    "may": "May %",
    "jun":"Jun %",
    "jul":"Jul %",
    "aug":"Aug %",
    "sep":"Sep %",
    "oct":"Oct %",
    "nov":"Nov %",
    "dec":"Dec %",
    "ytd":"YTD %",
    "q1":"Ach Q1 %",
    "q2":"Ach Q2 %",
    "q3": "Ach Q3 %",
    "q4": "Ach Q4 %"
}

# =========================================
# COLUMN VALUE MAP
# =========================================

COLUMN_VALUE_MAP = {
    "jan":"JAN",
    "feb":"FEB",
    "mar":"MAR",
    "apr":"APR",
    "may":"MAY",
    "jun":"JUN",
    "jul":"JUL",
    "aug":"AUG",
    "sep":"SEP",
    "oct":"OCT",
    "nov":"NOV",
    "dec":"DEC",
    "ytd":"Total YTD",
    "q1":"Ach Q1",
    "q2":"Ach Q2",
    "q3":"Ach Q3",
    "q4":"Ach Q4"
}


# =========================================
# CONFIG
# =========================================

METRIC_CONFIG = {

    # =========================================
    # COMMERCIAL
    # =========================================
    "commercial": {

        # SALES
        "sales_loader": get_registered_sales,

        "sales_metrics": {
            "jan": get_minimum_achievement_jan_commercial,
            "feb": get_minimum_achievement_feb_commercial,
            "mar": get_minimum_achievement_mar_commercial,
            "apr": get_minimum_achievement_apr_commercial,
            "may": get_minimum_achievement_may_commercial,
            "jun": get_minimum_achievement_jun_commercial,
            "jul": get_minimum_achievement_jul_commercial,
            "aug": get_minimum_achievement_aug_commercial,
            "sep": get_minimum_achievement_sep_commercial,
            "oct": get_minimum_achievement_oct_commercial,
            "nov": get_minimum_achievement_nov_commercial,
            "dec": get_minimum_achievement_dec_commercial,
            "ytd": get_minimum_achievement_ytd_commercial,
            "q1": get_minimum_achievement_q1_commercial,
            "q2": get_minimum_achievement_q2_commercial,
            "q3": get_minimum_achievement_q3_commercial,
            "q4": get_minimum_achievement_q4_commercial
        },
        
        # =========================================
        # SMB SALES
        # =========================================
        "smb_loader": get_registered_smb_sales,

         # =========================================
        # ENTERPRISE SALES
        # =========================================
        "enterprise_loader": get_registered_enterprise_sales,
        
        # HEAD SALES
        "headsales_loader": get_registered_headsales_commercial,

        "headsales_metrics": {
            "jan": get_minimum_achievement_headsales_jan_commercial,
            "feb": get_minimum_achievement_headsales_feb_commercial,
            "mar": get_minimum_achievement_headsales_mar_commercial,
            "apr": get_minimum_achievement_headsales_apr_commercial,
            "may": get_minimum_achievement_headsales_may_commercial,
            "jun": get_minimum_achievement_headsales_jun_commercial,
            "jul": get_minimum_achievement_headsales_jul_commercial,
            "aug": get_minimum_achievement_headsales_aug_commercial,
            "sep": get_minimum_achievement_headsales_sep_commercial,
            "oct": get_minimum_achievement_headsales_oct_commercial,
            "nov": get_minimum_achievement_headsales_nov_commercial,
            "dec": get_minimum_achievement_headsales_dec_commercial,
            "ytd": get_minimum_achievement_headsales_ytd_commercial,
            "q1": get_minimum_achievement_headsales_q1_commercial,
            "q2": get_minimum_achievement_headsales_q2_commercial,
            "q3": get_minimum_achievement_headsales_q3_commercial,
            "q4": get_minimum_achievement_headsales_q4_commercial
        },
        
         # =========================================
         # UNIT HEAD
         # =========================================
        "unit_head_loader": get_registered_unit_head_commercial,

        "unit_head_metrics": {
            "jan": get_minimum_achievement_unit_head_jan_commercial,
            "feb": get_minimum_achievement_unit_head_feb_commercial,
            "mar": get_minimum_achievement_unit_head_mar_commercial,
            "apr": get_minimum_achievement_unit_head_apr_commercial,
            "may": get_minimum_achievement_unit_head_may_commercial,
            "jun": get_minimum_achievement_unit_head_jun_commercial,
            "jul": get_minimum_achievement_unit_head_jul_commercial,
            "aug": get_minimum_achievement_unit_head_aug_commercial,
            "sep": get_minimum_achievement_unit_head_sep_commercial,
            "oct": get_minimum_achievement_unit_head_oct_commercial,
            "nov": get_minimum_achievement_unit_head_nov_commercial,
            "dec": get_minimum_achievement_unit_head_dec_commercial,
            "ytd": get_minimum_achievement_unit_head_ytd_commercial,
            "q1": get_minimum_achievement_unit_head_q1_commercial,
            "q2": get_minimum_achievement_unit_head_q2_commercial,
            "q3": get_minimum_achievement_unit_head_q3_commercial,
            "q4": get_minimum_achievement_unit_head_q4_commercial
        },
    },
         
        
         # =========================================
         # REGIONAL
         # =========================================
        "regional": {

            # SALES
            "sales_loader": get_registered_regional_sales,

            "sales_metrics": {
                "jan": get_minimum_achievement_jan_regional,
                "feb": get_minimum_achievement_feb_regional,
                "mar": get_minimum_achievement_mar_regional,
                "apr": get_minimum_achievement_apr_regional,
                "may": get_minimum_achievement_may_regional,
                "jun": get_minimum_achievement_jun_regional,
                "jul": get_minimum_achievement_jul_regional,
                "aug": get_minimum_achievement_aug_regional,
                "sep": get_minimum_achievement_sep_regional,
                "oct": get_minimum_achievement_oct_regional,
                "nov": get_minimum_achievement_nov_regional,
                "dec": get_minimum_achievement_dec_regional,
                "ytd": get_minimum_achievement_ytd_regional,
                "q1": get_minimum_achievement_q1_regional,
                "q2": get_minimum_achievement_q2_regional,
                "q3": get_minimum_achievement_q3_regional,
                "q4": get_minimum_achievement_q4_regional
            },

            # HEAD SALES
            "headsales_loader": get_registered_headsales_regional,

            "headsales_metrics": {
                "jan": get_minimum_achievement_headsales_jan_regional,
                "feb": get_minimum_achievement_headsales_feb_regional,
                "mar": get_minimum_achievement_headsales_mar_regional,
                "apr": get_minimum_achievement_headsales_apr_regional,
                "may": get_minimum_achievement_headsales_may_regional,
                "jun": get_minimum_achievement_headsales_jun_regional,
                "jul": get_minimum_achievement_headsales_jul_regional,
                "aug": get_minimum_achievement_headsales_aug_regional,
                "sep": get_minimum_achievement_headsales_sep_regional,
                "oct": get_minimum_achievement_headsales_oct_regional,
                "nov": get_minimum_achievement_headsales_nov_regional,
                "dec": get_minimum_achievement_headsales_dec_regional,
                "ytd": get_minimum_achievement_headsales_ytd_regional,
                "q1": get_minimum_achievement_headsales_q1_regional,
                "q2": get_minimum_achievement_headsales_q2_regional,
                "q3": get_minimum_achievement_headsales_q3_regional,
                "q4": get_minimum_achievement_headsales_q4_regional
            }
        }
    }

       
# =========================================
# TERITORY FILTER
# =========================================

def filter_teritory(df, teritory):

    if not teritory:
        return df

    teritory_value = teritory.lower().strip()

    # =========================================
    # SMB ONLY
    # =========================================
    if teritory_value == "smb":

        return df[
            df["Teritory"]
            .astype(str)
            .str.lower()
            .str.strip()
            .str.startswith("smb")
        ]

    # =========================================
    # ENTERPRISE = NON SMB
    # =========================================
    elif teritory_value == "enterprise":

        return df[
            ~df["Teritory"]
            .astype(str)
            .str.lower()
            .str.strip()
            .str.startswith("smb")
        ]

    # =========================================
    # DEFAULT
    # =========================================
    return df[
        df["Teritory"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.startswith(teritory_value)
    ]


# =========================================
# PERFORMANCE ENGINE
# =========================================

def get_sales_performance(
    metric="ytd",
    region="commercial",
    teritory=None,
    headsales=False,
    unit_head=False,
    smb=False,
    enterprise=False
):

    metric = metric.lower()
    region = region.lower()

    # =========================================
    # VALIDATION REGION
    # =========================================
    if region not in METRIC_CONFIG:
        return {
            "error": "Invalid region",
            "available_region": list(METRIC_CONFIG.keys())
        }

    config = METRIC_CONFIG[region]

    # =========================================
    # SELECT TYPE
    # =========================================
    if unit_head:

        loader = config["unit_head_loader"]
        metric_map = config["unit_head_metrics"]
        type_name = "UNIT HEAD"

    # =========================================
    # HEAD SALES
    # =========================================
    elif headsales:

        loader = config["headsales_loader"]
        metric_map = config["headsales_metrics"]
        type_name = "HEAD SALES"

    # =========================================
    # SMB SALES
    # =========================================
    elif smb:

        loader = config["smb_loader"]
        metric_map = config["sales_metrics"]
        type_name = "SMB SALES"

    # =========================================
    # ENTERPRISE SALES
    # =========================================
    elif enterprise:

        loader = config["enterprise_loader"]
        metric_map = config["sales_metrics"]
        type_name = "ENTERPRISE SALES"

    # =========================================
    # ALL SALES
    # =========================================
    else:

        loader = config["sales_loader"]
        metric_map = config["sales_metrics"]
        type_name = "ALL SALES"

    # =========================================
    # VALIDATION METRIC
    # =========================================
    if metric not in metric_map:
        return {
            "error": "Invalid metric",
            "available_metric": list(metric_map.keys())
        }

    # =========================================
    # LOAD DATA
    # =========================================
    df = loader()

    # =========================================
    # FILTER TERITORY
    # =========================================
    df = filter_teritory(df, teritory)

    # =========================================
    # COLUMN
    # =========================================
    percent_column = COLUMN_PERCENT_MAP[metric]
    value_column = COLUMN_VALUE_MAP[metric]
    
# =========================================
# CLEAN NUMERIC
# =========================================
    df = df.copy()

    def convert_excel_percent(value):

        if pd.isna(value):
            return 0.0

        try:

            # string cleanup
            if isinstance(value, str):

                value = (
                    value
                    .replace("%", "")
                    .replace(",", ".")
                    .strip()
                )

            value = float(value)

            # =========================================
            # EXCEL FRACTION
            # 0.043182 -> 4.3182
            # =========================================
            # if value <= 1:
            #     value = value * 100

            return round(value, 1)

        except:
            return 0.0


    df[percent_column] = df[percent_column].apply(
        convert_excel_percent
    )

    # remove invalid
    df = df.dropna(subset=[percent_column])

    # force float
    df[percent_column] = pd.to_numeric(
        df[percent_column],
        errors="coerce"
    ).fillna(0.0)

    print("AFTER NORMALIZE")
    print(df[["Name", percent_column]].head())

    # =========================================
    # MINIMUM ACHIEVEMENT
    # =========================================
    metric_result = metric_map[metric]()

    minimum_achievement = metric_result["achievement"]
    minimum_achievement_value = metric_result["achievement_value"]

    # =========================================
    # RENAME COLUMN
    # =========================================
    df = df.rename(columns={
        percent_column: "Achievement",
        value_column: "Achievement Value"
    })

    # =========================================
    # PERFORMANCE LOGIC
    # =========================================
    def status(value):

        if value >= minimum_achievement:
            return "Perform"

        return "Underperform"

    df["Performance"] = df["Achievement"].apply(status)

    # =========================================
    # SUMMARY
    # =========================================
    total_sales = len(df)

    total_perform = int(
        (df["Performance"] == "Perform").sum()
    )

    total_underperform = int(
        (df["Performance"] == "Underperform").sum()
    )

    # =========================================
    # OUTPUT
    # =========================================
    output_df = df[[
        "Name",
        "Join Date",
        "Teritory",
        "Achievement",
        "Achievement Value",
        "Performance"
    ]]

    return {
        "region": region.upper(),
        "type": type_name,
        "metric": metric.upper(),
        "teritory": teritory if teritory else "ALL",

        # THRESHOLD
        "minimum_achievement": round(
            minimum_achievement,
            1
        ),
        
        "minimum_achievement_value": round(
            minimum_achievement_value ,0
        ),

        # SUMMARY
        "total_sales": total_sales,
        "total_perform": total_perform,
        "total_underperform": total_underperform,

        # PERCENTAGE
        "perform_percentage": round(
            (total_perform / total_sales) * 100,
            2
        ) if total_sales > 0 else 0,

        "underperform_percentage": round(
            (total_underperform / total_sales) * 100,
            2
        ) if total_sales > 0 else 0,

        # DATA
        "data": to_response(output_df)
    }