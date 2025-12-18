import os
from CEECxml import get_tei_collection_id


def list_files_recursive(path: str, xml_path_l: list):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path, xml_path_l)
        elif entry.endswith(".xml"):
            xml_path_l.append(full_path)

    return xml_path_l


def construct_xml_path_dict(data_path: str):
    l = []
    xml_paths = list_files_recursive(path=data_path, xml_path_l=l)
    print(len(xml_paths))

    tei_collection_path_d = {}
    for path in xml_paths:
        teiId = get_tei_collection_id(path)
        tei_collection_path_d[teiId] = path
    return tei_collection_path_d


if __name__ == "__main__":
    l = []
    d = construct_xml_path_dict(data_path="./data/CEEC-400/")
    len(d.keys())
    # xmls = list_files_recursive(path="./data/CEEC-400/", xml_path_l=l)
