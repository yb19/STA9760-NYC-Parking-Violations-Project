from sodapy import Socrata
from requests import HTTPError

def get_nycdata(YOUR_APP_KEY: str, page_size: int, num_pages: int = -1) -> list:

	assert type(YOUR_APP_KEY) is str
	assert type(page_size) is int

	try:
		client = Socrata("data.cityofnewyork.us", YOUR_APP_KEY)
		result = []
		
		if num_pages == -1:
			i = 0
			while True:
				r = client.get("nc67-uf89", limit = page_size, offset = page_size * i)
				result.append(r)
				if len(r) < page_size:
					break
				i += 1

		else:
			assert type(num_pages) is int
			for i in range(num_pages):
				r = client.get("nc67-uf89", limit = page_size, offset = page_size * i)
				result.append(r)
				if len(r) < page_size:
					break
		
		return result

	except HTTPError as e:
		print(f"Failed to make API call: {e}")
		raise

	except Exception as e:
		print(f"Something went wrong: {e}")
		raise
