# Generated by Django 3.0.3 on 2020-03-04 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultation', '0003_auto_20200302_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='paciente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]