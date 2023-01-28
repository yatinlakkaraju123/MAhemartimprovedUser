from django.db import models

# Create your models here.
class Payment(models.Model):
    
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
       # return self.user.username