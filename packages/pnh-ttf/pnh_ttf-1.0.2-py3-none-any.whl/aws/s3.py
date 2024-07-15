import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta


class S3Manager:
    def __init__(self, bucket_name: str, object_name: str, file_name: str = None, 
                 if_modified_since: datetime = None, region: str = 'eu-west-1', profile: str = 'default'):
        """
        Initialize an S3Manager instance.

        Args:
            bucket_name (str): The name of the bucket to upload to.
            object_name (str): The name of the key to upload to.
            file_name (str, optional): The path to the file to upload.
            if_modified_since (datetime, optional): Datetime to compare against. Defaults to five minutes earlier than now.
            region (str, optional): AWS region. Defaults to 'eu-west-1'.
            profile (str, optional): AWS profile name. Defaults to 'default'.
        """
        self.bucket = bucket_name
        self.object_name = object_name
        self.file_name = file_name
        self.if_modified_since = if_modified_since if if_modified_since else datetime.now() - timedelta(minutes=5)
        self.region = region
        self.profile = profile

        session = boto3.Session(profile_name=self.profile, region_name=self.region)
        self.s3_client = session.client('s3')

    def upload_file(self) -> dict:
        """
        Upload a file to an S3 bucket.

        Returns:
            dict: A dictionary containing the status code and status message.
        """
        try:
            # Attempt to upload the file to the specified S3 bucket and object name
            self.s3_client.upload_file(
                Filename=self.file_name,
                Bucket=self.bucket,
                Key=self.object_name
            )

            # Return a success message if the file was uploaded successfully
            return {
                'statusCode': 200,
                'statusMessage': (f"Successfully uploaded local file "
                                  f"'{self.file_name}' to S3 bucket "
                                  f"'{self.bucket}' as '{self.object_name}'.")
            }

        except (FileNotFoundError, OSError):
            # Handle the case where the local file was not found
            return {
                'statusCode': 400,
                'statusMessage': f"The local file '{self.file_name}' was not found."
            }
        except boto3.exceptions.S3UploadFailedError as e:
            # Handle specific S3 upload failure errors
            return {
                'statusCode': 400,
                'statusMessage': f"S3UploadFailedError: {e}"
            }
        except Exception as e:
            # Handle any other exceptions that occurred during the file upload
            return {
                'statusCode': 400,
                'statusMessage': f"An unexpected error occurred: {e}"
            }

    def check_file_exists(self) -> dict:
        """
        Check if the specified file exists in the S3 bucket and if it was 
        modified since the if_modified_since datetime.

        Returns:
            dict: A dictionary containing the status code and status message.
        """
        try:
            # Get the object's metadata from S3 with IfModifiedSince parameter
            response = self.s3_client.head_object(
                Bucket=self.bucket,
                Key=self.object_name,
                IfModifiedSince=self.if_modified_since
            )
            
            # If we reach here, the file exists and was modified since if_modified_since
            return {
                'statusCode': 200,
                'statusMessage': f"File '{self.object_name}' exists and was modified on {response['LastModified']}."
            }

        except ClientError as e:
            error_code = e.response['Error']['Code'] if e.response else None
            
            if error_code == '304':
                # File exists but was not modified since if_modified_since
                return {
                    'statusCode': 304,
                    'statusMessage': (f"File '{self.object_name}' exists but was not "
                                      f"modified since {self.if_modified_since}.")
                }
            elif error_code == '404':
                # File does not exist
                return {
                    'statusCode': 404,
                    'statusMessage': (f"File '{self.object_name}' not found in bucket '{self.bucket}'.")
                }
            else:
                # Other client errors
                return {
                    'statusCode': 400,
                    'statusMessage': f"ClientError: {e}"
                }

        except Exception as e:
            # Handle any unexpected errors
            return {
                'statusCode': 400,
                'statusMessage': f"An unexpected error occurred: {e}"
            }
