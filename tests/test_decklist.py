from edh_sim.cards.decklist import parse_decklist


def test_parse_decklist():
    assert parse_decklist("1 Sol Ring\n2x Island") == [(1, "Sol Ring"), (2, "Island")]
