from datetime import datetime

def time_now(time_now):
    formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
    
    day_of_week = time_now.strftime('%A')
    week_number = time_now.isocalendar()[1]
    
    print(f"Current Date and Time: {formatted_time}")
    print(f"Day of the Week: {day_of_week}")
    print(f"Week Number of the Year: {week_number}")

if __name__ == '__main__':
    current_time = datetime.now()
    time_now(current_time)
