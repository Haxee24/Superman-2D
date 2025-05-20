# Setting up speech Zara
import pyttsx3
import speech_recognition as sr
Rummy = 0
Pack_1st = 25
Pack_reg = 50
jhumjhum = pyttsx3.init('sapi5')
voices = jhumjhum.getProperty('voices')
print(voices)
jhumjhum.setProperty('voice', voices[1].id)
validscores = ["rummy", "pack"]
for i in range(0, 81):
    validscores.append(str(i))

def Speak(speech):
    jhumjhum.say(speech)
    jhumjhum.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
        return query

# The Main Program Score Calcutor for Rummy at Nani's


class PLayer:
    playercount = 0

    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        PLayer.playercount += 1


"""
for i in range(0, 11):
    Speak("Hijjdaa uney")
    Speak("Please baytoo")
"""

Rounds = 0
Speak("Welcome to the Game everyone, could you please type in the names of the players who will be playing tonight")
playernames = []
playerlist = []
while True:
    aa = input("Enter the players name: ")
    if aa == "":
        Speak("Enter a name you idiot")
    else:
        break
playerlist.append(PLayer(aa))
Speak("Welcome" + aa)
playernames.append(aa)
Speak("Do you want to add another player?")
while True:
    aa = input("Do you want to add another player?: \n")
    if aa.lower() == "yes":
        Speak("Enter the Player's name")
        aa = input("Enter the Player's name\n")
        if aa == "":
            Speak("Enter a name you idiot")
        else:
            playerlist.append(PLayer(aa))
            playernames.append(aa)
            Speak("Welcome" + aa)
    elif aa.lower() == "no":
        if PLayer.playercount >= 2:
            break
        else:
            Speak("You wanna play alone go play something else in you room, this requires 2 players to play so enter another name")
            aa = input("Enter the Player's name\n")
            if aa == "":
                Speak("Enter a name you idiot")
            else:
                playerlist.append(PLayer(aa))
                Speak("Welcome " + aa)
    else:
        Speak("Answer in yes or no you Idiot")
    Speak("Do you want to add another player?")

Speak("How many rounds of rummy will you be playing tonight")
aa = input()
Rounds = int(aa)
roundsplayed = 0
while True:
    packed = []
    if roundsplayed >= Rounds:
        scoresref = {}
        scores = []
        for i in range(0, len(playerlist)):
            scoresref[playerlist[i].score] = playerlist[i].name
        for i in range(0, len(playerlist)):
            scores.append(playerlist[i].score)
        scores.sort()
        Speak("Congratulations " + scoresref[scores[0]] + "you are the winner of today's game")
        if PLayer.playercount > 2:
            Speak("The runner ups are " + scoresref[scores[1]] + " and " + scoresref[scores[2]] + " respectively")
        else:
            Speak("The runner up is " + scoresref[scores[1]])
        for i in range(0, len(scores)):
            print(str(i + 1) + ". " + str(scoresref[scores[i]]))
        break
    Speak("Let me know when the round is over by pressing enter on this laptop, press h or help to make changes to the SSgame")
    aa = input()
    if aa.lower() == "help" or aa.lower() == 'h':
        Speak("Hey welcome to the Changes menu, press 1 if you wanna add another player, press 2 to end the game now and get the scores, press 3 to remove a player")
        aa = input("Press a number")
        if aa == str(1):
            while True:
                Speak("Enter the Player's name")
                aa = input("Enter the Player's name\n")
                if aa == "":
                    Speak("Enter a name you idiot")
                else:
                    playerlist.append(PLayer(aa, 25))
                    Speak("Welcome" + aa)
                    playernames.append(aa)
                    break
            continue
        elif aa == str(2):
            Speak("Are you sure you want to end this game now")
            while True:
                aa = input()
                if aa.lower() == "no":
                    break
                elif aa.lower() == "yes":
                    roundsplayed = Rounds
                    break
            continue
        elif aa == str(3):
            count = 0
            Speak("Enter the name of the player you want to remove from the following list")
            for name in playerlist:
                print(str(count) + ". " + name.name)
                count += 1
            aa = input("Enter the players name: ")
            if aa in playernames:
                for i in range(0, len(playerlist)):
                    if playerlist[i].name == aa:
                        Speak(playerlist.pop(i).name + " was removed from the game")
                        PLayer.playercount -= 1
                        break
                continue
            else:
                continue
        else:
            pass
    else:
        for i in range(0, len(playerlist)):
            if playerlist[i].name in packed:
                continue
            Speak("Enter your score " + playerlist[i].name)
            while True:
                aa = input("enter your score")
                if aa.lower() not in validscores:
                    Speak("Enter a valid score you Gaawaarr")
                else:
                    if aa.lower() == "rummy":
                        playerlist[i].score += Rummy
                        break
                    elif aa.lower() == "pack":
                        if roundsplayed == 1:
                            playerlist += Pack_1st
                            packed.append(playerlist[i].name)
                        else:
                            playerlist[i].score += Pack_reg
                            packed.append(playerlist[i].name)
                        break
                    else:
                        playerlist[i].score += int(aa)
                        break
        for i in range(0, len(playerlist)):
            print(playerlist[i].name + "'s Score: " + str(playerlist[i].score))
        roundsplayed += 1
