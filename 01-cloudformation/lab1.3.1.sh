#!/bin/sh

jq -r '.[]' usregions.json | while read region;
do
    aws cloudformation create-stack --stack-name gr-m01x31-training --template-body file://cloudformation1.3.1.yaml --parameters file://parameters.json --region $region
    echo $region
    echo "stack created.";
done