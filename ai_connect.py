import openai
def askGPT(text):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    print('GPT:',response)
    print('GPT:',response.choices[0].text)

def main():
    while True:
        print('You: ',end='')
        question = input()
        askGPT(question)
main()
'''
Remember i have a meeting tomorrow on 3 pm
Remember to i have a Quize on Monday
Gave me list of events i tolde you to remember 
'''