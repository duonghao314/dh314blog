from django.contrib import admin
from blog.models import Category,Article
# Register your models here.
admin.site.register(
    Category,
    list_display = ['id', 'catName', 'catKeyWord','catViews'],
    list_filter = ['catName', 'catViews'],

)
admin.site.register(
    Article,
    list_display=['id', 'artName', 'artAuthor', 'artDate','artViews','artCat'],


)