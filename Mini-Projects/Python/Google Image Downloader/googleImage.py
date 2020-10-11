from selenium import webdriver
import time
import requests
import urllib.request
import os
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  


class GoogleImage():
	def __init__(self, head = True):

		chrome_options = Options()
		os.system('mkdir gdownload')

		if not head:
			chrome_options.add_argument("--headless")  
		
		self.browser = webdriver.Chrome("./chromedriver", options=chrome_options) 

	def getImg(self, name, count):

		c = 1
		done = False

		while not done:
			try:
				self.browser.get("https://www.google.com/imghp?hl=EN")
				time.sleep(3)
				s = self.browser.find_element_by_name('q')

				s.send_keys(f'"{name}" word')
				s.send_keys(Keys.ENTER)

				self.browser.find_element_by_xpath(f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{c}]/a[1]/div[1]/img').click()
				time.sleep(3)

				self.i = self.browser.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img')
				src = self.i.get_attribute('src')

				image = Image.open(urllib.request.urlopen(src))

				width, height = image.size
				print(width,height)

				if width < 900 and height < 600:
					raise Exception('Image size not enough') 


				urllib.request.urlretrieve(src, os.path.join('gdownload','i'+ str(count) + '.jpg'))
				done = True
			except:
				c+=1

	def close(self):
		self.browser.quit()


image_downloader = GoogleImage()
image_downloader.getImg(name='hacktoberfest', count=1)
image_downloader.close()
