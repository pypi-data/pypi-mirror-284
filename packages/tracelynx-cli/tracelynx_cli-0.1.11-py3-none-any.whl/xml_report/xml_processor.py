# xml_report/xml_processor.py

import os
import xml.etree.ElementTree as ET

from xml_report.link_prediction_example import json_data


def process_xml_files(input_folder, jfilter, output_file):
    #with open(json_filter) as f:
    #    jfilter = json.load(f)
    xml_files = [f for f in os.listdir(input_folder) if f.endswith('.xml')]
    
    if not xml_files:
        raise ValueError("No XML files found in the input folder")

    # Use the root element of the first XML input file
    first_file_path = os.path.join(input_folder, xml_files[0])
    tree = ET.parse(first_file_path)
    testsuites_root = tree.getroot()
    # Remove all childrens to avoid duplicated at the root element
    for ts in testsuites_root.findall('testsuite'):
        testsuites_root.remove(ts)

    print(f"{testsuites_root.tag} - {testsuites_root.attrib['name']}")

    for xml_file in xml_files:
        file_path = os.path.join(input_folder, xml_file)
        tree = ET.parse(file_path)
        testsuite_root_element = tree.getroot()

        print(f"{testsuite_root_element.tag} - {testsuite_root_element.attrib['name']}")

        # Filter the test case elements based on classname and name

        for testsuite in testsuite_root_element:
            print(testsuite.get("timestamp"))
            for testcase in testsuite:
                classname = testcase.get('classname')
                name = testcase.get('name')
                print("  "+classname+" "+name)
                if classname and name:
                    if not find_link(jfilter, classname, name):
                        print("    mismatch -- removing")
                        testcase.set('MISMATCH', 'True')
            for child in list(testsuite):
                if child.get('MISMATCH') == 'True':
                    testsuite.remove(child)
            if len(testsuite):  
                testsuites_root.append(testsuite)

        # Create a new root element for filtered elements
        #new_root = ET.Element("testsuite")

        #for elem in filtered_testcases:
        #    new_root.append(elem)

   
    # Write the new XML to the output file
    tree = ET.ElementTree(testsuites_root)
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
    parser.add_argument('output_file', help='The path to the output XML file')

    args = parser.parse_args()
    process_xml_files(args.input_folder, json_data, args.output_file)

