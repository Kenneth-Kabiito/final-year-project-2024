from django.db import models


class Document(models.Model):
	file = models.FileField(upload_to='documents/')
	description = models.CharField(max_length=255)
