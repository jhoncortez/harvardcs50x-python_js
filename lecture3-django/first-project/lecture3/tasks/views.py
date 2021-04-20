from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

#tasks = ["foo", "bar", "baz"]
#tasks = []

class NewTaskForm(forms.Form):
    tasks_field = forms.CharField(label="New Task")
    #ex = forms.CharField(label="Example field")

# Index of tasks apps.
def index(request):

    # Check if there already exists a "tasks" key in our session

    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {"title": "Tasks", "tasks": request.session["tasks"]})

# Add a new task:
def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["tasks_field"]

            # Add the new task to our list of tasks
            #tasks.append(task) #no longer exist the list

            # Add the new task to our session of tasks
            request.session["tasks"] += [task]
            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {"title": "Error - Invalid form data", "form": form})

    return render(request, "tasks/add.html", {"title": "Add Task", "form": NewTaskForm()})
