import os
import boto
from boto.s3.key import Key

def upload_dir(access_key_id, access_key, bucket, src_dir):
    """
    Upload specific folder to S3 bucket.
    """
    c = boto.connect_s3(aws_access_key_id=access_key_id,
        aws_secret_access_key=access_key)
    b = c.get_bucket(bucket)
    k = Key(b)

    print "- Uploading file % s" % (src_dir,)

    for path, dir, files in os.walk(src_dir):
        for file in files:
            file_key = os.path.relpath(os.path.join(path,file),src_dir)
            print file_key
            k.key = file_key
            k.set_contents_from_filename(os.path.join(path,file))
            b.set_acl('public-read', k.key)

    print "- Uploading complete"