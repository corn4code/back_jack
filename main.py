import random


# draws card for player
def draw_card():
    random_card = random.choice(card_list)
    card_drawn_list_player.append(random_card)
    card_list.remove(random_card)
    return card_drawn_list_player, card_list


# draws card for dealer
def dealer_draw_card():
    random_card = random.choice(card_list)
    card_drawn_list_dealer.append(random_card)
    card_list.remove(random_card)
    return card_drawn_list_dealer, card_list


# get value of ace for player
def get_karo_ace_value_player(card_drawn_list_player):
    global points_player
    card_drawn_list_player.remove(karo_ace)
    card_drawn_list_player.append(1)
    points_player = sum(card_drawn_list_player)
    return card_drawn_list_player, points_player


def get_heart_ace_value_player(card_drawn_list_player):
    global points_player
    card_drawn_list_player.remove(heart_ace)
    card_drawn_list_player.append(1)
    points_player = sum(card_drawn_list_player)
    return card_drawn_list_player, points_player


def get_pik_ace_value_player(card_drawn_list_player):
    global points_player
    card_drawn_list_player.remove(pik_ace)
    card_drawn_list_player.append(1)
    points_player = sum(card_drawn_list_player)
    return card_drawn_list_player, points_player


def get_cross_ace_value_player(card_drawn_list_player):
    global points_player
    card_drawn_list_player.remove(cross_ace)
    card_drawn_list_player.append(1)
    points_player = sum(card_drawn_list_player)
    return card_drawn_list_player, points_player


# get value of ace for dealer
def get_karo_ace_value_dealer(card_drawn_list_dealer):
    global points_dealer
    card_drawn_list_dealer.remove(karo_ace)
    card_drawn_list_dealer.append(1)
    points_dealer = sum(card_drawn_list_dealer)
    return card_drawn_list_dealer, points_dealer


def get_heart_ace_value_dealer(card_drawn_list_dealer):
    global points_dealer
    card_drawn_list_dealer.remove(heart_ace)
    card_drawn_list_dealer.append(1)
    points_dealer = sum(card_drawn_list_dealer)
    return card_drawn_list_dealer, points_dealer


def get_pik_ace_value_dealer(card_drawn_list_dealer):
    global points_dealer
    card_drawn_list_dealer.remove(pik_ace)
    card_drawn_list_dealer.append(1)
    points_dealer = sum(card_drawn_list_dealer)
    return card_drawn_list_dealer, points_dealer


def get_cross_ace_value_dealer(card_drawn_list_dealer):
    global points_dealer
    card_drawn_list_dealer.remove(cross_ace)
    card_drawn_list_dealer.append(1)
    points_dealer = sum(card_drawn_list_dealer)
    return card_drawn_list_dealer, points_dealer


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

# game Variables
pik_card_list = [pik_two, pik_three, pik_four, pik_five, pik_six, pik_seven, pik_eight, pik_nine, pik_ten, pik_boy,
                 pik_queen, pik_king, pik_ace]
heart_card_list = [heart_two, heart_three, heart_four, heart_five, heart_six, heart_seven, heart_eight, heart_nine,
                   heart_ten, heart_boy, heart_queen, heart_king, heart_ace]
cross_card_list = [cross_two, cross_three, cross_four, cross_five, cross_six, cross_seven, cross_eight, cross_nine,
                   cross_ten, cross_boy, cross_queen, cross_king, cross_ace]
karo_card_list = [karo_two, karo_three, karo_four, karo_five, karo_six, karo_seven, karo_eight, karo_nine, karo_ten,
                  karo_boy, karo_queen, karo_king, karo_ace]
card_list = [pik_card_list, cross_card_list, heart_card_list, karo_card_list]
card_list = sum(card_list, [])
game_active = True
wins_player = 0
wins_dealer = 0

# variables for player
card_drawn_list_player = []
points_player = 0
another_card = True

# variables for dealer
card_drawn_list_dealer = []
points_dealer = 0
new_card_for_dealer = True

# first to cards
if __name__ == "__main__":
    while game_active:
        card_list = [pik_card_list, cross_card_list, heart_card_list, karo_card_list]
        card_list = sum(card_list, [])
        game_active = True

        # variables for player
        card_drawn_list_player = []
        points_player = 0
        another_card = True

        # variables for dealer
        card_drawn_list_dealer = []
        points_dealer = 0

        ask_new_game = input("New game? (y/n): ")
        if ask_new_game == "y":
            # draws your and dealers first two cards and gets your points
            for i in range(0, 2):
                draw_card()
                points_player = sum(card_drawn_list_player)
                dealer_draw_card()
                points_dealer = sum(card_drawn_list_dealer)
            print(f"Dealers first card: {card_drawn_list_dealer[0]}")
            print(f"your cards: {card_drawn_list_player}")
            print(f"you're at {points_player} right now ")
            # doesn't stop if ace exists because it can be worth less --> choice at player else player can't hit
            if points_player == 21:
                print("Black Jack")
                another_card = False

            if 21 > points_player > 16.5:
                print(f"Your points {points_player} ")
                another_card = False
                continue

            if points_player < 17:
                # asks if you want a new card and refreshes the points
                while another_card:
                    get_card = input("Hit? (y/n) ")
                    if get_card == "y":
                        draw_card()
                        print(f"your cards: {card_drawn_list_player}")
                        points_player = sum(card_drawn_list_player)
                        if karo_ace in card_drawn_list_player and points_player > 21.5:
                            get_karo_ace_value_player(card_drawn_list_player)
                        if heart_ace in card_drawn_list_player and points_player > 21.5:
                            get_heart_ace_value_player(card_drawn_list_player)
                        if pik_ace in card_drawn_list_player and points_player > 21.5:
                            get_pik_ace_value_player(card_drawn_list_player)
                        if cross_ace in card_drawn_list_player and points_player > 21.5:
                            get_cross_ace_value_player(card_drawn_list_player)
                        points_player = sum(card_drawn_list_player)
                        print(f"you're at {points_player} ")
                        if points_player > 21.5:
                            print("bust")
                            another_card = False
                            break

                        if 21.5 > points_player > 16.5:
                            another_card = False
                            break
                    elif get_card == "n":
                        another_card = False
            # decision if dealer gets another card or not
            if points_player < 21:
                new_card_for_dealer = True
            if points_player > 21:
                new_card_for_dealer = False
            while new_card_for_dealer:
                points_dealer = sum(card_drawn_list_dealer)

                if points_dealer < 17:
                    dealer_draw_card()
                    points_dealer = sum(card_drawn_list_dealer)

                # checks the value of ace in dealers cards
                if karo_ace in card_drawn_list_dealer and points_dealer > 21.5:
                    get_karo_ace_value_dealer(card_drawn_list_dealer)
                if heart_ace in card_drawn_list_dealer and points_dealer > 21.5:
                    get_heart_ace_value_dealer(card_drawn_list_dealer)
                if pik_ace in card_drawn_list_dealer and points_dealer > 21.5:
                    get_pik_ace_value_dealer(card_drawn_list_dealer)
                if cross_ace in card_drawn_list_dealer and points_dealer > 21.5:
                    get_cross_ace_value_dealer(card_drawn_list_dealer)
                if points_dealer > 17:
                    break

            # this checks if you won or lost
            print("-----------------")
            if 21.5 > points_player > points_dealer:
                print("you win")
                wins_player += 1
            if points_dealer > 21 and points_player < 21.5:
                print("you win")
                wins_player += 1
            if points_player < points_dealer < 21.5:
                print("you lose")
                wins_dealer += 1
            if points_player > 21:
                print("you lose")
                wins_dealer += 1
            if points_player == points_dealer:
                print("push")
            print(f"Your points: {points_player}")
            print(f"Dealers points: {points_dealer}")
            print("-----------------")
            print(
                f"cards player {card_drawn_list_player}, cards dealer {card_drawn_list_dealer}, rest cards {card_list}")
            print(f"your wins: {wins_player}")
            print(f"dealers wins: {wins_dealer}")
            print("-----------------")

        if ask_new_game == "n":
            game_active = False
