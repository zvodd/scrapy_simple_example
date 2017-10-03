# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)


class ExampleSpider(scrapy.Spider):
	name = "example"
	def __init__(self, *args, **kwargs):
		self.start_url=kwargs.get("target_url")
		super(ExampleSpider, self).__init__(*args, **kwargs)

	def start_requests(self):
		logger.info('URLTOSCRAPE= "' + self.start_url + '"')
		yield scrapy.Request(self.start_url, 
							# cookies=self.init_cookies,
							callback=self.first_parse,
							)

	def first_parse(self, response):
		for link in response.css('a::attr(href)'):
			yield {
				"link": link.extract()
			}


