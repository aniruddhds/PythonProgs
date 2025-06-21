from __future__ import print_function, division

class Time:
    """Represents the time of day. 
    attributes: hour, minute, second
    """
    def __init__(self, second):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.second = second % 60
        self.minute = (second % 3600)//60
        self.hour = second//3600

    def __str__(self):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time(seconds)
    return time

def main():
    start = Time(35100)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(35100)
    duration = Time(48900)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(27780)
    t2 = Time(27760)
    t3 = Time(27420)
    total = sum([t1, t2, t3])
    print(total)

if __name__ == '__main__':
    main()