import requests
import json
from pypercorn.utilities import Utilities


class Segmentation:
    def __init__(self):
        self.ip_server = "https://hypercornapi-1.azurewebsites.net"
        self.utilities = Utilities()

    def kmeans(self, image, as_bytes=False):
        files = self.utilities.decoding_file_image(image)
        response = json.loads(requests.post(url=f"{self.ip_server}/algorithms/images/segmentation/kmeans/",
                                            files=files, params={"as_bytes": as_bytes}).content)
        if "image" in response.keys() and type(response["image"]) == list:
            response = self.utilities.numpy_response(response, "image")
        return response

    def binarize(self, image, min_value, max_value, as_bytes=False):
        files = self.utilities.decoding_file_image(image)
        data_binarize = {"min_value": min_value, "max_value": max_value}
        response = json.loads(requests.post(url=f"{self.ip_server}/algorithms/images/segmentation/binarize/",
                                            files=files, data=data_binarize, params={"as_bytes": as_bytes}).content)
        if "image" in response.keys() and type(response["image"]) == list:
            response = self.utilities.numpy_response(response, "image")
        return response
