# Google Search Scraper

This is a Streamlit-based web application that scrapes Google search results using Selenium and displays the extracted URLs.

## Features

- Scrapes the first 3 pages of Google search results.
- Uses Selenium with Chrome WebDriver to automate web scraping.
- Displays extracted URLs in a table format using Streamlit.

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Google Chrome (latest version)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/MH-PAVEL/streamlit-ggl-search-website-url-collection.git
   cd streamlit-ggl-search-website-url-collection
   ```

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   This project uses:

- `streamlit` for the UI
- `selenium` for web scraping
- `webdriver-manager` for automatic WebDriver management
- `pandas` for handling search results

## Usage

1. **Run the Streamlit app:**

   ```sh
   streamlit run app.py
   ```

2. **Enter your search query** in the text input field and click "Submit".
3. **Wait for the results** to be scraped and displayed in the table.

## Known Issues & Limitations

- Google may block automated scraping, leading to CAPTCHAs or IP bans.
- This script does **not** bypass Google's security measures.
- Consider using **Google Custom Search API** or **SerpAPI** for better results.
