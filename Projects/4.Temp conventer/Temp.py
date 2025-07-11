unit = input ("Is this temp in in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C':
    temp = round((9*temp)/ 5 +32,1)
    print (f"Tem in Fahrenheit is : {temp}° F")

elif unit == 'F':
    temp = round((temp-32)* 5/9,1)
    print (f"Tem in Celsius is : {temp}° C")

else:
    print ("Choose between C or F")