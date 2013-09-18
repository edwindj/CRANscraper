# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class RPackage(Item):
    name = Field()    
    author = Field()
    description = Field()
    depends = Field()
    imports = Field()
    enhances = Field()
    suggests = Field()
    version = Field()
    in_views = Field()
    published = Field()
    version = Field()
    dump = Field()
    # define the fields for your item here like:
    # name = Field()
