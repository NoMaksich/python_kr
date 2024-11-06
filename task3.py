from datetime import datetime, timedelta

def time_now(time_now, count_day):
    future_time = time_now + timedelta(days=count_day)
    
    formatted_future_time = future_time.strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Resulting Date and Time: {formatted_future_time}")

if __name__ == '__main__':
    current_time = datetime.now()
    count_day = int(input("Введите количество дней от текущей даты: "))
    time_now(current_time, count_day)
