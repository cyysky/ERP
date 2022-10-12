from django.db import models
from django.utils.safestring import mark_safe 
from PIL import Image as Im                  # new

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='pics')

    def save(self):                        # new
        super().save()

        img = Im.open(self.photo.path)

        # resize it
        if img.height > 1920 or img.width > 1080:
            output_size = (1920,1080)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def image_tag(self):                     
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))
 

