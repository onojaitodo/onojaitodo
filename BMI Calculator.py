# 1) This program will calulate your body mass index to determine you health
print('Hello')
print('We will be calculating your BMI')
myname=input('What is your name: ')
print('Its A Joy To Meet You ' + myname)
height= input('How tall are you (in inches): ')
weight= input('How much do you weigh (in pounds): ')

kg= float(weight)*0.453592
meters= float(height)*0.0254
bmi=float(kg/meters**2)

print('That means your total BMI is ' + str(bmi))
print('A healthy bmi is between 18.5 - 24.9')
above= bmi-24.9
below= 18.5-bmi
if bmi>24.9:
    print('You are ' +str(above) + ' above the healthy average')
if bmi<18.5:
    print('You are ' +str(below) + ' below the healthy average')
if 18.5<= bmi <= 24.9:
    print('Keep it up ' +str(myname)  +'! You are within the healthy range! ')
    
    
    
     
     