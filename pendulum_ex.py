import pendulum

now = pendulum.now("Europe/Paris")

# Changing timezone
now.in_timezone("America/Toronto")

# Default support for common datetime formats
now.to_iso8601_string()

# Shifting
now. add(days=2)

dt = pendulum.datetime(1975, 5, 21)
dt.format('dddd DD MMMM YYYY', locale='de')
'Mittwoch 21 Mai 1975'

dt. format('dddd DD MMMM YYYY')
'Wednesday 21 May 1975'


pendulum.set_locale('en')
print(pendulum.now().add(years=1).diff_for_humans())


# 'it 1 Jahr'
pendulum.set_locale('en')
dt3 = pendulum.now()
print(dt3)
