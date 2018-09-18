# Authors
- Roger Johnson
- Zach Gagnon

# Requirements
- The battle engine is working great! But one morning Roger comes in and utters those 5 fateful words: “I’ve done some market research.” He wants to pause development on the DnD game. “The kids are all into Pokemon Cards now, it’s the latest thing.” He guarantees “we can both retire with just one good Card Battle game.” He says you can probably even repurpose some of the logic you built for the battle engine to save time. He lays out the requirements for the proof of concept as follows:
    - Minimum 3 types of cards:
        - Hero card (Stays in play until health reaches 0, then is discarded)
            - Name
            - Description
            - Health
            - Strength
        - Spell Card (Immediately damages an enemy Hero or heals a friendly Hero, then is discarded)
            - Name
            - Description
            - Strength
        - Buff card (Provides a status modifier to all cards; stays in play until health reaches 0, then is discarded)
            - Name
            - Description
            - Health
    - Gameplay
        - There is one human player and one AI player
        - There are minimum 30 cards in the deck
        - Both players are dealt 7 cards
        - Maximum 7 cards in play at one time for each player
        - At the beginning of each Player’s round, that player’s cards in play perform an attack against a random card for the opponent. Vanquished cards are then discarded
        - Player chooses a card to put in play
            - If the card is a hero or a buff, it remains in play until vanquished
            - If the card is a spell, it performs its effect and is immediately discarded
        - Player automatically draws a new card

# Tasks to MVP 
- done - zach - create human and ai players
- done - zach - populate deck details
- done - roger - build the deck-in-play
- done - roger - populate player hand with initial 7 cards
- done - roger - populate ai_player hand with initial 7 cards
- done - roger - way to draw 1 card from the deck-in-play
- done - roger - player selects card to be played during the round
- done - zach - way to police the number of cards in the player's hand
- done - roger - ai_player selects card to be played during the round
- done - zach - track cards in play
- done - zach - UI for displaying player's hand to the human player
- done - roger - new card is drawn from deck at end of player's turn
- done - roger - game intro, explaining what's what
----------------------------------------------------------
- zach - selected card attacks other player's card in play, randomly selected
- once a card's health reaches zero, discard
- if spell card, apply it's effect then discard


