'''Generate database from data files.'''

import json
import polars as pl


def db(options):
    '''Main driver.'''
    url = f'sqlite:///{options.dbfile}'

    csv_to_db(url, 'sample', options.samples)
    csv_to_db(url, 'site', options.sites)
    csv_to_db(url, 'survey', options.surveys, 'survey_id', 'site_id', 'date')

    assays = json.load(open(options.assays, 'r'))
    json_to_db(url, assays, 'staff')
    json_to_db(url, assays, 'experiment')
    json_to_db(url, assays, 'performed')
    json_to_db(url, assays, 'plate')
    json_to_db(url, assays, 'invalidated')


def csv_to_db(url, name, source, *columns):
    '''Create table from CSV.'''
    df = pl.read_csv(source)
    if columns:
        df = df[list(columns)]
    df.write_database(name, url, if_table_exists='replace')


def json_to_db(url, data, name):
    '''Create table from JSON.'''
    df = pl.DataFrame(data[name])
    df.write_database(name, url, if_table_exists='replace')
