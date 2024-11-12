import requests
from bs4 import BeautifulSoup

# Example for scraping a list of deals from a platform
url = "https://www.realtymogul.com/investment-opportunities"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract deal titles
deals = soup.find_all("h2", class_="investment-title")
for deal in deals:
    print(deal.text.strip())
