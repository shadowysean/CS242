# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RedditCopperPipeline(object):
    def process_item(self, item, spider):
        if spider == 'subreddits-list':
            return item['subreddit']
        else:
            return item
