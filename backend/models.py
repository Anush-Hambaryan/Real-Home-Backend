from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import datetime
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFill
from PIL import Image


# Create your models here.

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing', blank=False, null=False)
    
    # Transaction information 
    TRANSACTION_CHOICES = (
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    )
    transaction = models.CharField(max_length=4, choices=TRANSACTION_CHOICES, blank=False, null=False)

    RENT_PERIOD_CHOICES = (
        ('Daily', 'Daily'),
        ('Monthly', 'Monthly'),
    )
    rent_period = models.CharField(max_length=7, choices=RENT_PERIOD_CHOICES, blank=True, null=True)

    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('AMD', 'AMD'),
        ('RUB', 'RUB')
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=False, null=False)
    
    price = models.PositiveIntegerField(blank=False, null=False)

    # General Information
    HOME_TYPE_CHOICES = (
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Townhome', 'Townhome'),
    )
    home_type = models.CharField(max_length=9, choices=HOME_TYPE_CHOICES, blank=False, null=False)

    year_built = models.PositiveSmallIntegerField(blank=False, null=False, validators=[MinValueValidator(1800), MaxValueValidator(datetime.datetime.now().year)])
    area = models.PositiveSmallIntegerField(blank=False, null=False)
    lot_size = models.PositiveSmallIntegerField(blank=True, null=True)  # blank for Apartment
    floor = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(25)]) # blank for House, Townhome
    number_of_floors = models.PositiveSmallIntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(25)])
    number_of_rooms = models.PositiveSmallIntegerField(blank=False, null=False)
  
    FURNISHING_CHOICES = (
        ('Full', 'Full'),
        ('Only Kitchen', 'Only Kitchen'),
        ('None', 'None')
    )
    furnishing = models.CharField(max_length=12, choices=FURNISHING_CHOICES, blank=False, null=False)

    # Address
    street_building = models.CharField(max_length=200)
    DISTRICT_CHOICES = (
        ('Ajapnyak', 'Ajapnyak'),
        ('Arabkir', 'Arabkir'),
        ('Avan', 'Avan'),
        ('Davtashen', 'Davtashen'),
        ('Erebuni', 'Erebuni'),
        ('Kanaker-Zeytun', 'Kanaker-Zeytun'),
        ('Kentron', 'Kentron'),
        ('Malatia-Sebastia', 'Malatia-Sebastia'),
        ('Nork-Marash', 'Nork-Marash'),
        ('Nor Nork', 'Nor Nork'),
        ('Nubarashen', 'Nubarashen'),
        ('Shengavit', 'Shengavit'),
    )
    district = models.CharField(max_length=16, choices=DISTRICT_CHOICES, blank=False, null=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # Amenities  
    air_conditioning = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    central_heating = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    pwd_accessable = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)

    # Description 
    description = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    #image_medium = models.ImageField(upload_to='images/%Y/%m/%d')
    image_medium = ProcessedImageField(upload_to='images/%Y/%m/%d', processors=[ResizeToFill(900, 600)], format='JPEG', options={'quality': 80, 'progressive': True, 'optimize': True})