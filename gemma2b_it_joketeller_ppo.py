#init gemma7b as reward model to score a joke 

#init both A B model as PEFT mode for rl

#outer loop

#inner RL loop

#load all models seperatly

#all models generate a joke seperatly,using a different random seed

#reward model give all the jokes a score seperatly

#both model A B run a PPO step,and save the generation as positive sample if reward is bigger than threshhold

#inner rl loop end

#model save checkpoint
#evaluate with reward model

#A model sfted by positive sample from B, vice versa

#model save checkpoint
#eval with reward model

#end outer loop