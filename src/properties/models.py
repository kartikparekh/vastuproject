from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.
class Property_Information(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    address = models.TextField(max_length=10000)
    BHK_OPTIONS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('other','other')
    )
    BHK = models.CharField(max_length=100,choices=BHK_OPTIONS, default=1)
    image = models.ImageField(blank=True)
    area = models.CharField(max_length=500,default='0sqft')
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pincode = models.IntegerField()
    parking = models.BooleanField(default=0)
    small_thumbnail = models.ImageField(upload_to="images/")
    STATUS_CHOICE = (
        ('Rent','Rent'),
        ('Sale','Sale'),
        ('Under-Const.','Under-Construction'),
    )
    status = models.CharField(max_length=100,choices=STATUS_CHOICE,default='Rent')
    FURNISHING_CHOICE = (
        ('Un-Furnished','Un-Furnished'),
        ('Semi-Furnished','Semi-Furnished'),
        ('Furnished','Furnished'),
        ('Fully-Furnished','Fully-Furnished'),
    )
    furnishing = models.CharField(max_length=100,choices=FURNISHING_CHOICE)
    AMENITIES_CHOICE = (
        ('Gym','Gym'),
        ('Swimming Pool','Swimming Pool'),
        ('Garden','Garden'),
        ('Club House','Club House'),
        ('Cafe Area','Cafe Area'),
        ('Children Play Area','Children Play Area'),
        ('Intercom','Intercom'),
        ('Amphitheatre','Amphitheatre'),
        ('Yoga club','Yoga club'),
        ('Servent room','Servent room'),
        ('High security','High security'),
        ('CCTV camera','CCTV camera'),
        ('Mini banquet','Mini banquet'),
    )
    amenities = MultiSelectField(choices=AMENITIES_CHOICE)
    PROPERTY_TYPE = (
        ('Builder Floor','Builder Floor'),
        ('Residential Plot','Residential Plot'),
        ('Commercial Shops','Commercial Shops'),
    )
    property_type = models.CharField(max_length=100,choices=PROPERTY_TYPE,default='Residentail Plot')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property_detail',kwargs={
            'id':self.id
        })

    
class PropertyImage(models.Model):
    propertY = models.ForeignKey(Property_Information, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/") 

    def __str__(self):
        return self.propertY.name