# Generated by Django 3.1.1 on 2020-09-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200905_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='askqua',
            name='status',
            field=models.CharField(choices=[('imp', 'imp'), ('spirua', 'spirua'), ('to join', 'to join')], max_length=200, null=True),
        ),
    ]