import openai

class davinci_AI:
    def __init__(self) -> None:
        # Set up OpenAI API key
        openai.api_key = "YOUR-API-KEY-FROM-OPENAI" # Go to "https://platform.openai.com/account/api-keys" Create new secret key 

        # Initialize the conversation history list
        self.conversation_history = []

        # Set up OpenAI davinci model
        self.model_engine = "text-davinci-002"
        self.prompt = "Conversation with OpenAI's davinci AI:\n"

    # Create function to generate response from davinci model
    def generate_response(self, prompt, model_engine, conversation_history):
        # Concatenate the prompt and conversation history
        conversation_text = prompt + '\n'.join(conversation_history)
        
        # Generate response using davinci model
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
    def Request_davinci(self, query):
        
        # Add user input to conversation history
        self.conversation_history.append('User: ' + query)

        # Generate response using davinci model
        generated_text = self.generate_response(self.prompt, self.model_engine, self.conversation_history)

        # Add generated text to conversation history
        self.conversation_history.append('AI: ' + generated_text)

        # Print the AI's response
        return generated_text


if __name__ == '__main__':
    question = davinci_AI()
    print(question.Request_davinci('hello'))
    print(question.Request_davinci('Remember i have a meeting tomorrow on 3 pm'))
    print(question.Request_davinci('Remember to i have a Quize on Monday'))
    print(question.Request_davinci('Gave me list of events i tolde you to remember '))
    print(question.conversation_history)
