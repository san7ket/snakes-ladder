import pytest
import snakes_ladder as game

snakes = {14: 7, 23: 17, 45: 5, 51: 33, 99: 24}

ladder = {8: 29, 22: 61, 54: 68, 66: 97, 72: 93}


def test_run(mocker):
    mocker = mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    assert (game.snakesladder({}, {}))


@pytest.mark.parametrize("input_entry,expected", [(True, [2, 4, 6]), (False, [1, 2, 3, 4, 5, 6])])
def test_dice_roll(mocker, input_entry, expected):
    mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    dice = game.snakesladder({}, {}).dice_roll(crooked=input_entry)
    assert dice in expected


@pytest.mark.parametrize("snake_entry,", (list(snakes.keys())))
def test_snake(mocker, snake_entry):
    mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    position = game.snakesladder(snakes, ladder).check_snake(snake_entry)
    assert position == snakes.get(snake_entry)


@pytest.mark.parametrize("ladder_entry,", (list(ladder.keys())))
def test_ladder(mocker, ladder_entry):
    mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    position = game.snakesladder(snakes, ladder).check_ladder(ladder_entry)
    assert position == ladder.get(ladder_entry)


@pytest.mark.parametrize("crook", [True, False])
def test_core_logic(mocker, crook):
    mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    assert game.snakesladder(snakes, ladder).run(crook) <= 100


@pytest.mark.parametrize("pos", range(90, 105))
def test_status_check(mocker, pos):
    mocker.patch('builtins.input', mocker.mock_open(read_data="apple"))
    state = game.snakesladder(snakes, ladder).check_status(pos, 8)
    if pos >= 100:
        assert state
    else:
        assert not state
