# The program is designed to challenge myself to make the program more complex thru my skills and efforts.
# The way the program is designed to do so is to actively come up with new ideas and fail me if I can't implement them properly.
# This would make for a confusing project to track on Github
# This also would mean that a normal user trying to engage with my program wouldn't really understand or see the point in it.
# I plan to change the direction of the program to still challenge my coding skills, but also be interactive and intend to display said skills.

#todo: change project aim and scope

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
    
    
