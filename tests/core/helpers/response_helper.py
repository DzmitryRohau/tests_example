from requests import Response


def get_json_data_from_response(response: Response) -> dict:
    try:
        output_json = response.json()
    except Exception:
        raise Exception("Couldn't get json from response data")
    return output_json


def get_access_token_from_response(json_data: dict) -> str:
    try:
        access_token = json_data["access_token"]
    except Exception:
        raise Exception("Couldn't get json from json data. Print json: " + str(json_data))
    return access_token


def get_text_from_response(response: Response) -> str:
    try:
        response_text = response.text
    except Exception:
        raise Exception("Couldn't get text from response.")
    return response_text
