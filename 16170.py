from datetime import datetime, timedelta

utc_now = datetime.utcnow()

seoul_now = utc_now + timedelta(hours=0)

print(seoul_now.strftime("%Y"))
print(seoul_now.strftime("%m"))
print(seoul_now.strftime("%d"))