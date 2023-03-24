import numpy as np 
import random

#HU
#03.2023

number_of_coin_flip=50 # the number of times a coin is tossed
number_of_trials=10000 # the number of tossed process 

def coin_flip(n): # one coin flip 50 times

    results_of_flips=[]   
    
    for i in range(n):
        random_side_of_coin=random.randint(0,1) 
        
        if random_side_of_coin == 0:
   
            results_of_flips.append('T') # 0 represent TAIL
        else :
  
            results_of_flips.append('H') # 1 represent HEAD
        
    
    return results_of_flips


def longest_run(fliped_coins_data,condition1='T',condition2='H'):
    
    current_longest_run=[0,0] # create empty array 
    max_longest_run =[0,0]    # create empty array

    for i in range (len(fliped_coins_data)):# looking for Tails and find max length 
  
        if (fliped_coins_data[i] == 'T'):
       
                current_longest_run[0]+=1
               
                if(current_longest_run[0]>max_longest_run[0]):
                    max_longest_run[0]=current_longest_run[0]
                    
        else: 
            current_longest_run[0]=0
            
    
    for i in range (len(fliped_coins_data)): # after looking for Heads and find max length 
 
        if (fliped_coins_data[i] == 'H'):
             
                current_longest_run[1]+=1
           
                if(current_longest_run[1]>max_longest_run[1]):
                    max_longest_run[1]=current_longest_run[1]
                    
        else: 
            current_longest_run[1]=0
                
            
    return max([max_longest_run[0],max_longest_run[1]]) # return max value of longest run
                                                        # max_longest_run array contains Tail longest run value in index 0 
                                                        # max_longest_run array contains Head longest run value in index 1 
    
    
def trials_10k(): # one join flip 50 times and that process run 10k times
                  # process calculate longest run of every 50 coin
    
    results_of_trials=[] 
    for i in range(number_of_trials):
        results_of_trials.append(longest_run(coin_flip(number_of_coin_flip)))
        ## first coin_flip function invoke and its data is given longest_run function to calculate longest run 
        ## after these process repeated as many times as number_of_trial
    return results_of_trials


def calc_prob_of_run_8_more(array_of_trials,n):# probability is find by using iteration 
    
    number_of_8_or_more=0
    
    for i in range(n):
        
        if array_of_trials[i]>=8:
            number_of_8_or_more+=1
            
    return number_of_8_or_more/n
        


probability_of_process=calc_prob_of_run_8_more(trials_10k(),number_of_trials)

print('When you throw a coin 50 times and do this process 10000 times')
print('the probability of the longest runes being greater than 8 is shown below.')
print('\nProbability: ',probability_of_process)
