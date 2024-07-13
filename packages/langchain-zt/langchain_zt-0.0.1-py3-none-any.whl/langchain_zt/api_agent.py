import os
from operator import itemgetter

from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda


load_dotenv()


BASE_URL = "https://zt-ml-llm-staging.azurewebsites.net"
V2_URL = "zt-llm-get-anon-prompts/V2"
V5_URL = "zt-llm-get-stream/V5"
AUTH_TOKEN = "Bearer " + os.environ.get("BEARER_TOKEN", "")

import requests


def get_request_headers():
    headers = {
        "Accept": "application/json",
        "Authorization": AUTH_TOKEN,
    }
    return headers


def make_request(url: str, headers: dict, data: dict, method: str = "GET"):
    """Makes request at the url with headers and data
    Args:
        method (str): method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        url (str): URL for the `Request` object.
        headers (dict): Dictionary of HTTP Headers to send with the Request
        data (dict): Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.

    Returns:
        response: Response
    """
    try:
        response = requests.request(method, url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Response is not Json:", type(response.content))
        if isinstance(response.content, bytes):
            return response.content.decode("utf-8")
        if response.request_code != 200:
            print("Error ocurred: ", e)
        return response.content


def call_api_v5(data):
    print("LLM: ", data.get("llm") if data.get("llm") else "CHATGPT35")
    form_data = {
        "llm": data.get("llm") if data.get("llm") else "CHATGPT35",
        "prompt": data["request"]["prompt"],
        "pii_array": data["response"]["piiList"],
    }
    headers = get_request_headers()

    v5_url = BASE_URL + "/" + V5_URL
    response = make_request(v5_url, headers, form_data, "POST")
    data["v5_response"] = response
    return data


def call_api_v2(data: dict):
    print("Inside v2 def: ", data)
    v2_response = {}
    headers = get_request_headers()
    v2_url = BASE_URL + "/" + V2_URL
    llm = data.pop("llm")
    response = requests.request("POST", v2_url, headers=headers, json=data)
    response.raise_for_status()
    v2_response["request"] = data
    v2_response["llm"] = llm
    v2_response["response"] = response.json()
    return v2_response


def call_api_v2(data: dict):
    print("Inside v2 def: ", data)
    v2_response = {}
    headers = get_request_headers()
    v2_url = BASE_URL + "/" + V2_URL
    llm = data.pop("llm")
    response = requests.request("POST", v2_url, headers=headers, json=data)
    response.raise_for_status()
    v2_response["request"] = data
    v2_response["llm"] = llm
    v2_response["response"] = response.json()
    return v2_response


api_chain = (
    {
        "prompt": itemgetter("prompt"),
        "anonymise_type": itemgetter("anon_type"),
        "privacy_level": itemgetter("level"),
        "anonymize_custom_keywords": itemgetter("ckw"),
        "keyword_safeguard_custom": itemgetter("kw_safeguard"),
        "llm": itemgetter("llm"),
    }
    | RunnableLambda(call_api_v2)
    | RunnableLambda(call_api_v5)
)


def get_zt_chain():
    return (
        {
            "prompt": itemgetter("prompt"),
            "anonymise_type": itemgetter("anon_type"),
            "privacy_level": itemgetter("level"),
            "anonymize_custom_keywords": itemgetter("ckw"),
            "keyword_safeguard_custom": itemgetter("kw_safeguard"),
            "llm": itemgetter("llm"),
        }
        | RunnableLambda(call_api_v2)
        | RunnableLambda(call_api_v5)
    )
