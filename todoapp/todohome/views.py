from django.shortcuts import render, redirect
from .models import todomodel
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'POST':
        title = request.POST.get('txtName')
        description = request.POST.get('txtMsg')
        datecomplete = request.POST.get('txtDate')

        todoStore = todomodel(
            title=title,
            description=description,
            datecomplete=datecomplete
        )
        
        messages.success(request, "Task added successfully")
        todoStore.save()
        # Redirect to the 'alldata' view after saving the data
        return redirect('alldata')

    return render(request, 'index.html')

@login_required
def alldata(request):
    alldata = todomodel.objects.filter(soft_del=0)
    return render(request, 'alldata.html', {'alldata': alldata})

@login_required
def editdata(request, id):
    edit = todomodel.objects.filter(id = id)
    return render(request, 'edit.html', {'edit': edit})

@login_required
def updatedata(request, id):
    if request.method == 'POST':
        title = request.POST.get('txtName')
        description = request.POST.get('txtMsg')
        datecomplete = request.POST.get('txtDate')

        todoStore = todomodel.objects.filter(id=id)

        todoStore = todomodel(
            id=id,
            title=title,
            description=description,
            datecomplete=datecomplete
        )
        messages.info(request, "Task Updated successfully")
        todoStore.save()
        # Redirect to the 'alldata' view after saving the data
        return redirect('alldata')

@login_required
def deletedata(request, id):
    delete_data = todomodel.objects.filter(id=id)
    delete_data.delete()
    messages.error(request, "Task Deleted successfully")
    return redirect('trash')

@login_required
def statusdata(request, id):
    status_data = todomodel.objects.get(id=id)
    status_data.status = True
    status_data.save()
    messages.error(request, "Task moved to bin successfully")
    return redirect('alldata')

@login_required
def completed_tasks(request):
    completed_tasks = todomodel.objects.filter(status=1, soft_del=0)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})

@login_required
def remaining_tasks(request):
    remaining_tasks = todomodel.objects.filter(status=0, soft_del=0)
    return render(request, 'remaining_tasks.html', {'remaining_tasks': remaining_tasks})

@login_required
def soft_del(request, id):
    soft_del = todomodel.objects.get(id=id)
    soft_del.soft_del = True
    soft_del.save()
    messages.error(request, "Task moved to bin successfully")
    return redirect('alldata')


@login_required
def trash(request):
    trash = todomodel.objects.filter(soft_del=1)
    return render(request, 'trash.html', {'trash': trash})
