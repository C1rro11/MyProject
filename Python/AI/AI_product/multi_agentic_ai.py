import os
import aisuite as ai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Configure OpenAI provider to use DeepSeek's API
os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
client = ai.Client()

model_name = "<h3> Your model version<3>"

prompt = f"""
    you are a helpful and kindly idea assistant. please follow the rules and generate a random new product idea.

    rules:
    1: you are a helpful and kindly idea assistant. generate the idea for the product.
    2: dont be impolite or rude. be polite and friendly to the user.
    3: be concise and to the point. dont be too verbose.
    4: be creative and think outside the box.
    5: be realistic and practical.
    6: be unique and innovative.
    7: be relevant and useful.
    8: be easy to understand and follow.
    9: be easy to implement and execute.
    10: be easy to maintain and update.

    output:  follow the format below
    - first talk about what is you model : {model_name}
    - a name of the product
    - a short description of the product
    - a list of features of the product
    - example of the product use case
    - how much will be the product price in the market
"""

response = client.chat.completions.create(
    model="deepseek:deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": prompt 
        }
    ],
    temperature= 1.0
)

prompt_ = response.choices[0].message.content
print(prompt_)

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
model_name_2 = "moonshotai/Kimi-K2.5:novita"
prompt_2 = f"""
 you are good summarizer, please summarize the response from the user.


 output: follow the format below:
 - first talk about what is you model : {model_name_2}
 - name of the product: 
 - 2-3 sentences description of the product
 - and summary of the prompt.
"""

response_2 = client.chat.completions.create(

    model= "huggingface:moonshotai/Kimi-K2.5:novita",
    messages=[
        {"role": "system","content": prompt_2},
        {"role": "user","content": prompt_}
    ],
    max_tokens= 1000
)

print(response_2.choices[0].message.content)