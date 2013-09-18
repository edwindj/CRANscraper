from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from CRAN.items import RPackage
from pattern.web import DOM, plaintext

class PackagesSpider(CrawlSpider):
    name = 'packages'
    allowed_domains = ['cran.r-project.org']
    start_urls = ['http://cran.r-project.org/web/packages/available_packages_by_name.html']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'index.html'), callback='parse_package', follow=True),
    )

    def parse_package(self, response):
        dom = DOM(response.body)

        package = RPackage()
        
        nd = plaintext(dom("h2")[0].content)
        i = nd.find(':')
        
        package['name'] = nd[:i]
        package['description'] = nd[i+1:].strip()
        
        table0 = dom('table')[0]

        for tr in table0("tr"):
            td = tr("td")
            key = (td[0].content).strip(':').lower().replace(" ", "_")
            value= plaintext(td[1].content)
            if package.fields.has_key(key):
                package[key] = value
        
        #package['dump'] = plaintext(dom.content)
        return package
