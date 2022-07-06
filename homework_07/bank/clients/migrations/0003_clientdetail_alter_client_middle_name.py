# Generated by Django 4.0.6 on 2022-07-06 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='details', serialize=False, to='clients.client')),
                ('bio', models.TextField(blank=True)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
