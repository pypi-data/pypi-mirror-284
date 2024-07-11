import os
import xml.etree.ElementTree as ET
import json

from pathlib import Path


def find_upwards(cwd: Path, filename: str) -> Path | None:
    print("cwd:", cwd)
    print("filename:", filename)
    if cwd == Path(cwd.root) or cwd == cwd.parent:
        return None

    fullpath = cwd / filename
    print("fullpath", fullpath)

    return fullpath if fullpath.exists() else find_upwards(cwd.parent, filename)


def process_xml_files(input_folder, json_filter, output_file):
    print("Processing XML files...")
    print(json_filter)

    # usage example:
    json_filter2 = find_upwards(Path.cwd(), "tests/data/jest_test_suite/link_prediction_example.json")

    print("json_filter2", json_filter2)

    with open(json_filter2) as f:
        jfilter = json.load(f)

    xml_files = [f for f in os.listdir(input_folder) if f.endswith('.xml')]
    
    # Create the root element of the new XML
    root = ET.Element("testsuites")

    for xml_file in xml_files:
        file_path = os.path.join(input_folder, xml_file)
        tree = ET.parse(file_path)
        root_element = tree.getroot()

        # Filter the test case elements based on classname and name
        filtered_elements = []
        for elem in root_element.findall(".//testcase"):
            classname = elem.get('classname')
            name = elem.get('name')
            print(classname+" "+name)
            if classname and name:
                if find_link(jfilter, classname, name):
                    filtered_elements.append(elem)

        # Create a new root element for filtered elements
        new_root = ET.Element("testsuite")
        for elem in filtered_elements:
            new_root.append(elem)

        root.append(new_root)
   
    # Write the new XML to the output file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


def find_link(jfilter, title, title_label):
    for item in jfilter.get("items", []):
        target_artifact = item.get("target", {}).get("artifact", {})
        if (target_artifact.get("api") == "testrail" and
            target_artifact.get("title") == title and
            target_artifact.get("title_label") == title_label.lower().replace(" ", "_")):
            return target_artifact.get("link")
        source_artifact = item.get("source", {}).get("artifact", {})
        if (source_artifact.get("api") == "testrail" and
            source_artifact.get("title") == title and
            source_artifact.get("title_label") == title_label.lower().replace(" ", "_")):
            return source_artifact.get("link")
    return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process XML files in a folder and create a new XML file.')
    parser.add_argument('input_folder', help='The path to the folder containing XML files')
    parser.add_argument('json_filter', help='The path of the json file containing JSON filter')
    parser.add_argument('output_file', help='The path to the output XML file')

    args = parser.parse_args()
    process_xml_files(args.input_folder, args.json_filter, args.output_file)

