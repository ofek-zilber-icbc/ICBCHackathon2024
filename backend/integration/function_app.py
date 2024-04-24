import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="HttpIntegration")
def HttpIntegration(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    response = {
        "calls": [
            {
                "representative": "Adrian Smith",
        "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
        "customerName": "Bobby",
        "summary": "Call the customer to check status of treatment plan",
        "callLength": 15,
        "flags": [
                {
                    "isCustomer": True,
                    "isRepresentative": False,
                    "timestamp": 2
                },
                {
                    "isCustomer": True,
                    "isRepresentative": True,
                    "timestamp": 4
                },
                {
                    "isCustomer": False,
                    "isRepresentative": True,
                    "timestamp": 10
                }
            ]
            }
        ]
        
    }

    return func.HttpResponse(json.dumps(response),
                status_code=200                
            )
    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )