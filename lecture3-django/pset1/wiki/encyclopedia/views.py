from django.http import HttpResponse
from django.shortcuts import render

from . import util

# Create index view passing the list of entries of encyclopedia from util.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Create get view function passing entry to html file to display.
def show_entry(request, ent):
    return render(request, "encyclopedia/entry.html", {
        "page_request": ent ,
        "entry": util.get_entry(ent)
    })