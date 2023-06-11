from django.contrib import admin
from django.urls import path
from bunin_pages import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("content/<str:article>/", views.get_page_handler),
    path('exhibit/<slug:slug>/', views.show_exhibit, name='exhibit'),
]
