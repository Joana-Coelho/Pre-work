#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # The Snail and the Well
# 
# A snail falls at the bottom of a 125 cm well. Each day the snail rises 30 cm. But at night, while sleeping, slides 20 cm because the walls are wet. How many days does it take for the snail to escape the well?
# 
# **Hint**: The snail gets out of the well when it surpasses the 125cm of height.
# 
# ## Tools
# 
# 1. Loop: **while**
# 2. Conditional statements: **if-else**
# 3. Function: **print()**
# 
# ## Tasks
# 
# #### 1. Assign the challenge data to variables with representative names: `well_height`, `daily_distance`, `nightly_distance` and `snail_position`.

# In[16]:


well_height = 125
daily_distance = 30 
nightly_distance = 20
snail_position = daily_distance-nightly_distance
print(snail_position)


# #### 2. Create a variable `days` to keep count of the days that pass until the snail escapes the well. 

# In[23]:


day = 0


# In[ ]:





# In[ ]:





# #### 3. Find the solution to the challenge using the variables defined above. 

# In[33]:


end_position = 0
day = 0
while end_position < well_height:
    day +=1
    end_position = snail_position*day
    print("the day is:", day, "the position is:",end_position)
    
print(day)


# In[ ]:





# #### 4. Print the solution.

# In[34]:


print(day)


# In[ ]:





# ## Bonus
# The distance traveled by the snail each day is now defined by a list.
# ```
# advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
# ```
# On the first day, the snail rises 30cm but during the night it slides 20cm. On the second day, the snail rises 21cm but during the night it slides 20cm, and so on. 
# 
# #### 1. How many days does it take for the snail to escape the well?
# Follow the same guidelines as in the previous challenge.
# 
# **Hint**: Remember that the snail gets out of the well when it surpasses the 125cm of height.

# In[46]:


advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
night_slide = 20
day = 0
overall_up = 0
objective = 125

for i in advance_cm:
    if overall_up > objective:
        print(day)
        break
    else:
        daily_up = i -night_slide
        overall_up += daily_up
        day += 1
        print("on day :", day, "the snake whent up:", daily_up, "already climbed:",overall_up)


# #### 2. What is its maximum displacement in one day? And its minimum? Calculate the displacement using only the travel distance of the days used to get out of the well. 
# **Hint**: Remember that displacement means the total distance risen taking into account that the snail slides at night.  

# In[55]:


night_slide = 20
day = 0
overall_up = 0
objective = 125
overall_up_list = []
for i in advance_cm:
    if overall_up > objective:
        break
    else:
        daily_up = i -night_slide
        overall_up += daily_up
        overall_up_list.append(daily_up)
        day += 1
        

maxi_displacement = max(overall_up_list)
min_displacement= min(overall_up_list)
print("the maximum displacement in one day is", maxi_displacement, "cm and the minimum is", min_displacement, "cm")


# In[ ]:





# #### 3. What is its average progress? Take into account the snail slides at night.

# In[62]:



a= 0
for i in overall_up_list:
    a +=i
average = a/day
print(round(average,1))


# #### 4. What is the standard deviation of its displacement? Take into account the snail slides at night.

# In[67]:


import statistics 
statistics.stdev(overall_up_list)


# In[ ]:




