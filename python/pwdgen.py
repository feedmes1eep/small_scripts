import os
import string
import random
import pyperclip

length = 12
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

ps = (''.join(random.choice(chars) for i in range(length)))
pyperclip.copy(ps)
print(f'{ps} is copied to your clipboard')
