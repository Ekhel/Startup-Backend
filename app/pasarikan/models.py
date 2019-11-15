from django.db import models
from django.shortcuts import reverse
from django.conf import settings

class Distrik(models.Model):
    id_distrik = models.AutoField(primary_key="True")
    nama_distrik = models.CharField(max_length=200)

    class Meta:
        ordering = ('id_distrik',)

    def __str__(self):
        return self.nama_distrik
    
    
class Kampung(models.Model):
    id_kampung = models.AutoField(primary_key="True")
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    nama_kampung = models.CharField(max_length=100)

    class Meta:
        ordering = ('id_kampung',)

    def __str__(self):
        return self.nama_kampung


class Nelayan(models.Model):
    id_nelayan = models.AutoField(primary_key="True")
    nama = models.CharField(max_length=250)
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    kampung = models.ForeignKey(Kampung, on_delete=models.CASCADE)
    ttl = models.DateField(auto_now=False)
    GENDER_CHOICES = (
        ('laki-laki','LAKI-LAKI'),
        ('perempuan', 'PEREMPUAN'),
    )
    jekel = models.CharField(max_length=15, choices=GENDER_CHOICES,default='laki-laki')

    class Meta:
        ordering = ('id_nelayan',)

    def __str__(self):
        return self.nama


class Produk(models.Model):
    id_produk = models.AutoField(primary_key="True")
    nama_produk = models.CharField(max_length=250)
    deskripsi = models.CharField(max_length=250)
    stock = models.DecimalField(max_digits=10, decimal_places=0)
    ukuran = models.CharField(max_length=50)
    KONDISI_CHOICES = (
        ('Frosen','Frosen'),
        ('Fresh','Fresh'),
    )
    slug = models.SlugField()
    kondisi = models.CharField(max_length=15, choices=KONDISI_CHOICES,default='Frosen')
    min_order = models.IntegerField(default=1)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    show = models.CharField(max_length=20)

    class Meta:
        ordering = ('id_produk',)

    def __str__(self):
        return self.nama_produk

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Produk, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.nama_produk}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
