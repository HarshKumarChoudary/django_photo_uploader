from django.db import models

class imageTable(models.Model):

    image = models.ImageField(upload_to= "imgdb")
    date = models.DateTimeField(auto_now_add=True)