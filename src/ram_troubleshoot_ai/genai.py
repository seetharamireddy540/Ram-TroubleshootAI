import boto3
import json


def list_foundation_models():
    profile_name = 'prorca'
    region_name = 'us-east-1'
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    bedrock_client = session.client('bedrock')
    try:
        response = bedrock_client.list_foundation_models()
        models = response["modelSummaries"]
        print(f"Found {len(models)} foundation models:")
        for model in models:
            print(f"- {model['modelName']}")
    except Exception as e:
        print(f"Error listing foundation models: {str(e)}")


def invoke_model(prompt):
    profile_name = 'prorca'
    region_name = 'us-east-1'
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    bedrock_runtime = session.client('bedrock-runtime')
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"  # Claude 3 Sonnet
    
    try:
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        })
        
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']
    except Exception as e:
        print(f"Error invoking model: {str(e)}")
        return None


def main():
    print("Listing available foundation models:")
    list_foundation_models()
    
    print("\nInvoking Claude 3 Sonnet model:")
    prompt = "Explain the concept of machine learning in one paragraph."
    response = invoke_model(prompt)
    if response:
        print("Model response:")
        print(response)


if __name__ == "__main__":
    main()
