from lib.composite.composite import Composite
# https://www.tensorflow.org/tutorials/structured_data/feature_columns
# https://www.tensorflow.org/tutorials/keras/regression
# https://www.tensorflow.org/tutorials/keras/overfit_and_underfit

# Branch 1
from lib.composite.components.etl.download  import Download
from lib.composite.components.etl.extract   import Extract
from lib.composite.components.etl.transform import Transform
from lib.composite.components.etl.load      import Load


# Branch 2
from lib.composite.components.eda.analyse     import Analyse
from lib.composite.components.eda.preprocess  import Preprocess
from lib.composite.components.eda.impute      import Impute
from lib.composite.components.eda.split       import Split
from lib.composite.components.eda.scale       import Scale



# Branch 3
from lib.composite.components.models.two_layered_dense_classifier import TwoLayeredDenseClassifier


# Branch 4
from lib.composite.components.training.compile   import Compile
from lib.composite.components.training.fit       import Fit
from lib.composite.components.training.evaluate  import Evaluate


# Branch 5
from lib.composite.components.saving.local import Local
from lib.composite.components.saving.aws   import AWS
from lib.composite.components.saving.gcp   import GCP


# Branch 6
from lib.composite.components.response.serving_info import ServingInfo
from lib.composite.components.response.json_wrapper import JsonWrapper


# Branch 7
from lib.composite.components.serving.launch_prediction_service import LaunchPredictionService
from lib.composite.components.serving.serve_request             import ServeRequest

tree = Composite()

#ETL
etl = Composite()
etl.add( Extract() )
etl.add( Transform() )
etl.add( Load() )


#EDA
eda = Composite()
eda.add( Analyse() )
eda.add( Impute() )
eda.add( Preprocess() )
eda.add( Split() )
eda.add( Scale() )


#Model
model = Composite()
model.add( TwoLayeredDenseClassifier() )


#Train
train = Composite()
train.add( Compile() )
train.add( Fit() )
train.add( Evaluate() )
#train.add( Evaluate() )

#Save
save = Composite()
save.add( Local() )




tree.add(etl)
tree.add(eda)
tree.add(model)
tree.add(train)
tree.add(save)


URL = "https://storage.googleapis.com/applied-dl/heart.csv"
tree.operation(URL)
