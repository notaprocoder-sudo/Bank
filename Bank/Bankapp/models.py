from django.db import models


class district(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class bran(models.Model):
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Cust(models.Model):
    name = models.CharField(max_length=150)
    Date_of_Birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField( max_length=20)
    Phone_Number = models.IntegerField()
    Email = models.CharField(max_length=100)
    address = models.TextField()
    District = models.ForeignKey(district, on_delete=models.SET_NULL,blank=True, null=True)
    Branch = models.ForeignKey(bran, on_delete=models.SET_NULL,blank=True, null=True)
    Account_type = models.CharField(max_length=20)
    Cheque_book = models.CharField(max_length=50)
    Debit_Card =  models.CharField(max_length=50) 
    Credit_Card = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name