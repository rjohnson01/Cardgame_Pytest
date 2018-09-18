from card_game.main import build_play_deck
#from card_game.blueprint import Player, Herocard, Spellcard, Buffcard
#from card_game.deck import deck

# verify that the play_deck contains 30 cards
def test_build_play_deck_length():
    test_deck = build_play_deck()
    assert len(test_deck) == 30                # verify initial deck build contains 30 cards


# verify that the play_deck contains the correct number of hero, spell, and buff cards
def test_play_deck_contents(incoming_deck):
    hero_card_count = 0
    spell_card_count = 0
    buff_card_count = 0
    
    for cards in incoming_deck:
        if cards.type == "hero":
            hero_card_count = hero_card_count + 1
        elif cards.type == "spell":
            spell_card_count = spell_card_count + 1
        elif cards.type == "buff":
            buff_card_count = buff_card_count + 1

    assert hero_card_count == 15                # verify deck contains 15 hero cards
    assert spell_card_count == 12               # verify deck contains 12 spell cards
    assert buff_card_count == 3                 # verify deck contains 3 spell cards

test_build_play_deck_length()

#play_deck_to_test = build_play_deck()
#test_build_play_deck_length(play_deck_to_test)
#test_play_deck_contents(play_deck_to_test)


