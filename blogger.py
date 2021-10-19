from selenium import webdriver

import time
from datetime import date

#getting to day's date
today = date.today()
print(f"{today.day} {today.month}")

#set the header option for the webdriver
PATH = "/home/hama/Documents/chromedriver"
driver = webdriver.Chrome(PATH)


#scrapping the meduim blog site
def blog_scrapper():
    url = f"https://medium.engineering/"
    driver.get(url)
    time.sleep(2)

    links = [item.find_elements_by_tag_name('a')[1].get_attribute('href') for item in driver.find_elements_by_class_name('lw')]
    print(len(links))
    
    i = 0 
    for link in links :
        i+=1 
        if i == 2:
            break
        
        driver.get(link)
        time.sleep(3)
        
        title = driver.find_element_by_tag_name('h1').text
        print(title)
        image = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/article/div/section/div/div/figure[1]/div/div/img').get_attribute('src')
        print(image)
        y = 250
        for timer in range(0,20):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 250  
            time.sleep(1)
        
        body = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/article/div/section/div').get_attribute('innerHTML')
        print(body)
        
'''
https://www.ign.com/reviews/tv
https://www.ign.com/reviews/movies
https://www.ign.com/reviews/games
'''

#main runner
def main():
    blog_scrapper()

if __name__ == '__main__':
    main()