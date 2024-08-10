from django.db import models

# Create your models here.

class userlogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UOM(models.Model):
    uom= models.CharField(max_length=100)


class Company(models.Model):
    companyName = models.CharField(max_length=50, null=True)
    printCompanyName = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=50, null=True)
    address2 = models.CharField(max_length=50, null=True)
    address3 = models.CharField(max_length=50, null=True)
    address4 = models.CharField(max_length=50, null=True)
    pincode = models.CharField(max_length=50, null=True)
    contact=models.CharField(max_length=50, null=True)
    gstRegType = models.CharField(max_length=50, null=True)
    salesEntry = models.CharField(max_length=50, null=True)
    saleInclusive = models.CharField(max_length=50, null=True)
    blankSaleItems = models.CharField(max_length=50, null=True)
    makeRoundOff=models.CharField(max_length=50, null=True)
    showDiscount=models.CharField(max_length=50, null=True)
    showGstDetails = models.CharField(max_length=50, null=True)
    gstIn = models.CharField(max_length=50, null=True)
    termsConditions=models.CharField(max_length=50, null=True)
    bankdetails=models.CharField(max_length=50, null=True)

class Customer(models.Model):
    customerName = models.CharField(max_length=50, null=True)
    companyName = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    gstin = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    state=models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=50, null=True)
    gstRegType = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.companyName

class Item(models.Model):
    itemid=models.CharField(max_length=50, null=True)
    itemName = models.CharField(max_length=50, null=True)
    hsnCode = models.CharField(max_length=50, null=True)
    uom = models.CharField(max_length=50, null=True)
    isGoodOrService = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    ratePerUnit = models.CharField(max_length=50, null=True)

    totalGstPercent = models.CharField(max_length=50, null=True)
    sgstPercent = models.CharField(max_length=50, null=True)
    cgstPercent = models.CharField(max_length=50, null=True)
    igstPercent= models.CharField(max_length=50, null=True)

class Quot(models.Model):
    customerName = models.CharField(max_length=50, null=True)
    companyName = models.CharField(max_length=100)
    state = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=100)
    gstRegType = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    address =models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    itemName = models.CharField(max_length=100)
    hsnCode = models.CharField(max_length=100)
    ratePerUnit = models.CharField(max_length=100)
    quantity =models.CharField(max_length=100)
    totalGstPercent = models.CharField(max_length=100)
    sgstPercent =models.CharField(max_length=100)
    cgstPercent = models.CharField(max_length=100)
    igstPercent = models.CharField(max_length=100)
    quot_Number = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    uom = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description=models.CharField(max_length=100)

     # Ensure 'uom' is included here

    def __str__(self):
        return f"Quotation {self.quot_Number}"



