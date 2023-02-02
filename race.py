import random, csv
from cars import *
# from betting import *
from time import sleep
from datetime import datetime

print('== == == == == WELCOME TO THE == == == == ==')
print('== = == NEED FOR SPEED TERMINAL RACE == = ==\n')

race = True
while race:
    for x in range(number_of_cars):
        place[x] = 0
    length = random.randint(20, 30)
    racenr += 1
    answer = input(
        '\nChoose the option (type option number):\n'
        f'1 Start race {length}\n'
        '2 Betting\n'
        '3 See score - board\n'
        '4 Quit the game\n'
    )
    racetrack = True
    if answer == '1':
        print(f'Race on track-length {length}')
        clear()
        for x in range(number_of_cars):
            print(*get_track(place[x], race_car[x], length))
        print()
        sleep(1.5)
        time_start = datetime.now()
        while racetrack:
            clear()
            for x in range(number_of_cars):
                speed[x] = random.randint(1, 2)
                place[x] += speed[x]
                print(*get_track(place[x], race_car[x], length))
            print()
            for y in range(number_of_cars):
                if place[y] >= length:
                    print(f'Car {race_car[y]} win! ')
                    car_winner = race_car_id[y]
                    get_save(racenr, race_car[y], length, time_start)
                    racetrack = False
                    if car_choice == car_winner:
                        sum_bet_money += int(amount_bet)
                        print(f'You win! Amount money is {sum_bet_money}')
                    elif int(car_choice) > 0:
                        sum_bet_money -= int(amount_bet)
                        print(f'Sorry, you lost. Amount money is {sum_bet_money} ')
                    else:
                        print("You don't bet")
                    break

            sleep(0.5)

    elif answer == '2':
        clear()
        line_count2 = 0
        your_bet = input('Do you want to bet on next race? Yes/No: ')
        if your_bet.upper() == 'Y':
            print('You give 100 points for playing')
            sum_bet_money = 100
            print('There are 8 cars in start')
            with open('cars.csv') as cars_csv:
                csv_reader = csv.DictReader(cars_csv)

                for row in csv_reader:
                    if line_count2 == 0:
                        line_count2 += 1
                    print(row['ID'], row['BRAND'], row['COLOUR'])
                    line_count2 += 1
            car_choice = input(f'What car you want to bet on: 1..{line_count2 - 1} : ')
            amount_bet = input(f'How much you want to bet? Max is {sum_bet_money} ')
        else:
            print('Then watch without betting')
    elif answer == '3':
        with open('results.txt') as results:
            for line in results:
                print(line, end='')
            print()
    elif answer == '4':
        race = False
        print('See you on the next race!')
    else:
        print('no such option is offered')
