# PictoSearch

PictoSearch is a image search application created by the students in CS4440 to explore AWS DynamoDB. The images are sourced from ImageNET and can be queried using text or from a random image. Searching by image uploads the image to our database as well. 
![Screenshot of a sample query search](screenshot.jpg)
Note: 
Due to deployment issues, the random image must be classified locally first by our provided classifier. 
While our word stemming can handle synonyms and similar words, the search queries work best with classes already in our database. The list of words can be found in app\service\wnid_classes.txt.
A broad search query such as “bird” would take longer to run than a more focused query such as “albatross”.


## Setup

Once you have the app deployed on the AWS servers, you should be able to access the front end by navigating to “https://$BUCKET_URL$/index.html”.

## Sources
https://github.com/mf1024/ImageNet-datasets-downloader
http://image-net.org/download-API
https://aws.amazon.com/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/module-one/
https://aws.amazon.com/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/module-two/
https://aws.amazon.com/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/module-three/
https://codepen.io/siwicki/pen/FHkwu



