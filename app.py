import streamlit as st
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Function to scrape Google search results
def google_search(query):
    chrome_options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    all_urls = []

    for page in range(1, 4):  # First 3 pages
        url = f"https://www.google.com/search?q={query}&start={(page-1)*10}"
        driver.get(url)
        time.sleep(15)  # Wait for page to load
        driver.refresh()
        driver.maximize_window()

        links = driver.find_elements(
            By.XPATH, "//a[@jsname='UWckNb']")
        for link in links:
            href = link.get_attribute("href")
            if href and "google.com" not in href:  # Filter out Google internal links
                all_urls.append(href)

        time.sleep(1)

    driver.quit()
    return all_urls


# Streamlit UI
st.title("Google Search Scraper")

query = st.text_input("Enter your search query:")
if st.button("Submit"):
    if query:
        with st.spinner("Scraping Google search results... This may take a moment."):
            urls = google_search(query)

        if urls:
            st.success(f"Scraping completed! Found {len(urls)} links.")
            df = pd.DataFrame({"Website Links": urls})
            st.dataframe(df, use_container_width=True,
                         height=500)  # More space for results
        else:
            st.warning("No results found.")

        # Clear input field
        st.session_state.query = ""
    else:
        st.error("Please enter a search query.")

# """

# <a jsname="UWckNb" href="https://www.pcmag.com/picks/the-best-laptops" data-ved="2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBoQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://www.pcmag.com/picks/the-best-laptops&amp;ved=2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBoQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">The Best Laptops We've Tested (February 2025)</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAMFBMVEXrAC7rAC7rAC7////rAC3rACHqAAzxaHf71dn0lJ72qbH0jpntLknvRVr5v8XygY2OVQFAAAAAA3RSTlP79UxVRkCsAAAAr0lEQVQokb2T2w7EIAhEtQUUq/L/f7teSG1s7b51HgxyIlEYzWbNQnYzBlYytjLs0tyIK0TXBVQzlDgEAVRIuyoXGn2PmSZY6IgFJ7iDGzEN6FvaHW3Ndb2c9DRgDN/DlETkgAXUDk7vTG+QuJdtrZ6g6/B2odrZUu4ZeqIyhyVsg/4PHxrf4GJk1A10MrmdBIzKgtoED2YWNR+SCzlzJDUYXI1Zd3Rac23qAt++ww+hTQ0S76vIdgAAAABJRU5ErkJggg==" style="height:26px;width:26px" alt="" data-csiid="PUinZ42SBZi-vr0Pm8DHqAc_3" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf">PCMag</span></div><div class="byrV5b"><cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://www.pcmag.com<span class="ylgVCe ob9lvb" role="text"> › Best Products › Laptops</span></cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>


# <a jsname="UWckNb" href="https://www.cnet.com/tech/computing/best-laptop/" data-ved="2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBkQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://www.cnet.com/tech/computing/best-laptop/&amp;ved=2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBkQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">Best Laptops of 2025</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAqUlEQVR4AWJwL/ABtFvHNgCCQBSGK3t74gbswSbswUpMwwaOQIlncpXmESTkxaDFXxnzGVE4ah8H921bJCd5KXTmqqBCqxSlMqAAQcVM5WavD7NcMvomYg+YAOZa1kjx3ATKRQuwghG4JE2gB2DGAERDCxhGgLquKwG8wZkNJjZozgggaDpQfzM39UdTOKBuk+ytLTI3b8s8nuw7D2D+iMEfojD6D8JPOgD3hgaEjDQqGgAAAABJRU5ErkJggg==" style="height:26px;width:26px" alt="" data-csiid="PUinZ42SBZi-vr0Pm8DHqAc_5" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf">CNET</span></div><div class="byrV5b"><cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://www.cnet.com<span class="ylgVCe ob9lvb" role="text"> › Tech › Computing</span></cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>

