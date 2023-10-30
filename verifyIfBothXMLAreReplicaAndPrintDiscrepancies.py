import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def compare_xml(file1, file2):
    root1 = parse_xml(file1)
    root2 = parse_xml(file2)

    missing_data = []

    for elem1 in root1.iter():
        found = False
        for elem2 in root2.iter():
            if elem1.tag == elem2.tag and elem1.attrib == elem2.attrib and elem1.text == elem2.text:
                found = True
                break

        if not found:
            missing_data.append(elem1)

    return missing_data

def save_missing_data_to_xml(missing_data, output_file):
    root = ET.Element("MissingData")

    for elem in missing_data:
        root.append(elem)

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def main():
    #MYSQL file
    file1_path = 'SG PP - sitemaps/MySQL/new-sitemap-CLIPS-1.xml'
    #DDB File
    file2_path = 'SG PP - sitemaps/DDB/new-sitemap-CLIPS-1.xml'
    #Output file
    output_file = 'Output/MissingDDBRecords.xml'

    missing_data = compare_xml(file1_path, file2_path)

    if missing_data:
        print(f"Missing data count in File2.xml: {len(missing_data)}")
        print("Saving missing data to MissingData.xml")
        save_missing_data_to_xml(missing_data, output_file)
    else:
        print("No missing data found.")

if __name__ == "__main__":
    main()
