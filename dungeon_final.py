#Silicon Beach Software
#CST 205 - FINAL
#David Henderson
#Christopher Calderon
#Nicholas Nelson
#Nathan Muaga
#Haley Dimapilis


#This Lets us pick a media folder, and then not have to ask for each file
setMediaFolder(pickAFolder())
#This is just to deal with JES oddities, so our code can find the rest of our modules
sys.path.append(getMediaPath())


from gameCore import *


def main():
  myText = Text()                                         #this function prompts the player upon initialization of the game
  myText.intro_Outputs()
  myText.help()
  printNow("The door is not locked")
  printNow("The door suddenly locks behind you. You must now find a way out.")
  showInformation("The door is not locked" + "\n" + "The door suddenly locks behind you. You must now find a way out.")
  Run()



main()
