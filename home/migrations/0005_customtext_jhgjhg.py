# Generated by Django 2.2.14 on 2020-07-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_customtext_jhgjhg'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='jhgjhg',
            field=models.GenericIPAddressField(blank=True, null=True, unpack_ipv4=True),
        ),
    ]
