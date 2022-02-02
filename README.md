# gateway-firehose-lambda-S3
This infra sets up a complete pipeline that receive json data within post request, then stores data temporarily in firehose. A lambda function is added to add new-line "\n" before sending json object to S3.  
