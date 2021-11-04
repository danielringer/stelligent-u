import boto3
import json

def adminStack():
    
    try:
        aws.create_stack(StackName='gr-m01x32-training',TemplateBody=open('cloudformation1.3.1.yaml').read()) # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_stack

    except aws.exceptions.AlreadyExistsException: # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html

        try:
            aws.update_stack(StackName='gr-m01x32-training', TemplateBody=open('cloudformation1.3.1.yml').read()) # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_stack

        except aws.exceptions.ClientError as e: # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html
            print(e)

if __name__ == "__main__": # https://www.freecodecamp.org/news/if-name-main-python-example/
    
    for region in json.load(open('usregions.json')): # https://www.geeksforgeeks.org/read-json-file-using-python/

        print(region)
        aws = boto3.client('cloudformation', region) # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html

        adminStack()