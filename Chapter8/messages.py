#8-15
#from messages_activity import *

#from messages_activity import show_messages
#from messages_activity import send_messages

#import messages_activity as messages

#import messages_activity

from messages_activity import show_messages, send_messages as show, send

#8-9
lstMessages = ["Text message 1", "Reply message!", "You'll find that this is a message", "Stop texting me your tests..."]

#viewable in messages_activity.py - moved due to exercise 8-15
show(lstMessages)
print()

#8-10
sent_messages = []

#viewable in messages_activity.py - moved due to exercise 8-15
send(lstMessages, sent_messages)
print(lstMessages)
print(sent_messages)


#8-11 -- Please note: the wording on the exercise is confusing to me; I ended up using the slice notation to 
#        execute this, but the wording is funky.

#viewable in messages_activity.py - moved due to exercise 8-15
send(sent_messages[:], lstMessages)
print(lstMessages)
print(sent_messages)