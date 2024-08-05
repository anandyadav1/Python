year=int(input("Enter the any year \n"))
if year%400==0:
    print("Thhis is a leap year\n")
elif year%100:
    print("this year is not leap year\n")
elif year%4:
    print("this year is  a leap year\n")
else:
    print("this year is not leap year]n")
    