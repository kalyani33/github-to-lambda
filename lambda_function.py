import json
import pandas as pd

def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]
    print('Bucket Name:' + bucket_name)
    print('S3 File Name:' + s3_file_name)
  
    json_file = 's3://' + bucket_name + '/' + s3_file_name
    print('JSON File:' + json_file)
    
    #data_frame = wr.s3.read_json(path=json_file, orient='records', lines=True)
    df = pd.read_json(json_file,lines=True,orient='records')
    #print(df)
    df = df[df['status'] == 'delivered']
    print(df)
    
    new_s3_file_name = 's3://doordash-target-zn-10' + '/' + s3_file_name
    
    df.to_json(path_or_buf=new_s3_file_name,orient='records')
    print("Output file uploaded to : ",new_s3_file_name)
    return {
        'statusCode': 200,
        'body': json.dumps("Output file uploaded to : {} ".format(new_s3_file_name))
    }