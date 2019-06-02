import api
import enum
import money_util
import datetime
from dateutil.relativedelta import relativedelta

class STRATEGY(enum.Enum):
    EVERY_MONTH = 0
    EVERY_WEEK = 1
    EVERY_2_WEEK= 3


class investment:
    def __init__(self, principal, start_date, end_date, fund_code, strategy=STRATEGY.EVERY_MONTH, base_interest_rate=0.06):
        self.principal = principal #每次投入本金
        self.total_principal = 0 #总投入本金
        self.total_interest = 0 #总收益
        self.start_date = start_date #开始投入时间
        self.end_date = end_date #结束时间
        self.strategy = strategy # 定投按月，按周，按两周
        self.fund_code = fund_code # 基金代码
        self.base_interest_rate = base_interest_rate# 基准收益利率
        self.base_compair_total_value = 0
        self.fund_unit = 0 #基金份额
        self.fund_interest_rate = 1 #　基金收益率
        self.end_total_value = 0
        self.fund_return_rate = 0
        self.base_return_rate = 0

    def calculate(self):
        """
        1. get this time period value for the fund_code
        2. cal
        """
        query_end_date = money_util.str2date(self.end_date) + datetime.timedelta(days=30)
        fund_value_df = api.get_fund_value(fund_code=self.fund_code, start_date=self.start_date, end_date=money_util.date2str(query_end_date))
        invest_peroid = money_util.get_period(self.start_date, self.end_date)

        if self.strategy == STRATEGY.EVERY_MONTH:
            invest_date = money_util.str2date(self.start_date)
            end_date = money_util.str2date(self.end_date)
            invest_times = 0
            base_interest = 0
            while(invest_date < end_date):
                fund_value = money_util.get_value_by_date(fund_value_df, invest_date)
                self.fund_unit = self.fund_unit + self.principal / fund_value
                self.total_principal = self.total_principal + self.principal
                base_interest = base_interest + self.principal * (end_date - invest_date).days * self.base_interest_rate / 360
                invest_date = invest_date + relativedelta(months=1)
                invest_times = invest_times + 1

            self.end_total_value = self.fund_unit * money_util.get_value_by_date(fund_value_df, end_date)
            self.base_compair_total_value = self.total_principal + base_interest
            self.fund_return_rate = (self.end_total_value - self.total_principal) / self.total_principal
            self.base_return_rate = base_interest / self.total_principal

            print("You invest fund %s %d times" % (self.fund_code, invest_times))
            print("Total input: %d" % self.total_principal)
            print("Fund total value: %s, Fund return rate: %s" % (str(self.end_total_value), str(self.fund_return_rate)))
            print("Base value: %s, base return rate: %s" % (str(self.base_compair_total_value), str(self.base_return_rate)))



        elif self.strategy == STRATEGY.EVERY_WEEK:
            pass
        elif self.strategy == STRATEGY.EVERY_2_WEEK:
            pass
        else:
            pass


if __name__ == '__main__':
    start_date = '2014-01-01'
    end_date = '2019-05-01'
    invest1 = investment(1000, start_date, end_date, '519069') #　汇添富价值精选
    invest1.calculate()
    print()
    invest2 = investment(1000, start_date, end_date, '000311') # 沪深300
    invest2.calculate()



