from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Item(TimeStampModel):
	category = models.CharField(max_length=255)
	subcatgeory = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	amount = models.PositiveIntegerField()

	def __str__(self) -> str:
		return self.name

