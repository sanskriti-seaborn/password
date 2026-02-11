import random
import string
def password_generator(l=8):
  characters = string.ascii_letters + string.digits +'_'
  password = ''.join(random.choice(characters) for i in range(l))
    
  return password

  
