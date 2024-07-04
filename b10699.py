from datetime import datetime, timedelta

utc_now = datetime.utcnow()

seoul_now = utc_now + timedelta(hours=9)

formatted_date = seoul_now.strftime("%Y-%m-%d")
print(formatted_date)