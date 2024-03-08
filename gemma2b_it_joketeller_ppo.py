#init gemma7b as reward model to score the joke 

#init A Bmodel as PEFT mode for rl


#outer loop

#inner RL loop

#load all models seperatly

#all models generate a joke seperatly,using a random seed

#reward model give all the jokes a score seperatly

#both model AB run a ppo step,and save the generation if reward is bigger than threshhold

#inner rl loop end

#model save checkpoint
#eval

#A model sfted by positive sample from B, vice versa

#model save checkpoint
#eval