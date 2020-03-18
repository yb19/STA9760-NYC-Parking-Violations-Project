from elasticsearch import Elasticsearch


def create_and_update_index(index_name: str, doc_type: str):

	es = Elasticsearch()

	try:
		es.indices.create(index = index_name)
	except Exception:
		pass

	# es.indices.put_mapping(index = index_name, doc_type = doc_type)

	return es