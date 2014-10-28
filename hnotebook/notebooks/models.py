from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    private = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


class Housing(models.Model):
    RENT = 'RE'
    BUY = 'BU'
    CATEGORY_CHOICES = (
        (RENT, "Rent"),
        (BUY, "Buy"),
    )

    HOUSE = 'HO'
    FLAT = 'FL'
    PROPERTY_TYPE_CHOICES = (
        (HOUSE, "House"),
        (FLAT, "Flat"),
    )

    notebook          = models.ForeignKey('Notebook', null=False)
    category          = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=RENT, null=False)
    property_type     = models.CharField(max_length=2, choices=PROPERTY_TYPE_CHOICES, default=FLAT, null=False)
    description       = models.TextField(null=False)
    town              = models.CharField(max_length=200, null=False)
    address           = models.TextField()

    price             = models.FloatField(null=False)
    currency          = models.CharField(max_length=10, default='$')
    caution           = models.FloatField(default=0.0)
    guarantee         = models.FloatField(default=0.0)
    maintenance_fee   = models.FloatField(default=0.0)

    surface           = models.IntegerField(null=False)
    floor             = models.IntegerField()
    elevator          = models.BooleanField(default=False)

    num_rooms         = models.IntegerField('Rooms', null=False)
    num_bedroom       = models.IntegerField('Bedrooms')
    num_restroom      = models.IntegerField('Restrooms')
    num_living_room   = models.IntegerField('Living rooms')
    num_dining_room   = models.IntegerField('Dining rooms')
    num_balcony       = models.IntegerField('Balconies')
    num_car_park_slot = models.IntegerField('Car park slots')
    kitchen           = models.BooleanField(default=False)

    offer_url         = models.URLField(default='http://www.example.com', null=False)

    def __str__(self):
        category_name = self.get_category_display()
        property_type_name = self.get_property_type_display()
        price = self.price
        currency = self.currency

        return '{}, {}, {} {}'.format(category_name, property_type_name, currency, price)
