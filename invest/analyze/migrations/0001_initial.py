# Generated by Django 2.2.1 on 2019-06-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regress_invest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(max_length=20, verbose_name='基金代码')),
                ('fund_name', models.CharField(max_length=20, verbose_name='基金名称')),
                ('start_date', models.DateField(auto_now=True, verbose_name='开始时间')),
            ],
        ),
    ]