def parse_decklist(text: str) -> list[tuple[int, str]]:
    """Parse simple lines such as '1 Sol Ring' or '1x Sol Ring'."""
    cards = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        first, sep, rest = line.partition(" ")
        if not sep:
            continue
        count_text = first.lower().removesuffix("x")
        try:
            count = int(count_text)
        except ValueError:
            continue
        cards.append((count, rest.strip()))
    return cards
