import mlflow.sagemaker as mfs
# import mlflow

experiment_id = '955555633699414793'
run_id = '60125cf5eece4a3b9b76abc2d0937131'
region = 'us-east-2'
aws_id = '047810789005'
arn = 'arn:aws:iam::754158409989:role/aws-sagemaker-for-deploy-ml-model'
app_name = 'model-application'
model_uri = f'mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model'
tag_id = '2.2.2'


image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id


mfs.deploy(app_name,
	model_uri=model_uri,
	region_name=region,
	mode='create',
	execution_role_arn=arn,
	image_url=image_url)


# mlflow.sagemaker.deploy(app_name=app_name,
#            model_uri=model_uri,
#            region_name=region,
#            mode='create',
#            execution_role_arn=arn,
#            image_url=image_url,
#            flavor='mlflow.pyfunc')

# mfs._deploy(app_name=app_name,
#            model_uri=model_uri,
#            execution_role_arn=arn,
#            region_name=region,
#            image_url=image_url,
#            mode='create')