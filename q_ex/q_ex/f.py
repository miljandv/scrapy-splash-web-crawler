from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files\ChromeDriver\chromedriver.exe")

browser.get("https://angel.co/companies")

nav = browser.find_element_by_class_name("startup-link")

print(nav.text)