import datetime 
import json 

def my_date_handler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not serializable")

test_data = {
    "timestamp": datetime.datetime(2024, 3, 15, 10, 30, 0)
}

result_string = json.dumps(test_data, default=my_date_handler)

print(result_string)