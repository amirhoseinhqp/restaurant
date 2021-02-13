# Generated by Django 3.1.6 on 2021-02-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20210211_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('DRINKS', 'نوشیدنی ها'), ('DINNER', 'شام'), ('LUNCH', 'ناهار')], default='DRINKS', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
