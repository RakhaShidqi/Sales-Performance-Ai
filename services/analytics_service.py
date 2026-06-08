import pandas as pd

from services.query_service import (
    get_registered_sales,
    get_registered_regional_sales,
    get_registered_headsales_commercial,
    get_registered_headsales_regional,
    get_registered_unit_head_commercial
)

# =========================================
# CLEAN METRIC
# =========================================

def clean_metric_dataframe(df, *column_names):

    df = df.copy()

    for column in column_names:

        if column not in df.columns:
            continue

        df[column] = (
            pd.to_numeric(
                df[column],
                errors="coerce"
            )
        )

    df = df.dropna(
        subset=["Name", *column_names]
    )

    return df


# =========================================
# SALES CALCULATION
# =========================================

def calculate_sales_achievement(
    df,
    value_col,
    percent_col
):

    df = df.copy()

    df = df[df["No"] != 1]

    df = clean_metric_dataframe(
        df,
        value_col,
        percent_col
    )

    total_sales = len(df)

    if total_sales == 0:
        return {
            "achievement_percent": 0.0,
            "achievement_value": 0.0,
            "total_sales": 0
        }

    return {
        "achievement": round(
            df[percent_col].mean(),
            2
        ),
        "achievement_value": round(
            df[value_col].sum(),
            2
        ),
        "total_sales": total_sales
    }

# =========================================
# HEAD SALES CALCULATION
# =========================================

def calculate_headsales_achievement(
    df,
    value_col,
    percent_col
):

    df = df.copy()

    df = df[df["No"] == 1]

    df = df[
        ~df["Teritory"]
        .astype(str)
        .str.upper()
        .isin([
            "VP OF COMMERCIAL",
            "VP OF REGIONAL"
        ])
    ]

    df = clean_metric_dataframe(
        df,
        value_col,
        percent_col
    )

    total_headsales = len(df)

    if total_headsales == 0:
        return {
            "achievement_percent": 0.0,
            "achievement_value": 0.0,
            "total_headsales": 0
        }

    return {
        "achievement": round(
            df[percent_col].mean(),
            2
        ),
        "achievement_value": round(
            df[value_col].sum(),
            2
        ),
        "total_headsales": total_headsales
    }


# =========================================
# GENERIC HELPERS
# =========================================

def sales_metric(loader, value_col, percent_col):
    return calculate_sales_achievement(loader(), value_col, percent_col)


def headsales_metric(loader, value_col, percent_col):
    return calculate_headsales_achievement(loader(), value_col, percent_col)


# =========================================
# COMMERCIAL SALES
# =========================================

def get_minimum_achievement_jan_commercial():
    return sales_metric(get_registered_sales, "JAN", "Jan %")

def get_minimum_achievement_feb_commercial():
    return sales_metric(get_registered_sales, "FEB", "Feb %")

def get_minimum_achievement_mar_commercial():
    return sales_metric(get_registered_sales, "MAR", "Mar %")

def get_minimum_achievement_apr_commercial():
    return sales_metric(get_registered_sales, "APR", "Apr %")

def get_minimum_achievement_may_commercial():
    return sales_metric(get_registered_sales, "MAY", "May %")

def get_minimum_achievement_jun_commercial():
    return sales_metric(get_registered_sales, "JUN", "Jun %")

def get_minimum_achievement_jul_commercial():
    return sales_metric(get_registered_sales, "JUL", "Jul %")

def get_minimum_achievement_aug_commercial():
    return sales_metric(get_registered_sales, "AUG", "Aug %")

def get_minimum_achievement_sep_commercial():
    return sales_metric(get_registered_sales, "SEP", "Sep %")

def get_minimum_achievement_oct_commercial():
    return sales_metric(get_registered_sales, "OCT", "Oct %")

def get_minimum_achievement_nov_commercial():
    return sales_metric(get_registered_sales, "NOV", "Nov %")

def get_minimum_achievement_dec_commercial():
    return sales_metric(get_registered_sales, "DEC", "Dec %")

def get_minimum_achievement_ytd_commercial():
    return sales_metric(get_registered_sales, "Total YTD", "YTD %")

def get_minimum_achievement_q1_commercial():
    return sales_metric(get_registered_sales, "Ach Q1", "Ach Q1 %")

def get_minimum_achievement_q2_commercial():
    return sales_metric(get_registered_sales, "Ach Q2", "Ach Q2 %")

def get_minimum_achievement_q3_commercial():
    return sales_metric(get_registered_sales, "Ach Q3", "Ach Q3 %")

