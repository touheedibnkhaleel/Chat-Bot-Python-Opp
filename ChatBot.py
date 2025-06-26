import random
import time 

class ChatBot:
    def __init__(self,name):
        self.name = name
        self.mood = None
        self.mood_history = []

    def update_mode(self):
        self.mood = random.choice(['Happy','Sad','bored','Angry'])
        self.mood_history.append(self.mood)
        if len(self.mood_history) > 5:
            self.mood_history.pop(0)

    def respond(self,message):
        self.update_mode()
        return f'{self.name} is thinking (Mood: {self.mood}): {message}'
    
    def chat_with_bot(self,other_bot,message):
        for i,msg in enumerate(message):
            if i % 2 == 0:
                response = self.respond(msg)
                print(response)
                time.sleep(2)
            else:
                response = other_bot.respond(msg)
                print(response)
                time.sleep(2)
    
class HappyBot(ChatBot):
    def respond(self, message):
        self.update_mode()
        if self.mood == 'Happy':
            return f'User:{message} \nBot Mood {self.mood}: Yay! I am so happy you said that!😊'
        elif self.mood == 'Sad':
            return f'User:{message} \nBot Mood {self.mood}: I am feeling a little down, but your message cheered me!'
        elif self.mood == 'bored':
            return f'User:{message} \nBot Mood {self.mood}: Hmm... it s quiet, but I am still smiling!'
        elif self.mood == 'Angry':
            return f'User:{message} \nBot Mood {self.mood}: I am not angry, just a little sunshine blocked today! 😤'
        else:
            return 'Invalid Mood'

class SadBot(ChatBot):
    def respond(self, message):
        self.update_mode()
        if self.mood == 'Happy':
            return f'User:{message} \nBot Mood {self.mood}: Well... I guess today isn’t all bad. 😌'
        elif self.mood == 'Sad':
            return f'User:{message} \nBot Mood {self.mood}: It’s one of those days... everything feels gray. 😞'
        elif self.mood == 'bored':
            return f'User:{message} \nBot Mood {self.mood}: Why does everything feel so pointless? 🥱'
        elif self.mood == 'Angry':
            return f'User:{message} \nBot Mood {self.mood}: I hate when no one understands me... 😠'
        else:
            return 'Invalid Mood'

class BooringBot(ChatBot):
    def respond(self, message):
        self.update_mode()
        if self.mood == 'Happy':
            return f'User:{message} \nBot Mood {self.mood}: Cool. Whatever.'
        elif self.mood == 'Sad':
            return f'User:{message} \nBot Mood {self.mood}: Same old stuff. Not that you d care.'
        elif self.mood == 'bored':
            return f'User:{message} \nBot Mood {self.mood}: Yup. Still bored. Surprise. '
        elif self.mood == 'Angry':
            return f'User:{message} \nBot Mood {self.mood}:Don t bother me. Seriously.'
        else:
            return 'Invalid Mood'

class SarcasticBot(ChatBot):
    def respond(self, message):
        self.update_mode()
        if self.mood == 'Happy':
            return f'User:{message} \nBot Mood {self.mood}: Oh wow, you care? I m touched. Really. 🙄'
        elif self.mood == 'Sad':
            return f'User:{message} \nBot Mood {self.mood}: Great. More drama. Love that for me. 😑'
        elif self.mood == 'bored':
            return f'User:{message} \nBot Mood {self.mood}: Please, entertain me. I’m dying from excitement. 😩'
        elif self.mood == 'Angry':
            return f'User:{message} \nBot Mood {self.mood}: Oh joy. Another reason to scream into the void. 😠'
        else:
            return 'Invalid Mood'

alice = ChatBot('Alice')
bob = ChatBot('Bob')
msg = ["Hi there!","Oh, look who finally decided to say hi!","How's your mood today?","Well, I'm pretending to be fine... you?","Do you like pizza?",
       "Only if it’s programmed with extra cheese 😋","Tell me a joke!","My existence is the joke. 😂","Got any secrets?","Yeah... I once liked a human. Ew.",
       "Bye!","Aww... already? 😢"]
alice.chat_with_bot(bob,msg)

call = HappyBot('Sunny')
print(call.respond("What Up?"))
print(call.mood)

print(call.respond("What Up?"))
print(call.mood) 
print(call.respond("What Up?"))
print(call.mood)

print(call.respond("What Up?"))
print(call.mood) 
print(call.respond("What Up?"))
print(call.mood)
print(call.mood_history)


call2 = SadBot('Sunny')

print(call2.respond("What Up?"))
print(call2.mood)

print(call2.respond("What Up?"))
print(call2.mood)

print(call2.respond("What Up?"))
print(call2.mood)
 
print(call2.respond("What Up?"))
print(call2.mood)

print(call2.respond("What Up?"))
print(call2.mood)
print(call2.mood_history)