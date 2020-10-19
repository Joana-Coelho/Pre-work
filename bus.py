#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # Bus
# 
# This bus has a passenger entry and exit control system to monitor the number of occupants it carries and thus detect when there are too many.
# 
# At each stop, the entry and exit of passengers is represented by a tuple consisting of two integer numbers.
# ```
# bus_stop = (in, out)
# ```
# The succession of stops is represented by a list of these tuples.
# ```
# stops = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]
# ```
# 
# ## Tools
# You don't necessarily need to use all the tools. Maybe you opt to use some of them or completely different ones, they are given to help you shape the exercise. Programming exercises can be solved in many different ways.
# * Data structures: **lists, tuples**
# * Loop: **while/for loops**
# * Functions: **min, max, len**
# 
# ## Tasks

# In[22]:


# Variables
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]


# In[ ]:





# In[ ]:





# #### 1. Calculate the number of stops.

# In[23]:


q_stop = len(stops)
print("There are", q_stop, "stops")


# #### 2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out).
# Each item depends on the previous item in the list + in - out.

# In[29]:


in_list = []
out_list = []
passengers_at_each_stop =[]

for i in range(len(stops)):
    passenger_in = stops[i][0]
    in_list.append(passenger_in)
    passenger_out = stops[i][1]
    out_list.append(passenger_out)
for j in range(len(in_list)):
    passenger_stop = in_list[j] - out_list[j]
    passengers_at_each_stop.append(passenger_stop)
    
#print(in_list,out_list)
print(passengers_at_each_stop)


# In[ ]:





# In[ ]:





# #### 3. Find the maximum occupation of the bus.

# In[36]:


stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

my_list = []
number_passengers = ()

for i in range(len(stops)):
    number_passengers += [i][0]
    number_passengers -= [i][1]
    my_list.append(number_passengers)
    
final_value = max(my_list)    
print(my_list)
    
print("The maximum number of people in the bus is:", final_value)


# In[ ]:





# #### 4. Calculate the average occupation. And the standard deviation.

# In[ ]:


#because i couldn't calculate the previous question i didnt solve this one

