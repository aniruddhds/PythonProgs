class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
def from_seconds(total_seconds):
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return Time(int(hours), int(minutes), int(seconds))

def mul_time(time_obj, number):
    total_seconds = time_obj.to_seconds() * number
    return from_seconds(total_seconds)

def average_pace(finishing_time, distance):
    """Calculate average pace (time per mile).
    finishing_time: Time object representing total race time.
    distance: float or int representing distance in miles.
    Returns a Time object representing average pace per mile."""
    if distance == 0:
        raise ValueError("Distance must be greater than zero")
    pace_seconds = finishing_time.to_seconds() / distance
    return from_seconds(pace_seconds)

h=int(input("Enter finish time hours: "))
m=int(input("Enter finish time minutes: "))
s=int(input("Enter finish time seconds: "))
finish = Time(h,m,s)
distance = int(input("Enter total distance: "))  # miles
pace = average_pace(finish, distance)
print(f"Average pace per mile: {pace}")
double_time = mul_time(finish, 2)
print(f"Double finishing time: {double_time}") 
