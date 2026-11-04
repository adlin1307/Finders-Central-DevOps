def validate_item(name, category, location, description, report_type):

    if not name or not category or not location or not description:
        return "Invalid Report"

    elif report_type.lower() not in ["lost", "found"]:
        return "Invalid Report"

    else:
        return "Valid Report"