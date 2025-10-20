from rest_framework.serializers import ModelSerializer

from BuzbeeApp.models import *


class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password', 'UserType']


class PassangerSerializer(ModelSerializer):
    class Meta:
        model = PassangerTable
        fields = ['Name', 'Email', 'Age', 'Contact_NO', 'Gender', 'Address']

class BusSerializer(ModelSerializer):
    class Meta:
        model = BusTable
        fields = ['Busname','Bus_NO','Capacity','RC_NO','Photo','Status']

class BusRouteSerializer(ModelSerializer):
    class Meta:
        model = BusRouteTable
        fields = ['Source','Destination']

class BusStopSerializer(ModelSerializer):
    class Meta:
        model = BusStopTable
        fields =['Stop_name','Landmark','Photo']

class Assign_BusSerializer(ModelSerializer):
    class Meta:
        model = AssignTable
        fields = ['BUS','DRIVER','Conducter']

class AssignRouteSerializer(ModelSerializer):
    class Meta:
        model = AssignTable
        fields = ['BUS','ROUTE','Date','Start_Time','End_Time','Status']

class TimeSerializer(ModelSerializer):
    class Meta:
        model= TimeTable
        fields = ['ASSIGNBUSROUTE','BUSSTOP','Time','Status']

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = ['USER','BUS','Feedback','Date']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['USER','BUS','Complaint','Reply','Date']
        
class TicketSerializer(ModelSerializer):
    class Meta:
        model = TicketTable
        fields =  ['PASSANGER','STOP','Date','Status','Ticket_No','Paid_amount','Count']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['Name','BUSSTOP','Payment_Amount','Date','BUS']

class WalletSerializer(ModelSerializer):
    class meta:
        model = WalletTable
        fields = ['LOGIN','Balance','DateTime','Amount','Debit']