#3 files: (1) minnewaska.py - Scraper named by site (2) process.py takes output j.son file to see if it matches (3) matchers file whether location is open or not Return True if open

import scrapy

class AlertSpider(scrapy.Spider):
	name = 'alert'
	start_urls = [
	'https://parks.ny.gov/parks/minnewaska/details.aspx'
	]

	def parse(self, response):
		for alert in response.css('div.alert.alert-info'):
			yield {
				'text': alert.get()
			}
