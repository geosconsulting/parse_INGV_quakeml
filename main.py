from fastapi import FastAPI
from x2030_quakes.fetch_webservice_data import WSDataSource
from x2030_quakes.fetch_lib_data import LibDataSource

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'get INGV data as webservice or with python library'}


@app.get("/all_quakes")
async def quakes_within_bbox():
    ws_instance = WSDataSource(response_format='text')
    ws_instance.start_date = None
    ws_instance.end_date = None

    ws_instance.build_query_url()
    ws_instance.fetch_events()
    df, json_df = ws_instance.transform_events_to_df()
    return json_df


@app.get("/quakes/{province}")
async def quakes_by_province(province: str):
    ws_instance = WSDataSource(response_format='text')
    ws_instance.start_date = None
    ws_instance.end_date = None
    ws_instance.build_query_url()
    ws_instance.fetch_events()
    df, df_json = ws_instance.transform_events_to_df()
    gdf = ws_instance.transform_events_to_geo_df(df)
    df_province, df_province_json = ws_instance.filter_events_by_province(gdf, province)
    return df_province_json


@app.get("/quakes_lib")
async def quakes_library():
    lib_instance = LibDataSource()
    data_collected = await lib_instance.fetch_data()

    return data_collected
