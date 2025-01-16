"""
Description:
pipeline class

Requirements:
this pipeline class, needs to have the following methods:
    load
    warm_up
    predict
"""

import logging
from pipeline_base import PipelineBase as Base
import random

class ModelPipeline(Base):

    logger = logging.getLogger(__name__)

    @Base.track_exception(logger)
    def __init__(self, **kwargs):
        """
        init the pipeline with kwargs. To initialize self.results, call super().__init__()
        """
        self.logger.info("INIT")
        super().__init__()
        
        
    @Base.track_exception(logger)
    def load(self, configs):
        """
        create model instances with weight files
        if loading files fail, then don't create model instances
        """
        self.logger.info(f"CONFIGS {configs}")


    @Base.track_exception(logger)
    def warm_up(self, configs):
        """
        warm up all the models in the pipeline
        """
        self.logger.info(f"WARMUP")


    index = 0
    arr = ["Blister", "Crack", "Wane", "FishEye"]
    @Base.track_exception(logger)
    def predict(self, configs: dict, inputs: dict) -> dict:
        """predict on the inputs

        Args:
            configs (dict): runtime configs
            inputs (dict): inputs data

        Returns:
            dict: should return self.results defined in the pipeline base class
        """
        self.index += 1
        return {
            "outputs": {
                "annotated": inputs['image'],
            },
            "automation_keys": [ "decision", "color_data", "pair_data", "defect", "temp", "table_data"],
            "factory_keys":  ["tags", "decision"],
            "tags": ["round", "square"], 
            "should_archive": False,

            "decision": random.randint(0, 10),
            "color_data": [[random.randint(1, 60), "Yellow", [255,255,0]],[random.randint(1, 20), "Green", [34,139,34]],[random.randint(1, 20), "Blue", [30,144,255]]],
            "pair_data": [["Blister", random.randint(0, 5)], ["Crack", random.randint(0, 5)], ["Wane", random.randint(0, 5)], ["FishEye", random.randint(0, 5)]],
            "defect": self.arr[random.randint(0,3)],
            "table_data": {
                "Blister": random.randint(0, 10),
                "Crack": random.randint(0, 10),
                "Wane": random.randint(0, 10),
                "FishEye": random.randint(0, 10)
            },
            "temp": random.randint(0, 100)
        } 



if __name__ == '__main__':
    pass
