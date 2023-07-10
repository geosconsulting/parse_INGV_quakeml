from datetime import datetime
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from dateutil.relativedelta import relativedelta
from typing import List
import pandas as pd
import geopandas as gpd


class WSDataSource(object):
    def __init__(self, lat: float = 41.76337, lon: float = 12.33078, radius_km: int = 200, response_format: str = ''):

        self.provinces_gdf = gpd.read_file('gis_files/provinces.geojson')
        self.url_root = 'http://webservices.ingv.it/fdsnws/event/1/query?'
        self._start_date = None
        self._end_date = None
        self.lat = lat
        self.lon = lon
        self.minimum_magnitude = 2.0
        self.min_radius_km = 0.1
        self.max_radius_km = radius_km
        self.min_latitude_bbox = 35.0
        self.max_latitude_bbox = 49.0
        self.min_longitude_bbox = 5.0
        self.max_longitude_bbox = 20.0
        self.response_format = response_format
        self.query_string = None
        self.events = None

    def get_provinces(self):
        return self.provinces_gdf

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        if start_date is None:
            self._start_date = (datetime.utcnow() + relativedelta(months=-1)).strftime('%Y-%m-%dT00:00:00')

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        if end_date is None:
            self._end_date = datetime.now(tz=datetime.now().astimezone().tzinfo).strftime('%Y-%m-%dT%H:%M:%S')

    def build_query_url(self, search_method='buffer') -> str:

        query_string = f'{self.url_root}starttime={self.start_date}&endtime={self.end_date}' \
                       f'&minmag={self.minimum_magnitude}&format={self.response_format}'

        if search_method == 'buffer':
            query_string = f'{query_string}&lat={self.lat}&lon={self.lon}' \
                        f'&minradiuskm={self.min_radius_km}&maxradiuskm={self.max_radius_km}'

        elif search_method == 'bbox':
            query_string = f'{query_string}&minlatitude={self.min_latitude_bbox}' \
                           f'&maxlatitude={self.max_latitude_bbox}' \
                           f'&minlongitude={self.min_longitude_bbox}&maxlongitude={self.max_longitude_bbox}'

        self.query_string = query_string

    def fetch_events(self) -> None:
        if self.response_format != 'xml':
            self.events = urlopen(self.query_string).readlines()
        self.events = urlopen(self.query_string)

    def get_events(self) -> List[str]:
        if self.response_format != 'xml':
            return self.events
        return ET.parse(self.events)

    def transform_events_to_df(self):
        columns = self.events[0]
        cols = [col for col in str(columns).lstrip("b'#").split("|")]
        cols[-1] = cols[-1][:-3]

        coded_events = []
        for i in range(1, len(self.events)):
            event = str(self.events[i]).lstrip("b'").split("|")
            event[-1] = event[-1][:-3]
            coded_events.append(event)

        df = pd.DataFrame(coded_events, columns=cols)

        return df

    @staticmethod
    def transform_events_to_geo_df(df: pd.DataFrame) -> gpd.GeoDataFrame:
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326")
        return gdf

    def filter_events_by_province(self, df: pd.DataFrame, province: str) -> gpd.GeoDataFrame:
        joined = gpd.sjoin(left_df=df, right_df=self.provinces_gdf, how='left')
        list(joined['adm2_name'].unique())
        return joined.loc[joined['adm2_name'] == province]

    def process_xml_response(self):
        ns = {'q': "http://quakeml.org/xmlns/quakeml/1.2",
              'g': "http://quakeml.org/xmlns/bed/1.2",
              'i': "http://webservices.ingv.it/fdsnws/event/1"
              }
