# Generated by Django 3.0.3 on 2020-03-02 11:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specialties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('crm', models.CharField(max_length=10)),
                ('e_mail', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('telefone', models.CharField(max_length=20)),
                ('especialidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors_specialties', to='specialties.Specialties')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
    ]
