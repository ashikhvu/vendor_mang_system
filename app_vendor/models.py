from django.db import models
import uuid


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=200)
    contact = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)

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
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0,blank=True,null=True)

    status_coices = (
        ("pending","pending"),
        ("completed","completed"),
        ("cancelled","cancelled")
    )
    status = models.CharField(max_length=50,choices=status_coices,default="pending")

    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.po_number:
            while True:
                po_num = uuid.uuid4().hex[:8]
                try:
                    PurchaseOrder.objects.get(po_num=po_num)
                except PurchaseOrder.DoesNotExist:
                    self.po_number = po_num
                    break
        super().save(*args,**kwargs)

    def __str__(self):
        return self.po_number