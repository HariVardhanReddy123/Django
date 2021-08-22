from os import name
from django.http.request import host_validation_re
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from home.models import feeedback
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):

    try :
        if request.method == 'POST':
            username=request.POST.get("name")
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                return redirect('/desc')
            else:

                messages.success(request, 'Incorrect Username And Password!')
                return render(request,'login.html',  )
                # messages.success(request, 'Incorrect Username And Password')
    except Exception as a :
            return render(request,'login.html',{ 'error':a})





    return render(request, 'login.html')
    
        

def logoutuser(request):
    logout(request)
    return redirect('/login')

def signup(request):
    try:
        if request.method == 'POST':
                password=request.POST.get('password')
                confirmpassword=request.POST.get('confirmpassword')
                name=request.POST.get('name')
                email=request.POST.get('email')
                password=request.POST.get('password')
                user = User.objects.create_user(name,email,password)

                if password == confirmpassword:
                    user.save()
                    return render(request,'login.html')
                    
                    # messages.add_message(request, messages.INFO,'now u can ')
                else :
                    # error={ 'error':'passwords not matched'}
                    return render(request,'signup.html',{ 'error':'passwords not matched'})
    except Exception as e:
            # return render(request,'signup.html',e)

            # messages.success(request, e)
            return render(request,'signup.html',{ 'error':e})


        
            
        
    return render(request,'signup.html')

def feedback(request):

        # # return redirect(request,'/desc')

        # # messages.success(request, 'Incorrect Username And Password')
        # # return render(request,'feedback.html')
        # if request.method == 'post':

        #     return redirect(request,'/desc')


        return render(request,'feedback.html')


def desc(request):
        
            
            
        if request.method == 'POST':
            feedback = request.POST.get("feedback")
            
            username = request.POST.get("name")

            feedback= feeedback(name=username,feedback=feedback,datetime=datetime.today())
            feedback.save()

#             feedbackk ='''  
            
# '''+username + ''' :
#             '''+feedback 
#             file1 = open("myfiile.txt", "a")  # append mode
#             file1.write(feedbackk)
#             file1.close()
            messages.success(request, 'Successfully Submited Your Feedback!')
        
        return render(request,'desc.html')


     