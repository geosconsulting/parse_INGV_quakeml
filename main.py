from x2030_quakes.fetch_webservice_data import WSDataSource


def main():
    ws_instance = WSDataSource(response_format='text')
    ws_instance.start_date = None
    ws_instance.end_date = None

    print(ws_instance.start_date)
    print(ws_instance.end_date)
    ws_instance.build_query_url()
    ws_instance.fetch_events()
    print(ws_instance.get_events())


if __name__ == '__main__':
    main()
