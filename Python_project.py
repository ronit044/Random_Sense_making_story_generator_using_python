import random
print(" Personality has\n Power to UPLIFT,\n Power to DEPRESS,\n Power to CURSE,\n And Power to BLESS.")

readersname=input("To get a random story, Please Enter Your Name:\n")
print('Hello, '+readersname)
print("The story goes as follows:")

  
start = ['Somewhere in a big forest, ','About 100 years ago, ', ' In 20th BC, ', 'Once upon a time, ']
name=['Ronit.','Tanishk.','Deepak.','Manjeetva.','Koushik.']
characters = ['there lived a woodcutter, named ',' there was a man, named ','there lived a farmer, named ']
time = [' One day, ', ' One full-moon night, ', ' One fine day, ', ' One fine evening, ']
story_plot = ['he was going to his work towards','he was passing by','he was going for a picnic to']
place = [' the mountains, ', ' the garden, ', ' the city, ']
second_character = [' he saw an old man', ' he saw a lady']
age = [' who seemed to be in late 20s, ', ' who seemed very old and feeble, ']
work = ['sitting idle.','lost in their own world.','searching something.', 'digging a well on roadside.']
  
print(random.choice(start)+random.choice(characters)+random.choice(name)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))
