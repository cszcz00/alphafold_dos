# PDB Search API Documentation: https://search.rcsb.org/#search-api
import requests

query = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
        {
            "type": "terminal",
            "service": "text",
            "parameters": {
            "attribute": "rcsb_entry_info.resolution_combined",
            "operator": "less_or_equal",
            "value": 2
            }
        },
        {
            "type": "terminal",
            "service": "text",
            "parameters": {
            "attribute": "rcsb_entry_info.structure_determination_methodology",
            "value": "experimental",
            "operator": "exact_match"
            }
        },
        {
            "type": "group",
            "nodes": [
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                "attribute": "entity_poly.rcsb_entity_polymer_type",
                "value": "Protein",
                "operator": "exact_match"
                }
            },
            {
                "type": "group",
                "logical_operator": "and",
                "nodes": [
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                    "attribute": "rcsb_polymer_instance_annotation.annotation_lineage.name",
                    "value": "All alpha proteins",
                    "operator": "exact_match"
                    }
                },
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                    "attribute": "rcsb_polymer_instance_annotation.type",
                    "operator": "exact_match",
                    "value": "SCOP"
                    }
                }
                ],
                "label": "nested-attribute"
            }
            ],
            "logical_operator": "and"
        }
        ],
        "label": "text"
    },
    "return_type": "entry",
    "request_options": {
        "return_all_hits": True
    }
    }

url = "https://search.rcsb.org/rcsbsearch/v2/query"

response = requests.post(url, json=query)

if response.status_code == 200:
    data = response.json()
    for result in data.get('result_set', []):
        print(result['identifier'])
else:
    print(f"Request failed with status code {response.status_code}")

