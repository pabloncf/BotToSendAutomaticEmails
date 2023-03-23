# Install:
# pip install selenium
# pip install pyautogui
# pip install webdriver-manager
# Browser webdriver

from selenium import webdriver  # import the selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # use to run the chrome drive
import time
from model.Table import Table

# ele vai instalar a versão do driver mais recente
serviceDriver = Service(ChromeDriverManager().install())

# if you are trying to login to a website and it is printing an error put these 2 lines of options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


class SendEmail:
    browser = webdriver.Chrome(options=options, service=serviceDriver)

    def __init__(self):
        self.browser = SendEmail.browser

    # Accessing the site
        self.browser.get(
            'https://accounts.google.com/v3/signin/identifier?dsh=S2097239754%3A1679524535140959&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AWnogHf9HvbyPU6_GYv3QTdVDrScTGb-j_e-GJP6CpXZWBna8KOEVVPkZabTUQI4AUFcBUX6sMc5&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    # when the login starts, the user puts his email and password and the bot continues
    def loginValidation(self):
        input()

    def send_email(self):

        self.browser = SendEmail.browser

        self.browser.find_element(
            'xpath', '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()

        self.table = Table().colectingActivePartners()
        self.partnes_email = self.table['Emails']

        for email in self.partnes_email:
            self.browser.find_element(
                'xpath', '//*[@id=":bf"]'
            ).send_keys(email)

            self.browser.find_element(
                'xpath', '//*[@id=":bf"]'
            ).send_keys(', ')
            time.sleep(1)

        self.subjectInput = input("Digite o assunto: ")
        self.bodyInput = input("Digite o corpo do email: ")

        self.browser.find_element(
            'xpath', '//*[@id=":7h"]'
        ).send_keys(self.subjectInput)

        self.browser.find_element(
            'xpath', '//*[@id=":8q"]'
        ).send_keys(self.bodyInput)

        time.sleep(2)

        self.browser.find_element(
            'xpath', '//*[@id=":77"]').click()


bot = SendEmail()
bot.loginValidation()
bot.send_email()
