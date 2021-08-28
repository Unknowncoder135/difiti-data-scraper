from selenium import webdriver



from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
import time
import urllib.request
import urllib
import os
import wget
# PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

for x in range(1,2):
    driver.get(f"https://www.dafiti.com.br/roupas-masculinas/camisetas/?page={x}")
    time.sleep(3)

    # main_div = driver.find_element_by_class_name("catalog-ajax-loading")
    # print(main_div)

    mm  = driver.find_elements_by_class_name("product-box")
    # print(len(mm))

    main_url = []
    for x in mm:
        cc = x.find_element_by_tag_name("a").get_attribute("href")
        main_url.append(cc)
    # print(main_url)
    main_url = main_url[1:]
    main_item_list = []
    for v in main_url:
        driver.get(v)
        time.sleep(2)
        boy_name = driver.find_element_by_xpath("//*[@id='wrapper']/div[3]/div[3]/div[2]/div[2]/div[1]/a").text
        # print(boy_name)
        address = driver.find_element_by_xpath("//*[@id='wrapper']/div[3]/div[3]/div[2]/div[2]/h1").text
        # print(address)
        try:
            price = driver.find_element_by_class_name("catalog-detail-price-value").text
            # print(price)
        except:
            price  = driver.find_element_by_class_name("catalog-detail-price-special").text
            # print(price)
        discription = driver.find_element_by_class_name("product-information-description").text
        img_url  = driver.find_element_by_tag_name("img").get_attribute('src')
        # print(img_url,discription)
        main_dir={
            "boy_name":boy_name,
            "address":address,
            "item_price":price,
            "item_description":discription,
            "item_imgurl":img_url
        }
        main_item_list.append(main_dir)
    print(main_item_list)
    print(f"page no..{x}")


df = pd.DataFrame(main_item_list)
df.to_csv("main_data.csv",index=False)
print("Mission Complate")





