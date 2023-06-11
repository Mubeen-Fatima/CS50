from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Category(models.Model):
    caid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
class Listing(models.Model):
    lid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    starting_bid = models.IntegerField()
    # image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Listing_category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_user")

class Bid(models.Model):
    bid = models.BigAutoField(primary_key=True)
    bid_price = models.IntegerField()
    bid_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bid")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user")

class Comments(models.Model):
    cid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=256)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")


