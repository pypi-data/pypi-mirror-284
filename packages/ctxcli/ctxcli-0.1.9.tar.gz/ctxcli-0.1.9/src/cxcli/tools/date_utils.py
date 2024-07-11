import datetime
import sys

def validate_date_range(start_date, end_date):
    date_difference = (end_date - start_date).days

    if date_difference > 30:
        print("Error: Date range exceeds 30 days.")
        sys.exit(1)
        
        
def transform_dates(start_date, end_date):    
    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    start_datetime = start_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    end_datetime = end_datetime.replace(hour=23, minute=59, second=59, microsecond=0)
    
    validate_date_range(start_datetime, end_datetime)

    start_iso = start_datetime.isoformat() + "Z"
    end_iso = end_datetime.isoformat() + "Z"

    return start_iso, end_iso