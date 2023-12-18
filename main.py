import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re





def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"--user-agent={get_random_user_agent()}")
    driver = webdriver.Remote(
    command_executor='http://192.168.0.138:3000/webdriver',
        options=chrome_options,
    )
    # para correrlo localmente con selenium
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    return driver


def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    ]
    return random.choice(user_agents)


def main(URL,search_term):
   
    driver = get_driver()
    driver.get(URL)
    page_name= search_term.replace(" ", "_")
   
    home_folder="data"
    folder_date_name=datetime.now().strftime("%d-%m-%Y")
    file_hour_name=datetime.now().strftime("%I%p")
    start_time = time.time()
    if not os.path.exists(os.path.join(home_folder,folder_date_name,page_name)):
        os.makedirs(os.path.join(home_folder,folder_date_name,page_name),exist_ok=True)
    try:
        btn_cookies=driver.find_element(By.XPATH, "//*[contains(text(), 'Aceptar cookies')]").click()
        counter=1
        while True:
                driver.implicitly_wait(3)
                print(driver.title,"Pagina: ",counter)
                html_content=driver.page_source
                print("Guardando pagina: ",counter)
                with open(os.path.join(home_folder,folder_date_name,page_name,f"webpage-{counter}_Hour-{file_hour_name}.html"), "w", encoding="utf-8") as file:
                    file.write(html_content)
                menu_navegacion=driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[9]/nav')
                next_btn=menu_navegacion.find_element(By.XPATH, "//*[contains(text(), 'Siguiente')]")
                next_btn.click()
                counter+=1            
    except Exception as e:
        print(e)
        driver.quit()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    search_term=os.environ.get("search_term")
    # search_term="tv"
    print("Buscando: ", search_term)
    if search_term:
        URL=f"https://listado.mercadolibre.com.ar/{search_term}"
    main(URL,search_term)
