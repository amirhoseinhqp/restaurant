from django.contrib import admin
from .models import blog , category , tag
# Register your models here.
admin.site.register(blog)
admin.site.register(category)
admin.site.register(tag)