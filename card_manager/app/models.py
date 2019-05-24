from django.db import models
from django.core.validators import RegexValidator


class CardClassification(models.Model):
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification


class Card(models.Model):
    company = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100, blank=True)
    phone_number_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True)
    email = models.EmailField(blank=True)
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$',
                                       message="Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed.")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, blank=True)
    office_address = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100, blank=True)
    memo = models.TextField(max_length=300, blank=True)
    card_img = models.FileField(upload_to='uploads/',
                                blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    card_classification = models.ForeignKey(CardClassification, on_delete=models.CASCADE)
