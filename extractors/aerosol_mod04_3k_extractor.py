from extractors import BaseModisExtractor

import numpy as np
from datetime import datetime

class AerosolM0D043KExtractor(BaseModisExtractor):
    START_TIME = np.datetime64(datetime.strptime("1993-01-01 00:00:00.0", "%Y-%m-%d %H:%M:%S.%f"))
    MIN_QA_FLAG = 2
    LAND_FLAGS = {
        0: 'Ocean',
        1: 'Land',
        2: 'Coastal',
        -9999: 'Unknown'
    }
    QUALITY_FLAGS = {
        0: 'Bad',
        1: 'Marginal',
        2: 'Good',
        3: 'Very Good'
    }

    def __init__(self):
        self._extractor_config = AerosolM0D043KExtractor.get_extractor_config()

    def _process_file(self, dataset, latitude_range, longitude_range):
        return super()._get_json_data(
            dataset=dataset,
            data_instructions=self._extractor_config,
            latitude_range=latitude_range,
            longitude_range=longitude_range,
            qa_flag_name='Land_Ocean_Quality_Flag',
            min_qa_flag=AerosolM0D043KExtractor.MIN_QA_FLAG
        )

    @staticmethod
    def get_extractor_config():
        return {
            'Scan_Start_Time': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: 'Time UTC+0',
                'value_transform_func': lambda xs: list(map(lambda x: AerosolM0D043KExtractor.START_TIME + np.timedelta64(int(x), 's'), xs))
            },
            'Latitude': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x
            },
            'Longitude': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x
            },
            'Optical_Depth_Land_And_Ocean': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x
            },
            'Image_Optical_Depth_Land_And_Ocean': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x  
            },
            'Corrected_Optical_Depth_Land': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x,
                'solutions': {
                    0: '0.47 microns',
                    1: '0.55 microns',
                    2: '0.66 microns'
                }
            },
            'Corrected_Optical_Depth_Land_wav2p1': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x  
            },
            'Land_Ocean_Quality_Flag': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: [f'{i} ({AerosolM0D043KExtractor.QUALITY_FLAGS[i]})' for i in x]
            },
            'Land_sea_Flag': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: [f'{i} ({AerosolM0D043KExtractor.LAND_FLAGS[i]})' for i in x]
            },
            'Topographic_Altitude_Land': {
                'column_name_func': lambda x: x.long_name,
                'units_func': lambda x: x.units,
                'value_transform_func': lambda x: x
            }
        }