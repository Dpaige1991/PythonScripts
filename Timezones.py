import datetime as dt
import pytz

dt1 = dt.datetime.now()
print(dt1)

dt2 = dt.datetime.now(pytz.utc)
print(dt2)

dt3 = dt.datetime.now(pytz.timezone("Europe/Vienna"))
print(dt3)

datetime_string = "2022-01-01 12:21:33"
datetime_newyork = dt.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")

current_timezone = pytz.timezone("US/Eastern")
target_timezone = pytz.timezone("Europe/Vienna")

localized_newyork = current_timezone.localize(datetime_newyork)
datetime_vienna = localized_newyork.astimezone(target_timezone)

print(datetime_newyork)
print(localized_newyork)
print(datetime_vienna)

print(datetime_vienna.replace(tzinfo=None))
print(datetime_vienna.timetz())

print(pytz.all_timezones)
print(pytz.common_timezones)
print(pytz.country_timezones["US"])