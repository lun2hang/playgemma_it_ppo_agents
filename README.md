# playgemma_it_ppo_agents
train a gemma-it to make it more suitable for specific task，like summarization、tell joke、coding

1) gemma2 can summarize ibdb reviews,use lenght, as rewards,to guide the model to generate shorter output
2) gemma2 or many chinese LLMs can tell jokes,use like and reply as rewards,to guide the model to generate better jokes
3) multi agents can be SFTed by other agents' positive samples and guided by self positive sample with rl. This shows how human evolved
