from flask import Flask, jsonify, json, Response, request, render_template
from flask_cors import CORS
import imageNETTableClient
import wnid_searcher as ws
# A very basic API created using Flask that has two possible routes for requests.

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
CORS(app)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route("/healthcheck")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /imagenet instead."})

# @app.route("/imagenet")
# def getImageNET():
    # filterCategory = request.args.get('filter')
    # if filterCategory:
    #     filterValue = request.args.get('value')
    #     queryParam = {
    #         'filter': filterCategory,
    #         'value': filterValue
    #     }
    #     # a filter query string was found, query only for those images.
    #     serviceResponse = imageNETTableClient.queryImageNET(queryParam)
    # else:
    #     # no filter was found, retrieve all images.
    # #     serviceResponse = imageNETTableClient.getAllImages()

    # flaskResponse = Response(serviceResponse)
    # flaskResponse.headers["Content-Type"] = "application/json"

    # return flaskResponse
@app.route("/")
def queryForm():
    return render_template('search.html')

@app.route("/", methods=['POST'])
def querySearch():
    query = request.form['queryinput']
    return (ws.get_wnid(query))
    # return render_template('search.html', ws.get_wnid(query))

# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    querySearch()
    app.run(host="0.0.0.0", port=8080)