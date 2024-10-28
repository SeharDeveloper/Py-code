#Write a program that calculates BMI (weight in kg / height in m²) based on user input. Then #classify the result:
#BMI < 18.5: "Underweight"
#18.5 ≤ BMI < 24.9: "Normal weight"
#25 ≤ BMI < 29.9: "Overweight"
#BMI ≥ 30: "Obesity"

weight=float(input("Enter your weight in kg:"))
height_cm=float(input("Enter your height in cm:"))
  
#hieght in meters to cm
height_m=height_cm/100
#BMi calaculator
bmi=weight/(height_m**2)
print(f"Your BMI is {bmi:.2f}")
#BMI classification
if bmi<18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi  < 29.9:
    print("Overweight")
else:
    print("Obesity")
