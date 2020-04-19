from lib.composite.components.component import Component

"""
curl -X POST http://localhost:8501/v1/models/saved_model:predict -d \
       '{"instances": [ [ \
                          0.3, -1.4, 0.8, -0.1, -0.9, -0.3, -1.0, \
                          -0.7, -0.6, -0.3, 0.6, -0.7, -0.4 ] ] \
        }'

"""

class ServeRequest(Component):
  def __init(self):
    pass

  def operation(self, obj):
    pass
