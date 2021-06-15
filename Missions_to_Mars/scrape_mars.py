def scrape():
    from splinter import Browser
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd

    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #NASA Mars News
    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    nasa_news = {}    
    nasa_news["date"] = soup.find("div", class_="list_date").get_text()
    nasa_news["title"] = soup.find("div", class_="content_title").get_text()
    nasa_news["paragraph"] = soup.find("div", class_="article_teaser_body").get_text()

    
    #JPL Mars Space Images
    url = "https://spaceimages-mars.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    featured_image = soup.find("img", class_="headerimage").get('src') 
    featured_image_url = url + "/" + featured_image

    
    #Mars Facts
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    df = pd.read_html(url)
    mars_facts = df[1]
    mars_facts.rename(columns={0: "Stats", 1:  "Mars"}, inplace=True)
    mars_facts.set_index("Stats", inplace=True)
    html = mars_facts.to_html()

    
    #Mars Hemispheres
    url = "https://marshemispheres.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    hemisphere_image_urls = []
    
    for row in soup.find_all("div", class_="item"):
        img_url = url + row.find("img", class_="thumb").get('src')
        title = row.find("h3").get_text()
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        

    # Quit the browser
    browser.quit()

    full_dict = {"NASA":  nasa_news,
                 "JPL":  featured_image_url,
                 "Facts":  html,
                 "Hemispheres":  hemisphere_image_urls}
    
    return full_dict