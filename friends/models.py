from django.db import models

# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=13)
    addr = models.CharField(max_length=200, null=True)
    birthday = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name + "/ " + self.phone + "/ " + self.addr + " /" + self.birthday