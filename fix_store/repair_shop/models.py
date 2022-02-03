import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from datetime import datetime


class ClientCard(models.Model):
    is_fixed = models.BooleanField(default=False, verbose_name='Fixed')
    brand = models.CharField(max_length=50, verbose_name='Brand')
    package = models.CharField(max_length=250, verbose_name='Package')
    breakage = models.CharField(max_length=250, verbose_name='Breakage')
    name = models.CharField(max_length=150, verbose_name='Client name')
    phone_number = models.CharField(max_length=50, verbose_name='Phone number')
    in_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of reception')
    master = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, max_length=200, unique=True)
    break_fix = models.CharField(null=True, max_length=250, verbose_name='Repairs carried out')
    price = models.IntegerField(null=True, verbose_name='Price')
    warranty = models.CharField(default='3 міс.', null=True, max_length=50, verbose_name='Warranty')
    out_date = models.DateTimeField(null=True, max_length=50, verbose_name='Date of issue')

    def __str__(self):
        return f"{self.in_date} {self.name}"

    def get_absolute_url(self):
        return reverse('queued')


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = str(uuid.uuid1())
    instance.out_date = datetime.now()


pre_save.connect(slug_generator, sender=ClientCard)
