def show_messages(messages):
    """simply prints all messages in a list called messages..."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """simulation of sending messages and transferring
    messages to othe list"""
    while messages:
        current_msg = messages.pop()
        print(f"sending message {current_msg}")
        sent_messages.append(current_msg)

messages = ["Hii", "Hello", "How are you?", "Hey!, what's up!"]
sent_messages = []

send_messages(messages, sent_messages)

#cheking whether all messages transferred from messages[] to sent_messages[]...
print(messages)
print(sent_messages)










