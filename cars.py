from datetime import datetime
import os, csv

racenr = 0
number_of_cars = 0

place = {}
speed = {}
race_car = {}

with open('cars.csv') as cars_csv:
    csv_reader = csv.DictReader(cars_csv)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        race_car[line_count - 1] = row['NAME']
        line_count += 1
    number_of_cars = line_count - 1


def clear():
    os.system('cls')


def get_track(place, car, length):
    driving = []
    if place == 0:
        driving.append(car)
        driving.append('|')
    for x in range(0, place):
        driving.append('_')
    if 0 < place < length:
        driving.append(car)
    for y in range(place, length):
        driving.append('_')
    if place >= length:
        driving.append('|')
        driving.append(car)
    else:
        driving.append('|')
    return driving


def get_save(racenr, winner, length, time_start):
    time_finish = length * (datetime.now() - time_start)
    time_all = str(time_finish).split('.')[0]
    with open('results.txt', mode='a') as file:
        file.write(f'\n{racenr}, {winner}, {time_all}')
