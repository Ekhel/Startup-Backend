# Generated by Django 2.2.6 on 2019-11-10 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pasarikan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nelayan',
            fields=[
                ('id_nelayan', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=250)),
                ('ttl', models.DateField()),
                ('jekel', models.CharField(choices=[('laki-laki', 'LAKI-LAKI'), ('perempuan', 'PEREMPUAN')], default='laki-laki', max_length=15)),
                ('distrik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasarikan.Distrik')),
                ('kampung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasarikan.Kampung')),
            ],
            options={
                'ordering': ('id_nelayan',),
            },
        ),
    ]