# <a jsname="UWckNb" href="https://www.techradar.com/news/mobile-computing/laptops/best-laptops-1304361" data-ved="2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBsQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://www.techradar.com/news/mobile-computing/laptops/best-laptops-1304361&amp;ved=2ahUKEwjNpJiwhLSLAxUYn68BHRvgEXUQFnoECBsQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">The best laptop 2025: top portable picks for all budgets</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAZlBMVEX//////P7++fzyqsriAHbjAHzkAITpV6DxmsL63+zkAILjAH7iAHnnN5L2vtj0ttLoTZvrZabpUZ3nQZb75vD+9Pr51ubiAHf63uvvj73yosf2xNvugrXraaj4zuHwl8HterHmKI0GNBgPAAAA7klEQVR4AbSQBZKEQAxFgyT0JMHd4f6X3DCu5ftKkG/VDf+L53s/tSBEpMidvovIhmicfBHTLC9IhVnLCr5Sp5mabOHvNLFQG8ArneuH0QdjUmrfsoGKoM7HnlPS6uMoQqzuyAqXr7VLt6wkpJt9xKwjfDAoHdlGOYZPlstexnqCB2mx58uRFZ7tS8Q9tEKZue3tjUh9qJWju7YiUyTULvYqOJqF6S4S7wCVcG6rKIM1Md40X88T0WHpUKw9Z/RvqnB2zheWDNWMGYbeTdxEMrezppYMgg4gDR6X75OwMBbwFX8TJfc3OBdTnoFuAABMFAv5Wk9OFAAAAABJRU5ErkJggg==" style="height:26px;width:26px" alt="" data-csiid="PUinZ42SBZi-vr0Pm8DHqAc_7" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf">TechRadar</span></div><div class="byrV5b"><cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://www.techradar.com<span class="ylgVCe ob9lvb" role="text"> › Computing › Laptops</span></cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>

# <a jsname="UWckNb" href="https://www.rtings.com/laptop/reviews/best/laptop" data-ved="2ahUKEwjDzozbh7SLAxWLUfUHHT4tExE4ChAWegQIGhAB" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://www.rtings.com/laptop/reviews/best/laptop&amp;ved=2ahUKEwjDzozbh7SLAxWLUfUHHT4tExE4ChAWegQIGhAB"><br><h3 class="LC20lb MBeuO DKV0Md">The 8 Best Laptops of 2025</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAb1BMVEVHcEzoAADtOzvvWlroAADoAADmAADnAADsMTHlAADxb2/oAADqGxvoAADoAADoAADoAADpCAjoAADoAADoAQH//v7/+Pj5xMT4u7v82trwaWntRUXuT0/ziorqGxv1n5/+8PD+6Ojxdnb70tL3ra0aTkXhAAAAFHRSTlMAc/79W6QyVv4V8Vjt8ToPMOy5hVRGcGsAAADWSURBVCiR5dBbcoMwDAVQsElDHGiaVg+/jYH9r7GCCclXu4D2flk+Hsmjpvkneb+ef0h3a04rr71nyz6lbJUvEG3JMHOCt+ZEi3PaImvLPZZUoS60RmT0G3qFkCmAILnkAuXE8oaT4FRKhZ7ijsQuTMFr6QFb24nkcCCioCYHHu0+c/Z44GQ3zMUpHXDeMbzQk1MU1yVNUMsTMQJLW7XITxDnXImUoOkHMw5mGGPMPgcNd6PvY2+UzLxdJOe2bT/hkS8pPrbbY4dd1z3XeJXi8uvK/1q+AUaUF1XYHDTWAAAAAElFTkSuQmCC" style="height:26px;width:26px" alt="" data-csiid="vEunZ8OAF4uj1e8PvtrMiAE_3" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf">RTINGS.com</span></div><div class="byrV5b"><cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://www.rtings.com<span class="ylgVCe ob9lvb" role="text"> › Laptop › Best</span></cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>
# """
