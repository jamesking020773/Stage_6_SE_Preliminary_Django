
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):

    #POST request used to process the data enter by the user
    if request.method == "POST":
        form = NewTaskForm(request.POST) #Creates a blank form accepting request.POST that contains all the data entered by the user as an argument
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index")) #Return the user to the list displaying the added item (confirmation)
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    #GET request used to present a blank form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })