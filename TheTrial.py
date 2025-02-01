import time
import conversationTracker
Scene = conversationTracker.scenePlay 

Wait = time.sleep

# OH YEAAAAH!

YOU = 'UserAgent'
COMPUTER = 'ComputerAgent'

Scene.sceneIntro()

print(f'I want an input! Give me an input, MAKE ME ASK FOR IT!')

print(f'Input... may I have... input?')
inputGiven = input('dAta feed   me dataAAAAAAAAA: ')
if inputGiven == '':
    print('YOU THINK YOU CAN GIVE ME NOTHING? EXECUTING BRANCH 1.')

else:
    print(f'Input verified. Input given: {inputGiven}. Continuing...')
    
    
    