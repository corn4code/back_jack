import random

def draw_card():
    random_card = random.choice(card_list)
    card_drawn_list_player.append(random_card)
    card_list.remove(random_card)
    return card_drawn_list_player, card_list


def dealer_draw_card():
    random_card = random.choice(card_list)
    card_drawn_list_dealer.append(random_card)
    card_list.remove(random_card)
    return card_drawn_list_dealer, card_list


# cross cards
cross_two = 2
cross_three = 3
cross_four = 4
cross_five = 5
cross_six = 6
cross_seven = 7
cross_eight = 8
cross_nine = 9
cross_ten = 10
cross_boy = 10
cross_queen = 10
cross_king = 10
cross_ace = 11


# karo cards
karo_two = 2
karo_three = 3
karo_four = 4
karo_five = 5
karo_six = 6
karo_seven = 7
karo_eight = 8
karo_nine = 9
karo_ten = 10
karo_boy = 10
karo_queen = 10
karo_king = 10
karo_ace = 11

# pik cards
pik_two = 2
pik_three = 3
pik_four = 4
pik_five = 5
pik_six = 6
pik_seven = 7
pik_eight = 8
pik_nine = 9
pik_ten = 10
pik_boy = 10
pik_queen = 10
pik_king = 10
pik_ace = 11

# heart cards
heart_two = 2
heart_three = 3
heart_four = 4
heart_five = 5
heart_six = 6
heart_seven = 7
heart_eight = 8
heart_nine = 9
heart_ten = 10
heart_boy = 10
heart_queen = 10
heart_king = 10
heart_ace = 11

# game
draw = 5
pik_card_list = [pik_two, pik_three, pik_four, pik_five, pik_six, pik_seven, pik_eight, pik_nine, pik_ten, pik_boy, pik_queen, pik_king, pik_ace]
heart_card_list = [heart_two, heart_three, heart_four, heart_five, heart_six, heart_seven, heart_eight, heart_nine, heart_ten, heart_boy, heart_queen, heart_king, heart_ace]
cross_card_list = [cross_two, cross_three, cross_four, cross_five, cross_six, cross_seven, cross_eight, cross_nine, cross_ten, cross_boy, cross_queen, cross_king, cross_ace]
karo_card_list = [karo_two, karo_three, karo_four, karo_five, karo_six, karo_seven, karo_eight, karo_nine, karo_ten, karo_boy, karo_queen, karo_king, karo_ace]
card_list = [pik_card_list, cross_card_list, heart_card_list, karo_card_list]
card_list = sum(card_list, [])


# variables for player
card_drawn_list_player = []
points_player = 0
another_card = True

# variables for dealer
card_drawn_list_dealer = []
points_dealer = 0

# first to cards
for i in range(0, 2):
    draw_card()
    points_player = sum(card_drawn_list_player)
    dealer_draw_card()
print(f"Dealers first card: {card_drawn_list_dealer [0]}")
print(f"you're at {points_player} right now ")

if 17 <= points_player <= 21:
    print(f"Your points {points_player} ")

elif points_player == 21:
    print("Black Jack")

elif points_player < 17:

    while True:
        if another_card is True:
            get_card = input("Hit? (y/n) ")

            if get_card == "y":
                draw_card()
                points_player = sum(card_drawn_list_player)
                print(f"you're at {points_player} ")

            elif get_card == "n":
                another_card = False

            if points_player > 21:
                print("bust")
                another_card = False

            if points_player == 21:
                another_card = False

            if another_card is False:
                break

points_dealer = sum(card_drawn_list_dealer)
while True:
    if points_dealer < 17:
        dealer_draw_card()
        points_dealer = sum(card_drawn_list_dealer)
    if points_player > 17:
        break
print("-----------------")
if 21.5 > points_player > points_dealer:
    print("you win")
if points_player < points_dealer or points_player > 21:
    print("you lose")
if points_player == points_dealer:
    print("push")
print(f"Your points: {points_player}")
print(f"Dealers points: {points_dealer}")
print("-----------------")
print(f"cards player {card_drawn_list_player}, rest cards {card_list}, cards dealer {card_drawn_list_dealer}")
