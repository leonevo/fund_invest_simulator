from django.db import models
import django.utils.timezone as timezone
import logging
from analyze.money import investment
import analyze.api as api
import analyze.money_util as money_util


logger = logging.getLogger('analyze')

# Create your models here.

class regress_invest(models.Model):
    fund_code = models.CharField(max_length=20, verbose_name='基金代码')
    fund_name = models.CharField(max_length=20, verbose_name='基金名称')
    start_date = models.DateField(default=timezone.now, verbose_name='开始时间')
    end_date = models.DateField(default=timezone.now, verbose_name='结束时间')
    each_invest_money = models.DecimalField(default=1000, max_digits=100, decimal_places=2, verbose_name='每次投入金额')
    invest_times = models.IntegerField(verbose_name='投资次数', null=True, blank=True)
    invest_days = models.IntegerField(verbose_name='投资时长', null=True, blank=True)
    total_principal = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='总投入本金', null=True, blank=True)
    total_interest = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='总收益', null=True, blank=True)
    base_interest_rate = models.FloatField(verbose_name='基准对照收益率', default=0.05)
    fund_unit = models.FloatField(verbose_name='基金份额', null=True, blank=True)
    fund_return_rate = models.FloatField(verbose_name='基金回报率', null=True, blank=True)
    end_fund_total_value = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='最终基金市值', null=True, blank=True)
    end_base_total_value = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='基准对照总市值', null=True, blank=True)
    base_return_rate = models.FloatField(verbose_name='基础对照回报率', null=True, blank=True)


    def save(self, *args, **kwargs):
        inv = investment(float(self.each_invest_money),
                         str(self.start_date),
                         str(self.end_date),
                         self.fund_code,
                         base_interest_rate=self.base_interest_rate)
        inv.calculate()
        self.invest_times = inv.invest_times
        self.invest_days = (self.end_date - self.start_date).days
        self.total_principal = inv.total_principal
        self.total_interest = inv.total_interest
        self.fund_unit = inv.fund_unit
        self.fund_return_rate = inv.fund_return_rate
        self.end_fund_total_value = inv.end_total_value
        self.end_base_total_value = inv.base_compair_total_value
        self.base_return_rate = inv.base_return_rate

        super(regress_invest, self).save(*args, **kwargs) # Call the "real" save() method.

# signals

