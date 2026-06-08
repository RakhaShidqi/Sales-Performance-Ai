from flask import Flask, jsonify, request

from services.performance_service import get_sales_performance
from services.summary_service import get_summary_dashboard
from services.ranking_service import get_top_sales, get_bottom_sales

from services.query_service import (
    get_registered_sales,
    get_registered_regional_sales,
    get_registered_headsales_commercial,
    get_registered_headsales_regional,
    get_registered_unit_head_commercial,
    get_sales_by_territory,
    search_sales_name,
    search_sales_total_po,
    search_sales_gap_ach_ytd,
    search_sales_leads_on_progress,
    search_sales_vs_gap,
    search_sales_name_database,
    search_applicant_name,
    search_division,
    get_sales_by_status,
    get_sales_with_ytd,
    get_registered_smb_sales,
    get_registered_enterprise_sales
)

from services.analytics_service import (
    get_minimum_achievement_ytd_commercial,
    get_minimum_achievement_q1_commercial,
    get_minimum_achievement_q2_commercial,
    get_minimum_achievement_q3_commercial,
    get_minimum_achievement_q4_commercial,
    get_minimum_achievement_headsales_ytd_commercial,
    get_minimum_achievement_headsales_q1_commercial,
    get_minimum_achievement_headsales_q2_commercial,
    get_minimum_achievement_headsales_q3_commercial,
    get_minimum_achievement_headsales_q4_commercial,
    
    get_minimum_achievement_unit_head_ytd_commercial,
    get_minimum_achievement_unit_head_q1_commercial,
    get_minimum_achievement_unit_head_q2_commercial,
    get_minimum_achievement_unit_head_q3_commercial,
    get_minimum_achievement_unit_head_q4_commercial,
    
    get_minimum_achievement_ytd_regional,
    get_minimum_achievement_q1_regional,
    get_minimum_achievement_q2_regional,
    get_minimum_achievement_q3_regional,
    get_minimum_achievement_q4_regional,
    get_minimum_achievement_headsales_ytd_regional,
    get_minimum_achievement_headsales_q1_regional,
    get_minimum_achievement_headsales_q2_regional,
    get_minimum_achievement_headsales_q3_regional,
    get_minimum_achievement_headsales_q4_regional
    
)

app = Flask(__name__)


# =========================================
# BASE RESPONSE
# =========================================

def success_response(data):
    return jsonify({
        "success": True,
        "data": data
    })


def error_response(message):
    return jsonify({
        "success": False,
        "message": message
    }), 400


# =========================================
# HOME
# =========================================

@app.route("/")
def home():
    return success_response({
        "status": "running",
        "service": "Sales Achievement API",
        "version": "2.0.0"
    })


# =========================================
# REGION VALIDATION
# =========================================

def validate_region(region):

    region = region.lower()

    if region not in ["commercial", "regional"]:
        return None

    return region


# =========================================
# COMMON QUERY PARAMS
# =========================================

def get_common_params():

    teritory = request.args.get("teritory")
    headsales = request.args.get("headsales", "false").lower() == "true"

    return teritory, headsales


# =========================================
# SALES PERFORMANCE
# =========================================

@app.route("/<region>/sales-performance/")
@app.route("/<region>/sales-performance/<metric>")
def sales_performance(region, metric="ytd"):

    region = validate_region(region)

    if not region:
        return error_response(
            "Region must be 'commercial' or 'regional'"
        )

    teritory, headsales = get_common_params()
    
    unit_head = (
        request.args
        .get("unit_head", "false")
        .lower() == "true"
    )
    smb = (
        request.args
        .get("smb", "false")
        .lower() == "true"
    )

    enterprise = (
        request.args
        .get("enterprise", "false")
        .lower() == "true"
    )

    # =========================================
    # VALIDATION
    # regional tidak punya unit head
    # =========================================
    if region == "regional" and unit_head:
        return error_response(
            "Regional does not have unit head"
        )

    # =========================================
    # RESULT
    # =========================================
    result = get_sales_performance(
        metric=metric,
        region=region,
        teritory=teritory,
        headsales=headsales,
        unit_head=unit_head,
        smb=smb,
        enterprise=enterprise
    )

    return success_response(result)


# =========================================
# RANKING TOP
# =========================================

