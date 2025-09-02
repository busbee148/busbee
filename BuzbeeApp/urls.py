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
    path('ConducterHome',ConducterHome.as_view(),name="ConducterHome"),
    path('AddBusRoute',AddBusRoute.as_view(), name="AddBusRoute"),
    path('ViewBusRoutes',ViewBusRoutes.as_view(), name="ViewBusRoutes"),
    path('AddBusStop',AddBusStop.as_view(), name="AddBusStop"),
    path('ViewBusStop',ViewBusStop.as_view(),name="ViewBusStop"),
    path('SearchStop',SearchStop.as_view(),name="SearchStop"),
    path('DeleteBusStop/<int:sid>',DeleteBusStop.as_view(),name="DeleteBusStop"),
    path('DeleteBusRoute/<int:rid>',DeleteBusRoute.as_view(),name="DeleteBusRoute"),
    path('ApproveBusDetails',ApproveBusDetails.as_view(), name="ApproveBusDetails"),
    path('ApproveBusDetail/<int:lid>',ApproveBusDetail.as_view(),name="ApproveBusDetail"),
    path('RejectBusDetail/<int:lid>',RejectBusDetail.as_view(),name="RejectBusDetail"),
    path('BlockBus',BlockBus.as_view(),name="BlockBus"),
    path('BlockBuss/<int:bus_id>',BlockBuss.as_view(),name='BlockBuss'),
    path('UnblockBus/<int:bus_id>',UnblockBus.as_view(),name='UnblockBus'),
    path('FeedBack',FeedBack.as_view(),name="FeedBack"),
    path('OwnerRegistration',OwnerRegistration.as_view(),name="OwnerRegistration"),
    path('ManageOwner',ManageOwner.as_view(),name="ManageOwner"),
    path('ManageOwner1',ManageOwner1.as_view(),name="ManageOwner1"),
    path('VVBR',VVBR.as_view(),name="VVBR"),
    path('ApproveVVBR/<int:lid>',ApproveVVBR.as_view(),name="ApproveVVBR"),
    path('RejectVVBR/<int:lid>',RejectVVBR.as_view(),name="RejectVVBR"),
    path('ViewComplaint',ViewComplaint.as_view(),name="ViewComplaint"),
    path('ComplaintReply/<int:c_id>',ComplaintReply.as_view(),name="ComplaintReply"),
    path('ViewOwner',ViewOwner.as_view(),name="ViewOwner"),
    path('ApproveOwner/<int:lid>',ApproveOwner.as_view(),name="ApproveOwner"),
    path('RejectOwner/<int:lid>',RejectOwner.as_view(),name="RejectOwner"),
    
    # //////////////////////////////////  BUSDRIVER ///////////////////////////////////////////////

    path('DriverHome',DriverHome.as_view(),name="DriverHome"),
    path('TripStatus',TripStatus.as_view(),name="TripStatus"),

    # ///////////////////////////////////////////  CONDUCTER ///////////////////////////////////////
    path('VerifyTicket',VerifyTicket.as_view(),name="VerifyTicket"),
    
    #//////////////////////////////////////////  OWNER  ////////////////////////////////////////// 
    path('AddBus',AddBus.as_view(),name="AddBus"),
    path('ViewBusDriver',ViewBusDriver.as_view(),name="ViewBusDriver"),
    path('DriverRegister',DriverRegister.as_view(),name="DriverRegister"),
    path('EditBusDriver/<int:dr_id>',EditBusDriver.as_view(),name="EditBusDriver"),
    path('DeleteBusDriver/<int:lid>',DeleteBusDriver.as_view(),name="DeleteBusDriver"),
    path('TrackBus',TrackBus.as_view(),name="TrackBus"),
    path('ViewBus',ViewBus.as_view(),name="ViewBus"),
    path('DeleteBus/<int:bid>',DeleteBus.as_view(),name="DeleteBus"),
    path('ViewBusRoute',ViewBusRoute.as_view(),name="ViewBusRoute"),
    path('ViewConducter',ViewConducter.as_view(),name="ViewConducter"),
    path('AddConducter',AddConducter.as_view(),name="AddConducter"),
    path('DeleteConducter/<int:lid>',DeleteConducter.as_view(),name="DeleteConducter"),
    path('EditConducter/<int:dr_id>',EditConducter.as_view(),name="EditConducter"),
    ]
