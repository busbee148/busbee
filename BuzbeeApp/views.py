from django.shortcuts import render
from django.views import View

from BuzbeeApp.models import *

# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "administration/login.html")
    def post(self,request):
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            user=LoginTable.objects.get(Username=username,Password=password)
            request.session['login id'] = user.id
            if user.UserType=='administration':
                return render(request,'administration/AdminHome.html')
            elif user.UserType=='owner':
                return render(request,'owner/OwnerHome')
            elif user.UserType=='busdriver':
                return render(request,'busdriver/DriverHome')
            elif user.UserType=='conducter':
                return render(request,'conducter/ConducterHome')
        except LoginTable.DoesNotExist:
            return render (request,'"Administration/Login.html',{'error':'Invalid username or password'})
    
# /////////////////////////////////////// administration /////////////////////////////////

        
class AdminHome(View):
    def get(self,request):
        return render(request,"administration/adminhome.html") 
       

class OwnerHome(View):
    def get(self,request):
        return render(request,"owner/ownerhome.html") 
    
class DriverHome(View):
    def get(self,request):
        return render(request,"busdriver/driverhome.html") 
    
class ConducterHome(View):
    def get(self,request):
        return render(request,"conducter/conducterhome.html") 
class AddBusDriver(View):
    def get(self,request):
        return render(request,"administration/addbusdriver.html") 
      
class AddBusRoute(View):
    def get(self,request):
        return render(request,"administration/addbusroute.html")
      
class AddBusStop(View):
    def get(self,request):
        return render(request,"administration/addbusstop.html")  
    
class ApproveBusDetails(View):
    def get(self,request):
        return render(request,"administration/approvebusdetails.html") 

class BlockBus(View):
    def get(self,request):
        return render(request,"administration/blockbus.html") 

class EditBus(View):
    def get(self,request):
        return render(request,"administration/editbus.html") 
    
class FeedBack(View):
    def get(self,request):
        return render(request,"administration/feedback.html") 
    
class ManageOwner(View):
    def get(self,request):
        return render(request,"administration/manageowner.html") 
    
class ManageOwner1(View):
    def get(self,request):
        return render(request,"administration/manageowner1.html") 
    
class VVBR(View):
    def get(self,request):
        return render(request,"administration/view&verifybusroute.html")   
    
class ViewBusDriver(View):
    def get(self,request):
        return render(request,"administration/viewbusdriver.html") 
    
class ViewComplaint(View):
    def get(self,request):
        return render(request,"administration/viewcomplaint.html") 
    
class ViewOwner(View):
    def get(self,request):
        return render(request,"administration/viewowner.html") 
# ///////////////////////////////////////////////// BUSDRIVER    ///////////////////////////////////
#     
class TripStatus(View):
    def get(self,request):
        return render(request,"busdriver/tripstatus.html")
     
#///////////////////// CONDUCTER ////////////////////////////// 
    
class VerifyTicket(View):
    def get(self,request):
        return render(request,"conducter/verify ticket.html") 

#////////////////////////// OWNER  ////////////////////////////////////    
    
class AddBus(View):
    def get(self,request):
        return render(request,"owner/addbus.html")

class Register(View):
    def get(self,request):
        return render(request,"owner/register.html")
      
class TrackBus(View):
    def get(self,request):
        return render(request,"owner/trackbus.html") 
    
class ViewBus(View):
    def get(self,request):
        return render(request,"owner/viewbus.html") 
    
class ViewBusDrivers(View):
    def get(self,request):
        return render(request,"owner/viewbusdrivers.html") 
    
class ViewBusRoute(View):
    def get(self,request):
        return render(request,"owner/viewbusroute.html") 
    
class ViewConducter(View):
    def get(self,request):
        return render(request,"owner/viewconducter.html") 