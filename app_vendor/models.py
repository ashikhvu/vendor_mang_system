from django.db import models
import uuid


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=200)
    contact = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.vendor_code:
            while True:
                unique_id = uuid.uuid4().hex[:8]
                try:
                    Vendor.objects.get(vendor_code=unique_id)
                except Vendor.DoesNotExist:
                    self.vendor_code = unique_id
                    break
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name