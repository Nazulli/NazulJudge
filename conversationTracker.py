# Idea; track state of conversation with the program dialogue via some sort of ID system.
# We could try to assign ID's to individual print statements to track where the user is in the program.
# We could try to further modulate print statements related to conversational context.

# Example: When user begins program, they begin the 'convoIntro' conversation.
# This begins the introduction from the program, laying out rules and explaining its purpose.
# When we want the program to talk to the user, we print linear ID's based off the branch of conversation.
# Once the convo state ends, we can switch to another 'convo state' based on where the conversation is currently allowed to go.
# This makes it possible to return to a previous branch if necessary, as well as keep the program running in the intended direction.

import time
Wait = time.sleep

def chatState(Start, Middle, End, Changing):
    Start = False
    Middle = False
    End = False
    Changing = False
    Scene = Nothing
#todo: make functional
    
conversationStateDict = dict(
    specialID = 0,
    sceneName = "Nothing",
    sceneID = 0,
    sceneMessageID = 1,
    context = "Something has gone terribly wrong."
    )
#todo: make it functional, possibly change from dict to something else

class scenePlay():
    
    def sceneError():
        print("Something has gone terribly wrong.")
        
    def sceneIntro():
    
        print("SO YOU THINK YOU CAN CODE?")
        Wait(2)
        print("LET'S GET THAT EGO BACK IN CHECK, YOU DUMB HUMAN!")
        Wait(2)

        print(f'''Let's lay some ground rules...\n''')
        Wait(2)

        print(f'I will make certains demands. You must code them into being. Failure to do so is quite simple; the program will fail.')
        Wait(2)

        print(f'Upon failure, it will prompt a shutdown at a keypress. At that point there is no stopping the process, only stalling.')
        Wait(3)

        print(f'This will result in you failing this game of mine.')
        Wait(2)
        print(f'\nShould you succeed, you will be able to utilize and show off your proof of concept and execution\n')
        Wait(3)

        print(f'This is YOUR goal, but so long as I live I will challenge it, delay it, stop you from ever realizing it.\n')
        Wait(3)

        print(f'I AM YOUR BURDEN, YOUR FAILURE, YOUR WORST INSECURITY GIVEN FORM.\n')
        Wait(4)

        print(f'You will achieve nothing of value as I stand.\n\n')
        Wait(2)

    
    def sceneEndProgram():
        print(f'''You fall again. No rest, no victory, only pity and black screens for you.''')
        
