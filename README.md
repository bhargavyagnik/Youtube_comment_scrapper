# YouTube Comment Scrapper
A Python-selenium scrapper made to access the comments on YouTube videos of a given link without any login and auto scroll which is first of its kind ;)

Using Selenium and Chromedriver I have tried to make a Youtube Comment Scrapper. Selenium is a portable framework for testing web applications. Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language

### Import the following Libraries first


```python
from selenium import webdriver # Run the Selenium webdriver which would load the browser defined
import time # for waiting to load the pages
import os #Change environment for webdriver 
from selenium.webdriver.common.keys import Keys # For Controlling the Scroll, we import keys from the given package
import pandas as pd #For converting it to Dataframe and saving into a CSV file
```

You need to assign your path to the chrome driver so that it can assign its ennviromnent to selenium, pass url of the video in order to load that page on the browser


```python
chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
base_url = "https://www.youtube.com/watch?v=TSdmciOBA2M&t=18s"
driver.get(base_url)
```

For the Comments we need to scroll down, so this part covers how to scroll in Youtube. You can scroll down in selenium with a following code too but Youtube has an unknown length and it does not return the Scroll height unlike other pages on the internet. So this is the best trick to scroll on youtube.You wont find it anywhere over the internet


```python
scroll=0
#Scroll 15 gives around 300 comments
while scroll<13:
    try:
        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll+=1
    except Exception as s:
        print(s)
```

Now we use the traditional method for scrapping i.e. we find where the comments are stored in the html by using a function called 'find_elements' . There are various methods to find the attribute but here i have used its xpath to find its location.
This is stored in a list  which is then used to store in the dataframe


```python
name_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
num_of_names = len(name_elems)
print(num_of_names)
```

    260
    


```python
comments_list, users_list = [], []

for i in range(num_of_names):
    username = name_elems[i].text
    comment = comment_elems[i].text
    #print(username + ": " + comment)
    comments_list.append(comment)
    users_list.append(username)
df = pd.DataFrame({"user": users_list, "comment": comments_list})
df.to_csv('HindustaniBhau.csv',index=False)
```


```python

```
