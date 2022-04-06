#name = input('What is your name?\n')
#print('Hi, %s.' % name)
import json
# Python with Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
name = input('Enter Product to search in Amazon?\n')
driver.get("https://www.amazon.in/s?k=%s"%name)
amazonSearchResult = driver.find_elements(By.XPATH, './/div[@data-component-type="s-search-result"]')
item = []
myDict = {}
#for items in amazonSearchResult:
#  name = items.find_element(By.XPATH,'.//div[@class="a-spacing-micro"]')
#  print(name.text)
#driver.findElement(By.xpath("//input[@id='usernamereg-firstName']"))
#amazonSearchResult = driver.find_elements_by_xpath('.//div[@data-component-type="s-search-result"]')
#print(items)
for items in amazonSearchResult:
  
  #print(items.find_elements(By.TAG_NAME,'span')[3].text)
#  print(items.find_element(By.CSS_SELECTOR,'span.a-color-secondary').text)
  myDict["name"] = items.find_element(By.CSS_SELECTOR,'span.a-text-normal').text
#  item.append(items.find_element(By.CSS_SELECTOR,'span.a-text-normal').text)
  try:
    s = items.find_element(By.CSS_SELECTOR,'span.a-color-secondary')
    if(s.text == "Sponsored"):
      myDict["sponsored"] = "yes"
#      item.append(s.text)
  except NoSuchElementException:
    myDict["sponsored"] = "no"
    pass

  try:
    s = items.find_element(By.CSS_SELECTOR,'span.a-price-whole')
    myDict["price"] = s.text
#      item.append(s.text)
  except NoSuchElementException:
    myDict["price"] = ""
    pass
    
#  item.append(items.find_element(By.CSS_SELECTOR,'span.a-price-whole').text)
#  myDict["price"] = items.find_element(By.CSS_SELECTOR,'span.a-price-whole').text
#  item.append(items.get_attribute('data-asin'))
  myDict["asin"] = items.get_attribute('data-asin')
  item.append(myDict)
  myDict = {}
  #item.append(items.find_elements(By.TAG_NAME,'span')[3].text)
  #print(items.find_elements(By.TAG_NAME,'span')[10].text)  
  #item.append(items.find_elements(By.TAG_NAME,'span')[10].text)
#print(amazonSearchResult)
jsonOutput = json.dumps(item)
print(jsonOutput)
