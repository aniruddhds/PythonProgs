from datetime import datetime,timedelta

def n_times_older_day(birth1_str, birth2_str, n):

    if n <= 1:
        raise ValueError("n must be greater than 1")

    birth1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    birth2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    # Identify older and younger
    if birth1 < birth2:
        older, younger = birth1, birth2
    else:
        older, younger = birth2, birth1

    age_diff = (younger - older).total_seconds()

    # Formula:
    # t = n * (t - age_diff)
    # t = n*t - n*age_diff
    # n*age_diff = (n-1)*t
    # t = n*age_diff / (n-1)
    t_seconds = n * age_diff / (n - 1)
    n_day_date = older + timedelta(seconds=t_seconds)

    print(f"The day when one is {n} times older than the other: {n_day_date.date()}")

bday1=input("Enter first bday as YYYY-MM-DD: ")
bday2=input("Enter second bday as YYYY-MM-DD: ")
n=int(input("Enter n times: "))
n_times_older_day(bday1, bday2, n)