# Generated by Django 4.1.5 on 2023-01-19 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexnetix', '0003_remove_school_school_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_id', models.CharField(blank=True, max_length=5, null=True)),
                ('info_name', models.CharField(max_length=100)),
                ('info_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('info_email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_role', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_school',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='class_teacher',
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='member',
            name='member_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lexnetix.classes'),
        ),
        migrations.AddField(
            model_name='member',
            name='member_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lexnetix.info'),
        ),
        migrations.AddField(
            model_name='member',
            name='member_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexnetix.school'),
        ),
    ]
