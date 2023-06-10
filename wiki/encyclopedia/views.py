import random
from django.shortcuts import render, redirect
from . import util
from django.http import HttpResponseRedirect

# from markdown import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def content(request, title):
    # markdown = Markdown()
    entryPage = util.get_entry(title)
    if entryPage:  
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "FileContent":  entryPage
        } )
    else:
        return render(request, "encyclopedia/404.html", {
            "title": title 
        } )
         
def search(request):
    if request.method == "GET":
        value = request.GET['q']
        content = util.get_entry(value)
        entries = util.list_entries()
    if content:
        return render(request, "encyclopedia/title.html", {
            "title": value,
            "FileContent":  content
        } )
    else:
        search_entries = []
        for entry in entries:
            if value.lower() in entry.lower():
                search_entries.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": search_entries,
            "value": value
        } )

def newpage(request):
    
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        if title in util.list_entries():
            return render(request, "encyclopedia/newpage.html", {
                "message": "Error: This entry already exsist, Try Again"
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/title.html", {
            "title": title,
            "FileContent":  content
        } )

def edit(request, title):
    entryPage = util.get_entry(title)
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        entryPage = util.get_entry(title)
        return render(request, "encyclopedia/title.html",{
            "title": title,
            "FileContent":  entryPage
        })
    else:
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "FileContent":  entryPage
        })

def random_entry(request):
    all_entries = util.list_entries()
    random_element = random.choice(all_entries)
    content = util.get_entry(random_element)
    return render(request, "encyclopedia/title.html", {
            "title": random_element,
            "FileContent":  content
        } )
