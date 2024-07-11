import httpx

from xml_report import process_xml_files
from xml_report.link_prediction_example import json_data


def authenticate(username: str, password: str) -> str:
    print("authenticating: ", username)
    auth = httpx.BasicAuth(username, password)
    response = httpx.post(
        "https://api.lm-dev.koneksys.com/api/v1/auth/login",
        auth=auth
    )
    print(response.json)
    return f"{username} authenticated"


def process_xml(username: str, password: str, xml_input: str | None = None, xml_output: str | None = None,
                data: str | None = None) -> None:
    print(authenticate(username=username, password=password))
    print(f"processing xml from {xml_input} to {xml_output}")
    process_xml_files(xml_input, json_data, xml_output)
