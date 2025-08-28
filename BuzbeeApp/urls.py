"""
URL configuration for Buzbee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from BuzbeeApp.views import *
urlpatterns = [
    path('', LoginPage.as_view(), name="LoginPage"),

    # ///////////////////////////////////// ADMIN //////////////////////////////////////////
    path('AdminHome',AdminHome.as_view(),name="AdminHome"),
    path('OwnerHome',OwnerHome.as_view(),name="OwnerHome"),
    path('OwnerRegistration',OwnerRegistration.as_view(),name="OwnerRegistration"),
    path('DriverRegister',DriverRegister.as_view(),name="DriverRegister"),
    path('DriverHome',DriverHome.as_view(),name="DriverHome"),
    path('ConducterHome',ConducterHome.as_view(),name="ConducterHome"),
    path('AddBusDriver',AddBusDriver.as_view(), name="AddBusDriver"),
    path('AddBusRoute',AddBusRoute.as_view(), name="AddBusRoute"),
    path('AddBusStop',AddBusStop.as_view(), name="AddBusStop"),
    path('ApproveBusDetails',ApproveBusDetails.as_view(), name="ApproveBusDetails"),
    path('BlockBus',BlockBus.as_view(),name="BlockBus"),
    path('BlockBuss/<int:lid>',BlockBuss.as_view(),name='BlockBuss'),
    path('UnblockBus/<int:lid>',UnblockBus.as_view(),name='UnblockBus'),
    path('EditBusDriver',EditBusDriver.as_view(),name="EditBusDriver"),
    path('FeedBack',FeedBack.as_view(),name="FeedBack"),
    path('ManageOwner',ManageOwner.as_view(),name="ManageOwner"),
    path('ManageOwner1',ManageOwner1.as_view(),name="ManageOwner1"),
    path('VVBR',VVBR.as_view(),name="VVBR"),
    path('ViewBusDriver',ViewBusDriver.as_view(),name="ViewBusDriver"),
    path('ViewComplaint',ViewComplaint.as_view(),name="ViewComplaint"),
    path('ViewOwner',ViewOwner.as_view(),name="ViewOwner"),
    path('ApproveOwner/<int:lid>',ApproveOwner.as_view(),name="ApproveOwner"),
    path('RejectOwner/<int:lid>',RejectOwner.as_view(),name="RejectOwner"),
    
    # //////////////////////////////////  BUSDRIVER ///////////////////////////////////////////////

    path('TripStatus',TripStatus.as_view(),name="TripStatus"),

    # ///////////////////////////////////////////  CONDUCTER ///////////////////////////////////////
    path('VerifyTicket',VerifyTicket.as_view(),name="VerifyTicket"),
    
    #//////////////////////////////////////////  OWNER  ////////////////////////////////////////// 
    path('AddBus',AddBus.as_view(),name="AddBus"),
    # path('Register',Register.as_view(),name="Register"),
    path('TrackBus',TrackBus.as_view(),name="TrackBus"),
    path('ViewBus',ViewBus.as_view(),name="ViewBus"),
    path('ViewBusDrivers',ViewBusDrivers.as_view(),name="ViewBusDrivers"),
    path('ViewBusRoute',ViewBusRoute.as_view(),name="ViewBusRoute"),
    path('ViewConducter',ViewConducter.as_view(),name="ViewConducter"),
    ]
