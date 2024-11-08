# Generated by Django 5.1.2 on 2024-10-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_type_pet_pet_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petsitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('contact', models.IntegerField()),
                ('start_data', models.DateField(blank=True, null=True)),
                ('End_data', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='Available', max_length=100)),
            ],
        ),
    ]
