import json 
import boto3

Queue_url = "https://sqs.ap-south-1.amazonaws.com/585768157192/demo-queue-00007"

event = {
    "source": "data.ingestion",
    "detail-type" : "RawDataAvailable",
    "detail" : {
        "bucket" : "tempbucket00007",
        "prefix" : "matches.csv",
        "dataset": "matches"

    }
}

sqs = boto3.client("sqs")

sqs.send_message(
    QueueUrl= Queue_url,
    MessageBody = json.dumps(event)
)

print("Integration event sent to SQS")