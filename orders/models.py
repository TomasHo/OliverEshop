from django.db import models
from shop.models import Product


class Order(models.Model):
    meno = models.CharField(max_length=50)
    priezvisko = models.CharField(max_length=50)
    email = models.EmailField()
    adresa = models.CharField(max_length=250)
    PSC = models.CharField(max_length=5)
    mesto = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    zaplatene = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Objednávka {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    objednavka = models.ForeignKey(Order, related_name='items')
    produkt = models.ForeignKey(Product, related_name='order_items')
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mnozstvo = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cena * self.mnozstvo