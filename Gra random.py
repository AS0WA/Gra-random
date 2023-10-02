import random
import sys

def number_generator(drom_range, to_range):
    numbers = random.randint(drom_range, to_range)
    return numbers

def show_points():
    print("Punkty Gracza:", player_points)
    print("Punkty Komputera:", computer_points)

def add_point_player(player_point):
    return player_point + 1

def add_point_computer(computer_point):
    return computer_point + 1

def player1000_subtract(player_1000,playerNumber):
    player_1000 -= int(playerNumber)
    print("pozostało:", str(player_1000))
    return player_1000

#Zasady
print("""Zasady:
Zadaniem gracza jest wpisanie liczb w pięciu rundach, suma liczb musi być równa 1000.
Po wprowadzeniu każdej liczby, komputer prezentuje swoją wylosowaną liczbę.
Jeśli liczba podana przez gracza jest większa niż liczba komputera, gracz otrzymuje jeden punkt.
Jeśli jest mniejsza, komputer otrzymuje jeden punkt.
W przypadku remisu żadnej ze stron nie przyznaje się punktu.""")

while True:

    range_from = 100
    range_to = 600

    while True:
        computer_number_1 = number_generator(range_from, range_to)
        computer_number_2 = number_generator(range_from, range_to)
        computer_number_3 = number_generator(range_from, range_to)
        computer_number_4 = number_generator(range_from, range_to)
        computer_number_5 = number_generator(range_from, range_to)
        total = computer_number_1 + computer_number_2 + computer_number_3 + computer_number_4 + computer_number_5
        if total == 1000:
            break

    while True:
        player_points = 0
        computer_points = 0
        player1000 = 1000

        try:
            player_number_1 = input("\nRunda 1: ")
            print("Liczba Komputera:", computer_number_1)

            if int(player_number_1) >= 100 and int(player_number_1) <= player1000:
                pass
            else:
                print("\nNie poprawna liczba, zacznij od początku.")
                break

            player1000 = player1000_subtract(player1000, player_number_1)

            if int(player_number_1) > computer_number_1:
                player_points = add_point_player(player_points)
            elif int(player_number_1) < computer_number_1:
                computer_points = add_point_computer(computer_points)
            else:
                pass

            show_points()

            player_number_2 = input("\nRunda 2: ")
            print("Liczba Komputera:", computer_number_2)

            if int(player_number_2) >= 100 and int(player_number_2) <= player1000:
                pass
            else:
                print("\nNie poprawna liczba, zacznij od początku.")
                break

            player1000 -= int(player_number_2)
            print("pozostało:", str(player1000))

            if int(player_number_2) > computer_number_2:
                player_points = add_point_player(player_points)
            elif int(player_number_2) < computer_number_2:
                computer_points = add_point_computer(computer_points)
            else:
                pass

            show_points()

            player_number_3 = input("\nRunda 3:" )
            print("Liczba Komputera:", computer_number_3)

            if int(player_number_3) >= 100 and int(player_number_3) <= player1000:
                pass
            else:
                print("\nNie poprawna liczba, zacznij od początku.")
                break

            player1000 -= int(player_number_3)
            print("pozostało: " + str(player1000))

            if int(player_number_3) > computer_number_3:
                player_points = add_point_player(player_points)
            elif int(player_number_3) < computer_number_3:
                computer_points = add_point_computer(computer_points)
            else:
                pass

            show_points()

            player_number_4 = input("\nRunda 4:" )
            print("Liczba Komputera:", computer_number_4)

            if int(player_number_4) >= 100 and int(player_number_4) <= player1000:
                pass
            else:
                print("\nNie poprawna liczba, zacznij od początku.")
                break

            player1000 -= int(player_number_4)
            print("pozostało: " + str(player1000))

            if int(player_number_4) > computer_number_4:
                player_points = add_point_player(player_points)
            elif int(player_number_4) < computer_number_4:
                computer_points = add_point_computer(computer_points)
            else:
                pass

            show_points()

            player_number_5 = input("\nRunda 5:" )
            print("Liczba Komputera:", computer_number_5)

            if int(player_number_5) >= 100 and int(player_number_5) <= player1000:
                pass
            else:
                print("\nNie poprawna liczba, zacznij od początku.")
                break

            player1000 -= int(player_number_5)
            print("pozostało: " + str(player1000))

            if int(player_number_5) > computer_number_5:
                player_points = add_point_player(player_points)
            elif int(player_number_5) < computer_number_5:
                computer_points = add_point_computer(computer_points)
            else:
                pass

            if player1000 != 0:
                print("Błąd")
                break

            print()
            show_points()
            print()

            if player_points > computer_points:
                print("Brawo, Wygrywasz")
            elif player_points < computer_points:
                print("Przegrywasz")
            else:
                print("Remis")

            play_again = input("Czy chcesz zagrać ponownie? (Tak/Nie): ")
            if play_again == "nie" or play_again == "Nie":
                sys.exit()
                
        except ValueError:
            print("\nNie poprawna liczba, zacznij od początku.\n")