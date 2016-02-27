import random
import sys


def generate_cards():
    temp = []
    for i in range(0, 7):
        for j in range(i, 7):
            temp.append((i, j))
    return temp


def diff(a, b):
    '''
        return elements that exist in a and not exist in b
    '''
    return [aa for aa in a if aa not in b]


def compare_card(selected_item, other_card):
    '''
    :param selected_item: user selected item
    :param other_card: player_two_cards
    :return: all cards that match left and right of selected tie
    '''

    left_side, right_side = selected_item
    final_res = []
    res1 = [item for item in other_card if left_side in item]
    if left_side == right_side:
        final_res = res1
        return final_res
    else:
        res2 = [item for item in other_card if right_side in item]
        final_res = res1 + res2
        return final_res


def distribute_cards(cards):
    print "there is now two players playing "
    player_one_cards = random.sample(cards, 7)
    print "player_one_cards are %s" % player_one_cards
    # get the rest of items and generate another 7 random of them
    rest_of_cards = diff(cards, player_one_cards)
    print "rest of cards after player one has taken his cards%s" % rest_of_cards
    player_two_cards = random.sample(rest_of_cards, 7)
    print "player_two_cards are %s" % player_two_cards
    rest_of_cards = diff(rest_of_cards, player_two_cards)
    print '''rest of cards after player one and two have taken there cards%s''' % rest_of_cards
    return [player_one_cards, player_two_cards, rest_of_cards]


def pull_card(player_cards, rest_of_cards):
    print "player has to pull card from the rest_of_cards"
    try:
        rest_of_cards_selection = random.sample(rest_of_cards, 1)[0]
    except ValueError, e:
        sys.exit("You lose the Game ...")
    rest_of_cards.remove(rest_of_cards_selection)
    player_cards.append(rest_of_cards_selection)
    return rest_of_cards_selection
