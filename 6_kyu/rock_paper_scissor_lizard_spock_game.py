# To increase the odds of the old fashioned game (Rock, Paper, Scissors) Sam Kass and Karen Bryla
# reinvented the game with 5 different items instead of 3: Rock, Paper, Scissor, Lizard, Spock. It
# was later also featured in the sitcom "The Big Bang Theory".

# Game Rules

# See image in Kata

# Examples

# "rock", "spock"       -->  "Player 2 won!"      because Spock vaporizes rock
# "scissor", "lizard"   -->  "Player 1 won!"      because scissor decapitates lizard
# "scissor", "Scissor"  -->  "Draw!"              because they are the same
# "foo", "Bar"          -->  "Oh, Unknown Thing"  because they are not valid


def result(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()

    losing_states_for_player_one = {
        "rock": ["spock", "paper"],
        "paper": ["scissor", "lizard"],
        "scissor": ["spock", "rock"],
        "lizard": ["scissor", "rock"],
        "spock": ["paper", "lizard"],
    }

    if set([p1, p2]) <= set(losing_states_for_player_one.keys()):
        if p1 == p2:
            result = "Draw!"
        else:
            player_two_states_that_confirm_player_one_loses = losing_states_for_player_one[p1]

            if p2 in player_two_states_that_confirm_player_one_loses:
                result = "Player 2 won!"
            else:
                result = "Player 1 won!"
    else:
        result = "Oh, Unknown Thing"

    return result