def get_minimum_achievement_q4_commercial():
    return sales_metric(get_registered_sales, "Ach Q4", "Ach Q4 %")


# =========================================
# COMMERCIAL HEAD SALES
# =========================================

def get_minimum_achievement_headsales_jan_commercial():
    return headsales_metric(get_registered_headsales_commercial, "JAN", "Jan %")

def get_minimum_achievement_headsales_feb_commercial():
    return headsales_metric(get_registered_headsales_commercial, "FEB", "Feb %")

def get_minimum_achievement_headsales_mar_commercial():
    return headsales_metric(get_registered_headsales_commercial, "MAR", "Mar %")

def get_minimum_achievement_headsales_apr_commercial():
    return headsales_metric(get_registered_headsales_commercial, "APR", "Apr %")

def get_minimum_achievement_headsales_may_commercial():
    return headsales_metric(get_registered_headsales_commercial, "MAY", "May %")

def get_minimum_achievement_headsales_jun_commercial():
    return headsales_metric(get_registered_headsales_commercial, "JUN", "Jun %")

def get_minimum_achievement_headsales_jul_commercial():
    return headsales_metric(get_registered_headsales_commercial, "JUL", "Jul %")

def get_minimum_achievement_headsales_aug_commercial():
    return headsales_metric(get_registered_headsales_commercial, "AUG", "Aug %")

def get_minimum_achievement_headsales_sep_commercial():
    return headsales_metric(get_registered_headsales_commercial, "SEP", "Sep %")

def get_minimum_achievement_headsales_oct_commercial():
    return headsales_metric(get_registered_headsales_commercial, "OCT", "Oct %")

def get_minimum_achievement_headsales_nov_commercial():
    return headsales_metric(get_registered_headsales_commercial, "NOV", "Nov %")

def get_minimum_achievement_headsales_dec_commercial():
    return headsales_metric(get_registered_headsales_commercial, "DEC", "Dec %")

def get_minimum_achievement_headsales_ytd_commercial():
    return headsales_metric(get_registered_headsales_commercial, "Total YTD", "YTD %")

def get_minimum_achievement_headsales_q1_commercial():
    return headsales_metric(get_registered_headsales_commercial, "Ach Q1", "Ach Q1 %")

def get_minimum_achievement_headsales_q2_commercial():
    return headsales_metric(get_registered_headsales_commercial, "Ach Q2", "Ach Q2 %")

def get_minimum_achievement_headsales_q3_commercial():
    return headsales_metric(get_registered_headsales_commercial, "Ach Q3", "Ach Q3 %")

def get_minimum_achievement_headsales_q4_commercial():
    return headsales_metric(get_registered_headsales_commercial, "Ach Q4", "Ach Q4 %")


# =========================================
# UNIT HEAD COMMERCIAL
# =========================================

def get_minimum_achievement_unit_head_jan_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "JAN", "Jan %")

def get_minimum_achievement_unit_head_feb_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "FEB", "Feb %")

def get_minimum_achievement_unit_head_mar_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "MAR", "Mar %")

def get_minimum_achievement_unit_head_apr_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "APR", "Apr %")

def get_minimum_achievement_unit_head_may_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "MAY", "May %")

def get_minimum_achievement_unit_head_jun_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "JUN", "Jun %")

def get_minimum_achievement_unit_head_jul_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "JUL", "Jul %")

def get_minimum_achievement_unit_head_aug_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "AUG", "Aug %")

def get_minimum_achievement_unit_head_sep_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "SEP", "Sep %")

def get_minimum_achievement_unit_head_oct_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "OCT", "Oct %")

def get_minimum_achievement_unit_head_nov_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "NOV", "Nov %")

def get_minimum_achievement_unit_head_dec_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "DEC", "Dec %")

def get_minimum_achievement_unit_head_ytd_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "Total YTD", "YTD %")

def get_minimum_achievement_unit_head_q1_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "Ach Q1", "Ach Q1 %")

def get_minimum_achievement_unit_head_q2_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "Ach Q2", "Ach Q2 %")

def get_minimum_achievement_unit_head_q3_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "Ach Q3", "Ach Q3 %")

def get_minimum_achievement_unit_head_q4_commercial():
    return headsales_metric(get_registered_unit_head_commercial, "Ach Q4", "Ach Q4 %")


# =========================================
# REGIONAL SALES
# =========================================

def get_minimum_achievement_jan_regional():
    return sales_metric(get_registered_regional_sales, "JAN", "Jan %")

