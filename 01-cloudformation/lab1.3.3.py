import boto3
import json

def deleteStack():

    try:
        aws.delete_stack(StackName='gr-m01x32-training')
    except Exception as e:
        print(e)

if __name__ == "__main__": # https://www.freecodecamp.org/news/if-name-main-python-example/
    
    for region in json.load(open('usregions.json')): # https://www.geeksforgeeks.org/read-json-file-using-python/

        print(region)
        aws = boto3.client('cloudformation', region) # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
    
        deleteStack()