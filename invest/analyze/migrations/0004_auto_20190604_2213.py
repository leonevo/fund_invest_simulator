# Generated by Django 2.2.1 on 2019-06-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0003_auto_20190604_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regress_invest',
            name='base_return_rate',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='基础对照回报率'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='end_base_total_value',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=100, null=True, verbose_name='基准对照总市值'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='end_fund_total_value',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=100, null=True, verbose_name='最终基金市值'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='fund_return_rate',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='基金回报率'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='fund_unit',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='基金份额'),
        ),
    ]
