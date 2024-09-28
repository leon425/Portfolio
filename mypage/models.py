from django.db import models

class HomePage(models.Model):
    img_name= models.CharField(max_length=200, default="img_name")
    img = models.ImageField(null=True, blank=True, upload_to="mypage/images") #inside the media directory,

    def __str__ (self):
        return self.img_name 
                                        
