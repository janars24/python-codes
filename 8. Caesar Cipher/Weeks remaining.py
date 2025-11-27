def life_in_weeks(age):
    print(f"Entered age is {age}")
    remaining_years = 90 - age
    total_weeks = remaining_years * 52
    print(f"You have {total_weeks} weeks left.")


life_in_weeks(27)
life_in_weeks(40)
life_in_weeks(70)