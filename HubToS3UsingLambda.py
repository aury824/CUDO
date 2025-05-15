import boto3 
import json
import logging
from datetime import datetime

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    account = event["detail"]["findings"][0]["AwsAccountId"]
    region = event["detail"]["findings"][0]["Resources"][0]["Region"]
    
    uploadBucket = 'aws-securityhub-logs-airsm-us-east-1'
    current_time = datetime.now().strftime('%H-%M')
    current_date = datetime.now().strftime('%d')
    current_month = datetime.now().strftime('%m')
    current_year = datetime.now().strftime('%Y')

    if account == '600143373011':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '205247088522':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '696244143318':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '426571224475':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '822636663275':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '111482303320':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'
    elif account == '386932009883':
        uploadPath = f'{account}/{region}/{current_year}/{current_month}/{current_date}/{region}_{account}_{current_time}.json'

#<account>/<region>/<yyyy>/<mm>/<dd>/[ap-southeast-1]_[111482303320]_2023-11-13_16-17-46.json

    json_data = json.dumps(event)
    body = json_data

    s3_client = boto3.client('s3')

    response = s3_client.put_object(
        Bucket=uploadBucket,
        Key=uploadPath,
        Body=body
    )

    # 업로드 완료 후 로깅
    logger.info(f"Uploaded to S3: {uploadBucket}/{uploadPath}")
    logger.info(f"Response: {json.dumps(response)}")