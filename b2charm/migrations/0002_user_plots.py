# Generated by Django 3.2.5 on 2021-07-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2charm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(max_length=2000)),
                ('img_id', models.UUIDField()),
            ],
        ),
    ]