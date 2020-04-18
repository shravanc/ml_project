from lib.composite.components.component import Component

"""
tensorflow_model_server \
 --rest_api_port="8501" \
 --model_name="saved_model" \
 --model_base_path="/home/shravan/tf/all_models/temp/serving_model/"

"""


class LaunchPredictionService(Component):
  def __init__(self):
    pass

  def operation(self, obj):
    pass
