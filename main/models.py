from django.db import models

# Create your models here.
class custom_extension(models.Model):
	extension = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.extension

class Long_URL(models.Model):
    short = models.ForeignKey(custom_extension ,null=True, on_delete=models.CASCADE)
    full_url = models.URLField(default="www.google.com" , null=False)
    def __str__(self):
        return self.full_url