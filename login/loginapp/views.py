from audioop import reverse
from urllib import response
from django.views.decorators.cache import never_cache
from django.shortcuts import render,redirect
from django.contrib import messages 

user='mizbah'
passw='123'
@never_cache
def index(request):
    if request.COOKIES.get('username') and  'sessionid' in request.COOKIES:
        return redirect('home')
    else:
        return render(request,'index.html')

        
def home(request):
    if 'username' in request.COOKIES and  'sessionid' in request.COOKIES: 
        return render(request,'homepage.html')    
    else:
        return redirect('/')


def userlogin(request):
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
       
        if username == user and password == passw:
            a=redirect('home')
            a.set_cookie('username',username)
            request.session['username'] = username
            return a
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')
    else:
        return redirect('/')


def user_logout(request):
    a=redirect('/')
    a.delete_cookie('sessionid')
    a.delete_cookie('username')
    request.session.flush()
    return a





# from django.http import HttpResponse
# from django.contrib.auth import authenticate
# Create your views here
#def user_login(request):
#    if 'username' in request.session:
#        return redirect(homepage)
#    
#    if request.method =='POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        print(username)
#        print(password)
#        if username == user and password == passw:
#    #   user = authenticate(username=username,password=password)
#    #  if user is not None:
#        
#            a=redirect('homepage')
#            a.set_cookie('username',username)
#            request.session['username'] = username
#            return a
#        else:
#            print('invalid credentials')
#            return redirect('login')
#    else:
#        return redirect('login')
#    
#def homepage(request):
#   if request.COOKIES.get('username') and request.session.get('username'):
#        return render(request,'homepage.html')
#   return redirect('login')
#    
#def user_logout(request):
#    a=redirect('/')
#    a.delete_cookie('sessionid')
#    a.delete_cookie('username')   
#    return a
#
#@never_cache
#def login(request):
#    if 'username' in request.session:
#        return redirect('homepage')
#    else:
#        return render (request,'index.html')
#
## def logout(request):
#     response = HttpResponseRedirect(reverse('index'))
#     request.session.flush()
#     response.delete_cookie('username')
#     return response
   
   #a.delete_cookie('username')   
# if 'username' in request.session:      
#  authenticate.logout(request)
#  return redirect(login)
# 
# return render(request,'index.html')
