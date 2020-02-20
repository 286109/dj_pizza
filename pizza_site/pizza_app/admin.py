from django.contrib import admin
from .models import Pizza, PizzaComponent, Topping

admin.site.register(Pizza)
admin.site.register(PizzaComponent)
admin.site.register(Topping)