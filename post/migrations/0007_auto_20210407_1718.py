# Generated by Django 3.1.4 on 2021-04-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_adminpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('i', 'investigation'), ('b', 'back')], max_length=1),
        ),
    ]