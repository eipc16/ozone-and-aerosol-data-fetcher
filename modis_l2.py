from api.modis import Modis
import os

from extractors.aerosol_mod04_l2_extrator import AerosolMOD04L2Extractor

ex = AerosolMOD04L2Extractor()

def process_result(dirname, latitude_range, longitude_range):
    ex.process_files(
        dirname=dirname,
        out_file=dirname + "/result.csv",
        latitude_range=latitude_range,
        longitude_range=longitude_range,
        delete_after=True
    )


if __name__ == "__main__":
    api2 = Modis(config_name="ModisAPI-MOD04_L2")
    api2.download_and_process(
        download_path=os.path.abspath('./data/PM2.5/Lisbon/MOD04_L2'),
        process_func=process_result
    )