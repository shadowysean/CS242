import scrapy
import logging

from scrapy.spiders import Spider


class SubredditsSpider(Spider):
    name = 'subreddits'

    def start_requests(self):
        with open('out/subreddits-list.csv', 'r') as f:
            urls = f.readlines()
        for url in urls:
            if not url.startswith('##'):
                yield scrapy.Request(url=url[:-2] + '/', callback=self.parse)
            else:
                continue

    def parse(self, response):
        post_entries = response.selector.css('.thing')
        for entry in post_entries:
            yield {
                'subreddit': entry.css('::attr(data-subreddit)').extract(),
                'type': entry.css('::attr(data-type)').extract(),
                'id': entry.css('::attr(id)').extract(),
                'author': entry.css('::attr(data-author)').extract(),
                'timestamp': entry.css('::attr(data-timestamp)').extract(),
                'url': entry.css('::attr(data-url)').extract(),
                'permalink': entry.css('::attr(data-permalink)').extract(),
                'comments_count': entry.css('::attr(data-comments-count)').extract(),
                'upvote': entry.css('::attr(data-score)').extract(),
            }
        next_page = response.selector.css('#siteTable > div.nav-buttons > span > span.next-button > a::attr(href)'). \
            extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)
