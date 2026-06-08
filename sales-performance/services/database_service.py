import pandas as pd

from services.query_service import (
    to_response,
    get_registered_regional_sales,
    get_registered_sales
)

def get_database_sales_with_division(
    division="Commercial"
):

    # =========================================
    # REGIONAL
    # =========================================
    if division == "Regional":

            df = get_registered_regional_sales()

    # =========================================
    # COMMERCIAL
    # =========================================
    else:
            df = get_registered_sales()

    return to_response(df)

# =========================================
# FILTER SALES BY TERRITORY
# =========================================

def get_database_sales_by_territory(
    territory,
    division="Commercial"
):

    # =========================================
    # LOAD DATA
    # =========================================
    if division == "regional":
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
        .str.strip()
        .str.startswith(
            territory.lower()
        )
    ]

    return result



