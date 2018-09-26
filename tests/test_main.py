from card_game.game import build_play_deck, fill_players_hand, game_intro, draw_new_card, player_card_selection, card_actions
from card_game.blueprint import Player, Herocard, Spellcard, Buffcard
import pytest

# fixture that builds the play_deck
#@pytest.fixture(scope="module")
@pytest.fixture()
def test_play_deck():
    print("Building test_play_deck")
    test_play_deck = build_play_deck()

    return test_play_deck


# testing that the play_deck contains 30 cards after the initial build
@pytest.mark.deckbuild
def test_build_play_deck_length(test_play_deck):
    assert len(test_play_deck) == 30

# testing that the correct number of hero cards are in the play_deck after the initial build
@pytest.mark.deckbuild
def test_hero_card_count(test_play_deck):
    hero_card_count = 0

    for cards in test_play_deck:
        if cards.type == "hero":
            hero_card_count = hero_card_count + 1

    assert hero_card_count == 15

# testing that the correct number of spell cards are in the play_deck after the initial build
@pytest.mark.deckbuild
def test_spell_card_count(test_play_deck):
    spell_card_count = 0

    for cards in test_play_deck:
        if cards.type == "spell":
            spell_card_count = spell_card_count + 1

    assert spell_card_count == 12

# testing that the correct number of buff cards are in the play_deck
@pytest.mark.deckbuild
def test_buff_card_count(test_play_deck):
    buff_card_count = 0

    for cards in test_play_deck:
        if cards.type == "buff":
            buff_card_count = buff_card_count + 1

    assert buff_card_count == 3   

# testing that the player's hand is being populated with the correct number of cards
def test_fill_players_hand(test_play_deck):
    test_player_hand = fill_players_hand(test_play_deck)

    assert len(test_player_hand) == 7

# testing that a new card is drawn from the play_deck
def test_draw_new_card(test_play_deck):
    test_deck_cardcount = len(test_play_deck)
    drawn_card = draw_new_card(test_play_deck)

    #assert drawn_card.name != ""
    assert drawn_card.name != "" and test_deck_cardcount > len(test_play_deck)

# testing that player_card_selection is pulling cards out of the player hand
def test_player_card_selection(test_play_deck):
    test_player = Player()
    test_player.hand = fill_players_hand(test_play_deck)
    hand_length = len(test_player.hand)
    test_player.play_random_card()

    assert hand_length > len(test_player.hand)


# testing the Hero card card_actions attack
@pytest.mark.cardattacks
def test_card_actions_herocard(test_play_deck):
    test_card_hero = test_play_deck[0]
    test_card_defending = test_play_deck[1]

    hero_strength, defending_health = test_card_hero.strength, test_card_defending.health
    calculated_health = defending_health - hero_strength
    
    card_actions(test_card_hero, test_card_defending)
    
    assert test_card_defending.health == calculated_health

# testing the Buff card card_actions heal
@pytest.mark.cardattacks
def test_card_actions_buffcard(test_play_deck):
    test_card_buff = test_play_deck[-1]
    test_card_to_heal = test_play_deck[0]

    buff_health, card_hp = test_card_buff.health, test_card_to_heal.health
    calculated_healing = card_hp + buff_health
    
    card_actions(test_card_buff, test_card_to_heal)

    assert test_card_to_heal.health == calculated_healing 

# testing the Spell card card_actions attack
@pytest.mark.cardattacks
def test_card_actions_spellcard(test_play_deck):
    test_card_spell = test_play_deck[16]
    test_card_defending = test_play_deck[2]

    spell_strength, defending_health = test_card_spell.strength, test_card_defending.health
    calculated_health = defending_health - spell_strength

    card_actions(test_card_spell, test_card_defending)

    assert test_card_defending.health == calculated_health

    # import pdb; pdb.set_trace()
