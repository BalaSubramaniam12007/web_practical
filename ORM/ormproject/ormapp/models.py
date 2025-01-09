from django.contrib import admin
from django.db import models

class Bankloan (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=100)
    loan_amt=models.IntegerField()
    cust_no=models.IntegerField()
    cust_name=models.CharField(max_length=100)
 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amt','cust_no','cust_name')