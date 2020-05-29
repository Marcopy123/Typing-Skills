import random 
import time
from tkinter import *
import tkinter.font as font

root = Tk() # instantiate from class Tk()
root.title('Typing Skills') # set title
root.geometry('1200x500') # set the size of window


accuracy_label = '' 
texts = ''
WPM_label = ''

accuracy = 0
words_scored = 0
WPM = 0

pure_texts = []

fontStyle = font.Font(family = 'Arial', size = 50) # set a font


def retrieve_input(): # make function to retrieve input from user
    inputValue = ''
    inputValue = text_entered.get() # retrieve input
    get_accuracy(words_scored, inputValue) # call get_accuracy
    

with open('typing_skills.rtf', 'r') as file_with_texts: # open the file containing texts
    texts += file_with_texts.read() # add everything in file_with_texts to texts
        

texts = texts.replace('}', '') # replace '}' with nothing

for line in texts.split('|')[1:]: # for each section separated by | after the first one
    pure_texts.append(line) # append to list pure_texts
    

welcome = Label(root, text="Hello And Welcome to \"Test Your Typing Skills!\"",
                font=fontStyle, bg='cyan') # add a welcoming label with a nice font and cyan bg
welcome.pack() # bring it to existance


text_chosen = random.choice(pure_texts) # chose a random text from the pure_texts

text_chosen = text_chosen.replace(',', '').replace('\'',
                         '').replace('\"', '').replace('.', '.\n') # replace all unnecessary things

text = Label(root, text = text_chosen) # add the text they have to type
text.config(font = ("Courier", 15)) # put it in nice font and size
text.pack() # bring it to existance

text_input = StringVar() # define text_input which we will store their input
text_entered = Entry(root, textvariable = text_input, width = 130) # ask for their text
text_entered.pack() # bring the entry to existance


def get_accuracy(words_scored, inputValue): # define function get_accuracy with parameter words_scored
    if inputValue != 0: # if they did not submit button yet
        for input_word, real_word in zip(inputValue.split(),
                                         text_chosen.split()): # for every word in input and every word in text_chosen
            
            if input_word == real_word: # if words match
                words_scored += 1 # increment words_scored
                
    accuracy = words_scored / len(text_chosen.split()) * 100 # calculate accuracy
    accuracy_label = Label(root, text=f"Your accuracy is {round(accuracy)}%") # put output on screen
    accuracy_label.config(font = ("Courier", 20)) # make it in nice font and size
    accuracy_label.place(x = 490,y = 230) # place it directly at a place to overwrite previous accuracy
    get_WPM(WPM,inputValue) # call get_words_per_minute



def get_WPM(WPM, inputValue): # define function taking WPM as parameter
    speed = round(len(str(inputValue).split())/time.perf_counter() * 60) # calculate their words per minute
    WPM = Label(root,
                text = f"Your speed is {speed} words per minute.") # Output their speed
    
    WPM.config(font = ("Courier", 20)) # put it in nice font and size
    WPM.place(x = 390, y = 260) # place it directly at a place to overwrite previous speed
    

submitButton = Button(root, height=1, width=10, text='Submit', command=retrieve_input) # make submit button which uses retrieve_input as command
submitButton.pack() # bring it to existance
    

root.mainloop() # continue looping
    

