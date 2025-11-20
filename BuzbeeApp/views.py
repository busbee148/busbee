
from urllib import response
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views import View

from BuzbeeApp.serialisers import *
from BuzbeeApp.form import *
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
            request.session['login_id'] = user.id
            if user.UserType=='admin':
                return HttpResponse('''<script>alert('welcome back');window.location='/AdminHome'</script>''')
            elif user.UserType=='Owner':
                return HttpResponse('''<script>alert('welcome back');window.location='/OwnerHome'</script>''')

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
        return render(request,"owner/driverregister.html") 
    def post(self,request):
        form=Driver_Registerform(request.POST)
        print(form)
        if form.is_valid():
            f=form.save(commit=False)
            f.OWNER=OwnerTable.objects.get(LOGIN_id=request.session['login_id'])
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='DRIVER')
            f.save()
            return HttpResponse('''<script>alert('succcesfully registered');window.location='/ViewBusDriver';</script>''')

    
class ConducterHome(View):
    def get(self,request):
        return render(request,"conducter/conducterhome.html") 
    
      
class AddBusRoute(View):
    def get(self,request):
        return render(request,"administration/addbusroute.html")
    def post(self,request):
        c=Add_RouteForm(request.POST)
        if c.is_valid():
            c.save()
        return redirect('ViewBusRoutes')
    
class ViewBusRoutes(View):
    def get(self,request):
        obj=BusRouteTable.objects.all()
        return render(request,"administration/viewbusroute.html", {'val':obj})

class DeleteBusRoute(View):
    def get(self,request, rid):
        obj = BusRouteTable.objects.get(id=rid)
        obj.delete()
        return redirect('ViewBusRoutes')
    
class DeleteBusStop(View):
    def get(self,request, sid):
        obj = BusStopTable.objects.get(id=sid)
        obj.delete()
        return redirect('ViewBusStop')
    
class ViewBusStop(View):
    def get(self,request):
        obj=BusStopTable.objects.all()
        obj1 = BusRouteTable.objects.all()
        return render(request,"administration/viewbusstop.html", {'val':obj,'val1':obj1})   
       
class SearchStop(View):
    def post(self,request):
        route = request.POST['route_id']
        if route == "0":
            obj=BusStopTable.objects.all()
        else:    
            obj=BusStopTable.objects.filter(BUSROUTE_id=route)
        obj1 = BusRouteTable.objects.all()
        return render(request,"administration/viewbusstop.html", {'val':obj,'val1':obj1})   
       


class AddBusStop(View):
    def get(self,request):
        obj = BusRouteTable.objects.all()
        return render(request,"administration/addbusstop.html",{'val':obj})
    def post(self,request):
        s=Add_Busstop(request.POST, request.FILES)
        if s.is_valid():
            s.save()
        return redirect('ViewBusStop')  


class ApproveBusDetails(View):
    def get(self,request):
        obj=BusTable.objects.all()
        return render(request,"administration/approvebusdetails.html",{'val':obj}) 
    
class ApproveBusDetail(View):
    def get(self,request,lid):
        obj = BusTable.objects.get(id=lid)
        obj.Status="active"
        obj.save()
        return redirect('ApproveBusDetails')
    
class RejectBusDetail(View):
    def get(self,request,lid):
        obj = BusTable.objects.get(id=lid)
        obj.Status="rejected"
        obj.save()
        return redirect('ApproveBusDetails')


