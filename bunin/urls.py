"""bunin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path
from django.views.generic import TemplateView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import ExhibitSitemap
from django.conf.urls import handler404


from rollyourown.seo.admin import register_seo_admin
from django.contrib import admin
from myapp.seo import MyMetadata



#register_seo_admin(admin.site, MyMetadata)

sitemaps = {
    'exhibits': ExhibitSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bunin/", include('bunin_pages.urls')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="bunin/robots.txt", content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
]

handler404 = 'bunin_pages.views.page_not_found_view'
