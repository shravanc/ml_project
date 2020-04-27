import app.helpers.template as tmp

class Launch(tmp.Template):

  def __init__(self):
    super(Launch, self).__init__()

  def etl(self):
    etl = tmp.Composite()
    etl.add(tmp.Extract() )
    etl.add( tmp.Transform() )
    etl.add( tmp.Load() )
    
    return etl

  def eda(self):
    eda = tmp.Composite()
    eda.add( tmp.Analyse() )
    eda.add( tmp.Impute() )
    eda.add( tmp.Preprocess() )
    eda.add( tmp.Split() )
    eda.add( tmp.Scale() )

    return eda
    
  def model(self):
    model = tmp.Composite()
    model.add( tmp.TwoLayeredDenseClassifier() )
    return model

  def train(self):
    train = tmp.Composite()
    train.add( tmp.Compile() )
    train.add( tmp.Visualize() )
    train.add( tmp.Fit() )
    train.add( tmp.Evaluate() )

    return train

  def save(self):
    save = tmp.Composite()
    save.add( tmp.Local() )
    return save

  def serve(self):
    serve = tmp.Composite()
    serve.add( tmp.LaunchPredictionService() )
    return serve

