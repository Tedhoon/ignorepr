from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/') #미디어 폴더안 images란 폴더안에 사진을 넣어줄거다.
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title