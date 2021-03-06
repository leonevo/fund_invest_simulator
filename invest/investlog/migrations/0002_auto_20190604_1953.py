# Generated by Django 2.2.1 on 2019-06-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transation_log',
            name='product_code',
            field=models.CharField(max_length=20, verbose_name='产品编码'),
        ),
        migrations.AlterField(
            model_name='transation_log',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='产品名称'),
        ),
        migrations.AlterField(
            model_name='transation_log',
            name='transation_date',
            field=models.DateField(verbose_name='交易日期'),
        ),
    ]
