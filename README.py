from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://tigers.co.kr/players/outfielder"
    print(f"가져올 페이지: {url}")
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "name"))
    )

    soup = bs(driver.page_source, "html.parser")

    player_name_tags = soup.find_all("li", class_="name")
    player_names = [tag.get_text(strip=True) for tag in player_name_tags]

    print("\n외야수 선수 명단:")
    for name in player_names:
        print(f"- {name}")

except Exception as e:
    print("선수 리스트가 로딩되지 않았습니다.")
    print(e)

finally:
    driver.quit()
