import requests
from tkinter import Tk
import webbrowser
from bs4 import BeautifulSoup
import sys
import time


class Datasheet():


	def __init__(self,findProduct=''):
		self.findProduct=findProduct
		self.login()
		self.getProductPage()
		self.getProductDatasheetLink()
		self.openWebPage(self.dataSheet)

	def login(self):
		self.c=requests.Session()
		self.productsUrl='http://www.ldbiopharma.com/en/products.asp'
		
		# print(products)

	@staticmethod
	def cleanHtml(html):
		return str(html).lower()

	def getProductPage(self):
		self.products=self.c.get(self.productsUrl).text	

		soup = BeautifulSoup(self.products, 'lxml')
		found=False
		for product in soup.find_all('a'):
			if self.findProduct.lower() in self.cleanHtml(product):
				print(product)
				# print(product['href'])
				productPage=product['href'].strip('..')
				site='http://www.ldbiopharma.com'
				site+=productPage
				print(site)
				self.productPage=site
				found=True
				break
		if found is False:
			print('Nothing Found')
			time.sleep(2)
			sys.exit()

	def getProductDatasheetLink(self):
		productPage=self.c.get(self.productPage).text	

		soup = BeautifulSoup(productPage, 'lxml')
		find='Download Datasheet'
		for link in soup.find_all('a'):
			if find.lower() in self.cleanHtml(link):
				print(link)
				dataSheet=link['href']
				self.dataSheet=dataSheet



	def openWebPage(self,url):
		webbrowser.open(url)
		
def pasteFile():

	root=Tk()
	root.withdraw()
	content=root.clipboard_get()
	
	
	return content


if __name__ == '__main__':
	clipboard=pasteFile()
	print('Trying to find',clipboard)
	Datasheet(clipboard)