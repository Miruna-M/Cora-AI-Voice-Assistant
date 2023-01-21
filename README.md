# Virtual-AI-Voice-Assistant
This is a python program that uses PyAudio to follow voice commands and converse with the user in return. It is an Artificial Intelligence program that takes in the user's voice command as an audio file, transcribes it in text, then responds back both through audio and in text. The program adjusts for ambient noise, then listens for the user's commands. 

It can respond to the following commands: 

1. **Name**\
   When asked, the program can tell the user its name, and if the user's name has not already been provided, it will ask for the user's name. Once the user provides    their name, the program remembers it to be used in further conversation.
  
2. **Greeting**\
   The program can respond to a verbal greeting from the user.
  
3. **Search Youtube**\
   Upon verbal request, the program can open Youtube and search whatever the user tells it to.
  
4. **Search Google**\
   Upon verbal request, the program can open Google and search whatever the user tells it to.
   
5. **Weather**\
   When the user asks for weather, the program can present the local forecast.
   
6. **Location**\
   When the user asks for their location, the program can show their location on Google Maps.
   
7. **Definition**\
   When the user asks for the definition of a word, the program presents all possible definitions sourced from Wikipedia. If there are no definitions listed on          Wikipedia, the program tells the user to try a web search.
   
8. **Time**\
   Upon verbal request, the program can tell the user the current local time.
   
9. **Calculator**\
   Upon verbal request of any mathematical operation (plus, minus, multiply, divide, power), the program performs the requested operation(s) and says the answer.
   
10. **Screenshot**\
    Upon verbal request, the program takes a scrrenshot of the current screen and saves it as a png.
    
11. **Play Music**\
    Upon verbal request, the program can play music that is downloaded on the PC.
    
12. **Stop Music**\
    Upon verbal request, the program can stop the music playing.
    
13. **Empty Recycle Bin**\
    Upon verbal request, the program can empty the Recycle Bin on the PC, and then update the user that it has been emptied.
    
14. **Clean Up Directory**\
    When the user verbally requests the program to clean up directory, the program asks the user to provide a directory path, then it performs the requested function     and updates the user that the directory has been cleaned.
    
15. **Play Rock Paper Scissors**\
    When the user verbally requests a game, the program plays a game of rock paper scissors. The program randomly chooses one of the three choices, then prompts the     user to do the same. Then, if both the user and the program chose the same option, the program considers it a tie. In any other situation, the program informs       the user whether they won or lost the match.
    
16. **Flip A Coin**\
    Upon verbal request, the program can virtually flip a coin by randomly choosing between heads and tails, then informing the user of their choice.
    
17. **Tell A Joke**\
    Upon verbal request, the program can generate a joke using pyjokes.
    
18. **Exit Program**\
    Upon verbal request, the program ends and says goodbye.
