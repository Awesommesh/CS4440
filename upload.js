// Remember to include jQuery somewhere.
$(function() {

  $('#theForm').on('submit', sendFile);
});

var imagenetApiEndpoint = "http://imagenet-nlb-b4fcd380459e9b61.elb.us-east-2.amazonaws.com";

var metadata = {};
function sendFile(e) {
    //document.write(9);
    // get the reference to the actual file in the input
    e.preventDefault();

    var theFormFile = $('#theFile').get()[0].files[0];
    $.ajax({
        url: imagenetApiEndpoint + '/metadata?query_class=' + $('input[name="uploadClass"]').val(),
        type: 'GET',
        success: function(data) {
            // returnedImage = '';
            // returnedImage = '<div>';
            metadata = JSON.parse(JSON.stringify(data));
            if (metadata !== {}) {
                console.log(uploadPreSignedUrl);
                console.log(metadata.index);
                uploadPreSignedUrl = s3.getSignedUrl('putObject', {
                    Bucket: 'imagenetbucket',
                    Key: 'images/' + metadata.index.toString() + '.jpg',
                    ACL: 'authenticated-read',
                    // This must match with your ajax contentType parameter
                    ContentType: 'binary/octet-stream',
                    Metadata: metadata
                    /* then add all the rest of your parameters to AWS puttObect here */
                });
                console.log(uploadPreSignedUrl);
                $.ajax({
                  type: 'PUT',
                  url: uploadPreSignedUrl,
                  // Content type must much with the parameter you signed your URL with
                  contentType: 'binary/octet-stream',
                  // this flag is important, if not set, it will try to send data as a form
                  processData: false,
                  // the actual file is sent raw
                  data: theFormFile,
                  Metadata: metadata
                });
                document.getElementById("query_input").value = metadata.class;
                $("#textform").submit()
            } else {
                alert('Enter an imagenet class')
            }
        }

    });

    return false;
  };


var s3 = new AWS.S3({
  region: 'us-east-2',
  signatureVersion: 'v4',
  accessKeyId: 'REPLACE ME WITH YOUR ACCESS KEY ID',
  secretAccessKey: 'REPLACE ME WITH YOUR SECRET ACCESS KEY'
});

var uploadPreSignedUrl = s3.getSignedUrl('putObject', {
    Bucket: 'imagenetbucket',
    Key: 'images/test.jpg',
    ACL: 'authenticated-read',
    // This must match with your ajax contentType parameter
    ContentType: 'binary/octet-stream'

    /* then add all the rest of your parameters to AWS puttObect here */
});