from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(r"C:\Users\Szefowa\Desktop\chromedriver.exe")

driver.get("https://promoklocki.pl/")

search = driver.find_element_by_name("s")
search.send_keys("72004", Keys.ENTER)

link = driver.find_element_by_link_text("LEGO Nexo Knights 72004 - Starcie technologicznych czarodziejów")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo1.text))
except:
    driver.quit()
num1 = int(klo1.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70348", Keys.ENTER)

link = driver.find_element_by_link_text("LEGO Nexo Knights 70348 - Bojowy pojazd Lance'a")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))

    klo2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    
    print(int(klo2.text))
except:
    driver.quit()
num2 = int(klo2.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70349", Keys.ENTER)

link = driver.find_element_by_link_text("LEGO Nexo Knights 70349 - Miażdżący pojazd Ruiny")
link.click()

try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo3 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo3.text))
except:
    driver.quit()
num3 = int(klo3.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70321", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70321 - Machina oblężnicza generała Magmara")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo4 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo4.text))
except:
    driver.quit()
num4 = int(klo4.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70323", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70323 - Wulkaniczna kryjówka Jestro")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo5 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo5.text))
except:
    driver.quit()
num5 = int(klo5.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70316", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70316 - Pojazd Zła Jestro")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo6 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo6.text))
except:
    driver.quit()
num6 = int(klo6.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70335", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70335 - Lavaria")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo7 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo7.text))
except:
    driver.quit()
num7 = int(klo7.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70330", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70330 - Clay")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo8 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo8.text))
except:
    driver.quit()
num8 = int(klo8.text)
time.sleep(0.5)

search = driver.find_element_by_name("s")
search.send_keys("70339", Keys.ENTER)
link = driver.find_element_by_link_text("LEGO Nexo Knights 70339 - Flama")
link.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main")))
    klo9 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/dl/dd[4]")
    

    print(int(klo9.text))
except:
    driver.quit()
num9 = int(klo9.text)
time.sleep(0.5)

print("***mam teraz***")
print(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9)
print("***kloclow***")

driver.quit()