# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobssearchItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位领域
    professional_field = scrapy.Field()
    # 职位名称
    occupation = scrapy.Field()
    # 基础信息
    basic_info = scrapy.Field()
    # 职位描述
    job_description = scrapy.Field()
    # 简历要求
    resume_requirements = scrapy.Field()
    # 截止日期
    deadline = scrapy.Field()
    # 工作地点
    place_of_work = scrapy.Field()

