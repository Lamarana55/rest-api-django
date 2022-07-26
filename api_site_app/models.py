
from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GeeksModel(TimeStampModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="images/%Y/%m/%d")


    def __str__(self) -> str:
        return self.title
