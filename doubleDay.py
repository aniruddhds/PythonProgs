from datetime import datetime,timedelta

def double_day(birth1_str, birth2_str):
    birth1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    birth2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    # Identify older and younger
    if birth1 < birth2:
        older, younger = birth1, birth2
    else:
        older, younger = birth2, birth1

    age_diff = (younger - older).total_seconds()

    # Double day formula:
    # older_age = 2 * younger_age
    # Let t be time since older's birth in seconds
    # t = 2 * (t - age_diff) => t = 2t - 2*age_diff => t = 2*age_diff
    double_day_seconds = 2 * age_diff
    double_day_date = older + timedelta(seconds=double_day_seconds)

    print(f"Double Day is on: {double_day_date.date()}")

bday1=input("Enter first bday as YYYY-MM-DD: ")
bday2=input("Enter second bday as YYYY-MM-DD: ")
double_day(bday1, bday2)