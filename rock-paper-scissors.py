#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # Rock, Paper & Scissors
# 
# Let's play the famous game against our computer. You can check the rules [here](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors). 
# 
# ## Task
# Create a program that imitates the playability of the well known game of rock, paper, scissors. Follow the guidelines provided.
# 
# ## Tools
# 1. Loop: **for/while**
# 2. Functions: **input(), print()...**
# 3. Conditional statements: **if, elif, else**
# 4. Definition of functions. Modular programming
# 5. Import modules
# 
# **To solve this challenge, the use of functions is recommended.**
# 
# #### 1. Import the choice function of the random module.

# In[ ]:


import random 


# #### 2. Create a list that includes the 3 possible gesture options of the game: 'rock', 'paper' or 'scissors'. Store the list in a variable called `gestures`.

# In[1]:


gestures = ["rock", "paper", "scissors"]


# #### 3. Create a variable called `n_rounds` to store the maximum number of rounds to play in a game. 
# Remember that the number of rounds must be odd: 1, 3, 5, ...

# In[4]:


n_rounds = 3


# In[ ]:





# #### 4. Create a variable called `rounds_to_win` to store the number of rounds that a player must win to win the game.
# **Hint**: the value stored in `rounds_to_win` depends on the value of `n_rounds`. 

# In[6]:


rounds_to_win = int(n_rounds/2 + 1)
print(rounds_to_win)


# In[ ]:





# #### 5. Create two variables to store the number of rounds that the computer and the player have won. Call these variables `cpu_score` and `player_score`.

# In[ ]:


cpu_score = 0
player_score = 0


# #### 6. Define a function that randomly returns one of the 3 gesture options.
# You will use this function to simulate the gesture choice of the computer. 

# In[3]:


import random 

gestures = ["rock", "paper", "scissors"]
random.choice(gestures)


# In[ ]:





# #### 7. Define a function that asks the player which is the gesture he or she wants to show: 'rock', 'paper' or 'scissors'.
# The player should only be allowed to choose one of the 3 gesture options. If the player's choice is not rock, paper or scissors, keep asking until it is.

# In[ ]:


def player_gesture():
    
    choice = input("rock,paper or scissors? Which one do you choose ?")

    while choice not in gestures:
        player_choice = input ("Sorry, that's not an option.\nstone,paper or scissors? ")


# #### 8. Define a function that checks who won a round. 
# The function should return 0 if there is a tie, 1 if the computer wins and 2 if the player wins.

# In[ ]:


if choice == "rock":
    


# #### 9. Define a function that prints the choice of the computer, the choice of the player and a message that announces who won the current round. 
# You should also use this function to update the variables that count the number of rounds that the computer and the player have won. The score of the winner increases by one point. If there is a tie, the score does not increase.

# In[ ]:





# #### 10. Now it's time to code the execution of the game using the functions and variables you defined above. 
# 
# First, create a loop structure that repeats while no player reaches the minimum score necessary to win and the number of rounds is less than the maximum number of rounds to play in a game.  
# 
# Inside the loop, use the functions and variables above to create the execution of a round: ask for the player's choice, generate the random choice of the computer, show the round results, update the scores, etc. 

# In[ ]:





# #### 11. Print the winner of the game based on who won more rounds.
# Remember that the game might be tied. 

# In[ ]:





# # Bonus: Rock, Paper, Scissors, Lizard & Spock
# ![](images/rpsls.jpg)
# 
# In this challenge, you need to improve the previous game by adding two new options. To know more about the rules of the improved version of rock, paper, scissors, check this [link](http://www.samkass.com/theories/RPSSL.html). 
# 
# In addition, you will also need to improve how the game interacts with the player: the number of rounds to play, which must be an odd number, will be requested to the user until a valid number is entered. Define a new function to make that request.
# 
# **Hint**: Try to reuse the code that you already coded in the previous challenge. If your code is efficient, this bonus will only consist of simple modifications to the original game.

# In[ ]:




