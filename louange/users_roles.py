from app.models import UserRole
from app.forms import UserRoleForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')
def index(request):
    user_role = UserRole.objects.all()
    return render(
        request,
        'app/users_roles/index.html',
        {
            'users_roles': user_role
        }
    )
    
    
@login_required(login_url='/login')   
def add(request):
    if request.method == 'GET':
        form = UserRoleForm
    return render(
        request,
        'app/users_roles/add.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login')
def store(request):
    if request.method == 'POST':
        form = UserRoleForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, " Vous avez enregistré avec succés ")
        return redirect('/users_roles')


@login_required(login_url='/login')    
def delete(request,id):
    user_role=UserRole.objects.get(pk = id)
    user_role.delete()
    messages.success(request, "Vous avez supprimé avec succés")
    return redirect('/users_roles')


@login_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        if id == 0:
            form = UserRoleForm()
        else:
            user_role = UserRole.objects.get(pk = id)
            form = UserRoleForm(instance = user_role)
        return render(
            request,
            'app/users_roles/edit.html',
            {
                'form':form
            }
        )


@login_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = UserRoleForm(request.POST)
        else:
            user_role = UserRole.objects.get(pk = id)
            form = UserRoleForm(request.POST, instance = user_role)
        if form.is_valid():
            form.save()
        messages.success(request, "Vous avez modifié avec succés")
        return redirect('/users_roles')