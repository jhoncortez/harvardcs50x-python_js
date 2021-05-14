from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import default_storage

from . import util

class EncyclopediaEntryForm(forms.Form):
    title_field = forms.CharField(label="Title")
    content_field = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

# Create index view passing the list of entries of encyclopedia from util.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Create get view function passing entry to html file to display.
def show_entry(request, ent):
    return render(request, "encyclopedia/entry.html", {
        "page_request": ent ,
        "entry": util.get_entry(ent),
        "title": f"Entry: {ent}"
    })

def search(request):
    # validate request exist
    if request.method == "GET" and request.GET.get('q') :

        # initializing values
        search_value = request.GET['q']
        filename = f"entries/{search_value}.md"

        # validate if file exist
        if default_storage.exists(filename):

            #redirect to entry page
            return HttpResponseRedirect(reverse("show_entry", args = (search_value,)))

        else:

            #show list list of entrys with the words matched word
            #return HttpResponse('nothing to do')
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(search_value),
                "title": f"Search for: {search_value}",
                "search_value": search_value
            })

    return HttpResponseRedirect(reverse("index"))

def add(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = EncyclopediaEntryForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the entry from the 'cleaned' version of form data
            title = form.cleaned_data["title_field"]
            content = form.cleaned_data["content_field"]

            # Add the new entry to our entries as .md file
            if util.save_entry(title, content):
                return HttpResponseRedirect(reverse("show_entry", args = (title,)))
            else:
                raise forms.ValidationError(
                    "Already exist an entry with title %(title)s",
                    params = {'title': title},
                )
        else: 
            # If the form is invalid, re-render the page with existing information.
            return render(request, "add.html", {"title": "Error - Invalid form data", "form": form})

    return render(request, "encyclopedia/add.html", {
        "form": EncyclopediaEntryForm()
    })

    