from biobox_analytics.data.adapters._base import Adapter
# import biobox_analytics.data.adapters.chipseq._structs as structs
import pandas as pd
import math
import gzip
import os
import json
import datetime
from nanoid import generate

class RnaSeqSingleExpressionAdapter(Adapter):
    def __init__(
        self,
        name: str,
        sample_id: str,
        sgc_filepath: str,
        noHeader: bool = False,
        objects_file: str = "objs.jsonl.gz",
        edges_file: str = "edges.jsonl.gz",
    ):
        super().__init__()
        self.name = name
        self.sample_id = sample_id
        self.sgc_filepath = sgc_filepath
        self.noHeader = noHeader
        self.objects_file = objects_file
        self.edges_file = edges_file
        self.rnaseq_id = generate()

        self.nodes = []
        self.edges = []

    def pull_data(self):
        if (self.noHeader):
            self.df = pd.read_csv(self.sgc_filepath, sep=None, engine='python', header=None)
        else:
            self.df = pd.read_csv(self.sgc_filepath, sep=None, engine='python')
    
    def iterate_nodes(self):
        return self.df.iterrows()
    
    def iterate_edges(self):
        return super().iterate_edges()
    
    def process_item(self, item):
        geneID = item.get(0)
        RAW = item.get(1)
        TPM = item.get(2)
        properties = {
            "RAW": RAW,
            "TPM": TPM
        }

        expresses = {
            "label": "expresses",
            "from": {
                "uuid": self.sample_id
            },
            "to": {
                "uuid": geneID
            },
            "properties": properties
        }

        return [
            expresses
        ]
    
    def describe_node_properties(self):
        return super().describe_node_properties()
    
    def describe_edge_properties(self):
        return super().describe_edge_properties()
    
    def extra_items(self):
        sample = {
            "_id": self.sample_id,
            "labels": [ "Sample" ],
            "properties": {
                "uuid": self.sample_id
            }
        }

        return [
            sample,
        ]
    
    def build(self):
        self.pull_data()
        iterator = self.iterate_nodes()
        for object in self.extra_items():
            print(object)

        for _, row in iterator:
            objects = self.process_item(row)
            for object in objects:
                print(object)

    def write(self):
        obs_file = os.path.join("", self.objects_file)
        edges_file = os.path.join("", self.edges_file)
        with gzip.open(obs_file, "at") as o, gzip.open(edges_file, "at") as e:
            self.pull_data()
            iterator = self.iterate_nodes()
            for object in self.extra_items():
                if "from" in object:
                    json.dump(object, e)
                    e.write("\n")
                else:
                    json.dump(object, o)
                    o.write("\n")

            for _, row in iterator:
                objects = self.process_item(row)
                for object in objects:
                    if "from" in object:
                        json.dump(object, e)
                        e.write("\n")
                    else:
                        json.dump(object, o)
                        o.write("\n")

    def list_schema(self):
        metadata = {
            "_meta": {
                "version": "0.0.1",
                "date_updated": str(datetime.datetime.now()),
            },
            "name": self.name,
            "key": self.name, 
            "description": "",
            "concepts": {
                "Sample": {
                    "label": "Sample",
                    "dbLabel": "Sample",
                    "definition": "Any material sample taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes, including a sample obtained from a living organism or taken from the biological object after halting of all its life functions. Biospecimen can contain one or more components including but not limited to cellular molecules, cells, tissues, organs, body fluids, embryos, and body excretory products.",
                }
            },
            "relationships": {
                "expresses": {
                    "from": "Sample",
                    "to": "Gene"
                }
            }
        }
        return metadata
