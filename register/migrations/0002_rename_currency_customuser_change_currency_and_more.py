# Generated by Django 5.0.3 on 2024-04-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='currency',
            new_name='change_currency',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='currency',
        ),
        migrations.AddField(
            model_name='profile',
            name='change_currency',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('GBP', 'British Pound'), ('EUR', 'Euro')], default='GBP', max_length=3),
        ),
    ]