@app.route("/<region>/ranking/top")
@app.route("/<region>/ranking/top/<metric>")
def ranking_top(region, metric="ytd"):

    region = validate_region(region)

    if not region:
        return error_response(
            "Region must be 'commercial' or 'regional'"
        )

    # =========================================
    # QUERY PARAMS
    # =========================================
    smb = (
        request.args
        .get("smb", "false")
        .lower() == "true"
    )

    enterprise = (
        request.args
        .get("enterprise", "false")
        .lower() == "true"
    )

    # =========================================
    # VALIDATION
    # =========================================
    if smb and enterprise:
        return error_response(
            "Cannot use smb and enterprise together"
        )

    # =========================================
    # RESULT
    # =========================================
    result = get_top_sales(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    return success_response(result)


# =========================================
# RANKING BOTTOM
# =========================================

@app.route("/<region>/ranking/bottom")
@app.route("/<region>/ranking/bottom/<metric>")
def ranking_bottom(region, metric="ytd"):

    region = validate_region(region)

    if not region:
        return error_response(
            "Region must be 'commercial' or 'regional'"
        )

    # =========================================
    # QUERY PARAMS
    # =========================================
    smb = (
        request.args
        .get("smb", "false")
        .lower() == "true"
    )

    enterprise = (
        request.args
        .get("enterprise", "false")
        .lower() == "true"
    )

    # =========================================
    # VALIDATION
    # =========================================
    if smb and enterprise:
        return error_response(
            "Cannot use smb and enterprise together"
        )

    # =========================================
    # RESULT
    # =========================================
    result = get_bottom_sales(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    return success_response(result)


# =========================================
# SUMMARY DASHBOARD
# =========================================

@app.route("/<region>/summary")
@app.route("/<region>/summary/<metric>")
def summary_dashboard(region, metric="ytd"):

    region = validate_region(region)

    if not region:
        return error_response(
            "Region must be 'commercial' or 'regional'"
        )
        
    # =========================================
    # QUERY PARAMS
    # =========================================
    smb = (
        request.args
        .get("smb", "false")
        .lower() == "true"
    )

    enterprise = (
        request.args
        .get("enterprise", "false")
        .lower() == "true"
    )
    
    # =========================================
    # VALIDATION
    # =========================================
    if smb and enterprise:
        return error_response(
            "Cannot use smb and enterprise together"
        )

    result = get_summary_dashboard(
        metric=metric,
        region=region,
        smb=smb,
        enterprise=enterprise
    )

    return success_response(result)


# =========================================
# COMMERCIAL SALES
# =========================================

@app.route("/commercial/sales")
def commercial_sales():

    headsales = request.args.get(
    "headsales",
    "false"
    ).lower() == "true"

    unit_head = request.args.get(
        "unit_head",
        "false"
    ).lower() == "true"

    smb = request.args.get(
        "smb",
        "false"
    ).lower() == "true"

    enterprise = request.args.get(
        "enterprise",
        "false"
    ).lower() == "true"

    if unit_head:

        result = get_registered_unit_head_commercial()
        type_name = "UNIT HEAD"

    elif headsales:

        result = get_registered_headsales_commercial()
        type_name = "HEAD SALES"

    elif smb:

        result = get_registered_smb_sales()
        type_name = "SMB SALES"

    elif enterprise:

        result = get_registered_enterprise_sales()
        type_name = "ENTERPRISE SALES"

    else:

        result = get_registered_sales()
        type_name = "ALL SALES"

    return success_response({
        "region": "commercial",
        "type": type_name,
        "total_sales": len(result),
        "data": result.to_dict(orient="records")
    })


# =========================================
# REGIONAL SALES
# =========================================

@app.route("/regional/sales")
def regional_sales():

    headsales = request.args.get(
        "headsales",
        "false"
    ).lower() == "true"

    if headsales:
        result = get_registered_headsales_regional()
    else:
        result = get_registered_regional_sales()

    return success_response({
        "region": "regional",
        "headsales": headsales,
        "total_sales": len(result),
        "data": result.to_dict(orient="records")
    })


# =========================================
# GLOBAL SEARCH
# =========================================

@app.route("/sales/search/<keyword>")
def sales_search(keyword):

    result = search_sales_name(keyword)

    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })
    
@app.route("/sales/search/<keyword>/total_po")
def sales_search_total_po(keyword):
    
    result = search_sales_total_po(keyword)
    
    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })
    
@app.route("/sales/search/<keyword>/gap_ach_ytd")
def sales_search_gap_ach_ytd(keyword):
    
    result = search_sales_gap_ach_ytd(keyword)
    
    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })

@app.route("/sales/search/<keyword>/leads_on_progress")
def sales_search_leads_on_progress(keyword):

    result = search_sales_leads_on_progress(keyword)
    
    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })

@app.route("/sales/search/<keyword>/vs_gap")
def sales_search_vs_gap(keyword):

    result = search_sales_vs_gap(keyword)
    
    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })

# =========================================
# SALES BY TERRITORY
# =========================================

@app.route("/sales/territory/<keyword>")
def sales_by_territory(keyword):

    result = get_sales_by_territory(keyword)

    return success_response({
        "territory": keyword,
        "total_sales": len(result),
        "data": result
    })


# =========================================
# SALES BY STATUS
# =========================================