def get_minimum_achievement_feb_regional():
    return sales_metric(get_registered_regional_sales, "FEB", "Feb %")

def get_minimum_achievement_mar_regional():
    return sales_metric(get_registered_regional_sales, "MAR", "Mar %")

def get_minimum_achievement_apr_regional():
    return sales_metric(get_registered_regional_sales, "APR", "Apr %")

def get_minimum_achievement_may_regional():
    return sales_metric(get_registered_regional_sales, "MAY", "May %")

def get_minimum_achievement_jun_regional():
    return sales_metric(get_registered_regional_sales, "JUN", "Jun %")

def get_minimum_achievement_jul_regional():
    return sales_metric(get_registered_regional_sales, "JUL", "Jul %")

def get_minimum_achievement_aug_regional():
    return sales_metric(get_registered_regional_sales, "AUG", "Aug %")

def get_minimum_achievement_sep_regional():
    return sales_metric(get_registered_regional_sales, "SEP", "Sep %")

def get_minimum_achievement_oct_regional():
    return sales_metric(get_registered_regional_sales, "OCT", "Oct %")

def get_minimum_achievement_nov_regional():
    return sales_metric(get_registered_regional_sales, "NOV", "Nov %")

def get_minimum_achievement_dec_regional():
    return sales_metric(get_registered_regional_sales, "DEC", "Dec %")

def get_minimum_achievement_ytd_regional():
    return sales_metric(get_registered_regional_sales, "Total YTD", "YTD %")

def get_minimum_achievement_q1_regional():
    return sales_metric(get_registered_regional_sales, "Ach Q1", "Ach Q1 %")

def get_minimum_achievement_q2_regional():
    return sales_metric(get_registered_regional_sales, "Ach Q2", "Ach Q2 %")

def get_minimum_achievement_q3_regional():
    return sales_metric(get_registered_regional_sales, "Ach Q3", "Ach Q3 %")

def get_minimum_achievement_q4_regional():
    return sales_metric(get_registered_regional_sales, "Ach Q4", "Ach Q4 %")


# =========================================
# REGIONAL HEAD SALES
# =========================================

def get_minimum_achievement_headsales_jan_regional():
    return headsales_metric(get_registered_headsales_regional, "JAN", "Jan %")

def get_minimum_achievement_headsales_feb_regional():
    return headsales_metric(get_registered_headsales_regional, "FEB", "Feb %")

def get_minimum_achievement_headsales_mar_regional():
    return headsales_metric(get_registered_headsales_regional, "MAR", "Mar %")

def get_minimum_achievement_headsales_apr_regional():
    return headsales_metric(get_registered_headsales_regional, "APR", "Apr %")

def get_minimum_achievement_headsales_may_regional():
    return headsales_metric(get_registered_headsales_regional, "MAY", "May %")

def get_minimum_achievement_headsales_jun_regional():
    return headsales_metric(get_registered_headsales_regional, "JUN", "Jun %")

def get_minimum_achievement_headsales_jul_regional():
    return headsales_metric(get_registered_headsales_regional, "JUL", "Jul %")

def get_minimum_achievement_headsales_aug_regional():
    return headsales_metric(get_registered_headsales_regional, "AUG", "Aug %")

def get_minimum_achievement_headsales_sep_regional():
    return headsales_metric(get_registered_headsales_regional, "SEP", "Sep %")

def get_minimum_achievement_headsales_oct_regional():
    return headsales_metric(get_registered_headsales_regional, "OCT", "Oct %")

def get_minimum_achievement_headsales_nov_regional():
    return headsales_metric(get_registered_headsales_regional, "NOV", "Nov %")

def get_minimum_achievement_headsales_dec_regional():
    return headsales_metric(get_registered_headsales_regional, "DEC", "Dec %")

def get_minimum_achievement_headsales_ytd_regional():
    return headsales_metric(get_registered_headsales_regional, "Total YTD", "YTD %")

def get_minimum_achievement_headsales_q1_regional():
    return headsales_metric(get_registered_headsales_regional, "Ach Q1", "Ach Q1 %")

def get_minimum_achievement_headsales_q2_regional():
    return headsales_metric(get_registered_headsales_regional, "Ach Q2", "Ach Q2 %")

def get_minimum_achievement_headsales_q3_regional():
    return headsales_metric(get_registered_headsales_regional, "Ach Q3", "Ach Q3 %")

def get_minimum_achievement_headsales_q4_regional():
    return headsales_metric(get_registered_headsales_regional, "Ach Q4", "Ach Q4 %")