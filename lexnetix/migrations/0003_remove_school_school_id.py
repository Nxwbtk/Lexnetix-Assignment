# Generated by Django 4.1.5 on 2023-01-19 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexnetix', '0002_alter_teacher_teacher_email_alter_teacher_teacher_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_id',
        ),
    ]