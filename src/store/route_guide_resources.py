"""Common resources used in the gRPC route guide example."""

import json
import os
from proto import route_guide_pb2
from creds import credentials
from utils.file import absolute_file_path


def read_route_guide_database():
    """Reads the route guide database.

    Returns:
      The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """

    feature_list = []
    DATA_DIR = os.getenv('DATA_DIR')
    DATA_JSON_FILE = os.getenv('DATA_JSON_FILE')
    data_json_file_path = absolute_file_path(os.path.join(DATA_DIR, DATA_JSON_FILE))

    with open(data_json_file_path) as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = route_guide_pb2.Feature(
                name=item["name"],
                location=route_guide_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"],
                ),
            )
            feature_list.append(feature)
    return feature_list
