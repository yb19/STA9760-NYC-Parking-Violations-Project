from sodapy import Socrata
from math import ceil


def get_client(url: str, app_token: str) -> Socrata:

    return Socrata(url, app_token)


def validate_num_pages(opts: dict, page_size: int) -> int:

    try:
        return int(opts['num_pages'])
    except KeyError:
        logger.warn("No option called 'num_pages' found! "
                    "Attempting to calculate from COUNT of all rows")
    except Exception as e:
        logger.warn("Failed to process num_pages. Here is why: "
                    f"{e}. Attempting to calculate from COUNT of all rows")

    try:
        results = client.get(DATA_ID, select='COUNT(*)')
        total = int(results[0]['COUNT'])
        return ceil(total / page_size)
    except Exception as e:
        logger.warn(f"Failed to count total: {e} "
                    "Stopping script and raising exception")
        raise
