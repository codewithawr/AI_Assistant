import openai
import time

# Set up OpenAI API key
openai.api_key = "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"

# Initialize the conversation history list
conversation_history = []

# Set up OpenAI GPT-3 model
model_engine = "text-davinci-002"
prompt = "Conversation with OpenAI's GPT-3 AI:\n"

# Create function to generate response from GPT-3 model
def generate_response(prompt, model_engine, conversation_history):
    # Concatenate the prompt and conversation history
    conversation_text = prompt + '\n'.join(conversation_history)
    print('-------------------',conversation_text,'-------------------')
    
    # Generate response using GPT-3 model
    response = openai.Completion.create(
        engine=model_engine,
        prompt=conversation_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    return generated_text

# Start the chat loop
while True:
    # Prompt user for input
    user_input = input('You: ')

    # Add user input to conversation history
    conversation_history.append('User: ' + user_input)

    # Generate response using GPT-3 model
    generated_text = generate_response(prompt, model_engine, conversation_history)

    # Add generated text to conversation history
    conversation_history.append('AI: ' + generated_text)

    # Print the AI's response
    print(generated_text)

    # Wait for a second before prompting the user again
    time.sleep(1)


# import openai
# def askGPT(text):
#     openai.api_key = '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'
#     response = openai.Completion.create(
#         engine = 'text-davinci-003',
#         prompt = text,
#         temperature = 0.6,
#         max_tokens = 150,
#     )
#     print('GPT:',response)
#     print('GPT:',response.choices[0].text)

# def main():
#     while True:
#         print('You: ',end='')
#         question = input()
#         askGPT(question)
# main()
'''
Remember i have a meeting tomorrow on 3 pm
Remember to i have a Quize on Monday
Gave me list of events i tolde you to remember 
'''