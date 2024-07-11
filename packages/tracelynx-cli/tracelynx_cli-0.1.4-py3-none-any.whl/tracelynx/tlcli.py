from tracelynx.xml_report import process_xml_files


def authenticate(username: str, password: str) -> str:
    print("authenticating: ", username)
    return f"{username} authenticated"


def process_xml(username: str, password: str, xml_input: str | None = None, xml_output: str | None = None,
                data: str | None = None) -> None:
    print(authenticate(username=username, password=password))
    print(f"processing xml from {xml_input} to {xml_output}")

    if data is None:
        data = "./tests/data/jest_test_suite/link_prediction_example.json"

    process_xml_files(xml_input, data, xml_output)
