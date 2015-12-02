#!/usr/bin/env python

#todo
#check if player one has vailed game to play 
# and if so he sould play it to pull from list
#--> check how won the game
#--> matching Dead lock case (Drow game)
#select number of players, get random 7 cards for each player
#number of players could be 2 or 4
from dom_utils import *

def start_player2(player_two_played_card):
	global game_tails
	print "player 2 has selected card",player_two_played_card
	if game_tails:
		game_tails=update_tails(game_tails, player_two_played_card)
	else :
		game_tails=update_tails(selected_item, player_two_played_card) 
	table_cards.append(player_two_played_card)
	player_two_cards.remove(player_two_played_card)
	print "now table cards are",table_cards	

number_of_players=int(raw_input('Enter number of players: '))

#in case that number of players are 2 then 
# each one has 7 unique cards and the rest are 14

if (number_of_players == 2):
	game_sceme=rest_of_cards_after_two()
	player_one_cards=game_sceme[0]
	player_two_cards=game_sceme[1]
	rest_of_cards=game_sceme[2]
	while player_one_cards or player_one_cards:
		print "Here is your cards please \n select which one you want to play by index:",player_one_cards
		index=int(raw_input('Enter index of element: '))
		try:
			selected_item=player_one_cards[index]
		except IndexError,e:
			raise IndexError ("index should be between zero and",len(player_one_cards)-1)
		if (table_cards):
			left_element,right_element = selected_item
			while (left_element not in game_tails) and (right_element not in game_tails):
				print "YOUR SELECTION SHOULD BE ON TAILS"
				selected_item =pull_card(player_one_cards,rest_of_cards)
				left_element,right_element = selected_item
				print "you don't have any cards to play\n"+\
				"we have pulled this card from rest"\
				,selected_item	

		if (game_tails):
			game_tails=update_tails(game_tails,selected_item)					
			final_res=compare_card(game_tails,player_two_cards)
		else:
			final_res=compare_card(selected_item,player_two_cards)	
		print "you have select card",selected_item
		table_cards.append(selected_item)
		player_one_cards.remove(selected_item)

		if len(final_res) >=1 :
			player_two_played_card=random.sample(final_res,1)[0]
			start_player2(player_two_played_card)
		else:
			# if computer has no vailed play 
			rest_of_cards_selection=pull_card(player_two_cards,rest_of_cards)
			#compare between what you get and current state of cards
			while len(compare_card(rest_of_cards_selection, table_cards)) == 0:
				rest_of_cards_selection=pull_card(player_two_cards,rest_of_cards)
				print "selected from rest",rest_of_cards_selection
			else:
				player_two_played_card=rest_of_cards_selection
				start_player2(player_two_played_card)

						

if (number_of_players == 4):
	game_sceme=rest_of_cards_after_two()
	player_one_cards=game_sceme[0]
	player_two_cards=game_sceme[1]
	rest_of_cards=game_sceme[2]
	player_three_cards=random.sample(rest_of_cards,7)
	print "player_three_cards are %s" %player_three_cards
	rest_of_cards=diff(rest_of_cards,player_three_cards)
	print "rest of cards after player there has taken his cards%s" %rest_of_cards
	player_four_cards=rest_of_cards
	print "player_four_cards are %s" %player_four_cards

