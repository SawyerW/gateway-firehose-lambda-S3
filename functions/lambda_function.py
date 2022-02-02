import logging
import boto3, base64
import json
import os

log_level = os.environ.get("LOG_LEVEL", "INFO")
logging.root.setLevel(logging.getLevelName(log_level))  # type: ignore
logger = logging.getLogger(__name__)

firehose_client = boto3.client("firehose")


def lambda_handler(event, context):

    output = []

    for record in event["records"]:
        payload = base64.b64decode(record["data"]).decode("utf-8")
        # logger.info("payload:" + payload)

        row_w_newline = payload + "\n"
        row_w_newline = base64.b64encode(row_w_newline.encode("utf-8")).decode("utf-8")

        output_record = {
            "recordId": record["recordId"],
            "result": "Ok",
            "data": row_w_newline,
        }
        output.append(output_record)

    logger.info("Processed {} records.".format(len(event["records"])))

    return {"records": output}
