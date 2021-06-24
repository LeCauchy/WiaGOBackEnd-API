# Generated by Django 3.2.4 on 2021-06-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node_R',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=12, unique=True)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=12)),
                ('date_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=12)),
                ('date_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
