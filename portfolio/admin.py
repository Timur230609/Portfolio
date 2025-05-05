from django.contrib import admin
from .models import Contact,Category,Portfolio, PortfolioCategory

# Register your models here.

admin.site.register((Contact,Category,Portfolio,PortfolioCategory)) 