# Generated by Django 2.1.1 on 2018-09-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='replied_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replied', to='feeds.Response'),
        ),
    ]
