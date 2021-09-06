# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5555/random'
proxy_ip = [
            {"http": "http://12.13.1.10:1234"},
            {"http": "http://12.11.2.15:2048"},
            {"http": "http://183.166.136.144:8888"},
            {"http": "http://121.52.208.200:808"},
            {"http": "http://180.119.68.10:9999"},
            {"http": "http://27.208.231.100:8060"},
            {"http": "http://123.169.99.177:9999"},
            {"http": "http://119.84.84.185:12345"},
            {"http": "http://101.132.190.101:80"},
            {"http": "http://114.99.54.65:8118"},
            {"http": "http://119.4.13.26:1133"},
            {"http": "http://58.253.158.177:9999"},
            {"http": "http://114.223.208.165:8118"},
            {"http": "http://112.84.73.53:9999"},
            {"http": "http://221.237.37.137:8118"},
            {"http": "http://117.45.139.84:9006"},
            {"http": "http://171.35.86.72:8118//"},
            {"http": "http://49.235.246.24:8118"},
            {"http": "http://114.223.103.47:8118"},
            {"http": "http://58.215.201.98:35728"},
            {"http": "http://60.188.65.73:3000"},
            {"http": "http://49.235.69.138:8118"},
            {"http": "http://112.14.47.6:52024"},
            {"http": "http://222.85.28.130:40505"},
            {"http": "http://116.204.142.62:8080"},
            {"http": "http://60.191.11.229:3128"},
            {"http": "http://163.125.71.198:9999"},
            {"http": "http://14.115.107.232:808"},
            {"http": "http://113.78.255.93:9000"},
            {"http": "http://60.191.11.237:3128"},
            {"http": "http://58.255.38.156:9000"},
            {"http": "http://163.125.71.195:8888"},
            {"http": "http://123.163.24.113:3128"},
            {"http": "http://222.240.184.126:8086"},
            {"http": "http://117.141.155.241:53281"},
            {"http": "http://218.22.7.62:53281"},
            {"http": "http://14.153.52.10:3128"},
            {"http": "http://61.164.39.69:53281"},
            {"http": "http://27.38.155.190:8118"},
            {"http": "http://113.65.163.199:9797"},
            {"http": "http://125.46.0.62:53281"},
            {"http": "http://111.164.20.86:8111"},
            {"http": "http://58.251.235.76:9797"},
            {"http": "http://183.166.103.164:9999"},
            {"http": "http://117.88.176.123:3000"},
            {"http": "http://171.35.163.132:9999"},
            {"http": "http://60.31.213.115:808"},
            {"http": "http://183.166.136.144:8888"},
            {"http": "http://27.208.231.100:8060"},
            {"http": "http://123.169.99.177:9999"},
            {"http": "http://119.84.84.185:12345"},
            {"http": "http://101.132.190.101:80"},
            {"http": "http://60.190.250.120:8080"},
            {"http": "http://125.94.44.129:1080"},
            {"http": "http://118.112.195.91:9999"},
            {"http": "http://118.89.91.108:8888"},
            {"http": "http://125.122.199.13:9000"},
            {"http": "http://59.62.35.130:9000"},
            {"http": "http://123.163.96.124:9999"},
            {"http": "http://175.44.108.164:9999"},
            {"http": "http://110.243.15.228:9999"},
            {"http": "http://59.62.24.87:9000"},
            {"http": "http://175.42.68.223:9999"},
            {"http": "http://180.104.63.242:9000"},
            {"http": "http://106.75.177.227:8111"},
            {"http": "http://121.233.206.211:9999"},
            {"http": "http://175.44.109.104:9999"},
            {"http": "http://163.204.240.107:9999"},
            {"http": "http://60.13.42.77:9999"},
            {"http": "http://49.89.86.30:9999"},
            {"http": "http://106.42.217.26:9999"},
            {"http": "http://115.29.170.58:8118"},
            {"http": "http://183.166.133.196:9999"},
            {"http": "http://175.44.109.71:9999"},
            {"http": "http://163.204.244.219:9999"},
        ]


class RandomProxyMiddleware(object):
    # 动态设置ip代理
    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(proxy_ip)


class JobssearchSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JobssearchDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
