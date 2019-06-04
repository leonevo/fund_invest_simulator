import datetime
import analyze.api as api

def str2date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')


def date2str(date):
    return date.strftime('%Y-%m-%d')


def get_period(start_date_str, end_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
    period = end_date - start_date
    total_days = period.days
    return period


def get_value_by_date_str(fund_value_df, date_str):
    try:
        value = fund_value_df[(fund_value_df.净值日期 == date_str)].iat[0, 2]
    except Exception as e:
        date = str2date(date_str) + datetime.timedelta(days=1)
        return get_value_by_date_str(fund_value_df, date2str(date))
    return value

def get_value_by_date(fund_value_df, date):
    date_str = date2str(date)
    return get_value_by_date_str(fund_value_df, date_str)


if __name__ == '__main__':
    #print(get_period('2014-10-03', '2018-05-12'))
    #print(str2date('2019-08-09'))
    #print(date2str(datetime.datetime.now()))
    df = api.get_fund_value('519069', '2018-05-01', '2019-05-30')
    print(get_value_by_date_str(df, '2018-10-01'))
