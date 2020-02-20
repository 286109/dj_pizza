from django.db import models


# добавить класс для денег

class Topping(models.Model):
    """
    A pizza toping.
    Set a name, weight and price for a single portion of the topping.
    """

    name = models.CharField(max_length=200)
    # weight in gramms, from 0 to 
    weight = models.PositiveSmallIntegerField()
    # price in cents/pennys 
    # price = models.IntegerField()


class PizzaComponent(models.Model):
    """
    An amount of particular topping for a pizza (similar to a line in an invoice).
    """
    pizza_component = models.ForeignKey(Topping, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField()


class Pizza(models.Model):
    """
    Pizza model.
    It as a "constructor" for a pizza: combine dough, toppings, set a price, etc.
    """

    DOUGH_THICKNESS_CHOICES = [
        ('thin', 'Thin dough (6 mm)'),
        ('thick', 'Thick dough (1 cm)'),
    ]

    SAUCE_CHOICES = [
        ('marinara', 'Marinara sauce'),
        ('bbq', 'Barbeque sauce'),
    ]

    dough = models.CharField(
        max_length=10,
        choices=DOUGH_THICKNESS_CHOICES,
        default=DOUGH_THICKNESS_CHOICES[0][0]
    )

    sauce = models.CharField(
        max_length=20,
        choices=SAUCE_CHOICES,
        default=SAUCE_CHOICES[0][0],
    )
    
    toppings = models.ManyToManyField(PizzaComponent)
