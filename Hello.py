from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\Deepak\\PycharmProjects\\FirstProject\\chromedriver.exe")
driver.get("https://www.google.com")
print("google launched")
print("Google Successfully automated")
driver.close()





