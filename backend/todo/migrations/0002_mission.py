# Generated by Django 4.1.5 on 2023-01-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_dep', models.DateField()),
                ('date_dest', models.DateField()),
                ('Ref_Rem', models.CharField(max_length=20)),
                ('chauf_ref', models.CharField(max_length=15)),
                ('Ref_Track', models.CharField(max_length=20)),
            ],
        ),
    ]