@app.route("/sales/status/<status>")
def sales_by_status(status):

    result = get_sales_by_status(status)

    return success_response({
        "status": status,
        "total_sales": len(result),
        "data": result
    })


# =========================================
# SALES YTD
# =========================================

@app.route("/sales/ytd")
def sales_with_ytd():

    region = request.args.get(
        "region",
        "commercial"
    ).lower()

    result = get_sales_with_ytd(region)

    return success_response({
        "region": region,
        "total_sales": len(result),
        "data": result
    })


# =========================================
# SALES MINIMUM ACHIEVEMENT
# =========================================

@app.route("/minimum-achievement/sales/")
@app.route("/minimum-achievement/sales/<metric>")
def minimum_achievement_sales(metric="ytd"):

    metric = metric.lower()

    metric_map = {
        "ytd": {
            "commercial": get_minimum_achievement_ytd_commercial,
            "regional": get_minimum_achievement_ytd_regional
        },
        "q1": {
            "commercial": get_minimum_achievement_q1_commercial,
            "regional": get_minimum_achievement_q1_regional
        },
        "q2": {
            "commercial": get_minimum_achievement_q2_commercial,
            "regional": get_minimum_achievement_q2_regional
        },
        "q3": {
            "commercial": get_minimum_achievement_q3_commercial,
            "regional": get_minimum_achievement_q3_regional
        },
        "q4": {
            "commercial": get_minimum_achievement_q4_commercial,
            "regional": get_minimum_achievement_q4_regional
        }
    }

    if metric not in metric_map:
        return error_response(
            "Metric must be ytd, q1, q2, q3, q4"
        )

    return success_response({
        "type": "SALES",
        "metric": metric.upper(),
        "commercial": metric_map[metric]["commercial"](),
        "regional": metric_map[metric]["regional"]()
    })


# =========================================
# HEAD SALES MINIMUM ACHIEVEMENT
# =========================================

@app.route("/minimum-achievement/headsales/")
@app.route("/minimum-achievement/headsales/<metric>")
def minimum_achievement_headsales(metric="ytd"):

    metric = metric.lower()

    metric_map = {
        "ytd": {
            "commercial": get_minimum_achievement_headsales_ytd_commercial,
            "regional": get_minimum_achievement_headsales_ytd_regional
        },
        "q1": {
            "commercial": get_minimum_achievement_headsales_q1_commercial,
            "regional": get_minimum_achievement_headsales_q1_regional
        },
        "q2": {
            "commercial": get_minimum_achievement_headsales_q2_commercial,
            "regional": get_minimum_achievement_headsales_q2_regional
        },
        "q3": {
            "commercial": get_minimum_achievement_headsales_q3_commercial,
            "regional": get_minimum_achievement_headsales_q3_regional
        },
        "q4": {
            "commercial": get_minimum_achievement_headsales_q4_commercial,
            "regional": get_minimum_achievement_headsales_q4_regional
        }
    }

    if metric not in metric_map:
        return error_response(
            "Metric must be ytd, q1, q2, q3, q4"
        )

    return success_response({
        "type": "HEAD SALES",
        "metric": metric.upper(),
        "commercial": metric_map[metric]["commercial"](),
        "regional": metric_map[metric]["regional"]()
    })


# =========================================
# UNIT HEAD MINIMUM ACHIEVEMENT
# =========================================

@app.route("/minimum-achievement/unithead/")
@app.route("/minimum-achievement/unithead/<metric>")
def minimum_achievement_unit_head(metric="ytd"):

    metric = metric.lower()

    metric_map = {
        "ytd": {
            "commercial": get_minimum_achievement_unit_head_ytd_commercial
        },
        "q1": {
            "commercial": get_minimum_achievement_unit_head_q1_commercial
        },
        "q2": {
            "commercial": get_minimum_achievement_unit_head_q2_commercial
        },
        "q3": {
            "commercial": get_minimum_achievement_unit_head_q3_commercial
        },
        "q4": {
            "commercial": get_minimum_achievement_unit_head_q4_commercial
        }
    }

    if metric not in metric_map:
        return error_response(
            "Metric must be ytd, q1, q2, q3, q4"
        )

    return success_response({
        "type": "UNIT HEAD",
        "metric": metric.upper(),
        "commercial": metric_map[metric]["commercial"](),
    })

@app.route("/database/sales/search/<keyword>")
def sales_database_search(keyword):

    result = search_sales_name_database(keyword)

    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })

@app.route("/database/applicants/search/<keyword>")
def applicant_database_search(keyword):

    result = search_applicant_name(keyword)

    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })
    
@app.route("/database/division/search/<keyword>")
def division_database_search(keyword):

    result = search_division(keyword)

    return success_response({
        "keyword": keyword,
        "total_found": len(result),
        "data": result
    })

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )