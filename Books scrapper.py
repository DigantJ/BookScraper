import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Scrape data from Books to Scrape
def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    books = []

    for page in range(1, 6):  # scrape first 5 pages (~100 books)
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title = article.h3.a["title"]
            price = article.find("p", class_="price_color").text.strip()
            availability = article.find("p", class_="instock availability").text.strip()
            rating = article.p["class"][1]  # e.g., "Three"

            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating
            })

    return pd.DataFrame(books)

# Streamlit UI
st.set_page_config(page_title="📚 Book Scraper", layout="wide")
st.title("📚 Book Scraper from BooksToScrape.com")

st.markdown("""
This app scrapes book information like title, price, rating, and availability from the [Books to Scrape](http://books.toscrape.com/) website.
""")

# Scrape and display
with st.spinner("Scraping books..."):
    df = scrape_books()

# Search box
search = st.text_input("🔍 Search by title")
if search:
    filtered_df = df[df["Title"].str.contains(search, case=False)]
else:
    filtered_df = df

st.success(f"Showing {len(filtered_df)} books")
st.dataframe(filtered_df, use_container_width=True)

# Export
csv = filtered_df.to_csv(index=False)
st.download_button("📥 Download CSV", csv, "books.csv", "text/csv")
