import asyncio
from aiohttp import ClientSession
from aio_quakeml_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiQuakeMLFeed
import pandas as pd
import geopandas as gpd
from datetime import datetime, timedelta


class LibDataSource(object):
    def __init__(self, lat: float = 41.76337, lon: float = 12.33078, radius_km: int = 800,
                 filter_minimum_magnitude: int = 2.0):
        self.lat = lat
        self.lon = lon
        self.radius_km = radius_km
        self.filter_minimum_magnitude = filter_minimum_magnitude

    def __str__(self):
        pass

    def __repr__(self, other):
        pass

    async def fetch_data(self):
        async with ClientSession() as web_session:
            feed = IngvCentroNazionaleTerremotiQuakeMLFeed(web_session, home_coordinates=(self.lat, self.lon),
                                                           filter_radius=self.radius_km,
                                                           filter_minimum_magnitude=self.filter_minimum_magnitude)
            status, entries = await feed.update()
            for_mapping = []
            # if entries:
            #     return entries
                # for entry in entries:
                #     lat_q, lon_q = entry.coordinates
                #     for_mapping.append([lat_q, lon_q, entry.magnitude.mag, entry.description, entry.distance_to_home])
            # Create the pandas DataFrame
            # df = pd.DataFrame(for_mapping, columns=['Latitude', 'Longitude', 'Magnitude', 'Description', 'Distance'])

        # return for_mapping

        return entries
