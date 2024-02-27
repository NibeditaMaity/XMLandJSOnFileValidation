import os
import requests
import xml.etree.ElementTree as ET

# Create the Output folder if it doesn't exist
output_folder = 'Output'
os.makedirs(output_folder, exist_ok=True)

# Parse the XML file
xml_file = 'sitemap migration - 21st Feb/after/new-sitemap-SECOND_LEVEL_LANDING_PAGES-1.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Open the output file for writing
output_file = os.path.join(output_folder, 'FailedResponse.txt')
with open(output_file, 'w') as f:
    # Iterate over the <loc> elements in the XML
    for url_element in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        url = url_element.text
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the response status code is not 200
        if response.status_code != 200:
            # Write the URL to the output file
            # f.write(f'{url}\n')
            # Write the URL and response code to the output file
            f.write(f'{url} - Response Code: {response.status_code}\n')