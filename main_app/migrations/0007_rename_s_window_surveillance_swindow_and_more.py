# Generated by Django 4.1.4 on 2022-12-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_surveillance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveillance',
            old_name='s_window',
            new_name='swindow',
        ),
        migrations.AlterField(
            model_name='surveillance',
            name='date',
            field=models.DateField(verbose_name='Surveillance Date'),
        ),
    ]
