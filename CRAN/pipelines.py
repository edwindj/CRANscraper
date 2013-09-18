# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class PackagePipeline(object):
    def process_item(self, item, spider):
        self.split(item, 'depends')
        self.split(item, 'imports')
        self.split(item, 'suggests')
        self.split(item, 'enhances')
        return item
    
    def split(self, item, key):
        if item.has_key(key):
            item[key] = item[key].split(', ')
      