#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # Temperature Sensor
# 
# There is a temperature sensor in the processor of your company's server. The company wants to analyze the data provided by the sensor to decide if they should change the cooling system for a better one. As changing the cooling system is expensive and you are an excellent data analyst, you can't make a decision without basis.
# 
# ## Tools
# You don't necessarily need to use all the tools. Maybe you opt to use some of them or completely different ones, they are given to help you shape the exercise. Programming exercises can be solved in many different ways.
# 1. Data structures: **lists**
# 2. Loops: **list comprehension**
# 3. Functions: **min, max, print, len**
# 4. Conditional statements: **if-elif-else**
# 
# ## Tasks
# The temperatures measured throughout the 24 hours of a day are:

# In[2]:


temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]


# In[ ]:





# The first element of the list is the temperature at 12am, the second element is the temperature at 1am, and so on. 
# 
# The company has decided that if one of the following events occurs, then the cooling system needs to be replaced for a new one to avoid damaging the processor.
# * More than 4 temperatures are greater than or equal to 70ºC.
# * Any temperature is above 80ºC.
# * The average temperature exceeds 65ºC.
# 
# Follow the steps so that you can make the decision.
# 
# #### 1. Find the minimum temperature of the day and store it in a variable.

# In[4]:


temperature_min = min(temperatures_C)
print(temperature_min)


# In[ ]:





# #### 2. Find the maximum temperature of the day and store it in a variable.

# In[5]:


temperature_max = max(temperatures_C)
print(temperature_max)


# In[ ]:





# #### 3. Create a list with the temperatures that are greater than or equal to 70ºC. Store it in a variable.

# In[13]:


high_temperature = []

for t in temperatures_C:
    if t >= 70:
        high_temperature.append(t)
print(high_temperature)


# In[ ]:





# #### 4. Find the average temperature of the day and store it in a variable.

# In[21]:


temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
denominator = len(temperatures_C)
numerator = sum(temperatures_C)
average = numerator/denominator
print(average)


# In[ ]:





# #### 5. Imagine that there was a sensor failure at 3am and the data for that specific hour was not recorded. How would you estimate the missing value? Replace the current value of the list at 3am for an estimation. 

# In[27]:


#print(temperatures_C)
temperatures_C.pop(3)
#print(temperatures_C)
temperatures_C.insert(3, average)
print(temperatures_C)


# In[ ]:





# #### 6. Bonus: the maintenance staff is from the United States and does not understand the international metric system. Help them by converting the temperatures from Celsius to Fahrenheit.
# To know more about temperature conversion check this [link](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature).
# 
# **Formula**: 
# 
# $F = 1.8 * C + 32$

# In[29]:


temperatures_F = []
for c in temperatures_C:
    f = 1.8*c +32
    f = round(f,2)
    temperatures_F.append(f)
print(temperatures_F)


# In[ ]:





# In[ ]:





# #### 7. Make a decision!
# Now it's time to make a decision taking into account what you have seen until now. 
# 
# Remember that if one of the following events occurs, then the cooling system needs to be replaced for a new one to avoid damaging the processor.
# * More than 4 temperatures are greater than or equal to 70ºC.
# * Any temperature is above 80ºC.
# * The average temperature exceeds 65ºC.
# 
# #### To make your decision, check if any of the three conditions above is met. You might need to use some of the variables you created in steps 1 to 6. Print a message to show if the cooling system needs to be changed or not.

# In[31]:


temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

denominator = len(temperatures_C)
numerator = sum(temperatures_C)
average = numerator/denominator
new_list = []

for t in temperatures_C: 
    
    if t >= 70:
        new_list.append(t)
        if len(new_list) > 4:
            print("Replace the cooling system")
            break
    if t > 80:
        print("Replace the cooling system")
        break
        
    if average > 65:
        print("Replace the cooling system")
        break
 


# In[ ]:





# ## Bonus
# 
# The company has decided that the decision you made is not valid. They want you to analyze the data again but this time, the conditions that need to be met in order to change the cooling system are different.
# 
# This time, if one of the following events occurs, then the cooling system needs to be replaced:
# * The temperature is greater than 70ºC during more than 4 consecutive hours.
# * Any temperature is above 80ºC.
# * The average temperature exceeds 65ºC.
# 
# Follow the steps so that you can make the decision.
# 
# #### 1. Create a list with the hours where the temperature is greater than 70ºC. Store it in a variable.

# In[33]:


superior_temp = []
for s in temperatures_C:
    if s > 70:
        superior_temp.append(s)
print(superior_temp)     


# In[ ]:





# In[ ]:





# #### 2. Check if the list you created in step 1 has more than 4 consecutive hours. 

# In[34]:


len(superior_temp)


# In[ ]:





# #### 3. Make the decision!
# To make your decision, check if any of the three conditions is met. Print a message to show if the cooling system needs to be changed or not.

# In[42]:


superior_temp = []

for temp in temperatures_C:
    if temp > 70:
        superior_temp.append(temp)
        if len(superior_temp) > 4:
            print("Replace the cooling system")
            break
    if temp > 80:
        print("Replace the cooling system")
        break
        
    if average > 65:
        print("Replace the cooling system")
        break


# In[ ]:





# #### 4. Find the average value of the temperature lists (ºC and ºF). What is the relation between both average values?

# In[47]:


temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

denominator_C = len(temperatures_C)
numerator_C = sum(temperatures_C)
temperatures_F = []

for c in temperatures_C:
    f = 1.8*c +32
    f = round(f,2)
    temperatures_F.append(f)
    
average_C = numerator_C/denominator_C

denominator_F = len(temperatures_F)
numerator_F = sum(temperatures_F)
average_F = numerator_F/denominator_F

print(average_C, average_F)

a = average_C*1.8 + 32

a == average_F


# In[ ]:





# #### 5. Find the standard deviation of the temperature lists (ºC and ºF). What is the relation between both standard deviations?

# In[49]:


import statistics
temperature_C_std = statistics.stdev(temperatures_C)
temperature_F_std = statistics.stdev(temperatures_F)
print(temperature_C_std)
print(temperature_F_std)


# In[ ]:




