from selenium import webdriver
import time
from playsound import playsound

browser = webdriver.Chrome()
browser.get("https://www.newegg.com/p/pl?d=3060&N=100007709%20601361654%20601359415%20601357250&isdeptsrh=1&page=1")

browser.maximize_window()
time.sleep(15)
buttunClose = browser.find_element_by_xpath('/html/body/div[10]/div/div/div/div[2]/div[2]/button[1]')

buttunClose.click()

time.sleep(3)

signInButton = browser.find_element_by_xpath("/html/body/div[7]/header/div[1]/div[4]/div[1]/div[1]/a/i")

signInButton.click()

time.sleep(3)
mail= browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form/div/div[1]/div/input')
mail.send_keys('mr.kerembozdag@gmail.com')
girişme = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form/div/div[3]/button')
girişme.click()                         
time.sleep(3)
backButton = browser.find_elements_by_css_selector(".fa.fa-arrow-circle-left")
backButton[0].click()
time.sleep(3)
sendOneButton = browser.find_elements_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form/div/div[4]/button")
sendOneButton[0].click()
time.sleep(3)
backButton2 = browser.find_elements_by_css_selector(".fa.fa-arrow-circle-left")
backButton2[0].click()
time.sleep(3)
girişme2 = browser.find_elements_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form/div/div[3]/button")
girişme2[0].click()
time.sleep(3)
şifre = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/input')
şifre.send_keys('Sabaz124578')
şifreButton= browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div/div[2]/form/div/div[3]/button')
şifreButton.click()
time.sleep(5)


generalLinks = []

for page in range(1,3):
    browser.get("https://www.newegg.com/p/pl?d=3060&N=100007709%20601361654%20601359415%20601357250&isdeptsrh=1&page=" + str(page))
    print(page)
    SCROLL_PAUSE_TIME = 4

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    

    elems = browser.find_elements_by_css_selector(".item-container [href]")
    links = [elem.get_attribute('href') for elem in elems]

    for link in links:
        if (link.startswith("https://www.newegg.com/")) and ("BrandStore" not in link) and ("https://www.newegg.com/p/" not in link) and ("3090" not in link):
            generalLinks.append(link)

    for i in generalLinks:
        print(i)

    time.sleep(3)

print("------------------------------------------------------")
for i in generalLinks:
    print(i)

while True:
    for i in generalLinks:
        browser.get(i)
        print(i)
        time.sleep(3)
        try:
            
            addButton = browser.find_elements_by_css_selector(".btn.btn-primary.btn-wide")
            
            addButton[0].click()
            print("Stok var!")

            time.sleep(3)
            
            browser.get("https://secure.newegg.com/shop/cart")

            time.sleep(3)

            notInterested = browser.find_element_by_xpath("/html/body/div[7]/div[1]/div/div/div/div[3]/div[2]/button[1]")

            notInterested.click()

            time.sleep(3)

            checkOut = browser.find_element_by_css_selector(".btn.btn-primary.btn-wide")

            checkOut.click()

            time.sleep(3)

            delivery = browser.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button")

            delivery.click()

            time.sleep(3)

            conPayment = browser.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button")

            conPayment.click()

            time.sleep(3)

            CVV = browser.find_element_by_css_selector('.form-text.mask-cvv-4')

            SCROLL_PAUSE_TIME = 4

            # Get scroll height
            last_height = browser.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            CVV.click()
            
            CVV.send_keys("889")

            review = browser.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[3]/button")

            review.click()

            time.sleep(3)

            placeOrder = browser.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[3]/div/div/div[5]/div/button")

            placeOrder.click()

            playsound('KURT_ULUMASI.mp3')

            time.sleep(300)



        except:
            print("Stok yok!")

            
