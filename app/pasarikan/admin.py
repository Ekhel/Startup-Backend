from django.contrib import admin
from .models import Distrik, Kampung, Nelayan, Produk

class PageDistrik(admin.ModelAdmin):
    list_display = ('id_distrik','nama_distrik')
    list_display_links = ('id_distrik','nama_distrik')
    search_fields = ('id_distrik','nama_distrik')
    list_per_page = 10

class PageKampung(admin.ModelAdmin):
    list_display = ('id_kampung','distrik','nama_kampung')
    list_display_links = ('id_kampung','distrik','nama_kampung')
    search_fields = ('id_kampung','distrik','nama_kampung')
    list_per_page = 10

class PageNelayan(admin.ModelAdmin):
    list_display = ('id_nelayan','nama','distrik','kampung','ttl','jekel')
    list_display_links = ('id_nelayan','nama','distrik','kampung','ttl','jekel')
    search_fields = ('id_nelayan','nama','distrik','kampung','ttl','jekel')
    list_per_page = 10

class PageProduk(admin.ModelAdmin):
    list_display = ('id_produk','nama_produk','deskripsi','stock','ukuran','kondisi','min_order','harga')
    list_display_links = ('id_produk','nama_produk','deskripsi','stock','ukuran','kondisi','min_order','harga')
    search_fields = ('id_produk','nama_produk','deskripsi','stock','ukuran','kondisi','min_order','harga')
    list_per_page = 10


admin.site.register(Distrik, PageDistrik)
admin.site.register(Kampung, PageKampung)
admin.site.register(Nelayan, PageNelayan)
admin.site.register(Produk, PageProduk)


