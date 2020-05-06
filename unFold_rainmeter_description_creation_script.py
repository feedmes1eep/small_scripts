# program=input('What Program button are you making: ') #single button description creator
sides=['left','right']

# for side in sides:
#     print('The {} side button for {}.'.format(side,program))

# below this comment is code for producing descriptions for many buttons
programs=[]
number=int(input(('how many buttons: ')))
space='-'*50


for x in range(number):
    program=input('What Program button are you making? ')
    programs.append(program)

x=1
for program in programs:
    for side in sides:
        if program == programs[-1]:
            if side == sides[-1]:
                prin=print('The {} side button for {}.'.format(side,program))
                print(space)
            else:
                print('The {} side button for {}.'.format(side,program))
        elif program == programs[0]:
            if side == sides[-1]:
                print('The {} side button for {}.'.format(side,program))
                print(space)
            else:
                print(space)
                print('The {} side button for {}.'.format(side,program))
        else:
            if side == sides[-1]:
                print('The {} side button for {}.'.format(side,program))
                print(space)
            else:
                print('The {} side button for {}.'.format(side,program))