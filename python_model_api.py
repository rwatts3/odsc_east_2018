


###############################################################################
# Train the model
###############################################################################
import numpy as np
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = GradientBoostingClassifier()
clf.fit(X, y)


###############################################################################
# Save out the model object
###############################################################################
from sklearn.externals import joblib

# Save the pickle file to the file system
# You can then point the 
joblib.dump(clf, 'model.pkl')


###############################################################################
# Build the API Call
###############################################################################
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=('POST',))
def GetPrediction():
    if request.content_type != 'application/json':
        return 'submit as a json file'
    try:
        json_ = request.json
        new_X = pd.DataFrame([json_])
        # For simplicity, set up for a single observation
        prediction = clf.predict(new_X)
        prediction = np.asscalar(prediction)
        print(type(prediction))
        return jsonify({'prediction': prediction})
    except ValueError:
        return jsonify({'value error': 1})


if __name__ == '__main__':
    app.run(port=5003)

