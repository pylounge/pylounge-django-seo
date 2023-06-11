from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class Exhibit(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse("exhibit", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)