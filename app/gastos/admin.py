""" Site de administração com todos os modelos """

from django.contrib import admin
from .models import Fixo

# Register your models here.
admin.site.register(Fixo)