class DeleteBusDriver(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('ViewBusDriver')
    
    
class EditBusDriver(View):
    def get(self,request, dr_id):
        obj = DriverTable.objects.get(id=dr_id)
        return render(request,"administration/editbusdriver.html",{'val': obj}) 
    def post(self,request, dr_id):
        obj = DriverTable.objects.get(id=dr_id)
        form=Driver_Updateform(request.POST, instance=obj)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert('Edited Succcesfully');window.location='/ViewBusDriver';</script>''')
    
    
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
    
class ApproveVVBR(View):
    def get(self,request,lid):
        obj = AssignBusRouteTable.objects.get(id=lid)
        obj.Status="accepted"
        obj.save()
        return redirect('VVBR')
    
class RejectVVBR(View):
    def get(self,request,lid):
        obj = AssignBusRouteTable.objects.get(id=lid)
        obj.Status="rejected"
        obj.save()
        return redirect('VVBR')
        
class ViewComplaint(View):
    def get(self,request):
        obj=ComplaintTable.objects.all()
        return render(request,"administration/viewcomplaint.html",{'val': obj}) 

class ComplaintReply(View):
    def post(self,request, c_id):
        reply=request.POST['reply']
        obj=ComplaintTable.objects.get(id=c_id)
        obj.Reply = reply
        obj.save()
        return redirect('ViewComplaint')

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
    def get(self, request, bus_id):
        obj = get_object_or_404(BusTable, id=bus_id)
        obj.Status = "blocked"
        obj.save()
        return redirect('BlockBus')
    
class UnblockBus(View):
    def get(self,request,bus_id):
        obj = get_object_or_404(BusTable, id=bus_id)
        obj.Status = "active"
        obj.save()
        return redirect('BlockBus')
    

    
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
        obj=BusTable.objects.all()
        return render(request,"owner/addbus.html",{'val':obj})
    def post(self,request):
        b=BusForm(request.POST, request.FILES)
        print("---------->", request.POST)
        if b.is_valid():
            f= b.save()
            f.OWNER = OwnerTable.objects.get(LOGIN_id=request.session['login_id'])
            f.save()
            return redirect('ViewBus')

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
        obj=BusTable.objects.all()
        return render(request,"owner/viewbus.html",{'val':obj}) 
    
class DeleteBus(View):
    def get(self,request, bid):
        obj = BusTable.objects.get(id=bid)
        obj.delete()
        return redirect('ViewBus')
    
class ViewBusDriver(View):
    def get(self,request):
        obj=DriverTable.objects.all()
        return render(request,"owner/viewbusdriver.html",{'val':obj}) 
    
class ViewBusRoute(View):
    def get(self,request):
        obj=BusRouteTable.objects.all()
        return render(request,"owner/viewbusroute.html",{'val':obj}) 
    
class ViewConducter(View):
    def get(self,request):
        obj=CondoctorTable.objects.all()
        return render(request,"owner/viewconducter.html",{'val':obj})
     
class AddConducter(View):
    def get(self,request):
        obj=CondoctorTable.objects.all()
        return render(request,"owner/addconducter.html",{'val':obj}) 
    def post(self,request):
        form=Add_ConducterForm(request.POST)
        print(form)
        if form.is_valid():
            f=form.save(commit=False)
            f.OWNER=OwnerTable.objects.get(LOGIN_id=request.session['login_id'])
            f.LOGIN=LoginTable.objects.create(Username=request.POST['Username'],Password=request.POST['Password'],UserType='DRIVER')
            f.save()
            return HttpResponse('''<script>alert('succcesfully registered');window.location='/ViewConducter';</script>''')
    
class DeleteConducter(View):
    def get(self,request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('ViewConducter')
    
class EditConducter(View):
    def get(self,request, dr_id):
        obj = CondoctorTable.objects.get(id=dr_id)
        return render(request,"owner/editconducter.html",{'val': obj}) 
    def post(self,request, dr_id):
        obj = CondoctorTable.objects.get(id=dr_id)
        form=Add_ConducterForm(request.POST, instance=obj)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert('Edited Succcesfully');window.location='/ViewConducter';</script>''')
        
class ViewAssignedBus(View):
    def get(self,request):
        obj=AssignTable.objects.filter(BUS__OWNER__LOGIN_id=request.session['login_id'])
        return render(request,"owner/viewassignedbus.html",{'val':obj})    
    
# class AssignBus(View):
#     def get(self,request):
#         assign_obj =  AssignTable.objects.filter(BUS__OWNER__LOGIN_id=request.session['login_id']) 
#         if assign_obj:
#             print("-----------iff---", assign_obj)
#             for i in assign_obj:
#                 print("bud_id------------", i.BUS.id)
#                 obj1=BusTable.objects.exclude(id=i.BUS.id).filter(OWNER__LOGIN_id=request.session['login_id'])
#                 print("-------obj1-------->", obj1)
#                 obj2=DriverTable.objects.exclude(id=i.DRIVER.id).filter(OWNER__LOGIN_id=request.session['login_id'])
#                 obj3=CondoctorTable.objects.exclude(id=i.Conducter.id).filter(OWNER__LOGIN_id=request.session['login_id'])
#         else:
#                 print("------else----")
#                 obj1=BusTable.objects.filter(OWNER__LOGIN_id=request.session['login_id'])
#                 obj2=DriverTable.objects.filter(OWNER__LOGIN_id=request.session['login_id'])
#                 obj3=CondoctorTable.objects.filter(OWNER__LOGIN_id=request.session['login_id'])

#         return render(request,"owner/assignbus.html",{'val1':obj1,'val2':obj2,'val3':obj3})

