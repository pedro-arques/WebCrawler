from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import timedelta
import re

class Application():
    def __init__(self):
        self.options = Options()
        self.service = webdriver.ChromeService(executable_path=r'chromedriver.exe')
        self.URL = '{placeholder}'
        self.padrao = r"(\d+) dias e (\d+) horas"

    def navigation(self,url):
        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        self.driver.get(url)

    def cardInfo(self):
        i = 1
        list_card = []
        while i != 8:
            element = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='newPerformanceCard']/div[2]/div[@class][" + str(i) + "]")))
            list_card.append(element.text)
            i += 1
        return list_card
    
    def scoreInfo(self):
        score = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='ra-new-reputation']/span[@class]/b[@class]")))
        score = score.text.split('/')[0]
        return score

    def formatting(self, card, score):
        print(len(card))
        regex = r'\d+\.?\d*'
        new_list = []
        for string in card[0:6]:
            matches = re.findall(regex, string)
            for match in matches:
                new_list.append(float(match))
        match = re.search(self.padrao, card[6])
        if match:
            days = int(match.group(1))
            hours = int(match.group(2))
            timedelta_c = timedelta(days=days, hours=hours)
            postgres_datetime = f"{timedelta_c.days} days {timedelta_c.seconds // 3600} hours"
            new_list.append(postgres_datetime)
        new_list.append(float(score))
        return new_list

    def navigationClose(self):
        self.driver.quit()
