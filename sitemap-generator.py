import argparse
import requests
from bs4 import BeautifulSoup


def create_sitemap(url):
    # Makes a GET request to the URL provided by the user
    response = requests.get(url)

    # Analyse the HTML of the page with the BeautifulSoup library
    soup = BeautifulSoup(response.text, "html.parser")

    # Create the sitemap XML content
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # For each link on the page, add a url element to the XML content
    for link in soup.find_all("a"):
        loc = link.get("href")
        lastmod = "2023-06-05"  # Replace with the appropriate last modified date
        changefreq = "daily"  # Replace with the appropriate change frequency
        priority = "1.0"  # Replace with the appropriate priority

        url_element = f'   <url>\n      <loc>{loc}</loc>\n'
        url_element += f'      <lastmod>{lastmod}</lastmod>\n'
        url_element += f'      <changefreq>{changefreq}</changefreq>\n'
        url_element += f'      <priority>{priority}</priority>\n   </url>\n'

        xml_content += url_element

    # Close the urlset tag
    xml_content += '</urlset>\n'

    # Write the XML content to the sitemap.xml file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)


if __name__ == "__main__":
    # Set command line arguments
    parser = argparse.ArgumentParser(description="Creates a sitemap from a URL.")
    parser.add_argument("url", help="The URL of the site you want to create a sitemap for.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Create the sitemap based on the provided URL
    create_sitemap(args.url)
