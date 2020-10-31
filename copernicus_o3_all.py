from api.sentinel import Sentinel5P
import os

from extractors.ozone_L2_O3 import CopernicusO3Extractor

ex = CopernicusO3Extractor()

def process_result(dirname, latitude_range, longitude_range):
    ex.process_files(
        dirname=dirname,
        out_file=dirname + "/result.csv",
        latitude_range=latitude_range,
        longitude_range=longitude_range,
        delete_after=True
    )


if __name__ == "__main__":
    api = Sentinel5P(config_name="SentinelAPI-O3")
    api.download_and_process(
        download_path=os.path.abspath('./data/O3/Lisbon/L2__O3____'),
        process_func=process_result
    )