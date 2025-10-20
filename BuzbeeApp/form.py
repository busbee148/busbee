from django.forms import ModelForm
from BuzbeeApp.models import *


class Owner_Registerform(ModelForm):
    class Meta:
        model = OwnerTable
        fields = ['Name','Age','Gender','Contact_NO','Email','Address']

class Driver_Registerform(ModelForm):
    class Meta:
        model = DriverTable
        fields = ['Driver_Name','Licence_NO','Age','Gender','Contact_NO','Address']

class Driver_Updateform(ModelForm):
    class Meta:
        model = DriverTable
        fields = ['Driver_Name','Licence_NO','Age','Gender','Contact_NO','Address']

class Add_RouteForm(ModelForm):
    class Meta:
        model = BusRouteTable
        fields = ['Source','Destination']

class Add_Busstop(ModelForm):
    class Meta:
        model = BusStopTable
        fields =['Stop_name','Landmark','Photo']

class BusForm(ModelForm):
    class Meta:
        model = BusTable
        fields = ['Busname','Bus_NO','Capacity','RC_NO','Photo','Status']

class Add_ConducterForm(ModelForm):
    class Meta:
        model = CondoctorTable
        fields = ['Name','Age','Contact_NO','Gender','Address']

class Assign_BusForm(ModelForm):
    class Meta:
        model = AssignTable
        fields = ['BUS','DRIVER','Conducter']   