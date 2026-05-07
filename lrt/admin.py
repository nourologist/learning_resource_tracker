from django.contrib import admin

# Register your models here.


from .models import Category, Tag, ResourceType, Status, Entry

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ResourceType)
admin.site.register(Status)
admin.site.register(Entry)
