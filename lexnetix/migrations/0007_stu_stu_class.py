# Generated by Django 4.1.5 on 2023-01-13 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexnetix', '0006_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu',
            name='stu_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lexnetix.classes'),
        ),
    ]
