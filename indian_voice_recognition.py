#importing all the necessary libraries required 
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer() #creating a listener to understand the voice input
engine = pyttsx3.init()


def talk(text):#A function to call the parameters passed to it 
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:#exception handling block
        with sr.Microphone() as source:#this is the declaration of the audio source
            print('listening...')#acts as indication to let us know that indian is ready to listen to the input
            voice = listener.listen(source)# calling the speech recognizer to listen to the source
            command = listener.recognize_google(voice)#passing the audio to google to get the text in return
            command = command.lower()#converting the command into the lower case
            if 'indian' in command:
                command = command.replace('indian', '')#to avoid calling indian each time while taking the voice input
                print(command)
    except:
        pass
    return command


def run_indian():#main function
    command = take_command()#calling the take_command() function
    print(command)
    if 'play' in command:#to play the song
        song = command.replace('play', '')#to remove the play keyword from the command
        talk('playing ' + song)#to receive the voice output
        pywhatkit.playonyt(song)#directs you to the youtube for playing the desired song
    elif 'time' in command:#to know the time
        time = datetime.datetime.now().strftime('%H:%M')#to get the time in hour and min format
        print(time)#displays time on the screen
        talk('Current time is ' + time)#to receive the voice output of time
    elif 'tell me about ' in command:#to get information about someone
        person = command.replace('tell me about ', '')
        info = wikipedia.summary(person, 3)#directs you to wikipedia
        print(info)#prints the desired information on the screen
        talk(info)#reads out the information printed on the screen
    elif 'joke' in command:#to listen to a joke
        talk(pyjokes.get_joke())#starts telling a joke
    else:
        talk('PLEASE REPEAT')#incase any of the command isn't clear, it ask you to repeat

while True:#to run the program in loop
 run_indian()#calling the function
