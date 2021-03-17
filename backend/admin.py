from django.contrib import admin

# Register your models here.
from .models import Listing, ListingImage

admin.site.register(Listing)
admin.site.register(ListingImage)