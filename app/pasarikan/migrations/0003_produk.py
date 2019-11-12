# Generated by Django 2.2.6 on 2019-11-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasarikan', '0002_nelayan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.AutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(max_length=250)),
                ('deskripsi', models.CharField(max_length=250)),
                ('stock', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ukuran', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('kondisi', models.CharField(choices=[('Frosen', 'Frosen'), ('Fresh', 'Fresh')], default='Frosen', max_length=15)),
                ('min_order', models.IntegerField(default=1)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('show', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('id_produk',),
            },
        ),
    ]