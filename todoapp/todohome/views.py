from django.shortcuts import render, redirect
from .models import todomodel
from django.contrib import messages

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


def alldata(request):
    alldata = todomodel.objects.all()
    return render(request, 'alldata.html', {'alldata': alldata})


def editdata(request, id):
    edit = todomodel.objects.filter(id = id)
    return render(request, 'edit.html', {'edit': edit})


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


def deletedata(request, id):
    delete = todomodel.objects.filter(id=id).delete()
    messages.error(request, "Task Deleted successfully")
    return redirect('alldata')


def statusdata(request, id):
    status_data = todomodel.objects.get(id=id)
    status_data.status = True
    status_data.save()
    return redirect('alldata')


def completed_tasks(request):
    completed_tasks = todomodel.objects.filter(status=1)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


def remaining_tasks(request):
    remaining_tasks = todomodel.objects.filter(status=0)
    return render(request, 'remaining_tasks.html', {'remaining_tasks': remaining_tasks})



