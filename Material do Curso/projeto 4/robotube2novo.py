from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RoboYoutube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        s=Service(ChromeDriverManager().install())
        self.webdriver = webdriver.Chrome(service=s, options=options)

    def busca(self, busca):
        url = "https://www.youtube.com/results?search_query=%s" %busca
        self.webdriver.get(url)

bot = RoboYoutube()
bot.busca("teste")