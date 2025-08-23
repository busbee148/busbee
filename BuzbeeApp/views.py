
from django.shortcuts import render, HttpResponse
from django.views import View

from BuzbeeApp.models import *

# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "administration/login.html")
    def post(self,request):
        Username = request.POST['Username']
        Password = request.POST['Password'] 
        try:
            user=LoginTable.objects.get(Username=Username,Password=Password)
            request.session['login id'] = user.id
            if user.UserType=='admin':
                return HttpResponse('''<script>alert('welcome back');window.location='/AdminHome'</script>''')
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
        obj=BusTable.objects.all()
        return render(request,"administration/approvebusdetails.html",{'val':obj}) 

class BlockBus(View):
    def get(self,request):
        obj=BusTable.objects.all()
        return render(request,"administration/blockbus.html",{'val':obj}) 

class EditBusDriver(View):
    def get(self,request):
        return render(request,"administration/editbusdriver.html") 
    
class FeedBack(View):
    def get(self,request):
        obj=FeedbackTable.objects.all()
        return render(request,"administration/feedback.html",{'val':obj}) 
    
class ManageOwner(View):
    def get(self,request):
        return render(request,"administration/manageowner.html") 
    
class ManageOwner1(View):
    def get(self,request):
        return render(request,"administration/manageowner1.html") 
    
class VVBR(View):
    def get(self,request):
        obj=AssignBusRouteTable.objects.all()
        return render(request,"administration/view&verifybusroute.html",{'val':obj})   
    
class ViewBusDriver(View):
    def get(self,request):
        obj=DriverTable.objects.all()
        return render(request,"administration/viewbusdriver.html",{'val':obj}) 
    
class ViewComplaint(View):
    def get(self,request):
        obj=ComplaintTable.objects.all()
        return render(request,"administration/viewcomplaint.html",{'val': obj}) 
    
class ViewOwner(View):
    def get(self,request):
        obj = OwnerTable.objects.all()
        return render(request,"administration/viewowner.html", {'val': obj}) 
    
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
    

class LogoutView(View):
    def get(self, request):
        return HttpResponse('''<script>alert('Logout successfully');window.location='/'</script>''')