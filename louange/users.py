from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from app.forms import UserForm
from app.models import Role
from app.models import RoleDroit
from app.models import Droit
from app.models import UserRole
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, get_object_or_404


@login_required(login_url='/login')
def index(request):
    users = User.objects.all()
    return render(
        request,
        'app/users/index.html',
        {
            'users': users
        }
    )
    
# Show register form
@login_required(login_url='/login')
def register(request):
    form = UserForm()
    return render(
        request, 
        'app/users/register.html',
        {
            'form': form
        }
    )

# Login



def user_login(request):
    page = "login"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            id = user.pk
            roles_ids = UserRole.objects.filter(utilisateur_id = id).values('role')
            role_ids = []
            
            for i in range(0, len(roles_ids)):
                role_ids.append(list(roles_ids[i].values())[0])
            
            droit_ids = []
            nom_roles = []
            for role_id in role_ids:
                droits_ids = RoleDroit.objects.filter(role_id = role_id).values('droit')
                role_names = Role.objects.filter(pk = role_id).values('nom')
                
                for i in range(0, len(droits_ids)):
                    droits = list(droits_ids[i].values())[0]
                    if droits not in droit_ids:
                        droit_ids.append(droits)
                
                for i in range(0, len(role_names)):
                    nom_roles.append(list(role_names[i].values())[0])
        
            request.session['permission'] = droit_ids
            request.session['nom_roles'] = nom_roles
            return redirect('/')
                    
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(
        request,
        'app/users/login.html',
        {
            'page': page
        }
    )


@login_required(login_url='/login')
# Register a new user    
def store(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/users')



# Logout a user authenticated  
def user_logout(request):
    logout(request)
    return redirect('/login')



@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(
            request,
            'app/users/edit.html',
            {
                'form': form
            }
        )
        
@login_required(login_url='/login')        
# Update a user
def update(request, id):
    user = get_object_or_404(User, id=id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        messages.success(request, "User has been updated successfully !")
        return redirect('/users')


@login_required(login_url='/login')    
# Remove a user    
def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request, "User has been removed successfully !")
    return redirect('/users')