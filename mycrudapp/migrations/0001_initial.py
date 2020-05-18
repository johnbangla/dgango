# Generated by Django 3.0.6 on 2020-05-15 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('emp_Code', models.CharField(max_length=20)),
                ('mobile_Number', models.CharField(max_length=20)),
                ('position_Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycrudapp.Position')),
            ],
        ),
    ]
