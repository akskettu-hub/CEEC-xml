from CEECxml import parse_tei_collection
from evaluation import evaluate_dir


if __name__ == "__main__":
    letters_to_print = [2]
    lettersd = {letter: True for letter in letters_to_print}

    ref = parse_tei_collection(
        "FTWINING.xml",
        print_letter_text=False,
        letters_to_print=lettersd,
        return_single_letter=True,
    )
    evaluate_dir(ref=ref, hyp_dir_path="eval")
