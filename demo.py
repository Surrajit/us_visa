'''
import os
mongo_db_url = os.getenv("MONGODB_URL")
print(mongo_db_url)

'''

from src.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()