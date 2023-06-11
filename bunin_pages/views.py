from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponse, HttpRequest, Http404, JsonResponse
from typing import Union, Optional
from django import template
from django.shortcuts import get_object_or_404
from .models import Exhibit

def page_not_found_view(request, exception):
    return render(request, f'{settings.ERRORS_TAMPLATES_PATH}/404.html', status=404)

async def get_page_handler(request:HttpRequest, article:str) -> Optional[Union[HttpResponse, HttpResponseNotFound]]:
    template_path: str = f'{settings.BUNIN_PAGES_TEMPLATES_PATH}/{article}.html'
    try:
        template.loader.get_template(template_path)
        return render(request, template_path)
    except template.TemplateDoesNotExist:
        if settings.DEBUG:
            return render(request, f'{settings.ERRORS_TAMPLATES_PATH}/404.html', status=404)
        else:
            raise Http404('Страница не существует')

def show_exhibit(request, slug):
    exhibit = get_object_or_404(Exhibit, slug=slug)
    return JsonResponse({'exhibit': exhibit.title, 'desc': exhibit.description})