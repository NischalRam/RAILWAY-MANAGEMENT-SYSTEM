from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import booking, newuser


# Create your views here.


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                user1 = newuser.objects.create(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user1.save();
                print('user created')
                return redirect('/')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')    

  
def booking_data(request):

    if request.method == 'POST':
        customer = request.POST['customer']
        phone = request.POST['phone']
        age = request.POST['age']
        goingfrom = request.POST['goingfrom']
        to = request.POST['to']
        date = request.POST['date']

        print('all done')
        booking_info = booking.objects.create(customer=customer, phone=phone, age=age, goingfrom=goingfrom, to=to, date=date)
        booking_info.save();
        print('all done')
        
        return redirect('booking')
       
    else:
        return render(request,'booking.html') 
     
      