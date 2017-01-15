# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = (
        'http://search.jd.com/Search?keyword=三星s7&enc=utf-8&wq=三星s7&pvid=tj0sfuri.v70avo',
    )

    def parse(self, response):
        print response.body
