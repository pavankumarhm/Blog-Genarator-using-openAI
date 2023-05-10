import openai
from dotenv import dotenv_values

# Load the environment variables from the '.env' file
config = dotenv_values('.env')

# Set the OpenAI API key using the environment variable
openai.api_key = config['API_KEY']

# Define a function to generate a blog paragraph
def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        model='text-davinci-003',  # Use the 'text-davinci-003' language model for generating the text
        prompt=f"Write a paragraph about {paragraph_topic}.",
        max_tokens=400,  # Set the maximum number of tokens to generate
        temperature=0.3  # Set the temperature (randomness of response) for generating the text
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog

# Allow the user to generate multiple blog paragraphs
while True:
    answer = input("Write a paragraph? (y/n): ")
    if answer == 'y':
        paragraph_topic = input("What should this paragraph talk about? ")
        print(generate_blog(paragraph_topic))
    else:
        break
