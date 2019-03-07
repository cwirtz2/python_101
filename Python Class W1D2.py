#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_name="Chris Wirtz"
my_age=32
my_weight=150
my_height=175
my_hair_color="dark brown"
my_eyes_color="hazel"


# In[6]:


my_wt_kg=my_weight*0.453592
my_BMI=my_wt_kg/((my_height/100)**2)
# ** represents 'to the power of'


# In[8]:


print("My name is ",my_name)
print(f"I am {my_height} centimeters tall and weigh {my_weight}")
print(f"My BMI is {my_BMI}")


# In[9]:


print(f"I want to show my BMI in two decimal places {round(my_BMI,2)}")


# In[11]:


print("I am not happy, I want to squareroot my BMI, how do I do that?")


# In[12]:


sqrt(my_BMI)


# In[13]:


import math as mt


# In[14]:


mt.sqrt(my_BMI)


# In[15]:


my_BMI**.5


# In[17]:


round(my_BMI**.5,1)


# # Introduction to conditions if statements
# - If BMI <25 then print not obese, else print obese

# In[21]:


if my_BMI <25:
    print("Not obese")
else:
        print("Obese")


# # Print 'not healthy' when BMI<18, when BMI is between 18 and 25 then print'not obese', and when BMI>25 print 'obese'

# In[28]:


if my_BMI<18:
    print("not healthy")
elif my_BMI>18 and my_BMI<25:
    print("not obese")
else:
    print("obese")
    


# # Ask the system to give a random number - print odd or even

# In[29]:


import random


# In[43]:


print(random.randint(1,6))


# In[31]:


print(random.randint(1,6))


# In[46]:


if (random.randint(1,6)%2) == 0:
    print(random.randint(1,6),"even")
else:
    print(random.randint(1,6),"odd")


# In[53]:


x=random.randint(1,6)
if x%2 > 0:
    print(x,"even")
else:
    print(x,"odd")


# # Randomly select 1-6, spell out each number

# In[52]:


x=random.randint(1,6)
if x==1:
    print(x,"one")
elif x==2:
    print(x,"two")
elif x==3:
    print(x,"three")
elif x==4:
    print(x,"four")
elif x==5:
    print(x,"five")
else:
    print(x,"six")


# In[54]:


range(1,10)


# In[59]:


for i in range(1,11):
    print(i,i+1)


# In[60]:


for i in range(11,1,-1):
    print(i,i+1)


# # Print numbers between 1 and 10 and print odd or even

# In[63]:


for i in range(1,11):
    if i%2 > 0:
        print(i,"odd")
    else:
        print(i,"even")


# # Do all math functions on your phone
# # Print all numbers between 1 and 100 - print odd, even and prime
# # Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# Algorithm
# 1) I need a for statement to print 1 to 101
# 2) Check if i is divisible by 3 (use %) - if true print 'Fizz'
# 3) Check if i is divisible by 5 (use %) - if true print 'Buzz'
# 4) Check if i is divisible by 3 and 5 - if true print 'FizzBuzz'

# In[67]:


for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
   


# In[ ]:




