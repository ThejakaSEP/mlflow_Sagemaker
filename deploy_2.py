from mlflow.deployments import get_deploy_client

experiment_id = '122030872860642476'
run_id = '7bf01973f8c34a088d963279ef617c8f'
region = 'us-east-2'
aws_id = '754158409989'
arn = 'arn:aws:iam::754158409989:role/aws-sagemaker-for-deploy-ml-model'
app_name = 'model-application'
model_uri = f'./mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model'
tag_id = '2.2.2'

image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id

# vpc_config = {
#     "SecurityGroupIds": [
#         "sg-123456abc",
#     ],
#     "Subnets": [
#         "subnet-123456abc",
#     ],
# }
config = dict(
    # assume_role_arn="arn:aws:123:role/assumed_role",
    execution_role_arn=arn,
    # bucket_name="my-s3-bucket",
    image_url=image_url,
    region_name=region,
    archive=False,
    # instance_type="ml.m5.4xlarge",
    # instance_count=1,
    # synchronous=True,
    # timeout_seconds=300,
    # vpc_config=vpc_config,
    # variant_name="prod-variant-1",
    # env={"DISABLE_NGINX": "1", "GUNICORN_CMD_ARGS": '"--timeout 60"'},
    # tags={"training_timestamp": "2022-11-01T05:12:26"},
)

client = get_deploy_client("sagemaker")
client.create_deployment(
    "my-deployment",
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)
