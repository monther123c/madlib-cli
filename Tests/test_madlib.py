import pytest
import madlib_cli.madlib as game

# Read Template test for   assets/dark_and_stormy_night_template.txt


def test_read_template_returns_stripped_string():
    actual = game.read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

# Read Template test for    assets/make_me_a_video_game_template.txt


def test_read_template_returns_stripped_string_make_me_a_video_game():
    actual = game.read_template("assets/make_me_a_video_game_template.txt")
    expected = '''Make Me A Video Game!
I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!
What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.'''
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = game.parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_parse_template_make_me_a_video():
    actual_stripped, actual_parts = game.parse_template(
        '''Make Me A Video Game!
I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!
What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.'''
    )
    expected_stripped = '''Make Me A Video Game!
I the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!
What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {}'s Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.'''
    expected_parts = ('Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal',
                      "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', 'First Name', 'Number', 'Plural Noun', 'Number', 'Plural Noun')

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
# test merge for assets/dark_and_stormy_night_template.txt
def test_merge():
    actual = game.merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        game.read_template(path)