from CEECxml import parse_tei_collection
from evaluation import evaluate_dir
from CEEC_400_data_parser import construct_xml_path_dict


if __name__ == "__main__":
    letters_to_print = [2]
    lettersd = {letter: True for letter in letters_to_print}
    xml_path_dict = construct_xml_path_dict(data_path="./data/CEEC-400/")
    tei_collection_id = "FTWINING"
    tei_collection_path = xml_path_dict[tei_collection_id]

    ref = parse_tei_collection(
        tei_collection_path,
        print_letter_text=True,
        letters_to_print=lettersd,
        return_single_letter=True,
    )

    if ref is not None:
        evaluate_dir(ref=ref, hyp_dir_path="eval", write_to_csv=True)
