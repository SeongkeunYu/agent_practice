from game import Game


def test_gutter_game():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_all_ones():
    game = Game()
    for _ in range(20):
        game.roll(1)
    assert game.score() == 20


def test_one_spare():
    game = Game()
    game.roll(5)
    game.roll(5)  # spare
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.score() == 16


def test_one_strike():
    game = Game()
    game.roll(10)  # strike
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 24


def test_perfect_game():
    game = Game()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300
