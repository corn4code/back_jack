import random

def draw_card():
    random_card = random.choice(card_list)
    card_drawn_list.append(random_card)
    card_list.remove(random_card)
    return card_drawn_list, card_list

#cross cards
cross_two = 2
cross_three = 3
cross_four = 4
cross_five = 5
cross_six = 6
cross_seven = 7
cross_eight = 8
cross_nine = 9
cross_ten = 10

#karo cards
karo_two = 2
karo_three = 3
karo_four = 4
karo_five = 5
karo_six = 6
karo_seven = 7
karo_eight = 8
karo_nine = 9
karo_ten = 10

#pik cards
pik_two = 2
pik_three = 3
pik_four = 4
pik_five = 5
pik_six = 6
pik_seven = 7
pik_eight = 8
pik_nine = 9
pik_ten = 10

#heart cards
heart_two = 2
heart_three = 3
heart_four = 4
heart_five = 5
heart_six = 6
heart_seven = 7
heart_eight = 8
heart_nine = 9
heart_ten = 10


#game
draw = 5
pik_card_list = [pik_two, pik_three, pik_four, pik_five, pik_six, pik_seven, pik_eight, pik_nine, pik_ten]
heart_card_list = [heart_two, heart_three, heart_four, heart_five, heart_six, heart_seven, heart_eight, heart_nine, heart_ten]
cross_card_list = [cross_two, cross_three, cross_four, cross_five, cross_six, cross_seven, cross_eight, cross_nine, cross_ten]
karo_card_list = [karo_two, karo_three, karo_four, karo_five, karo_six, karo_seven, karo_eight, karo_nine, karo_ten]
card_list = [pik_card_list, cross_card_list, heart_card_list, karo_card_list]
card_list = sum(card_list, [])
card_drawn_list = []
points = 0
another_card = True

#first to cards
for i in range(0, 2):
    draw_card()
    points = sum(card_drawn_list)
print(f"you're at {points} right now")

if 17 <= points <= 21:
    print(f"Your points {points}")
elif points > 21.5:
    print("bust")
elif points < 17:
    while True:
        if another_card == True:
            get_card = input("Hit? (y/n)")
            if get_card == "y":
                draw_card()
                points = sum(card_drawn_list)
                print(f"you're at {points}")
            elif get_card == "n":
                another_card = False

            if points > 21:
                print("bust")
                another_card = False
            if points == 21:
                print("Black Jack")
                another_card = False

            if another_card == False:
                break

print(f"Your points: {points}")
print(card_drawn_list, card_list)

#it works
