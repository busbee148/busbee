from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=30, blank=True, null=True)
    Password = models.CharField(max_length=30,blank=True,null=True)
    UserType = models.CharField(max_length=30, blank=True, null=True)

class PassangerTable(models.Model):
    Name = models.CharField(max_length=30, blank=True, null=True)
    Email = models.CharField(max_length=30,blank=True,null=True)
    Age = models.IntegerField(blank=True,null=True)
    Contact_NO = models.BigIntegerField(blank=True,null=True)
    Gender = models.CharField(max_length=2,blank=True,null=True)
    Address = models.CharField(max_length=50, blank=True, null=True)
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)

class DriverTable(models.Model):
    Driver_Name = models.CharField(max_length=30, blank=True, null=True)
    Address = models.CharField(max_length=30, blank=True, null=True)
    Licence_NO = models.CharField(max_length=16,blank=True,null=True)
    Age = models.IntegerField(blank=True,null=True)
    Contact_NO = models.BigIntegerField(blank=True,null=True)
    Gender = models.CharField(max_length=2,blank=True,null=True)
    Status = models.CharField(max_length=8,blank=True,null=True)
    Latitude =models.FloatField(blank=True,null=True)
    Longitude =models.FloatField(blank=True,null=True)
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)

class OwnerTable(models.Model):
    Name = models.CharField(max_length=30,blank=True,null=True)
    Age = models.IntegerField(blank=True,null=True)
    Contact_NO = models.BigIntegerField(blank=True,null=True)
    Address = models.CharField(max_length=30, blank=True, null=True)
    Gender = models.CharField(max_length=2,blank=True,null=True)
    Email = models.CharField(max_length=30,blank=True,null=True)
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)

class CondotorTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30,blank=True,null=True)
    Age = models.IntegerField(blank=True,null=True)
    Contact_NO = models.BigIntegerField(blank=True,null=True)
    Gender = models.CharField(max_length=2,blank=True,null=True)
    Address = models.CharField(max_length=50,blank=True,null=True)

class BusTable(models.Model):
     Busname = models.CharField(max_length=30,blank=True,null=True)
     Bus_NO = models.CharField(max_length=12,blank=True,null=True)
     Capacity = models.IntegerField(blank=True,null=True)
     RC_NO = models.CharField(max_length=15,blank=True,null=True)
     Photo = models.FileField(blank=True,null=True)

class BusRouteTable(models.Model):
    Route_ID = models.CharField(max_length=10,blank=True,null=True)
    Source = models.CharField(max_length=30,blank=True,null=True)
    Destination = models.CharField(max_length=30,blank=True,null=True)

class BusStopTable(models.Model):
    Stop_name = models.CharField(max_length=30,blank=True,null=True)
    Landmark = models.CharField(max_length=30,blank=True,null=True)
    Photo = models.FileField(blank=True,null=True)
    BUSROUTE = models.ForeignKey(BusRouteTable, on_delete=models.CASCADE)

class AssignBusRouteTable(models.Model):
    BUS = models.ForeignKey(BusTable, on_delete=models.CASCADE)
    ROUTE = models.ForeignKey(BusRouteTable, on_delete=models.CASCADE)
    DRIVER = models.ForeignKey(DriverTable, on_delete=models.CASCADE)
    CONDOCTOR = models.ForeignKey(CondotorTable, on_delete=models.CASCADE)
    Date = models.DateField()

class FeedbackTable(models.Model):
    USER = models.ForeignKey(PassangerTable, on_delete=models.CASCADE)
    BUS = models.ForeignKey(BusTable, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=100,blank=True,null=True)
    Date = models.DateField()

class ComplaintTable(models.Model):
    USER = models.ForeignKey(PassangerTable, on_delete=models.CASCADE)
    BUS = models.ForeignKey(BusTable, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=100,blank=True,null=True)
    Reply = models.CharField(max_length=100,blank=True,null=True)
    Date = models.DateField()

class TripStatustable(models.Model):
    ASSIGN = models.ForeignKey(AssignBusRouteTable, on_delete=models.CASCADE)
    Date= models.DateTimeField()
    Status = models.CharField(max_length=12,blank=True,null=True)

class TicketTable(models.Model):
    PASSANGER = models.ForeignKey(PassangerTable, on_delete=models.CASCADE)
    STOP = models.ForeignKey(BusStopTable, on_delete=models.CASCADE)
    Date= models.DateTimeField()
    Status = models.CharField(max_length=12,blank=True,null=True)
    Ticket_No = models.IntegerField(blank=True,null=True)
    Paid_amount =models.FloatField()
    Count = models.IntegerField(blank=True,null=True)

class BookingTable(models.Model):
    Name = models.CharField(max_length=30,blank=True,null=True)
    BUSSTOP = models.ForeignKey(BusStopTable, on_delete=models.CASCADE)
    Payment_Amount = models.FloatField()
    Date = models.DateTimeField()
    BUS = models.ForeignKey(BusTable, on_delete=models.CASCADE)
    
class WalletTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Balance = models.FloatField()
    DateTime = models.DateTimeField()
    Amount = models.FloatField()
    Debit = models.FloatField()

 