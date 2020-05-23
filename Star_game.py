from sys import exit
import random#for using choice
# from random import randint
# from random import *
# from random import randint, choice


class Sun_star():
    def enter(self):
        print("Hello, there! Welcome to the star at the center of the Solar System, Sun. It is the most important source of energy for life on Earth.")
        print("This either be the start point for you to go back to the earth or be the end of your life.")
        print("In this game, you will need to answer following questions on each planet and your answer will lead you to the destination.")
        print("Congradulation! If your destination is Earth. You can go on do whatever you like. Yay!")
        print("Otherwise, you failed! The destination is Pluto. You need to accept punishment for your after life.")
        print("Please answer below question,\nHow ofter does Mercury speed around the Sun? (earth day)\n")

        answer = input("> ")
        if answer == '88':
            return 'Mercury'

        else:
            return 'Pluto'

class Engine(object):

    def __init__(self, planet_sun):
        self.planet_sun = planet_sun

    def play(self):
        current_planet = self.planet_sun.opening_planet()
        last_planet = self.planet_sun.next_planet('Pluto')

        while current_planet != last_planet:
            next_planet_name = current_planet.enter()
            current_planet = self.planet_sun.next_planet(next_planet_name)

        current_planet.enter()

class Mercury_planet(Sun_star):

    def enter(self):
        print("Hi, this is Mercury.\nOn Earth, you understand the weather is constantly changing just like life.\nAre you sure you want to go back to continue your life?")

        answer_1 = input("> ")
        answer_1 = answer_1.capitalize()
        if answer_1 == "Yes":
            print("How old are you?")
            print("Please select\nA: 1 ~ 11\nB: 12 ~ 29\nC: 30 ~ 64\nD: 65 up\n")

            answer_2 = input("> ")
            answer_2 = answer_2.capitalize()

            if answer_2 == "A":
                return 'Neptunr'

            elif answer_2 == "B":
                return 'Jupiter'

            elif answer_2 == "C":
                return 'Saturn'

            elif answer_2 == "D":
                return 'Uranus'

            else:
                print("Hey! Don't mess with me.")
                exit(1)

        elif answer_1 == "No":
            return 'Pluto'

        else:
            print("Hey! Don't mess with me.")
            exit(1)

class Venus_planet():

    def enter(self):
        print("Hi, there's a saying 'Women come from Venus.\nWhat's your gender?")

        answer_1 = input("> ")
        answer_1 = answe_1.capitalize()
        if answer_1 == "Man" or "Male" or "Boy":
            return 'Mars'

        elif answe_1 == "Female" or "Female" or "Girl":
            print("Do you think only man and woman can fall in love in this world?")

            answer_2 = input("> ")
            answer_2 = answer_2.capitalize()
            if answer_2 == "Yes":
                return 'Pluto'

            elif answer_2 == "No":
                return 'Earth'

            else:
                print("Hey! Don't mess with me.")
                exit(1)

        else:
            print("Hey! Don't mess with me.")
            exit(1)

class Earth_planet():

    def enter(self):
        print("Congradulation! Welcome back to the Earth.")
        exit(0)

class Mars_planet():
    def enter(self):
        print("Hi, there's a saying 'Men come from Mars?'\nWhat's your gender?")

        answer_1 = input("> ")
        answer_1 = answer_1.capitalize()
        if answer_1 == "Man" or "Male" or "Boy":
            print("Do you think only man and woman can fall in love in this world?")

            answer_2 = input("> ")
            answer_2 = answer_2.capitalize()
            if answer_2 == "Yes":
                return 'Pluto'

            elif answer_2 == "No":
                return 'Earth'

            else:
                print("Hey! Don't mess with me.")
                exit(1)

        elif answe_1 == "Female" or "Female" or "Girl":
            return 'Venus'

        else:
            print("Hey! Don't mess with me or you have secrets.")
            exit(1)


class Jupiter_planet():

    def enter(self):
        print("Hi, this is Jupiter.\nYou have 3 opportunities to guess a number from 0 to 9 to access the next planet to Earth.\nOnce you run out your opportunity, we'll need to say good bye to you.\nPlease enter your answer.")

        number = f"{randint(0, 10)}"
        guess = input("> ")
        guesses = 1

        while guess != number and guesses < 3:
            print("BZZZEDDD!")
            guesses += 1
            guess = input("> ")

        if guess == number:
            print("Wow, you have such a luck guy! You are one more step to Earth.")
            list = ['Mars', 'Venus']
            return random.choice(list)

        else:
            print("Sorry, you ran out of your opportunity. BYE...")
            return 'Pluto'

class Saturn_planet():

    def enter(self):
        print("Hi, this is Saturn.\nDo you love your father?")

        answer = input("> ")
        answer = answer.capitalize()
        if answer == "Yes":
                list = ['Mars', 'Venus']
                res = random.choice(list)
                return res

        elif answer == "No":
            return 'Pluto'

        else:
            print("Hey! Don't mess with me.")

class Uranus_planet():

    def enter(self):
        print("Hi, this is Uranus.\nHow many grandfather do you have?")

        answer = int(input("> "))
        list = ['Mars', 'Venus']
        if answer == 1:
            return random.choice(list)

        else:
            print("Sorry, only who have one grandfather can continue.\nIt's what it is.")
            return 'Pluto'

class Neptunr_planet():

    def enter(self):
        print("Hi, this is Neptunr.\nWhat is the color of Neptunr?")

        answer = input("> ")
        answer = answer.capitalize()
        if answer == "Blue":
            list = ['Mars', 'Venus']
            return random.choice(list)

        else:
            return 'Pluto'

class Pluto_planet():

    def enter(self):
        print("This is Pluto - the death of the world.\nI am sorry. You must got the wrong answer.\nPlease be ready to accept punishment in your after life.")
        exit(0)

class Planet(object):
    planets = {
        'Sun': Sun_star(),
        'Mercury': Mercury_planet(),
        'Venes': Venus_planet(),
        'Earth': Earth_planet(),
        'Mars': Mars_planet(),
        'Jupiter': Jupiter_planet(),
        'Saturn': Saturn_planet(),
        'Uranus': Uranus_planet(),
        'Neptunr': Neptunr_planet(),
        'Pluto': Pluto_planet(),
    }

    def __init__(self, start_planet):
        self.start_planet = start_planet

    def next_planet(self, planet_name):
        val = Planet.planets.get(planet_name)
        return val

    def opening_planet(self):
        return self.next_planet(self.start_planet)

a_planet = Planet('Sun')
a_game = Engine(a_planet)
a_game.play()
