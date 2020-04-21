from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import os

def run():

	ACCESS_KEY = 'AKIA2LNZHUGZIPHB5KP3 '
	SECRET_KEY = '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'

	s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
	                      aws_secret_access_key=SECRET_KEY)

	file = "../../Downloads/gorilla.jpg"


	s3.upload_file("gorilla.jpg",'imagenetbucket','test_in/gorilla.jpg')

if __name__ == '__main__':
	run()

