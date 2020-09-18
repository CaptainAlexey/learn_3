from datetime import date, timedelta, datetime
delta_1 = timedelta(days = 1)
delta_30 = timedelta(days = 30)
dt_now = date.today()
delta_1 = dt_now - delta_1
delta_30 = dt_now - delta_30
dt_now.strftime('%d.%m.%Y')
delta_1.strftime('%d.%m.%Y')
delta_30.strftime('%d.%m.%Y')
print(f'Сегодня {dt_now}, вчера было {delta_1}, 30 дней назад было {delta_30}')

date_string = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)