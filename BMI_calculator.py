import streamlit as st
>>> w = float(input('Enter your Weight (in Kg) :'))
... h = float(input('Enter your Height (in Cm):'))
... 
... BMI = (w / (h**2*10**-4))
... print("Your Body Mass Index (BMI) is :",BMI))
... 
... if BMI<18.5:
...   print('You are Underweight')
... 
... elif 18.5<=BMI<=24.9:
...   print('You are Normal weight')
... 
... elif 25<=BMI<=29.9:
...   print('You are Over weight')
... 
... elif 30<=BMI<=39.9:
...   print('You are Obese')
... 
... else:
      Print('You are extramely obese')


