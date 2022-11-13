print("How Fat Are You?!")

w = float(input("Please State your Weight (kg): "))
h = float(input("Please State your Height (m): "))

bmi = round(w/h**2,2)

if bmi < 18.5:
    print(bmi, "Underweight : You need to gain some weight")
elif bmi >= 18.5 and bmi <= 24.9:
    print(bmi, "Normal Weight : You are Alright")
elif bmi >= 25 and bmi <= 29.9:
    print(bmi, "Overweight : You need to lose a little weight")
elif bmi >= 30 and bmi <= 34.9:
    print(bmi, "Obesity : You need to lose weight or else you would have a hard life")
elif bmi >= 35:
    print(bmi, "Extreme Obesity : You are FAT and for losing weight you can get money from Insurance. Live healthy")
    