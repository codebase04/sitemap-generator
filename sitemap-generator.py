import argparse
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def create_sitemap(url):
    # Makes a GET request to the URL provided by the user
    response = requests.get(url)

    # Analyse the HTML of the page with the BeautifulSoup library
    soup = BeautifulSoup(response.text, "html.parser")

    # Creates the root element of the sitemap XML
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # For each link on the page, create a url element in the XML sitemap
    for link in soup.find_all("a"):
        url = ET.SubElement(root, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = link.get("href")

    # Generate the XML sitemap file
    tree = ET.ElementTree(root)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    # Sets command line arguments
    parser = argparse.ArgumentParser(description="Creates a sitemap from a URL.")
    parser.add_argument("url", help="The URL of the site you want to create a sitemap for.")

    # Parses the command line arguments
    args = parser.parse_args()

    # Creates the sitemap based on the provided URL
    create_sitemap(args.url)