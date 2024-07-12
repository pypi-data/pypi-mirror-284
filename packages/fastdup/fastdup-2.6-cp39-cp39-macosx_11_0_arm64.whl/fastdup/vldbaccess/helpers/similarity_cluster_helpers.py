from typing import Mapping

EPS = 0.1


def get_distance_from_similarity_row(row: Mapping):
    if "distance" in row:
        distance = row["distance"]
    elif "img_relevance" in row:
        distance = 1 / (row["img_relevance"] + EPS)
    else:
        distance = None
    return distance
