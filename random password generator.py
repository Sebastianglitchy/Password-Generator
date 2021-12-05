import random

#this shuffles the password

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

lowercaseLetter1=chr(random.randint(97,122)) #This is sebastian speaking and says this makes a lower case letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #This is sebastian speaking and says this makes a lower case letter (based on ASCII code)

digit1=chr(random.randint(48,57)) #this makes random numbers, btw this is still sebastian
digit2=chr(random.randint(48,57)) #this makes random numbers, btw this is still sebastian

puntuationSign1=chr(random.randint(33,47)) #this makes a random punctuation, btw this is still sebastian, again
puntuationSign2=chr(random.randint(33,47)) #this makes a random punctuation, btw this is still sebastian, again

#this mkaes the random things above come together

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + puntuationSign1 + puntuationSign2
password = shuffle(password)

#this is the output (the password)

print("This is your now your Password, " + password)
