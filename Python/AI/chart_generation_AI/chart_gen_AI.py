import re # Python’s regular expression module, which you’ll use to extract snippets of code or structured text from the LLM’s output.
import json #Provides functions to read and write JSON, useful for handling structured responses returned by the LLM.

# Local helper module
import utils #A custom helper module provided for this lab. 
             #It includes utility functions to work with the dataset, generate charts, and display results in a clean, readable format.

#Loading dataset
df = utils.load_and_prepare_data('coffee_sales.csv')
# Grab a random sample to display
utils.print_html(df.sample(n=5), title="Random Sample of Coffee Sales Data")

'''Building pipeline:
1: prompt LLMs to write python code to generate a chart in response to a user query about coffee dataset
The dataset includes fields such as date, coffee_type, quantity, and revenue, and you will pass this schema into the LLM so it knows what data is available.
'''

def generate_chart_code(instructions:str, models: str, out_path_v1: str) -> str:
    #prompt is to tell AI instruction and what should follow, then pass it to LLM
    prompt = f"""            
    You are a data visualization expert.

    Return your answer *strictly* in this format:

    <execute_python>
    # valid python code here
    </execute_python>

    Do not add explanations, only the tags and the code.

    The code should create a visualization from a DataFrame 'df' with these columns:
    - date (M/D/YY)
    - time (HH:MM)
    - cash_type (card or cash)
    - card (string)
    - price (number)
    - coffee_name (string)
    - quarter (1-4)
    - month (1-12)
    - year (YYYY)

    User instruction: {instruction}

    Requirements for the code:
    1. Assume the DataFrame is already loaded as 'df'.
    2. Use matplotlib for plotting.
    3. Add clear title, axis labels, and legend if needed.
    4. Save the figure as '{out_path_v1}' with dpi=300.
    5. Do not call plt.show().
    6. Close all plots with plt.close().
    7. Add all necessary import python statements

    Return ONLY the code wrapped in <execute_python> tags.
    """
    
    response = utils.get_response(model, prompt)
    return response.strip()


code_v1 = generate_chart_code(
    instruction="Create a plot comparing Q1 coffee sales in 2024 and 2025 using the data in coffee_sales.csv.", 
    model="gpt-4o-mini", 
    out_path_v1="chart_v1.png"
)

utils.print_html(code_v1, title="LLM output with first draft code")