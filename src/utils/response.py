def api_response(status_code, message, data=None):
    result = {
        "status_code": status_code,
        "message": message,
        "data": data
    }
    print(result)
    return