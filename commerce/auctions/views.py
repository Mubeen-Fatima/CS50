from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "auctions/index.html",{
        "all_listing": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        bid = request.POST['bid']
        category = Category.objects.get(caid=request.POST['category'])
        user = request.user
        listing = Listing(
            title = title,
            description = description,
            category=category,
            user = user,
            price = int(price),
            starting_bid = bid,
        )
        listing.save()
        return HttpResponseRedirect(reverse(index))
    else:
        categories = Category.objects.all()
        return render(request, "auctions/newlisting.html",{
            "categories": categories
        })


def listing(request, listing_id):
    pass

def categories(request):
    pass

def category_listing(request, category_id):
    pass

def watchlist(request):
    pass

