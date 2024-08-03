import random as r
import string as str
def generate():
  print('---Password Generator---')
  #we are taking input from the user that is password length
  print('enter the length of the password')
  pswd= "" #empty password
  len=input()
  len=int(len)
  sml=str.ascii_lowercase
  cap=str.ascii_uppercase
  digit=str.digits
  sym=str.punctuation
  final=sml + cap + digit +sym
  # now we are going to generate the final password with all combinations 
  for i in range(len):
    pswd += r.choice(final)
  print("PASSWORD GENERATED:",pswd);
generate()
