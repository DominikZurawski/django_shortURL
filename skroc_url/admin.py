from django.contrib import admin

# Register your models here.
from .models import QueryURL, AnswerURL

admin.site.register(QueryURL)
#admin.site.register(AnswerURL)