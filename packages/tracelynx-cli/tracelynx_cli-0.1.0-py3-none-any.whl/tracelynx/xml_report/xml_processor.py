import os
import xml.etree.ElementTree as ET


def process_xml_files(input_folder: str, output_file: str):
    # Placeholder for future logic to process XML files
    xml_files = [f for f in os.listdir(input_folder) if f.endswith('.xml')]
    
    # Create the root element of the new XML
    root = ET.Element("root")

    for xml_file in xml_files:
        file_path = os.path.join(input_folder, xml_file)
        tree = ET.parse(file_path)
        root.append(tree.getroot())
    
    # Write the new XML to the output file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process XML files in a folder and create a new XML file.')
    parser.add_argument('input_folder', help='The path to the folder containing XML files')
    parser.add_argument('output_file', help='The path to the output XML file')

    args = parser.parse_args()
    process_xml_files(args.input_folder, args.output_file)

