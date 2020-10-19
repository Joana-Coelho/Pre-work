#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left"/>

# # Robin Hood
# Robin Hood has entered a competition to win the archery contest in Sherwood. With his bow and arrows, he needs to shoot on a target and try to hit as close as possible to the center.
# 
# ![](images/arrows.jpg)
# 
# ## Context
# In this challenge, the landing position of arrows shot by archers in the competition will be represented using 2-dimensional coordinates. 
# 
# In the 2-dimensional space, a point can be defined by a pair of values that correspond to the horizontal coordinate (x) and the vertical coordinate (y). For example, in our case, an arrow that hits the center of the archery target will land in position (0, 0) on the coordinate axes. 
# 
# The space can be divided into 4 zones (quadrants): Q1, Q2, Q3, Q4. If a point is in Q1, both its x coordinate and y coordinate are positive. Any point with a null x or y coordinate is considered to not belong to any quadrant. 
# 
# If you want to know more about the cartesian coordinate system, you can check this [link](https://en.wikipedia.org/wiki/Cartesian_coordinate_system). 
# 
# ## Tools
# You don't necessarily need to use all the tools. Maybe you opt to use some of them or completely different ones, they are given to help you shape the exercise. Programming exercises can be solved in many different ways.
# * Data structures: **lists, sets, tuples**
# * Conditional statements: **if-elif-else**
# * Loop: **while/for**
# * Minimum (optional sorting)
# 
# ## Tasks
# Robin Hood has hit the following points:

# In[2]:


points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


# In[ ]:





# #### 1. Robin Hood is famous for hitting an arrow with another arrow. Find the coordinates of the points where an arrow hits another arrow.

# In[3]:


for i,j in points:
    if points[i] == points[j]:
        print(i,j)
        
#why it's nor working?


# In[8]:


perfect= []
for i in range(len(points)):
    if points[i][0] == points[i][1]:
        print(points[i][0], points[i][1])

        


# In[ ]:





# #### 2. Calculate how many arrows have fallen in each quadrant. 
# **Note**: the arrows that fall in the axis (x=0 or y=0) don't belong to any quadrant.

# In[46]:


points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


# In[53]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[34]:



count_quadrandt1 = count_quadrant2 = count_quadrant3 = count_quadrant4 = count_center = 0
for i,j in points:   
  if i > 0 and j > 0:
      count_quadrandt1 +=1
  elif i> 0 and j < 0:
      count_quadrant2 +=1
  elif i < 0 and j < 0:
      count_quadrant3 +=1
  elif i > 0 and j < 0:
      count_quadrant4 +=1
  else:
      count_center +=1
      
print("The first quadrant has "+ str(count_quadrandt1) +" arrows" + "\n" + "The second quadrant has " + str(count_quadrant2) + " arrows" + "\n" + "The third quadrandt has " + str(count_quadrant3) + " arrows" + "\n" + "The fourth quadrant has " + str(count_quadrant4) + " arrows" + "\n" + "The center (0,0) has " + str(count_center) + " arrows")  


# In[ ]:





# In[ ]:





# #### 3. Find the point closest to the center. Calculate its distance to the center. 
# Take into account that there might be more than one point at the minimum distance to the center.
# 
# **Hint**: Use the Euclidean distance. You can find more information about it [here](https://en.wikipedia.org/wiki/Euclidean_distance).  
# **Hint**: Defining a function that calculates the distance to the center can help.

# In[49]:


from math import sqrt 

distance = 100000
x_min = 0
y_min = 0
    
for x,y in points:
    d= x**2 + y**2
    if d < distance:
        distance = d
        x_min = x
        y_min = y 
        
minimum_distance = math.sqrt(x_min**2+y_min**2)        
print("The minimum distance is: ", minimum_distance, "at point: ", x_min, "," ,y_min)


# In[ ]:





# #### 4. If the archery target has a radius of 9, calculate the number of arrows that won't hit the target. 
# **Hint**: Use the function created in step 3. 

# In[54]:


from math import sqrt 

x_new = 9
y_new = 9
count = 0
distance_new =math.sqrt(x_new**2+y_new**2)

for x,y in points:
    d= x**2 + y**2
    if d > distance_new:
        count +=1
print("There are ",count," arrows that don't hit the target")


# In[ ]:




