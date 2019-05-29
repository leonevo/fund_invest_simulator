import requests
import json
import re
import pandas as pd

def jsonp2json(jsonp_response):
    j = json.loads(re.findall(r'^\w+\((.*)\)$', jsonp_response)[0])
    print(type(j), j)
    return j


def get_fund_value(fund_code, start_date, end_date):
    url = "http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&page=%d&sdate=%s&edate=%s" % \
          (fund_code, 1, start_date, end_date)
    print(url)
    r = requests.get(url)
    result_str = str(r.content, encoding="utf-8")
    r2 = re.findall('apidata=(.*);', result_str)[0]
    table_str = re.findall('content:"(.*)"', r2)[0]
    records = int(re.findall('records:(\d+),', r2)[0])
    page_count = int(re.findall('pages:(\d+),', r2)[0])
    current_page = int(re.findall('curpage:(\d+)}', r2)[0])

    df = pd.read_html(table_str)[0]
    if page_count > 1:
        for i in range(2, page_count+2):
            url2 = "http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&page=%d&sdate=%s&edate=%s" % \
                   (fund_code, i, start_date, end_date)
            r = requests.get(url)
            result_str = str(r.content, encoding="utf-8")
            r2 = re.findall('apidata=(.*);', result_str)[0]
            table_str = re.findall('content:"(.*)"', r2)[0]
            df_i = pd.read_html(table_str)[0]
            df = df.append(df_i, ignore_index=True)
    return df


if __name__ == '__main__':
    get_fund_value('519069', '2019-05-01', '2019-05-30')
