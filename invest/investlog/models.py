from django.db import models

# Create your models here.


class transation_log(models.Model):
    product_code = models.CharField(max_length=20,verbose_name='产品编码')
    product_name = models.CharField(max_length=50, verbose_name='产品名称')
    transation_date = models.DateField(verbose_name='交易日期')
    TRANSACTION_TYPE_CHOICES = (
        ('SELL', '卖出'),
        ('BUY', '买入'),
        ('PROFITS', '分红'),
    )
    transation_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default='SELL'
    )

