import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def fetch_headlines():
    url = "https://www.bbc.com/news"   # You can replace with any other news site
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    raise Exception(soup)
    # Extract headlines (BBC uses <h2> with specific classes)
    headlines = []
    for h in soup.find_all("h2"):
        text = h.get_text().strip()
        if text and len(text) > 20:  # filter short texts
            headlines.append(text)

    return headlines


def save_to_csv(headlines):
    df = pd.DataFrame(headlines, columns=["Headline"])
    filename = f"headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"✅ Headlines saved to {filename}")


if __name__ == "__main__":
    headlines = fetch_headlines()
    if headlines:
        print("Top Headlines:\n")
        for i, h in enumerate(headlines[:10], start=1):
            print(f"{i}. {h}")

        save_to_csv(headlines)
