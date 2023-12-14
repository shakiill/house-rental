import datetime
import hashlib
import os
import uuid

from decouple import config
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.core.mail import EmailMessage
from django.db import models
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from apps.user.managers import StaffManager, CustomerManager, HouseOwnerManager


# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=True, blank=True)
    last_name = None
    first_name = None
    email = models.EmailField(verbose_name='Email Address', unique=True)
    name = models.CharField(verbose_name='Full Name', max_length=100)
    photo = models.ImageField(upload_to='user_photo', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='user_photo', null=True, blank=True)
    signature = models.ImageField(upload_to='signature', null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Staff(CustomUser):
    class Meta:
        proxy = True

    objects = StaffManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        password = get_random_string(length=6, allowed_chars='ABCD0123456789')
        print(password)
        self.set_password(password)
        super(Staff, self).save(*args, **kwargs)
        # send sms script


class Customer(CustomUser):
    class Meta:
        proxy = True

    objects = CustomerManager()

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='customer')
        self.username = self.email
        self.is_active = False
        self.groups.set([group])



class HouseOwner(CustomUser):
    class Meta:
        proxy = True

    objects = HouseOwnerManager()

    def save(self, *args, **kwargs):
        super(HouseOwner, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='owner')
        self.username = self.email
        self.is_active = False
        self.groups.set([group])


class OtpToken(models.Model):
    user = models.CharField(max_length=255, editable=False)
    otp = models.CharField(max_length=40, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    attempts = models.IntegerField(default=0)
    used = models.BooleanField(default=False)
    is_password_reset = models.BooleanField(default=False)
    reset_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    reset_link = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "OTP Token"
        verbose_name_plural = "OTP Tokens"

    def __str__(self):
        return "{} - {}".format(self.user, self.otp)

    @classmethod
    def create_otp_for_user(cls, email, is_password_reset=None):
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        otps = cls.objects.filter(user=email, timestamp__range=(today_min, today_max))

        if otps.count() <= getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 100000):
            otp = cls.generate_otp(length=getattr(settings, 'PHONE_LOGIN_OTP_LENGTH', 4))
            if is_password_reset:
                user = CustomUser.objects.get(email=email)
                url = f'https://iou.ac/password_reset_confirm/?otp={otp}&key={user.uuid}'
                otp_token = OtpToken(user=email, otp=otp, is_password_reset=is_password_reset, reset_link=url)
            else:
                otp_token = OtpToken(user=email, otp=otp)
            otp_token.save()
            print(f'Your otp is {otp}')
            if otp_token.is_password_reset:
                user = CustomUser.objects.get(email=email)
                context = {
                    'otp': otp,
                    'email': email,
                    'key': user.uuid,
                }
                print(user.uuid)
                html_content = render_to_string('password_reset.html', context)
            else:
                context = {
                    'otp': otp,
                    'email': email
                }
                html_content = render_to_string('otp.html', context)

            # html_content = render_to_string('email_template.html', context)

            # message = Mail(
            #     from_email='noreply@iou.ac',
            #     to_emails=email,
            #     subject='OTP for IOU',
            #     html_content=html_content
            # )
            # try:
            #     sg = SendGridAPIClient('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')
            #     response = sg.send(message)
            #     print(response.status_code)
            #     print(response.body)
            #     print(response.headers)
            # except Exception as e:
            #     print(str(e))

            return otp_token
        else:
            return False

    @classmethod
    def generate_otp(cls, length=4):
        hash_algorithm = getattr(settings, 'PHONE_LOGIN_OTP_HASH_ALGORITHM', 'sha256')
        m = getattr(hashlib, hash_algorithm)()
        m.update(getattr(settings, 'SECRET_KEY', None).encode('utf-8'))
        m.update(os.urandom(16))
        otp = str(int(m.hexdigest(), 16))[-length:]
        # otp = 1234
        return otp