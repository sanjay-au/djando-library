# Generated by Django 5.0 on 2024-01-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pdf', models.FileField(upload_to='book/pdf')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='book/image')),
            ],
        ),
    ]
