from datetime import datetime

dt_format = "%y%m%d%H%M%S"
dt = "210915120533"

print(datetime.strptime(dt, dt_format).date())

