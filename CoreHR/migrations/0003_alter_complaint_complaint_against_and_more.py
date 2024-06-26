# Generated by Django 4.2.11 on 2024-05-11 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0009_statutorydeductions_salarypension_overtime_and_more'),
        ('Client', '0001_initial'),
        ('CoreHR', '0002_warning_travel_transfer_termination_resignation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_against',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client'),
        ),
        migrations.AlterField(
            model_name='termination',
            name='termination_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee'),
        ),
        migrations.AlterField(
            model_name='warning',
            name='warning_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee'),
        ),
    ]
