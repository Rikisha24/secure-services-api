def app(request, response):
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response.body = b'{"services": ["Authentication", "Rate Limiting", "Threat Monitoring", "Logging", "API Gateway"]}'