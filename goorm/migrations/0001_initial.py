# Generated by Django 2.2.7 on 2020-01-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tobacco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(blank=True)),
                ('rel_date', models.DateTimeField(blank=True)),
                ('nicotine', models.FloatField()),
                ('TAR', models.FloatField()),
                ('feel_of_hit', models.CharField(max_length=10)),
                ('score', models.FloatField(default=0)),
                ('isMenthol', models.BooleanField(default=False)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
