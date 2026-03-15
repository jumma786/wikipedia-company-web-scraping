import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Add browser headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send request
response = requests.get(url, headers=headers)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the table
table = soup.find("table", {"class": "wikitable"})

rows = table.find_all("tr")

data = []

for row in rows[1:]:
    cols = row.find_all("td")
    if cols:
        rank = cols[0].get_text(strip=True)
        name = cols[1].get_text(strip=True)
        industry = cols[2].get_text(strip=True)
        revenue = cols[3].get_text(strip=True)
        revenue_growth = cols[4].get_text(strip=True)
        headquarters = cols[6].get_text(strip=True)

        data.append([rank, name, industry, revenue, revenue_growth, headquarters])

df = pd.DataFrame(data, columns=[
    "Rank",
    "Company",
    "Industry",
    "Revenue",
    "Revenue Growth",
    "Headquarters"
])

print(df.head())