import openai

class GPT_AI:
    def __init__(self) -> None:
        # Set up OpenAI API key
        openai.api_key = "YOUR-API-KEY-FROM-OPENAI" # Go to "https://platform.openai.com/account/api-keys" Create new secret key 

        # Initialize the conversation history list
        self.conversation_history = []

        # Set up OpenAI GPT-3 model
        self.model_engine = "text-davinci-002"
        self.prompt = "Conversation with OpenAI's GPT-3 AI:\n"

    # Create function to generate response from GPT-3 model
    def generate_response(self, prompt, model_engine, conversation_history):
        # Concatenate the prompt and conversation history
        conversation_text = prompt + '\n'.join(conversation_history)
        
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
    def GPT_Request(self, query):
        
        # Add user input to conversation history
        self.conversation_history.append('User: ' + query)

        # Generate response using GPT-3 model
        generated_text = self.generate_response(self.prompt, self.model_engine, self.conversation_history)

        # Add generated text to conversation history
        self.conversation_history.append('AI: ' + generated_text)

        # Print the AI's response
        return generated_text


if __name__ == '__main__':
    question = GPT_AI()
    print(question.GPT_Request('hello'))
    print(question.GPT_Request('Remember i have a meeting tomorrow on 3 pm'))
    print(question.GPT_Request('Remember to i have a Quize on Monday'))
    print(question.GPT_Request('Gave me list of events i tolde you to remember '))
    print(question.conversation_history)
