print('Funny Car Game!!!!!!!!!')
print('For help just enter "help"')
started = False
while True:
    user_input = input('>> ').lower()
    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to jump out from the car
        ''')
    elif user_input == 'start':
        if started:
            print('Your car is already started: No need to start again !!!!!')
        else:
            started = True
            print('Yahoo!!!! Your car is started ..... Enjoy the ride !!!')
    elif user_input == 'stop':
        if not started:
            print('The car is already stop !!!!!! Try to start it again !!!!')
        else:
            started = False
            print('Oh No !!! You just stopped your car !!!!')
    elif user_input == 'quit':
        print('You just jumped off your car !!!!!')
        exit()
    else:
        print("Hey baby I don't understand that !!!!!!")
