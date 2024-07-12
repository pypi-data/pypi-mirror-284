from biobox_analytics.data.adapters._base import Adapter
# import biobox_analytics.data.adapters.chipseq._structs as structs
import pandas as pd
import math
import gzip
import os
import json
import datetime
from nanoid import generate

class RnaSeqDiffExpAdapter(Adapter):
    def __init__(
        self,
        name: str,
        description: str,
        exp_group_ids,
        ref_group_ids,
        diffexp_filepath: str,
        geneIDColName: str,
        logRColName: str,
        padjColName: str,
        objects_file: str = "objs.jsonl.gz",
        edges_file: str = "edges.jsonl.gz",
        diffexp_id = generate(),
    ):
        super().__init__()
        self.name = name
        self.description = description
        self.exp_group_ids = exp_group_ids
        self.ref_group_ids = ref_group_ids
        self.diffexp_filepath = diffexp_filepath
        self.geneIDColName = geneIDColName
        self.logRColName = logRColName
        self.padjColName = padjColName
        self.objects_file = objects_file
        self.edges_file = edges_file
        self.diffexp_id = diffexp_id

        self.nodes = []
        self.edges = []

    def pull_data(self):
        self.df = pd.read_csv(self.diffexp_filepath, sep=None, engine='python')
    
    def iterate_nodes(self):
        return self.df.iterrows()
    
    def iterate_edges(self):
        return super().iterate_edges()
    
    def process_item(self, item):
        geneID = item.get(self.geneIDColName)
        padj = item.get(self.padjColName)
        logR = item.get(self.logRColName)
        properties = {
            "logR": logR,
            "padj": padj
        }

        if logR > 0:
            diffexpresses = {
                "label": "upregulates",
                "from": {
                    "uuid": self.diffexp_id
                },
                "to": {
                    "uuid": geneID
                },
                "properties": properties
            }
            return [
                diffexpresses
            ]
        
        elif logR < 0:
            diffexpresses = {
                "label": "downregulates",
                "from": {
                    "uuid": self.diffexp_id
                },
                "to": {
                    "uuid": geneID
                },
                "properties": properties
            }
            return [
                diffexpresses
            ]
    
    def describe_node_properties(self):
        return super().describe_node_properties()
    
    def describe_edge_properties(self):
        return super().describe_edge_properties()
    
    def extra_items(self):
        items = []
        diffexp_dataset = {
            "_id": self.diffexp_id,
            "labels": [ "DifferentialExpressionDataset" ],
            "properties": {
                "uuid": self.diffexp_id,
                "displayName": self.name,
                "description": self.description

            }
        }

        items.append(diffexp_dataset)

        for expID in self.exp_group_ids:
            item = {
                "_id": expID,
                "labels": [ "TumorSample", "Sample" ],
                "properties": {
                    "uuid": expID,
                }
            }
            items.append(item)
            connect = {
                "label": "experimental group includes",
                "from": {
                    "uuid": self.diffexp_id
                },
                "to": {
                    "uuid": expID
                }
            }
            items.append(connect)
        
        for refID in self.ref_group_ids:
            item = {
                "_id": refID,
                "labels": [ "NormalSample", "Sample" ],
                "properties": {
                    "uuid": refID,
                }
            }
            items.append(item)
            connect = {
                "label": "reference group includes",
                "from": {
                    "uuid": self.diffexp_id
                },
                "to": {
                    "uuid": refID
                }
            }
            items.append(connect)

        return items
    
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
            "description": "Differential expression dataset containing logR, padj, and ensembl gene ids",
            "concepts": {
                "Sample": {
                    "label": "Sample",
                    "dbLabel": "Sample",
                    "definition": "Any material sample taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes, including a sample obtained from a living organism or taken from the biological object after halting of all its life functions. Biospecimen can contain one or more components including but not limited to cellular molecules, cells, tissues, organs, body fluids, embryos, and body excretory products.",
                },
                "TumorSample": {
                    "label": "Tumor Sample",
                    "dbLabel": "TumorSample",
                    "definition": "A biological sample from a pathology diagnosed tumor",
                },
                "NormalSample": {
                    "label": "Normal Sample",
                    "dbLabel": "NormalSample",
                    "definition": "A sample of tissue or bio-molecules taken from a healthy tissue. Can be peripheral too disease tissue, or extracted from elsewhere in patient body",
                },
                "Differential Expression Dataset": {
                    "label": "Differential Expression Dataset",
                    "dbLabel": "DifferentialExpressionDataset",
                    "definition": "A file that contains a collection of differential gene expression observations. It must have connected reference and experimental factors that explain how the contrast was generated",
                }
            },
            "relationships": {
                "experimental group includes": {
                    "from": "DifferentialExpressionDataset",
                    "to": "Sample"
                },
                "reference group includes": {
                    "from": "DifferentialExpressionDataset",
                    "to": "Sample"
                },
                # "differentially expresses": {
                #     "from": "DifferentialExpressionDataset",
                #     "to": "Gene"
                # },
                "downregulates": {
                    "from": "DifferentialExpressionDataset",
                    "to": "Gene"
                },
                "upregulates": {
                    "from": "DifferentialExpressionDataset",
                    "to": "Gene"
                }
            }
        }
        return metadata
