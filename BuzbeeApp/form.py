from django.forms import ModelForm
from BuzbeeApp.models import DriverTable, OwnerTable


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


