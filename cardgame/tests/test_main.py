from card_game.main import build_play_deck


# verify that the play_deck contains 30 cards
def test_build_play_deck_length():
    test_deck = build_play_deck()
    assert len(test_deck) == 30                # verify initial deck build contains 30 cards



test_build_play_deck_length()



