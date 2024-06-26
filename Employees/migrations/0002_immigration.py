# Generated by Django 4.2.11 on 2024-04-29 07:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immigration',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document_type', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=200)),
                ('issue_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('eligible_review_date', models.DateField()),
                ('document_file', models.FileField(null=True, upload_to='media/employee_immigration_document')),
                ('country', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee')),
            ],
        ),
    ]
