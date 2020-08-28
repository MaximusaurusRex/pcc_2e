# def show_messages(texts):
#     for text in texts:
#         print(text)

def send_messages(texts):
    while texts:
        message = texts.pop()
        print(f'Sending message: {message}')
        sent_messages.append(message)


sent_messages = []
texts = ['how are you', 'what day is it today',
         'where am i', 'what is the meaning of life']

send_messages(texts[:])

print(texts)
print(sent_messages)
