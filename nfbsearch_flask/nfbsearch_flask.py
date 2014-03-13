from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(["vmdev.nfb.ca:9200"])


@app.route("/search")
def search():
    query = request.args.get('q', None)
    if not query:
        return "please provide a q parameter"

    return jsonify(**es.search(index="nfb_films", doc_type="films", body={
        "query": {
            "bool": {
                "should": {
                    "query_string": {
                        "default_field": "_all",
                        "query": query
                    }
                }
            }
        }
    }))

app.run()