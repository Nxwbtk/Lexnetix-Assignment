# Generated by Django 4.1.5 on 2023-01-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexnetix', '0007_alter_member_member_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='classes',
        ),
    ]