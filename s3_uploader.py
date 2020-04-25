import math
import os
import random
import tarfile
import urllib
import sys
from absl import flags
import json
import boto3

flags.DEFINE_string('raw_data_dir', None, 'Directory path for raw Imagenet dataset. ')

FLAGS = flags.FLAGS


def upload_to_s3(files, wnid, classname):
  """Upload TF-Record files to S3, at provided path."""

  # Find the S3 bucket_name and key_prefix for dataset files
  metadata = {'wnid': wnid, 'class': classname}
  s3 = boto3.client('s3')
  def _upload_files(filenames):
    """Upload a list of files into a specific subdirectory."""
    for i, filename in enumerate(sorted(filenames)):
      with open('index.json', 'r') as fil:
        data = json.load(fil)
        l = data['images']
        l += 1
      with open('index.json', 'w') as fil:
        data['images'] = l
        json.dump(data, fil)
      metadata['index'] = l
      f = str.split(filename, "/")[-1];
      s3.put_object(Body=filename, Bucket='$BUCKET_NAME$', Key='$FOLDER_NAME$/' + f, Metadata= metadata)


if __name__ == '__main__':  # pylint: disable=unused-argument
  FLAGS(sys.argv)

  # Download the dataset if it is not present locally
  #folder name
  raw_data_dir = FLAGS.raw_data_dir
  attributes = str.split(raw_data_dir, "_")
  raw_data_dir = "$PATH_TO_FOLDER$"  + raw_data_dir
  wnid = attributes[0]
  classname = attributes[1]
  files = os.listdir(raw_data_dir)

  files = [os.path.join(raw_data_dir, f) for f in files]
  # print(files)
  upload_to_s3(files, wnid, classname)