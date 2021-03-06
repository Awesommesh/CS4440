from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import imageNETTableClient
import resnet as res
import wnid_searcher as ws
# A very basic API created using Flask that has two possible routes for requests.

app = Flask(__name__)
CORS(app)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /imagenet instead."})

@app.route("/resnet")
def resnet():
    img_path = request.args.get('img_path')
    res.model_predict(img_path)
    return jsonify({"message" : "Testing Resnet."})

@app.route("/stemming")
def get_wnids():
    query = request.args.get('query_input')
    if query:
        results = ws.get_wnid(query)
        return results
    return jsonify({"message" : "Testing Stemming."})

@app.route("/metadata")
def metadata():
    classname = request.args.get('query_class').lower()
    imageMap = {}
    if classname:
        with open('class-wnids.json', 'r') as f:
            classes = json.load(f)
            indexes = [i for i,d in enumerate(classes) if classname in d]
            if len(indexes) == 0:
                wnid = ""
            else:
                wnid = classes[indexes[0]][classname]
                with open('index_var.json', 'r') as fil:
                    index = int(json.load(fil)['index'])
                    imageMap = {
                        'index': str(index),
                        'class': classname,
                        'wnid': wnid
                    }
                with open('index_var.json', 'w') as fil:
                    json.dump({'index': index+1}, fil)
    return jsonify(imageMap)

@app.route("/imagenet")
def getImageNET():
    filterCategory = request.args.get('filter')
    if filterCategory:
        filterValue = request.args.get('value')
        queryParam = {
            'filter': filterCategory,
            'value': filterValue
        }
        # a filter query string was found, query only for those images.
        serviceResponse = imageNETTableClient.queryImageNET(queryParam)
    else:
        # no filter was found, retrieve all images.
        serviceResponse = imageNETTableClient.getAllImages()

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)