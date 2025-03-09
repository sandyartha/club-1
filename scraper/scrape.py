from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

URL = "https://example.com"

def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)  # Tunggu hingga halaman dimuat

        # Ambil HTML setelah halaman dimuat
        html = page.content()
        browser.close()

        # Parsing dengan BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        
        # Contoh ekstraksi data
        data = []
        for item in soup.select(".data-item"):  # Gantilah dengan selector yang sesuai
            title = item.select_one(".title").text.strip()
            value = item.select_one(".value").text.strip()
            data.append({"title": title, "value": value})

        # Simpan hasil scraping ke JSON
        with open("scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    scrape()
