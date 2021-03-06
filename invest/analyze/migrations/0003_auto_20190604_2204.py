# Generated by Django 2.2.1 on 2019-06-04 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0002_regress_invest_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='regress_invest',
            name='base_interest_rate',
            field=models.FloatField(default=0.05, verbose_name='基准对照收益率'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='base_return_rate',
            field=models.FloatField(default=0.06, verbose_name='基础对照回报率'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='each_invest_money',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=100, verbose_name='每次投入金额'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='end_base_total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='基准对照总市值'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='end_fund_total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='最终基金市值'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='fund_return_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='基金回报率'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='fund_unit',
            field=models.FloatField(blank=True, null=True, verbose_name='基金份额'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='invest_days',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='投资时长'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='invest_times',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='投资次数'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='total_interest',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=100, null=True, verbose_name='总收益'),
        ),
        migrations.AddField(
            model_name='regress_invest',
            name='total_principal',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=100, null=True, verbose_name='总投入本金'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='regress_invest',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
    ]
