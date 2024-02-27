sitemap migration - 21st Febimport os
import xml.etree.ElementTree as ET

def extract_last_part(url):
    return url.split('/')[-1]

def validate_xml_files(file1, file2):
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()

    tree2 = ET.parse(file2)
    root2 = tree2.getroot()

    # 1. Check if the number of records are the same in both files
    if len(root1) != len(root2):
        extra_records = abs(len(root1) - len(root2))
        print(f"Extra number of records in {file1}: {extra_records}")

    # 2. Check if the last part of URLs in file1 can be found in file2 URLs
    missing_urls = []
    for url1 in root1.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        last_part1 = extract_last_part(url1.text)
        found = False
        for url2 in root2.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            if last_part1 in url2.text:
                found = True
                break
        if not found:
            missing_urls.append(url1.text)

    # Write missing URLs which are present in File 1 but not in File 2 to a file
    if missing_urls:
        output_dir = 'Output'
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, 'missing_urls.txt'), 'w') as f:
            f.write('\n'.join(missing_urls))
        print(f"Missing URLs written to {os.path.join(output_dir, 'missing_urls.txt')}")

# File paths
#Before File
file1 = 'sitemap migration - 21st Feb/before/new-sitemap-GENRES-1.xml'
#After File
file2 = 'sitemap migration - 21st Feb/after_tray_pages/new-sitemap-GENRES-1.xml'

# Validate the XML files
validate_xml_files(file1, file2)
