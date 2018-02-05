import scrapy
import logging
from time import gmtime, strftime

from scrapy.spiders import Spider


class SubredditsSpider(Spider):
    name = 'subreddits-list'

    def start_requests(self):
        urls = ['https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_links = response.xpath('//a/@href').extract()
        for link in all_links:
            if link.startswith('/r/'):
                yield {'##List of subreddits:': response.urljoin(link)}
