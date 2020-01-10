from selenium import webdriver # Run the Selenium webdriver which would load the browser defined
import time # for waiting to load the pages
import os #Change environment for webdriver
from selenium.webdriver.common.keys import Keys # For Controlling the Scroll, we import keys from the given package
import pandas as pd #For converting it to Dataframe and saving into a CSV file

def youtube_scrape(url,save_as,no_of_scrolls=10):
    chromedriver = "D:/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    scroll = 0
    # Scroll 15 gives around 300 comments
    while scroll < no_of_scrolls:
        try:
            time.sleep(3)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            scroll += 1
        except Exception as s:
            print(s)
    name_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
    comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
    num_of_names = len(name_elems)
    comments_list, users_list = [], []
    for i in range(num_of_names):
        username = name_elems[i].text
        comment = comment_elems[i].text
        # print(username + ": " + comment)
        comments_list.append(comment)
        users_list.append(username)
    df = pd.DataFrame({"user": users_list, "comment": comments_list})
    df.to_csv(str(save_as+'.csv'), index=False)



youtube_scrape(url='https://www.youtube.com/watch?v=LoZXboySl2I',save_as="shikara_comments",no_of_scrolls=15)

