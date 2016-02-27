#!/usr/bin/env python
from dom_utils import *


class Game(object):
    def __init__(self):
        self.cards = generate_cards()
        self.game_scheme = distribute_cards(self.cards)
        self.player_one_cards = self.game_scheme[0]
        self.player_two_cards = self.game_scheme[1]
        self.rest_of_cards = self.game_scheme[2]
        self.game_tails = None
        self.table_cards = []
        self.start_game()

    def start_game(self):
        number_of_players = int(raw_input('Enter number of players: '))
        if number_of_players == 2:
            while self.player_one_cards or self.player_one_cards:
                print "Here is your cards please \n " \
                      "select which one you want to play by index:", self.player_one_cards
                index = int(raw_input('Enter index of element: '))
                try:
                    self.selected_item = self.player_one_cards[index]
                except IndexError:
                    raise IndexError("index should be between zero and", len(self.player_one_cards) - 1)
                if self.table_cards:
                    left_element, right_element = self.selected_item
                    while (left_element not in self.game_tails) and (right_element not in self.game_tails):
                        print "YOUR SELECTION SHOULD BE ON TAILS"
                        self.selected_item = pull_card(self.player_one_cards, self.rest_of_cards)
                        left_element, right_element = self.selected_item
                        print "you don't have any cards to play\n" + \
                              "we have pulled this card from rest" \
                            , self.selected_item

                if self.game_tails:
                    self.game_tails = self.update_tails(self.game_tails, self.selected_item)
                    final_res = compare_card(self.game_tails, self.player_two_cards)
                else:
                    final_res = compare_card(self.selected_item, self.player_two_cards)
                print "you have select card", self.selected_item
                self.table_cards.append(self.selected_item)
                self.player_one_cards.remove(self.selected_item)

                if len(final_res) >= 1:
                    player_two_played_card = random.sample(final_res, 1)[0]
                    self.start_player2(player_two_played_card)
                else:
                    # if computer has no vailed play
                    rest_of_cards_selection = pull_card(self.player_two_cards, self.rest_of_cards)
                    # compare between what you get and current state of cards
                    while len(compare_card(rest_of_cards_selection, self.table_cards)) == 0:
                        rest_of_cards_selection = pull_card(self.player_two_cards, self.rest_of_cards)
                        print "selected from rest", rest_of_cards_selection
                    else:
                        player_two_played_card = rest_of_cards_selection
                        self.start_player2(player_two_played_card)

    def update_tails(self, selected_item, played_card):

        selected_left_side, selected_right_side = selected_item
        pc_left_side, pc_right_side = played_card

        if selected_left_side == pc_left_side:
            self.game_tails = (selected_right_side, pc_right_side)
            print "two tails are", self.game_tails
            return self.game_tails
        elif selected_left_side == pc_right_side:
            self.game_tails = (selected_right_side, pc_left_side)
            print "two tails are", self.game_tails
            return self.game_tails
        elif selected_right_side == pc_right_side:
            self.game_tails = (selected_left_side, pc_left_side)
            print "two tails are", self.game_tails
            return self.game_tails
        elif selected_right_side == pc_left_side:
            self.game_tails = (selected_left_side, pc_right_side)
            print "two tails are", self.game_tails
            return self.game_tails
        else:
            print "wrong move"
            return self.game_tails

    def start_player2(self, card):
        print "player 2 has selected card", card
        if self.game_tails:
            self.game_tails = self.update_tails(self.game_tails, card)
        else:
            self.game_tails = self.update_tails(self.selected_item, card)
        self.table_cards.append(card)
        self.player_two_cards.remove(card)
        print "now table cards are", self.table_cards

if __name__ == '__main__':
    mygame = Game()
