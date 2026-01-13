#Program HW 1
import functools
Word_Dictionary = { #Library of possible english words, Manual Segmentation, May not contain all english words
    "I", "YOU", "HE", "SHE", "WE", "THEY", "ME", "MY", "YOUR", "HIS", "HER", "OUR", "THEIR",
    "IT", "THIS", "THAT", "THE", "A", "AN",
    "AM", "IS", "ARE", "WAS", "WERE", "BE", "BEEN", "BEING",
    "HAVE", "HAS", "HAD", "DO", "DOES", "DID",
    "GO", "GOES", "WENT", "COME", "CAME", "MAKE", "MADE", "TAKE", "TOOK",
    "PLAY", "PLAYED", "PLAYING", "SEE", "SAW", "LOOK", "LOOKED", "LOOKING",
    "RUN", "RAN", "WALK", "WALKED", "SIT", "SAT", "STAND", "STOOD",
    "EAT", "ATE", "DRINK", "DRANK", "SLEEP", "SLEPT", "TALK", "TALKED", "SAY", "SAID",
    "MEET", "MET", "FIND", "FOUND", "ASK", "ASKED", "HELP", "HELPED", "LEARN", "LEARNED", "LEARNING",
    "AT", "TO", "FROM", "IN", "ON", "WITH", "BY", "FOR", "OF", "ABOUT", "OVER", "UNDER",
    "AND", "OR", "BUT", "IF", "THEN", "SO", "BECAUSE", "WHILE", "WHEN", "RANDOM",
    "HOME", "SCHOOL", "PARK", "STREET", "HOUSE", "ROOM", "CLASS", "OFFICE", "SHOP", "CITY",
    "APPLE", "BANANA", "BOOK", "PEN", "TABLE", "CHAIR", "CAR", "DOG", "CAT", "FRIEND", "FAMILY","MEAT",
    "PHONE", "COMPUTER", "FOOD", "WATER", "DRINK", "GAME", "MOVIE", "MUSIC", "FUN", "TOY", "BALL",
    "GOOD", "FAST", "SLOW", "HAPPY", "SAD", "BIG", "SMALL", "NEW", "OLD", "YOUNG", "LONG", "SHORT",
    "HELLO", "HI", "THANK", "PLEASE", "YES", "NO", "WELCOME", "SORRY", "CONGRATULATIONS"
}
def segment_word (input_text):#Function to segment the input string to valid english words 
    #Recursion Prioritizes Longest Valid Prefix First
    if input_text == "": #If input is empty return an empty list
        return []
    W_len=len(input_text) #Get the length of the Input String
    for i in range(1,W_len+1):
        prefix=input_text[0:i] # Take the substring from the start up to index i, This is the current prefix
        rem=input_text[i:] #Remaining substring from index i to the end
        if prefix in Word_Dictionary : #Check if the word can be found in the dictionary
          result=segment_word(rem) #Do recursion and check the remaining substring
          if result is not None: #Check if the remaining string can be successfully segmented
            return [prefix]+result # Combine the current word with the recursively segmented remainder
    return None
textInput=input().strip() #Take Input and remove any leading or trailing whitespace
if not textInput.isupper() or not textInput.isalpha(): #If the input is not Uppercase Letters or an alphabet
    print("Nonsense") #Print Nonsense
    exit() #End the Program
res=segment_word(textInput) #Insert the input to the segment word function
if res is None: #If the result of segment_word function is None
    print("Nonsense") #Print Nonsense
else:
   print(" ".join(res)) #Else print the segmented words separated by spaces

            
      
