from django.shortcuts import render

from . import util
import markdown2
import random

def convert_md_html(title):
    content = util.get_entry(title)
    markdowner = markdown2.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    coffee = util.get_entry("coffee")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    html_content = convert_md_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":html_content
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            entries = util.list_entries()
            recommendation = []
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "q": entry_search,
                "entries" : recommendation,
            })

def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_html(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
def save_entry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
def random_page(request):
    entries = util.list_entries()
    randomentry = random.choice(entries)
    html_content = convert_md_html(randomentry)
    return render(request, "encyclopedia/entry.html", {
        "title": randomentry,
        "content": html_content
    })