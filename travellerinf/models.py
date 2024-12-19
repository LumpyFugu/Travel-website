from django.db import models

# Create your models here.

class Travellerinf(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.IntegerField()
    head = models.FileField(upload_to='./templates/')

    def __str__(self):
        return self.user

class Comments(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    msg = models.TextField(verbose_name='Content')
    cs = models.IntegerField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name