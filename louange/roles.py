from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Role
from app.forms import RoleForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')
# get role list
def index(request):
    assert isinstance(request, HttpRequest)
    roles = Role.objects.all()
    return render(
        request,
        'app/roles/index.html',
        {
            'roles': roles
        }
    )


@login_required(login_url='/login')
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = RoleForm
    return render(
        request,
        'app/roles/add.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login')    
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, "vous avez insere avec succes !")
            
        return redirect('/roles')
    


@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = RoleForm()
        else:
            role = Role.objects.get(pk=id)
            form = RoleForm(instance=role)
        return render(
            request,
            'app/roles/edit.html',
            {
                'form': form
            }
        )


@login_required(login_url='/login')        
# Update a roles
def update(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if id == 0:
            form = RoleForm(request.POST)
        else:
            roles = Role.objects.get(pk=id)
            form = RoleForm(request.POST, instance=roles)
        if form.is_valid():
            form.save()
        messages.success(request, "vous avez ete modifier avec succes !")
        return redirect('/roles')


@login_required(login_url='/login')    
# Remove a roles    
def delete(request, id):
    roles = Role.objects.get(pk=id)
    roles.delete()
    messages.success(request, "vous avez ete supprimer avec succes !")
    return redirect('/roles')