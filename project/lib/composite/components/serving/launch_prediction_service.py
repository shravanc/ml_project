from lib.composite.components.component import Component
import os

"""
tensorflow_model_server \
 --rest_api_port="8501" \
 --model_name="saved_model" \
 --model_base_path="/home/shravan/tf/all_models/temp/serving_model/"
"""

#OR

#curl -X POST http://localhost:8501/v1/models/saved_model:predict -d '{"instances": [ [ 0.3, -1.4, 0.8, -0.1, -0.9, -0.3, -1.0,  -0.7, -0.6, -0.3, 0.6, -0.7, -0.4] ] }'


class LaunchPredictionService(Component):
  PORT="8501"
  MODEL_NAME="saved_model"
  MODEL_BASE_PATH="/home/shravan/tf/all_models/temp/serving_model/"

  def __init__( self,
                port=PORT,
                model_name=MODEL_NAME,
                model_base_path=MODEL_BASE_PATH):
    self.port             = port
    self.model_name       = model_name
    self.model_base_path  = model_base_path

  def operation(self, obj):
    print("---LaunchPredictionService---")
    self.__launch_prediction_service()
    return self

  def __launch_prediction_service(self):
    command = "nohup tensorflow_model_server " + \
              f"--rest_api_port={self.port} " + \
              f"--model_name={self.model_name} "+ \
              f"--model_base_path={self.model_base_path} " + \
              f"> /tmp/tf_serving &" 

    print("***Launching***", command)
    os.system(
      command
    )    

