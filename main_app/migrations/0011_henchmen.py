# Generated by Django 4.1.4 on 2023-01-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_surv6eillance_window_surveillance_surveillance_window'),
    ]

    operations = [
        migrations.CreateModel(
            name='Henchmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adjective', models.CharField(max_length=20)),
            ],
        ),
    ]
