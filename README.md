# playgemma_it_ppo_agents
train a gemma it to make it more suitable for specific task，like summarization、tell joke、coding

1) gemma2 can summarize a ibdb review,use lenght as a rewards,to guide the model to a shorter outpuy
2) gemma2 or some chinese LLM can tell jokes,use like and re as rewards,to guide the model to generate a better joke
3) multi agents can be sfted by other agents' positive sample and guided by self positive sample with rl. this is how human evolved
