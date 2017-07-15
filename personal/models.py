from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
	product_name=models.CharField(max_length=20)
	product_price=models.CharField(max_length=30)
	product_quality=models.CharField(max_length=30)
	product_date = models.DateField(null=True)
	product_image = models.FileField()

	def __str__(self):
		return self.product_name+"  "+self.product_price+"  "+self.product_quality

	def get_absolute_url(self):
	    return reverse('detail-pro', kwargs={'pk':self.pk})	