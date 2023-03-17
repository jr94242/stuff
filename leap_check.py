year = int(input("What year do you want to check, lek?\n "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f'{year} is NOT a leap year')
    else:
        print(f"{year} is a leap year")
else:
    print(f"nope, {year} not a leap year")

print("u cool now, homie?")
