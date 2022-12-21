import undetected_chromedriver.v2 as webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep



class SMS:
	def __init__(self, username, password):

		#chrome options
		chrome_options = Options()
		#chrome_options.add_argument("--headless")
		#chrome_options.add_argument("window-size=1920,1080")
	

		#load the webdriver and open the google voice page
		self.driver = webdriver.Chrome(options=chrome_options)
		self.driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-50159673%3A1671291074691262&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&osid=1&passive=1209600&service=grandcentral&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh56oVsr1IpTUolsL1qnF9sWhnwqVhLLJfLB63v2BUsgq1LZc3xpr2hYbMEAXB8wScODCKwVhQ")

		#this is the time to  wait on an element to load before returning an error
		self.wait = WebDriverWait(self.driver, 10)

		#select the email field and enter email address
		email_field = self.driver.find_element(By.NAME, "identifier")
		email_field.send_keys(username)
		email_field.send_keys(Keys.RETURN)

		#select the password field and enter the password
		password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
		password_field.send_keys(password)
		password_field.send_keys(Keys.RETURN)

	def send(self, recipient, message):

		#load the messages tab of google voice
		self.driver.get("https://voice.google.com/u/0/messages")

		#select start a new message so that the phone number slot opens up
		new_message_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='messaging-view']/div/md-content/div/div/div"))).click()


		#select the number field and input number
		recipient_field = self.driver.find_element(By.XPATH, "//*[@id='input_0']")
		recipient_field.send_keys(recipient)
		recipient_field.send_keys(Keys.RETURN)

		#select the message field and input message
		message_field = self.driver.find_element(By.XPATH, "//*[@id='input_1']")
		message_field.send_keys(message)
		message_field.send_keys(Keys.RETURN)


	def quit(self):
		#this time is so that any opperationis can be complete if run right against sending a message
		#experiement if this is actually needed
		sleep(1)
		self.driver.quit()