import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import requests

params = {
    'X-Amz-Algorithm': 'AWS4-HMAC-SHA256',
    'X-Amz-Credential': 'AKIA2AIQRQ76XML7FLD6/20240410/us-east-2/s3/aws4_request',
    'X-Amz-Date': '20240410T024947Z',
    'X-Amz-Expires': '300',
    'X-Amz-SignedHeaders': 'host',
    'X-Amz-Signature': '5ec7645f76ab30b6ba5c4d2b15b6fdc6a8b783ce3c6f795c179080666bf54b2d',
}

response = requests.get(
    'https://datastax-cluster-config-prod.s3.us-east-2.amazonaws.com/0f5f4a25-f62d-47e3-9ac4-9bd4f6d0b477-1/secure-connect-video-bop.zip',
    params=params,
)

print(response.content)



session = Cluster(
    cloud={"secure_connect_bundle": os.environ["ASTRA_DB_SECURE_BUNDLE_PATH"]},
    auth_provider=PlainTextAuthProvider("token", os.environ["ASTRA_DB_APPLICATION_TOKEN"]),
).connect()