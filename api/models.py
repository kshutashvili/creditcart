from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


# Create your models here.

# class CreditCardUser(AbstractUser): 
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
#     REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS


class CreditCardUser(AbstractUser): 
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS
    first_name = models.CharField(blank = True, null = True, max_length=50)
    second_name = models.CharField(blank = True, null = True, max_length=50)
    middle_name = models.CharField(blank = True, null = True, max_length=50)
    inn = models.PositiveIntegerField(blank = True, null = True)
    passport_number = models.PositiveIntegerField(blank = True, null = True)
    passport_code = models.CharField(blank = True, null = True, max_length=2)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True)
    
    class Meta(object):
        unique_together = ('email',)


class Rewiew(models.Model):
    review_text = models.CharField(blank=False, max_length = 512)
    reviewer_first_name = models.CharField(blank=False, max_length = 30)
    reviewer_last_name = models.CharField(blank=False, max_length = 30)
    review_date = models.DateTimeField(blank=False, default=datetime.now)
    reviewer_picture = models.ImageField(upload_to = 'avatars/', default = 'pic_folder/no-img.jpg', blank = False)

    def __str__(self):
            return self.reviewer_first_name + ' ' + self.reviewer_last_name


class Advantage(models.Model):
    advantage_title = models.CharField(blank=False, max_length=128)
    advantage_text = models.CharField(blank=False, max_length=1024)
    advantage_picture = models.ImageField(upload_to = 'advantage_pic/', default = 'pic_folder/no-img.jpg', blank = False)

    def __str__(self):
            return self.advantage_text


class Faq(models.Model):
    question = models.CharField(blank=False, max_length = 128)
    answer = models.CharField(blank=False, max_length = 256)

    def __str__(self):
        return self.question

class CreditRequestStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
            return self.name

class CreditRequest(models.Model):
    is_active = models.BooleanField(default = True)
    date_time_requested = models.DateTimeField(auto_now_add=True, editable=True)
    requested_good = models.CharField(max_length=500)
    sellers_shop = models.CharField(max_length=70)
    user = models.ForeignKey(CreditCardUser, on_delete=models.CASCADE)
    status = models.ForeignKey(CreditRequestStatus, on_delete=models.CASCADE, default = 2)
    is_accepted = models.BooleanField(default = False)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.middle_name + ' ' + self.user.second_name