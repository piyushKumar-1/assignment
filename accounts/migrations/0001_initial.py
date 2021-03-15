# Generated by Django 3.1.7 on 2021-03-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_pic', models.URLField(max_length=1000)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
