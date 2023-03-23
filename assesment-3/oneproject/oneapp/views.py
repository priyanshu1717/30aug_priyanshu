from django.shortcuts import render,redirect
from .forms import signupform
from .models import signup

# Create your views here.
def index(request):
    
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")
                return redirect('dashboard')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']
    
            userid=signup.objects.get(username=unm)

            user=signup.objects.filter(username=unm,password=pas)
            if user:
                    print("Login Successfull!")
                    request.session['username'] = unm
                    return redirect('dashboard')

        else:
            print(user.errors)       
    return render(request,'index.html')

def profile(request):
    return render (request,'profile.html')
def updateprofile(request):
    
    return render(request,'updateprofile.html')
def dashboard(request):
    return render(request,'dashboard.html')