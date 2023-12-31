# Generated by Django 4.2.3 on 2023-07-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('dimensions', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
