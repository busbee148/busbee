
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views import View

from BuzbeeApp.form import Owner_Registerform
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
    

class DriverRegister(View):
    def get(self,request):
        return render(request,"busdriver/driverregistration.html")
    def post(self,request):
        form=DriverRegister(request.POST)
        print(form)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='DRIVER')
            f.save()
            return HttpResponse('''<script>alert('succcesfully registered');window.location='/';</script>''')

    
class ConducterHome(View):
    def get(self,request):
        return render(request,"conducter/conducterhome.html") 
    
      
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
    
class ApproveOwner(View):
    def get(self,request,lid):
        obj = OwnerTable.objects.get(id=lid)
        obj.LOGIN.UserType="Owner"
        obj.LOGIN.save()
        return redirect('ViewOwner')
    
class RejectOwner(View):
    def get(self,request,lid):
        obj = OwnerTable.objects.get(id=lid)
        obj.LOGIN.UserType="rejected"
        obj.LOGIN.save()
        return redirect('ViewOwner')
class BlockBus(View):
    def get(self,request):
        obj=BusTable.objects.all()
        return render(request,"administration/blockbus.html",{'val':obj})     
    
class BlockBuss(View):
    def get(self, request, lid):
        login = get_object_or_404(LoginTable, id=lid)
        login.UserType = "blocked"
        login.save()
        return redirect('BlockBus')
    
class UnblockBus(View):
    def get(self,request,lid):
        login = get_object_or_404(LoginTable, id=lid)
        login.UserType = "bus"
        login.save()
        return redirect('BlockBus')
    

    
# ///////////////////////////////////////////////// BUSDRIVER    ///////////////////////////////////
#   

class AddBusDriver(View):
    def get(self,request):
        return render(request,"administration/addbusdriver.html") 
      
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
        form=(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=request.POST['email'],password=request.POST['password'],usertype='owner')
            f.save()
        return render(request,"owner/addbus.html")

class OwnerRegistration(View):
    def get(self,request):
        return render(request,"owner/register.html")
    def post(self,request):
        form=Owner_Registerform(request.POST)
        print(form)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='pending')
            f.save()
            return HttpResponse('''<script>alert('succcesfully registered');window.location='/';</script>''')

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