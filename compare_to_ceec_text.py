from CEECxml import parse_tei_collection


if __name__ == "__main__":
    letters_to_print = [24]
    lettersd = {letter: True for letter in letters_to_print}

    res = parse_tei_collection(
        "FTWINING.xml",
        print_letter_text=False,
        letters_to_print=lettersd,
        return_single_letter=True,
    )

    print(res)
