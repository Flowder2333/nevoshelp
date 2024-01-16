from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys



service = Service(executable_path="C:/Program Files (x86)/chromedriver.exe")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://helpdesk.evolutiongaming.com/nevos/selfservice/#login")


## QUESTIONS 

su_quest = input("Are you super user?")
if su_quest == "admin":
    login = "q.kikava@gmail.com"
    password = "Lucifer69@."

else:
    login = input("Enter mail: ")
    password = input("Enter password: ")

ask_for_building = input("In which building do you want to send reservation request?(A,C,D,E): ")
res_date = input("Enter date when do you want to send reservation request: ")
shift_type = input("In which shift type do you want to send reservation request? 1) Morning 2) Afternoon 3) Night:  ")




login_creds = driver.find_element(By.ID, 'login-input')
login_creds.send_keys(login)

password_creds = driver.find_element(By.ID, 'password-input')
password_creds.send_keys(password)

login_button = driver.find_element('xpath', '//*[@id="login-button"]')
login_button.click()
driver.implicitly_wait(10)


menu2 = driver.find_element('xpath', '//*[@id="navbar-requests-menu"]')
menu2.click()

menu3 = driver.find_element("xpath", '//*[@id="my-reservation-requests-link"]')
menu3.click()

req_res = driver.find_element("xpath", '//*[@id="request-reservation-button"]')
req_res.click()

req_res_Type = driver.find_element("xpath", '//*[@id="group-selector"]/div/button')
req_res_Type.click()

if ask_for_building == "A":
    a_building = driver.find_element("xpath", '//*[@id="group-selector-option-aab52763-28c1-4e16-9fd2-eac0ff1e34c0"]/a')
    a_building.click()
elif ask_for_building == "C":
    c_building = driver.find_element("xpath", '//*[@id="group-selector-option-feec473b-8285-4afd-9784-7a2e132417fb"]/a')
    c_building.click()
elif ask_for_building == "D":
    d_building = driver.find_element("xpath", '//*[@id="group-selector-option-7ad5db6d-f4b4-4f5b-8267-7d269db0b3ab"]/a')
    d_building.click()
elif ask_for_building == "E":
    e_building = driver.find_element("xpath", '//*[@id="group-selector-option-b4771f2b-f8c7-4909-b180-7d417e0b5983"]/a')
    e_building.click()

click_box = driver.find_element("xpath",'//*[@id="positions-for-16-01-2024"]/div[2]/div/div/div[2]/span/i')
click_box.click()


#### Reserveration full info
res_date_sub = driver.find_element("xpath", '//*[@id="reservation-shift-start-date-text"]/div/div/input')
res_date_sub.send_keys(Keys.CONTROL + "a")
res_date_sub.send_keys(Keys.DELETE)
res_date_sub.send_keys(res_date)

if shift_type == "1":
    shift_from = driver.find_element(By.ID, "reservation-shift-start-time")
    shift_from.send_keys(Keys.CONTROL + "a")
    shift_from.send_keys(Keys.DELETE)
    shift_from.send_keys("08:00")

    shift_till = driver.find_element(By.ID, "reservation-shift-end-time")
    shift_till.send_keys(Keys.CONTROL + "a")
    shift_till.send_keys(Keys.DELETE)
    shift_till.send_keys("16:00")
elif shift_type == "2":
    shift_from = driver.find_element(By.ID, "reservation-shift-start-time")
    shift_from.send_keys(Keys.CONTROL + "a")
    shift_from.send_keys(Keys.DELETE)
    shift_from.send_keys("16:00")

    shift_till = driver.find_element(By.ID, "reservation-shift-end-time")
    shift_till.send_keys(Keys.CONTROL + "a")
    shift_till.send_keys(Keys.DELETE)
    shift_till.send_keys("00:00")
elif shift_type == "3":
    shift_from = driver.find_element(By.ID, "reservation-shift-start-time")
    shift_from.send_keys(Keys.CONTROL + "a")
    shift_from.send_keys(Keys.DELETE)
    shift_from.send_keys("00:00")

    shift_till = driver.find_element(By.ID, "reservation-shift-end-time")
    shift_till.send_keys(Keys.CONTROL + "a")
    shift_till.send_keys(Keys.DELETE)
    shift_till.send_keys("08:00")

res_role = driver.find_element(By.ID,"reservation-role")
res_role.click()
res_role_ment2 = driver.find_element("xpath", '//*[@id="reservation-role-option-07d1a93a-33b1-46e4-9b12-dae4d4a236ac"]/a')
res_role_ment2.click()

submit_res = driver.find_element(By.ID, 'submit-reservation')
submit_res.click()
time.sleep(50)