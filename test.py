import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# variable declaration
wait = 5
url = "https://automationplayground.com/crm/login.html"
Email_id = "akintundetosin87@gmail.com"
password = "admin123"
EmailAddress = "akintundetosin87@gmail.com"
FirstName = "Tosin"
LastName = "williams"
City = "United State"
StateOrRegion = "ohio"

#initialize webdriver
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

#Login
Email_Id = driver.find_element(By.ID,"email-id")
Email_Id.send_keys(Email_id)

PassWord = driver.find_element (By.ID, "password")
PassWord.send_keys(password)

Submit_Id = driver.find_element(By.ID, "submit-id")
Submit_Id.click()
time.sleep(wait)


#Newcustomer registration
New_Customer = driver.find_element(By.ID,"new-customer")
New_Customer.click()
time.sleep(wait)

#Filling out the form
Email_Address = driver.find_element(By.ID,"EmailAddress")
Email_Address.send_keys(EmailAddress)

First_Name = driver.find_element(By.ID,"FirstName")
First_Name.send_keys(FirstName)

Last_Name = driver.find_element(By.ID,"LastName")
Last_Name.send_keys(LastName)

city = driver.find_element(By.ID,"City")
city.send_keys(City)

State_Or_Region = driver.find_element(By.ID,"StateOrRegion")
State_Or_Region.send_keys(StateOrRegion)

Gender = driver.find_element(By.NAME, "gender")
Gender.click()
time.sleep(wait)

#click submit
Submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
Submit_button.click()
time.sleep(wait)





