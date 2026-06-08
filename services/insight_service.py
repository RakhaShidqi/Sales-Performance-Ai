import pandas as pd

from services.performance_service import get_sales_performance
from services.ranking_service import get_top_sales, get_bottom_sales


# =========================================
# SAFE CONVERTER
# =========================================

def safe_to_float(value):
    try:
        if value is None or pd.isna(value):
            return 0.0
        return float(str(value).replace("%", "").strip())
    except:
        return 0.0


# =========================================
# TEAM INSIGHT (CLEAN + REGION SUPPORT)
# =========================================

def get_team_insight(metric="ytd", region="commercial"):

    metric = metric.lower()
    region = region.lower()

    performance_data = get_sales_performance(
        metric=metric,
        region=region
    )

    total_sales = performance_data.get("total_sales", 0)
    total_perform = performance_data.get("total_perform", 0)
    total_underperform = performance_data.get("total_underperform", 0)

    minimum_achievement = safe_to_float(
        performance_data.get("minimum_achievement", 0)
    )

    sales_data = performance_data.get("data", [])
    df = pd.DataFrame(sales_data)

    insights = []

    # =========================================
    # GUARD CLAUSE
    # =========================================

    if total_sales == 0:
        return {
            "region": region.upper(),
            "metric": metric.upper(),
            "minimum_achievement": f"{minimum_achievement:.2f}%",
            "total_sales": 0,
            "total_perform": 0,
            "total_underperform": 0,
            "insights": ["No sales data available."]
        }

    # =========================================
    # PERFORMANCE RATE (FIX LOGIC)
    # =========================================

    perform_percentage = round(
        (total_perform / total_sales) * 100,
        2
    ) if total_sales else 0

    if perform_percentage >= minimum_achievement:
        insights.append(
            f"Performance {region.upper()} sudah mencapai target minimum ({minimum_achievement:.2f}%). "
            f"Actual performance {perform_percentage}%."
        )
    else:
        insights.append(
            f"Performance {region.upper()} masih di bawah target minimum ({minimum_achievement:.2f}%). "
            f"Actual performance {perform_percentage}%."
        )

    # =========================================
    # UNDERPERFORM
    # =========================================

    if total_underperform > 0:
        insights.append(
            f"{total_underperform} sales masih underperform di {region.upper()}."
        )

    # =========================================
    # SAFE DATAFRAME HANDLING
    # =========================================

    if not df.empty:

        # IMPORTANT: force numeric conversion (fix string % bug)
        if "Achievement" in df.columns:
            df["Achievement_num"] = df["Achievement"].apply(safe_to_float)
        else:
            df["Achievement_num"] = 0.0

        high = df[df["Performance"] == "Perform"]
        low = df[df["Performance"] == "Underperform"]

        if not high.empty:
            avg_high = round(high["Achievement_num"].mean(), 2)
            insights.append(
                f"Rata-rata perform achievement: {avg_high}%."
            )

        if not low.empty:
            avg_low = round(low["Achievement_num"].mean(), 2)
            insights.append(
                f"Rata-rata underperform achievement: {avg_low}%."
            )

    # =========================================
    # TOP SALES
    # =========================================

    top_sales = get_top_sales(
        metric=metric,
        region=region,
        limit=3
    )

    top_names = [x.get("name") for x in top_sales.get("data", [])]

    if top_names:
        insights.append(
            f"Top performer {region.upper()} ({metric.upper()}): {', '.join(top_names)}."
        )

    # =========================================
    # BOTTOM SALES
    # =========================================

    bottom_sales = get_bottom_sales(
        metric=metric,
        region=region,
        limit=3
    )

    bottom_names = [x.get("name") for x in bottom_sales.get("data", [])]

    if bottom_names:
        insights.append(
            f"Lowest performer: {', '.join(bottom_names)}."
        )

    # =========================================
    # PIPELINE INSIGHT
    # =========================================

    if "VS Gap" in df.columns:

        df["VS Gap"] = pd.to_numeric(df["VS Gap"], errors="coerce")

        high_pipeline = df[df["VS Gap"] >= 100]

        if not high_pipeline.empty:
            insights.append(
                f"{len(high_pipeline)} sales memiliki pipeline >100% gap."
            )

    # =========================================
    # NEW JOINER INSIGHT
    # =========================================

    if "Join Date" in df.columns:

        df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")

        latest = df[df["Join Date"].notna()].sort_values(
            "Join Date",
            ascending=False
        )

        if not latest.empty:
            newest = latest.iloc[0]

            insights.append(
                f"{newest['Name']} adalah sales terbaru di {region.upper()}."
            )

    # =========================================
    # FINAL RESULT
    # =========================================

    return {
        "region": region.upper(),
        "metric": metric.upper(),
        "minimum_achievement": f"{minimum_achievement:.2f}%",
        "total_sales": total_sales,
        "total_perform": total_perform,
        "total_underperform": total_underperform,
        "insights": insights
    }