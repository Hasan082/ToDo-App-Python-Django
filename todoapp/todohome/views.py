from django.shortcuts import render, redirect
from .models import todomodel

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
        todoStore.save()
        # Redirect to the 'alldata' view after saving the data
        return redirect('alldata')

    return render(request, 'index.html')


def alldata(request):
    alldata = todomodel.objects.all()
    return render(request, 'alldata.html', {'alldata': alldata})


def remaining_tasks(request):
    # Render the "remaining_tasks.html" template
    return render(request, 'remaining_tasks.html')

def completed_tasks(request):
    # Render the "completed_tasks.html" template
    return render(request, 'completed_tasks.html')