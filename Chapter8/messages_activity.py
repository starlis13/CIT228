#8-15
def show_messages(msgs):
    for msg in msgs:
        print(msg)
        
def send_messages(messagesToBeSent, messagesSent):
    msgIndex = 0
    while len(messagesToBeSent) > 0:
        currentMessage = messagesToBeSent[msgIndex]
        
        print(currentMessage)
        messagesSent.append(currentMessage)
        messagesToBeSent.remove(currentMessage)