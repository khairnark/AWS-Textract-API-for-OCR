#import required python packages
import boto3
from trp import Document
import pandas as pd
import json
import csv
s3BucketName ="bucketname"
s3 = boto3.resource('s3')\n",
textractmodule = boto3.client('textract')
my_bucket = s3.Bucket(s3BucketName)
for s3_file in my_bucket.objects.all():
    response = textractmodule.detect_document_text(Document={'S3Object': {'Bucket': s3BucketName,'Name': s3_file.key}})
    text = " "
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE"
        textext = '\\033[94m' + item["Text"] + '\\033[0m'
        text = text + " " + item["Text"]
        s3_client = boto3.client('s3')
        filename1 = s3_file.key
        print(filename1)
        file_object  = open("filename", "mode")
        f= open("guru909.txt","a+")
        for i in range(10):
            f.write("This is line %d\\r\\n\" % (i+1))
            f.close()
