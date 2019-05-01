import datetime
import locale

#Convert to USD Format
def to_usd(value):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
        s = locale.currency(value, grouping=True)
        return s

#Convert Month Code
def month_converter(monthCode):
    full_month = {'1':'January','2':'February','3':'March','4':'April',
    '5':'May','6':'June','7':'July','8':'August','9':'September','10':'October',
    '11':'November', '12':'December'}
    return full_month[monthCode]

#Convert Timestamps
def hf_timestamp(utc_Stamp):
    today = utc_Stamp
    year = str(today.year)
    month = str(today.month)
    month = month_converter(month)
    day = str(today.day)
    hour = str(today.hour)
    minute = str(today.minute)
    today = month + " " + day + ", " + year + " " + hour + ":" + minute
    return today 