# Generated by Django 4.1.5 on 2023-01-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexnetix', '0004_info_member_remove_teacher_teacher_school_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_class',
        ),
        migrations.AddField(
            model_name='member',
            name='classes',
            field=models.ManyToManyField(blank=True, to='lexnetix.classes'),
        ),
    ]
