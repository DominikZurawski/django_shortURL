from django.db import models
from django.utils.crypto import get_random_string

def shortURL():
    shortname = get_random_string(length=6)
    return shortname

class QueryURL(models.Model):
	queryURL = models.URLField()
	shortURL = models.CharField(max_length=6, default=shortURL)

	def __str__(self):
		return self.queryURL

class AnswerURL(models.Model):
    URL = models.ForeignKey(QueryURL, on_delete=models.CASCADE)
    short_URL = shortURL()
