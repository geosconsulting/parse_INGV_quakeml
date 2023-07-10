from fastapi import FastAPI
from x2030_quakes.fetch_webservice_data import WSDataSource

app = FastAPI()
@app.get("/")
async def root():
    ws_instance = WSDataSource(response_format='text')
    ws_instance.start_date = None
    ws_instance.end_date = None

    ws_instance.build_query_url()
    ws_instance.fetch_events()
    df = ws_instance.transform_events_to_df()
    return df
