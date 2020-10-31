from api.modis import Modis
import os

from extractors.aerosol_mcd19a2 import AerosolMCD19A2

ex = AerosolMCD19A2()

def process_result(dirname, latitude_range, longitude_range):
    ex.process_files(
        dirname=dirname,
        out_file=dirname + "/result.csv",
        latitude_range=latitude_range,
        longitude_range=longitude_range,
        delete_after=True
    )


if __name__ == "__main__":
    api2 = Modis(config_name="ModisAPI-MCD19A2")
    api2.download_and_process(
        download_path=os.path.abspath('./data/PM2.5/Lisbon/MCD19A2'),
        process_func=process_result
    )