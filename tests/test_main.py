from card_game.main import build_play_deck, fill_players_hand, game_intro, draw_new_card
import sys
import pytest


@pytest.fixture(scope="module")
def test_play_deck():
    print("Building test_play_deck")
    test_play_deck = build_play_deck()

    return test_play_deck


# verify that the play_deck contains 30 cards
def test_build_play_deck_length(test_play_deck):
    #test_deck = build_play_deck()
    assert len(test_play_deck) == 30                # verify initial deck build contains 30 cards

# verify that the correct number of hero cards are in the play_deck
def test_hero_card_count(test_play_deck):
    #test_deck = build_play_deck()
    hero_card_count = 0

    for cards in test_play_deck:
        if cards.type == "hero":
            hero_card_count = hero_card_count + 1

    assert hero_card_count == 15                # verify there are 15 hero cards in the initial play_deck

# verify that the correct number of spell cards are in the play_deck
def test_spell_card_count(test_play_deck):
    #test_deck = build_play_deck()
    spell_card_count = 0

    for cards in test_play_deck:
        if cards.type == "spell":
            spell_card_count = spell_card_count + 1

    assert spell_card_count == 12                # verify there are 12 spell cards in the initial play_deck

# verify that the correct number of buff cards are in the play_deck
def test_buff_card_count(test_play_deck):
    #test_deck = build_play_deck()
    buff_card_count = 0

    for cards in test_play_deck:
        if cards.type == "buff":
            buff_card_count = buff_card_count + 1

    assert buff_card_count == 3                 # verify there are 3 buff cards in the initial play_deck   

# test to verify player's hand is being populated with the correct number of cards
def test_drawing_player_hand(test_play_deck):
    #test_deck = build_play_deck()
    test_player_hand = fill_players_hand(test_play_deck)

    assert len(test_player_hand) == 7

def test_game_intro(capsys):
    game_intro()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    
    assert "wins!" in out

def test_drawing_new_card(test_play_deck):
    play_deck = test_play_deck
    drawn_card = draw_new_card()

    assert drawn_card.name != ""






