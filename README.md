# BookScraper

I created a web scraper with Python, leveraging the requests library to retrieve HTML content and BeautifulSoup to parse and extract information. I utilized pandas to structure the scraped data into a DataFrame. My scraper extracts the first 5 pages of BooksToScrape.com, pulling each book's title, price, availability, and rating. I combined this with Streamlit to make an interactive app that allows users to search for books by name, display results as a table, and download the results as a CSV file.

The scraper is very precise since it's based on exact class names and HTML tags. Yet, its precision is reliant upon the structure of the website not changing—if the website alters the site structure or class names, I would have to reprogram the scraper. Currently, it's efficient and effective at the site structure it has been programmed for
