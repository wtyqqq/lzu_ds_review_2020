from collections import Counter

ONCE, MANY = '(', ')'


def parse(text: str) -> str:
    normalized_text = text.lower()
    letter_counter = Counter(normalized_text)

    result: str = normalized_text
    for letter in normalized_text:
        result = result.replace(
            letter,
            MANY if letter_counter.get(letter) > 1 else ONCE
        )

    return result


if __name__ == '__main__':
    print(parse("din"))
    print(parse("recede"))
    print(parse("Success"))
    print(parse("(( @"))
