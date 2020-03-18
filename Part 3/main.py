import logging
import os
import sys
from time import sleep
from datetime import datetime
from src.bigdata1.get_nycdata import get_client, validate_num_pages
from src.bigdata1.get_elasticsearch import create_and_update_index


logging.basicConfig(filename="./logs.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)


DATA_URL = "data.cityofnewyork.us"
DATA_ID  = "nc67-uf89"


def parse_args() -> dict:

    opts = {}
    args = sys.argv[1:]

    for arg in args:
        try:
            argname, argval = arg.split('=')
        except ValueError:
            logger.warn("Failed to split {arg} along '=', "
                        "assuming to be a boolean.")
            argname = arg
            argval = True
        except Exception:
            continue

        if argname.startswith('--'):
            argname = argname[2:]

        opts[argname] = argval

    return opts


def convert_data_type(item):

    assert type(item) is dict

    for key, value in item.items():

        if 'date' in key:
            item[key] = datetime.strptime(value, '%m/%d/%Y')
        elif 'number' in key:
            item[key] = int(value)
        elif 'amount' in key:
            item[key] = float(value)

    return item


if __name__ == '__main__':
    
    es = create_and_update_index('bigdata1', 'parkviolates')
    
    opts = parse_args()
    client = get_client(DATA_URL, os.environ['APP_TOKEN'])

    page_size = int(opts.get('page_size', 1000))
    num_pages = validate_num_pages(opts, page_size)

    i = 0
    logger.debug("Begin processing of data for "
                 f"page_size: {page_size} and num_pages: {num_pages}")
    
    while i < num_pages:
        
        resp = client.get(DATA_ID, limit = page_size, offset = i * page_size)
        logger.debug(f"Processed page {i+1}, limit={page_size} and "
                     f"offset={i*page_size}")

        i += 1
        write_to_file = 'output' in opts
        if write_to_file:
            with open(opts['output'], 'a+') as fh:
                for item in resp:
                    fh.write(f"{str(item)}\n")

        for item in resp:
        	item = convert_data_type(item)
        	res = es.index(index = 'bigdata1', doc_type = 'parkviolates', body = item,)
        	print(res['result'])

        print(f"DONE LOADING {i}, SLEEPING...")
        sleep(10)
        	
