from operator import ge
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def subs(request):
    return render(request,'subs.html')

def service(request):
    return render(request,'service.html')

def appointment(request):
    user = request.user
    # print(user.is_superuser)
    if(user.is_superuser):
        obj = Booking.objects.all()
        return render(request,'Appointment.html',{'obj':obj})    
    obj = Booking.objects.filter(user=request.user)
    return render(request,'Appointment.html',{'obj':obj})

def about(request):
    return render(request,'depression.html')

@login_required(login_url='index')
def booking(request):
    if request.method== 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        num = request.POST['user_num']
        appointment = request.POST['appointment']
        dis = request.POST['appointment_description']
        date = request.POST['date']
        time = request.POST['time']
        duration = request.POST['duration']
        gender = request.POST['gender']
        user = request.user
        new_data = Booking(name=name,email=email,num=num,appointment=appointment,dis=dis,date=date,time=time,duration=duration,gender=gender,user=user)
        new_data.save()
        return redirect(index)
    return render(request,'booking.html')

def sin_up(request):
    if request.method=="POST":
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        option = request.POST['appointment']
        men = False
        if(option=="Mentee"):
            men = True
        try:
            user = User.objects.get(username = name)
            return render(request,'login.html',{'error':'User Already exits'})
        except User.DoesNotExist:
            user = User.objects.create_user(username= name,password= password,email=email,is_superuser=men)
            # auth.login(request,user)

        return render(request,'index.html')
    else:
        return render(request,'login.html')


def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user  = auth.authenticate(username=uname,password=pwd)
                        
        if user is not None:
            auth.login(request,user)
            return redirect(index)
        else:
            return render(request,'login.html',{'error':"Invalid Username or Password "})

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect(index)
