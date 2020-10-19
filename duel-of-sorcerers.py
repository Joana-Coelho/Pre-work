#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # Duel of Sorcerers
# You are witnessing an epic battle between two powerful sorcerers: Gandalf and Saruman. Each sorcerer has 10 spells of variable power in their mind and they are going to throw them one after the other. The winner of the duel will be the one who wins more of those clashes between spells. Spells are represented as a list of 10 integers whose value equals the power of the spell.
# ```
# gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
# saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
# ```
# For example:
# - The first clash is won by Saruman: 10 against 23.
# - The second clash is won by Saruman: 11 against 66.
# - ...
# 
# You will create two variables, one for each sorcerer, where the sum of clashes won will be stored. Depending on which variable is greater at the end of the duel, you will show one of the following three results on the screen:
# * Gandalf wins
# * Saruman wins
# * Tie
# 
# <img src="images/content_lightning_bolt_big.jpg" width="400">

# ## Tools
# You don't necessarily need to use all the tools. Maybe you opt to use some of them or completely different ones, they are given to help you shape the exercise. Programming exercises can be solved in many different ways.
# 
# 1. Data structures: **lists, dictionaries**
# 2. Loop: **for loop**
# 3. Conditional statements: **if-elif-else**
# 4. Functions: **range(), len(), print()**
# 
# ## Tasks
# 
# #### 1. Create two variables called `gandalf` and `saruman` and assign them the spell power lists. Create a variable called `spells` to store the number of spells that the sorcerers cast. 

# In[1]:


gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]


# In[ ]:





# #### 2. Create two variables called `gandalf_wins` and `saruman_wins`. Set both of them to 0. 
# You will use these variables to count the number of clashes each sorcerer wins. 

# In[10]:


gandalf_wins = 0
saruman_wins = 0
tie = 0


# In[ ]:





# #### 3. Using the lists of spells of both sorcerers, update variables `gandalf_wins` and `saruman_wins` to count the number of times each sorcerer wins a clash. 

# In[11]:


for i in range(len(gandalf)):
    if gandalf[i] > saruman[i]:
        gandalf_wins +=1
    elif gandalf[i] < saruman[i]:
        saruman_wins += 1
    else:
        tie +=1
print(gandalf_wins, saruman_wins,tie)


# In[ ]:





# #### 4. Who won the battle?
# Print `Gandalf wins`, `Saruman wins` or `Tie` depending on the result. 

# In[8]:


if gandalf_wins > saruman_wins:
    if gandalf_wins> tie:
        print("Gandalf wins")
elif saruman_wins > gandalf_wins:
    if saruman_wins > tie:
        print("Saruman wins")
else: 
    ("Tie")


# In[ ]:





# ## Bonus
# 
# In this bonus challenge, you'll need to check the winner of the battle but this time, a sorcerer wins if he succeeds in winning 3 spell clashes in a row.
# 
# Also, the spells now have a name and there is a dictionary that associates that name to a power.
# 
# ```
# POWER = {
#     'Fireball': 50, 
#     'Lightning bolt': 40, 
#     'Magic arrow': 10, 
#     'Black Tentacles': 25, 
#     'Contagion': 45
# }
# 
# gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
#            'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
# saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
#            'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
# ```
# 
# #### 1. Create variables `POWER`, `gandalf` and `saruman` as seen above. Create a variable called `spells` to store the number of spells that the sorcerers cast. 

# In[17]:


power = {'Fireball': 50, 'Lightning bolt': 40, 'Magic arrow': 10, 'Black Tentacles': 25, 'Contagion': 45}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
spells = len(gandalf)


# #### 2. Create two variables called `gandalf_wins` and `saruman_wins`. Set both of them to 0. 

# In[12]:


gandalf_wins = 0
saruman_wins = 0


# In[ ]:





# #### 3. Create two variables called `gandalf_power` and `saruman_power` to store the list of spell powers of each sorcerer.

# In[15]:


gandalf_power = []
saruman_power = []

for i in gandalf: 
    if i not in gandalf_power:
        gandalf_power.append(i)
print(gandalf_power)

for s in saruman:
    if s not in saruman_power:
        saruman_power.append(s)
print(saruman_power)
        

    


# In[ ]:





# #### 4. The battle starts! Using the variables you've created above, code the execution of spell clashes. Remember that a sorcerer wins if he succeeds in winning 3 spell clashes in a row. 
# If a clash ends up in a tie, the counter of wins in a row is not restarted to 0. Remember to print who is the winner of the battle. 

# In[51]:


power = {'Fireball': 50, 'Lightning bolt': 40, 'Magic arrow': 10, 'Black Tentacles': 25, 'Contagion': 45}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
result = []

for i in range(spells):
    
    gandalf_attack = power[gandalf[i]]
    saruman_attack = power[saruman[i]]
    
    if gandalf_attack>saruman_attack:
        a = ["gandalf_win"]
        result.append(a)
    elif gandalf_attack<saruman_attack:
        b = ["saruman_win"]
        result.append(b)
    else:
        c = ["tie"]
        result.append(c)
      
    
for p in range(0,len(result)):
    if result[-p] == result[-p-1] == result[-p-2]:
        if result[-p] == ["gandalf_win"]:
            print ("gandalf_win")
            break
        if result[-p] == ["saruman_win"]:
            print("saruman_win")


# In[ ]:





# #### 5. Find the average spell power of Gandalf and Saruman. 

# In[56]:


gandalf_power= []
saruman_power = []

for gandalf_spell in gandalf:
    
    if gandalf_spell == 'Fireball':
        gandalf_spell = 50
        gandalf_power.append(gandalf_spell)
        
    elif gandalf_spell == 'Lightning bolt':
        gandalf_spell = 40
        gandalf_power.append(gandalf_spell)
    elif gandalf_spell == 'Magic arrow':
        gandalf_spell = 10
        gandalf_power.append(gandalf_spell)
    elif gandalf_spell == 'Black Tentacles':
        gandalf_spell = 25
        gandalf_power.append(gandalf_spell)
    else:
        gandalf_spell = 45
        gandalf_power.append(gandalf_spell)
        
        
for saruman_spell in saruman:
    
    if saruman_spell == 'Fireball':
        saruman_spell = 50
        saruman_power.append(saruman_spell)
        
    elif saruman_spell == 'Lightning bolt':
        saruman_spell = 40
        saruman_power.append(saruman_spell)
    elif saruman_spell == 'Magic arrow':
        saruman_spell = 10
        saruman_power.append(saruman_spell)
    elif saruman_spell == 'Black Tentacles':
        saruman_spell = 25
        saruman_power.append(saruman_spell)
    else:
        saruman_spell = 45
        saruman_power.append(saruman_spell)
        

gandalf_avg_power = round(sum(gandalf_power)/len(gandalf_power),1)
saruman_avg_power = round(sum(saruman_power)/len(saruman_power),1)
print(gandalf_avg_power)
print(saruman_avg_power)


# #### 6. Find the standard deviation of the spell power of Gandalf and Saruman. 

# In[58]:


import statistics
gandalf_std = statistics.stdev(gandalf_power)
saruman_std = statistics.stdev(saruman_power)
print(gandalf_std)
print(saruman_std)

