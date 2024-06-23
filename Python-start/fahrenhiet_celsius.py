def fahrenhiet_to_celsius(temp):
    temp_cel = (temp-32) * 5 / 9
    return temp_cel
def celsius_to_fahrenhiet(temp):
    temp_far = (temp*9)/5+32
    return temp_far
print("Which conversion would you like to perform?")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choise = input("Choise: ")
choise_Str = ""
if choise == "1":
    choise_Str = "Celsuis"
    
else:
    choise_Str = "Fahrenhiet"
print("Enter the temprature in ", choise_Str)
temprature = int(input())
if choise == "1":
    temprature_Wanted = celsius_to_fahrenhiet(temprature)
    print(f"{temprature}C is {temprature_Wanted}F")
else:
    temprature_Wanted = fahrenhiet_to_celsius(temprature)
    print(f"{temprature}F is {temprature_Wanted}C")