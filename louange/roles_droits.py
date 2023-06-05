from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import RoleDroit
from app.forms import RoleDroitForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')
# get roles et droits list
def index(request):
    assert isinstance(request, HttpRequest)
    roles_droits = RoleDroit.objects.all()
    return render(
        request,
        'app/roles_droits/index.html',
        {
            'roles_droits': roles_droits
        }
    )


@login_required(login_url='/login')
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = RoleDroitForm
    return render(
        request,
        'app/roles_droits/add.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login')    
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = RoleDroitForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, "vous avez ete insert avec succes !")
            
        return redirect('/rolesDroits')
    


@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = RoleDroitForm()
        else:
            horaire = RoleDroit.objects.get(pk=id)
            form = RoleDroitForm(instance=horaire)
        return render(
            request,
            'app/roles_droits/edit.html',
            {
                'form': form
            }
        )


@login_required(login_url='/login')        
# Update a roles_droits
def update(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if id == 0:
            form = RoleDroitForm(request.POST)
        else:
            roles_droits = RoleDroit.objects.get(pk=id)
            form = RoleDroitForm(request.POST, instance=roles_droits)
        if form.is_valid():
            form.save()
        messages.success(request, "vous avez ete modifier avec succes !")
        return redirect('/rolesDroits')


@login_required(login_url='/login')    
# Remove a roles_droits    
def delete(request, id):
    roles_droits = RoleDroit.objects.get(pk=id)
    roles_droits.delete()
    messages.success(request, "vous avez ete supprimer avec succes !")
    return redirect('/rolesDroits')