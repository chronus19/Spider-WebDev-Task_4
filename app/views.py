from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpRequest,QueryDict
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def dashboard(req):
    if req.user.is_authenticated() == True :
        return render(req,"dashboard.html",{'posts':list(Post.objects.all()),})
    else:
        return redirect(login)

def delete_post(req):
    if req.user.is_authenticated() == False or req.user.is_staff == 0:
        return redirect(login);
    
    if req.method != 'GET':
        return redirect(dashboard)
    post_id = req.GET.get('post_id','')
    Post.objects.filter(id=post_id).delete();
    return redirect(dashboard)

def admin_panel(req):
    if req.user.is_authenticated() == False or req.user.is_superuser == 0:
        return redirect(login);

    users = list(User.objects.all())  
    return render(req,'admin_panel.html',{'users':users,})
    

def update_access_level(req):
    if req.user.is_authenticated() == False or req.user.is_superuser == 0:
        return redirect(login);
    
    if req.method == 'POST':
        user_id = req.POST.get('user_id','')
        access_level = req.POST.get('access_level','1')

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return redirect(dashboard)
         
        if user.is_superuser == 1:
            return redirect(admin_panel)
      
        if access_level == '3':
            user.is_superuser = 1
            user.is_staff = 1
        elif access_level == '2':
            user.is_staff = 1
        else:
            user.is_staff = 0
        user.save()
        
        return redirect(admin_panel)

    else:
        return redirect(dashboard)

def add_post(req):
    if req.user.is_authenticated() == False :
        return redirect(login)
    if req.method != 'POST':
        return redirect(dashboard)

    title = req.POST.get('title','')
    body = req.POST.get('body','')
    username = req.user.first_name

    if len(title) < 0 or len(title)>40 or len(body)>400:
        return redirect(dashboard)

    Post.objects.create(user=username,title=title,body=body)
    return redirect(dashboard)
    

def login(req):
    if req.user.is_authenticated():
        return redirect(dashboard);
    if req.method != 'POST':
        return render(req,'login.html')
    
    username = req.POST.get('username','')
    passwd = req.POST.get('passwd','')

    user = auth.authenticate(username=username , password=passwd)
    if user is not None:
         auth.login(req,user)
         return redirect(dashboard);
    else:
        return render(req,"login.html",{'invalid':1,});

def logout(req):
    auth.logout(req)
    return redirect(login)

def register(req):
    if req.method != 'POST':   
        return render(req,'register.html')

    data = req.POST
    user = None
    username = data.get('username','')
    name = data.get('name','')
    email = data.get('email','')
    pwd = data.get('passwd','')

    if validate_data(data) != 0:                 # Validate input data
        return render(req,'register.html')

    if User.objects.filter(username=username).exists() == True:
        return render(req,'register.html')
    try: 
        user = User.objects.create_user(username=username, password=pwd, email=email, first_name=name)
    except ValidationError:
        return render(register)
    if user is not None:
        return render(req,'success.html')
    else:
        return redirect('login.html');


def validate_data(data,new_student=1):        # Function for validating input data from user
    username = data.get('username','')
    name = data.get('name','')
    email = data.get('email','')
    pwd = data.get('passwd','')

    if len(username) < 3 or len(username)>20 or len(name) < 3 or len(email) < 8 or len(email)>128 or len(pwd) < 8:
        return -1

    return 0
