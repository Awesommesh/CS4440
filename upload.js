// Remember to include jQuery somewhere.

$(function() {

  $('#theForm').on('submit', sendFile);
});

function sendFile(e) {
    //document.write(9);
    // get the reference to the actual file in the input
    e.preventDefault();

    var theFormFile = $('#theFile').get()[0].files[0];


    $.ajax({
      type: 'PUT',
      url: uploadPreSignedUrl ,
      // Content type must much with the parameter you signed your URL with
      contentType: 'binary/octet-stream',
      // this flag is important, if not set, it will try to send data as a form
      processData: false,
      // the actual file is sent raw
      data: theFormFile
    })


    return false;
  };


var s3 = new AWS.S3({
  region: 'us-east-2',
  signatureVersion: 'v4',
  accessKeyId: 'AKIA2LNZHUGZJL2DTE53',
  secretAccessKey: '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'
});

var uploadPreSignedUrl = s3.getSignedUrl('putObject', {
    Bucket: 'imagenetbucket',
    Key: 'test_in/index.jpg',
    ACL: 'authenticated-read',
    // This must match with your ajax contentType parameter
    ContentType: 'binary/octet-stream'

    /* then add all the rest of your parameters to AWS puttObect here */
});

var downloadPreSignedUrl = s3.getSignedUrl('getObject', {
    Bucket: 'imagenetbucket',
    Key: 'test_in/index.jpg',
    /* set a fixed type, or calculate your mime type from the file extension */
    ResponseContentType: 'image/jpeg'
    /* and all the rest of your parameters to AWS getObect here */
});

// now you have both urls
console.log( uploadPreSignedUrl, downloadPreSignedUrl ); 
