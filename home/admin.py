from django.contrib import admin
from home.models import Contact, Subscribe, Category, Strories, Tag, Comment

# Register your models here.

admin.site.register([Contact, Subscribe, Category, Strories, Tag, Comment])