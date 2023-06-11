from django.contrib.sitemaps import Sitemap
from bunin_pages.models import Exhibit

class ExhibitSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Exhibit.objects.all()

    def lastmod(self, obj):
        pass #return obj.publish