#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(brd_lst):
    clear_output()
    print(brd_lst[7]+'|'+brd_lst[8]+'|'+brd_lst[9])
    print('-'+'-'+'-'+'-'+'-')
    print(brd_lst[4]+'|'+brd_lst[5]+'|'+brd_lst[6])
    print('-'+'-'+'-'+'-'+'-')
    print(brd_lst[1]+'|'+brd_lst[2]+'|'+brd_lst[3])
    


# In[2]:


test_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)


# In[3]:


def player_input():
    player1_marker='b'
    player2_marker='c'
    while player1_marker not in ['x','X','o','O']:
        
        player1_marker=input('Enter your marker player 1 X or O:  ')
    
    player1_marker=player1_marker.upper()
    if player1_marker== 'X':
        player2_marker='O'
    else:
        player2_marker='X'
        
    return (player1_marker,player2_marker)
    


# In[4]:


def place_marker(board,marker,position):
    board[position]=marker
    return board

    


# In[5]:


#place_marker(test_board,'X',4)


# In[6]:


def win_check(board,marker):
    for n in range(1,10):
        if board[n]==board[n+1]==board[n+2]==marker:
             return True
            
        elif board[n]==board[n+3]==board[n+6]==marker:
            return True
            
        elif board[1]==board[5]==board[9]==marker or board[3]==board[5]==board[7]==marker:
            
            return True
            
            
    ##if board[1]==board[2]==board[3]==marker:
         ##print(f'{marker} wins')
     ##elif board[1]==board[4]==board[7]==marker:
        ## print(f'{marker} wins')
     ##elif board[1]==board[5]==board[9]==marker:
         ##print(f'{marker} wins')
     ##elif board[1]==board[5]==board[9]==marker:
    


# In[7]:


import random
def choose_firstplayer():
    
    
    k=random.randint(0,1)
    if k==1:
        return 'Player 1'
    if k==0:
        return 'Player 2'
        
    


# In[8]:


choose_firstplayer()


# In[9]:


def space_check(board,position):
    return board[position]==' '
        


# In[10]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[11]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
    
        
        


# In[12]:


def replay():
    rply=input("Do you want to play again? Y/N ")
    if rply.upper()=='Y':
        return True


# In[13]:



clear_output()
print('tic tac toe')
while True:
    theboard=[' ']*16
    player_1_m,player_2_m=player_input()
    print(player_1_m,player_2_m)
    turn=choose_firstplayer()
    print(turn+"  will go first ")
    game_on=True
    while game_on:
        
        if turn=='Player 1':
            
            
            
            
            #display_board(theboard)
               
            position=player_choice(theboard)
            place_marker(theboard,player_1_m,position)
            display_board(theboard)
            
            if win_check(theboard,player_1_m):
                print('\n 1 win')
                break
            elif full_board_check(theboard):
                print('\n draw')
                break

            else:
                
                turn='Player 2'
                
                
        if turn=='Player 2':
            
            
            #display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard,player_2_m,position)
            display_board(theboard)
            if win_check(theboard,player_2_m):
                print('\n 2 win')
                break
            elif full_board_check(theboard):
                print('\n draw')
                break
            
            else:
                
                turn='Player 1'
    #display_board(theboard)            
    if not replay():
        break


# In[ ]:





# In[14]:


#k,m=player_input()


# In[15]:


#k


# In[16]:


#m


# In[ ]:




