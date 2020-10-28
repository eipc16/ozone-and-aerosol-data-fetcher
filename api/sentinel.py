from api import API
from api.config import load_config, get_credentials

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

class Sentinel5P(API):
    CONFIG_PATH = "./config/config.json"

    def __init__(self, config_name="SentinelAPI"):
        self._config = load_config(Sentinel5P.CONFIG_PATH, config_name)
        self._defaults = self._config['default']
        self._api_link = self._config['api_link']
        user, password = get_credentials(self._config)
        self._api = SentinelAPI(user, password, self._api_link)

    def download(self, 
                download_path,
                area_gjson=None, 
                date_from=None, 
                date_to=None, 
                platform_name=None, 
                product_type=None):
        area = API.get_default_if_empty(area_gjson, self._defaults['area'])
        products = self._api.query(
            geojson_to_wkt(area) if area is not None else None,
            date=self._parse_date(
                API.get_default_if_empty(date_from, self._defaults['time']['start']), 
                API.get_default_if_empty(date_to, self._defaults['time']['end'])
            ),
            platformname=API.get_default_if_empty(platform_name, self._defaults['platform_name']),
            producttype=API.get_default_if_empty(product_type, self._defaults['product_type'])
        )
        self._api.download_all(products, directory_path=download_path)

    def _parse_date(self, date_from, date_to):
        return (date_from.replace('-', ''), date_to.replace('-', ''))

    def get_info(self):
        return {
            "config": self._config,
            "api_link": self._api_link
        }
