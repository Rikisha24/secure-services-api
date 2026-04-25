import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "services": [
                "Authentication",
                "Rate Limiting",
                "Threat Monitoring",
                "Logging",
                "API Gateway"
            ]
        })
    }