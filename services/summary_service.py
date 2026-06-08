from services.performance_service import get_sales_performance
from services.ranking_service import (
    get_top_sales,
    get_bottom_sales
)
from services.insight_service import get_team_insight

from services.analytics_service import (
    # =========================================
    # COMMERCIAL
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

    # =========================================
    # REGIONAL
    # =========================================
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
    get_minimum_achievement_q4_regional
)

# =========================================
# MINIMUM MAP
# =========================================

MINIMUM_MAP = {
    "commercial": {
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
        "q4": get_minimum_achievement_q4_commercial,
    },

    "regional": {
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
        "q4": get_minimum_achievement_q4_regional,
    }
}

# =========================================
# SUMMARY DASHBOARD
# =========================================

def get_summary_dashboard(
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

    if region not in MINIMUM_MAP:
        return {
            "error": "Invalid region"
        }

    if metric not in MINIMUM_MAP[region]:
        return {
            "error": "Invalid metric"
        }

    # =========================================
    # VALIDATION SMB
    # regional tidak punya SMB
    # =========================================

    if region == "regional" and smb:
        return {
            "error": "Regional does not have SMB division"
        }

    # =========================================
    # SALES TYPE
    # =========================================

    if smb:
        sales_type = "SMB SALES"

    elif enterprise:
        sales_type = "ENTERPRISE SALES"

    else:

        if region == "regional":
            sales_type = "REGIONAL SALES"
        else:
            sales_type = "ALL SALES"

    # =========================================
    # MINIMUM ACHIEVEMENT
    # =========================================

    minimum_raw = (
        MINIMUM_MAP[region][metric]()[
            "achievement"
        ]
    )

    minimum = float(minimum_raw)

    # =========================================
    # FIX SCALE
    # =========================================

    if minimum <= 1:
        minimum *= 100

    minimum = round(minimum, 2)

    # =========================================
    # PERFORMANCE DATA
    # =========================================

    performance = get_sales_performance(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    total_sales = performance.get(
        "total_sales",
        0
    )

    total_perform = performance.get(
        "total_perform",
        0
    )

    total_underperform = performance.get(
        "total_underperform",
        0
    )

    # =========================================
    # PERFORMANCE RATE
    # =========================================

    performance_rate = (
        (total_perform / total_sales) * 100
        if total_sales > 0 else 0
    )

    performance_rate = round(
        performance_rate,
        2
    )

    # =========================================
    # TOP / BOTTOM SALES
    # =========================================

    top_sales = get_top_sales(
        metric=metric,
        region=region,
        limit=3,
        smb=smb,
        enterprise=enterprise
    )

    bottom_sales = get_bottom_sales(
        metric=metric,
        region=region,
        limit=3,
        smb=smb,
        enterprise=enterprise
    )

    top_performer = (
        top_sales["data"][0]
        if top_sales.get("data")
        else None
    )

    lowest_performer = (
        bottom_sales["data"][0]
        if bottom_sales.get("data")
        else None
    )

    # =========================================
    # PIPELINE HEALTH
    # =========================================

    if performance_rate >= 70:
        pipeline_health = "Excellent"

    elif performance_rate >= 50:
        pipeline_health = "Healthy"

    elif performance_rate >= 30:
        pipeline_health = "Need Improvement"

    else:
        pipeline_health = "Critical"

    # =========================================
    # TEAM INSIGHT
    # =========================================

    team_insight = get_team_insight(
        metric,
        region
    )

    # =========================================
    # GAP
    # =========================================

    gap = round(
        performance_rate - minimum,
        2
    )

    # =========================================
    # EXECUTIVE NOTES
    # =========================================

    executive_notes = []

    # target note
    if gap >= 0:

        executive_notes.append(
            f"{sales_type} sudah mencapai "
            f"target minimum ({minimum:.2f}%)."
        )

    else:

        executive_notes.append(
            f"{sales_type} masih di bawah "
            f"target minimum ({minimum:.2f}%)."
        )

    # underperform note
    if total_underperform > 0:

        executive_notes.append(
            f"{total_underperform} sales "
            f"masih underperform."
        )

    # top performer note
    if top_performer:

        executive_notes.append(
            f"Top performer: "
            f"{top_performer['name']} "
            f"({top_performer['achievement']})."
        )

    # =========================================
    # FINAL RESPONSE
    # =========================================

    return {

        # BASIC
        "region": region.upper(),
        "sales_type": sales_type,
        "metric": metric.upper(),

        # KPI
        "minimum_achievement": f"{minimum:.2f}%",
        "performance_rate": f"{performance_rate:.2f}%",
        "gap": f"{gap:.2f}%",

        # HEALTH
        "pipeline_health": pipeline_health,

        # SUMMARY
        "total_sales": total_sales,
        "total_perform": total_perform,
        "total_underperform": total_underperform,

        # BEST / WORST
        "top_performer": top_performer,
        "lowest_performer": lowest_performer,

        # RANKING
        "top_sales": top_sales.get(
            "data",
            []
        ),

        "bottom_sales": bottom_sales.get(
            "data",
            []
        ),

        # INSIGHT
        "team_insights": team_insight.get(
            "insights",
            []
        ),

        # NOTES
        "executive_notes": executive_notes
    }

















