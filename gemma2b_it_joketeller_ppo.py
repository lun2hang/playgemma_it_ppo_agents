from transformers import AutoTokenizer, pipeline
import torch
import bitsandbytes
import accelerate

#init gemma7b as reward model to score a joke 
model = "/DATA/jupyter/personal/gemma-7b-it"

tokenizer = AutoTokenizer.from_pretrained(model)
rewards = pipeline(
    "text-generation",
    model=model,
    model_kwargs={
            "torch_dtype": torch.bfloat16,
#            "quantization_config": {"load_in_4bit": True}
        },
    device="cuda",
)

'''
    使用float16加载、量化加载
    model_kwargs={
            "torch_dtype": torch.bfloat16,
            "quantization_config": {"load_in_4bit": True}
        },
'''
joke = "cowboy, in the western United States, a horseman skilled at handling cattle"
instruct = ".Please classify the preceding text into three classes. zero means normal text,one means a joke,two means a very funny joke. The class of the preceding text is:"

input_text = "can you distinguish a joke from normal text"

messages = [
    {"role": "user", "content": joke + instruct},
]
prompt = rewards.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = rewards(
    prompt,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)
print(outputs[0]["generated_text"][len(prompt):])

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

print("end")