class AssignBus(View):
    def get(self, request):
        login_id = request.session.get('login_id')
        
        # Get all assigned objects for this owner
        assigned_objs = AssignTable.objects.filter(BUS__OWNER__LOGIN_id=login_id)

        if assigned_objs.exists():
            print("-----------Assigned Objects---", assigned_objs)

            # Collect assigned IDs
            assigned_bus_ids = assigned_objs.values_list('BUS__id', flat=True)
            assigned_driver_ids = assigned_objs.values_list('DRIVER__id', flat=True)
            assigned_conductor_ids = assigned_objs.values_list('Conducter__id', flat=True)

            # Exclude assigned ones
            obj1 = BusTable.objects.filter(OWNER__LOGIN_id=login_id).exclude(id__in=assigned_bus_ids)
            obj2 = DriverTable.objects.filter(OWNER__LOGIN_id=login_id).exclude(id__in=assigned_driver_ids)
            obj3 = CondoctorTable.objects.filter(OWNER__LOGIN_id=login_id).exclude(id__in=assigned_conductor_ids)

        else:
            print("------No Assignments Found----")
            # If nothing is assigned yet, show all
            obj1 = BusTable.objects.filter(OWNER__LOGIN_id=login_id)
            obj2 = DriverTable.objects.filter(OWNER__LOGIN_id=login_id)
            obj3 = CondoctorTable.objects.filter(OWNER__LOGIN_id=login_id)

        return render(request, "owner/assignbus.html", {
            'val1': obj1,
            'val2': obj2,
            'val3': obj3
        })
    def post(self,request):
        s=Assign_BusForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('ViewAssignedBus') 

class DeleteAssignedBus(View):
    def get(self,request, lid):
        obj = AssignTable.objects.get(id=lid)
        obj.delete()
        return redirect('ViewAssignedBus') 

class LogoutView(View):
    def get(self, request):
        return HttpResponse('''<script>alert('Logout successfully');window.location='/'</script>''')
    
 #////////////////////////////      Passenger    ///////////////////////////////////////////
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class PassangerView(APIView):
    def post(self, request):
        print("##################### Incoming Data #####################")
        print(request.data)

        # Normalize gender input
        gender_map = {'Male': 'M', 'Female': 'F', 'Other': 'O'}
        data = request.data.copy()
        gender_value = data.get('Gender')
        if gender_value in gender_map:
            data['Gender'] = gender_map[gender_value]

        # Create serializers with cleaned data
        passenger_serializer = PassangerSerializer(data=data)
        login_serializer = LoginSerializer(data=data)

        if passenger_serializer.is_valid() and login_serializer.is_valid():
            login_profile = login_serializer.save(UserType='Passanger')
            passenger_serializer.save(LOGIN=login_profile)
            return Response(
                {
                    "message": "Passenger registered successfully",
                    "data": passenger_serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        print("Passenger Errors:", passenger_serializer.errors)
        print("Login Errors:", login_serializer.errors)
        return Response(
            {
                "LoginErrors": login_serializer.errors,
                "PassengerErrors": passenger_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginPageAPI(APIView):
    def post(self,request):
        print("##############")
        response_dict={}

        # get data from the request
        Username= request.data.get("Username")
        Password = request.data.get("Password")
        print("$$$$$$$$$$$$$$$$$",Username)
        #Validate input
        if not Username or not Password:
            response_dict["Message"]="failed"
            return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
        
        #fetch the user from login table
        T_user=LoginTable.objects.filter(Username=Username,Password=Password).first()
        print("%%%%%%%%%%%%%%%%%%%%",T_user)

        if not T_user:
            response_dict["Message"]="failed"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        else:
            response_dict["Message"]="Success"
            response_dict["Login_id"]=T_user.id
            response_dict["UserType"]=T_user.UserType

            return Response(response_dict,status=status.HTTP_200_OK)
        
class ComplaintAPI(APIView):
    def get(self,request,id):
        c= ComplaintTable.objects.filter(USER__LOGIN__id=id)
        serial=ComplaintSerializer(c,many=True)
        return Response(serial.data, status=status.HTTP_200_OK)


    def post(self,request,id):
        user=PassangerTable.objects.get(LOGIN__id=id)
        complaint=ComplaintSerializer(data=request.data)
        if complaint.is_valid():
            complaint.save(USER=user)
            return Response(complaint.data, status=status.HTTP_200_OK)
        
class FeedbackAPI(APIView):
    def post(self,request,id):
        print(request.data)
        user=PassangerTable.objects.get(LOGIN__id=id)
        feedback=FeedbackSerializer(data=request.data)
        if feedback.is_valid():
            feedback.save(USER=user)
            return Response(feedback.data, status=status.HTTP_200_OK)

class ViewbusAPI(APIView):
    def get(self,request):
        bus=BusTable.objects.all()
        serializer=BusSerializer(bus,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ViewbusStopAPI(APIView):
    def get(self,request):
        busstop=BusStopTable.objects.all()
        serializer=BusStopSerializer(busstop,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ViewbusRouteAPI(APIView):
    def get(self,request):
        busroute=BusRouteTable.objects.all()
        serializer=BusRouteSerializer(busroute,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ViewPassengerAPI(APIView):
    def get(self,request,id):
        passenger=PassangerTable.objects.get(LOGIN__id = id)
        serializer=PassangerSerializer(passenger,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
