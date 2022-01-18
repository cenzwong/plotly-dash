```python
# Add installed library dependencies to Python PATH variable.
PATH=%env PATH
%env PATH={PATH}:/home/jupyter/.local/bin

# Retrieve and set PROJECT_ID and REGION environment variables.
PROJECT_ID = !(gcloud config get-value core/project)
PROJECT_ID = PROJECT_ID[0]
REGION = 'us-central1'

# Create a globally unique Google Cloud Storage bucket for artifact storage.
GCS_BUCKET = f"{PROJECT_ID}-bucket"

!gsutil mb -l $REGION gs://$GCS_BUCKET
```

```python
from google.cloud import aiplatform

# Import the Vertex SDK for Python into your Python environment and initialize it.
aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=f"gs://{GCS_BUCKET}")

# ...
# You will create a Tabular regression dataset for managing the sharing and metadata for this lab's dataset stored in BigQuery.
tabular_dataset = aiplatform.TabularDataset.create(display_name="online-retail-clv", bq_source=f"{BQ_URI}")


# ...
job = aiplatform.CustomContainerTrainingJob(
    display_name="online-retail-clv-3M-dnn-regressor",
    container_uri=IMAGE_URI,
    # https://cloud.google.com/vertex-ai/docs/predictions/pre-built-containers
    # gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest
    model_serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-3:latest",
)

model = job.run(
    dataset=tabular_dataset,
    model_display_name=MODEL_NAME,
    # GCS custom job output dir.
    base_output_dir=BASE_OUTPUT_DIR,
    # the BQ Tabular dataset splits will be written out to their own BQ dataset for reproducibility.
    bigquery_destination=f"bq://{PROJECT_ID}",
    # this corresponds to the BigQuery data split column.
    predefined_split_column_name="data_split",
    # the model training command line arguments defined in trainer.task.
    args=CMD_ARGS,
    # Custom job WorkerPool arguments.
    replica_count=1,
    machine_type="c2-standard-4",
    # Provide your Tensorboard resource name to write Tensorboard logs during training.
    tensorboard=TENSORBOARD_RESOURCE_NAME,
    # Provide your Vertex custom training service account created during lab setup.
    service_account=f"vertex-custom-training-sa@{PROJECT_ID}.iam.gserviceaccount.com"
)


# ...
# Specify sampled Shapley feature attribution method with path_count parameter 
# controlling the number of feature permutations to consider when approximating the Shapley values.

explain_params = aiplatform.explain.ExplanationParameters(
    {"sampled_shapley_attribution": {"path_count": 10}}
)

# https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/ExplanationSpec
input_metadata = {
    "input_tensor_name": serving_input,
    "encoding": "BAG_OF_FEATURES",
    "modality": "numeric",
    "index_feature_mapping": feature_names,
}

output_metadata = {"output_tensor_name": serving_output}

input_metadata = aiplatform.explain.ExplanationMetadata.InputMetadata(input_metadata)
output_metadata = aiplatform.explain.ExplanationMetadata.OutputMetadata(output_metadata)

explain_metadata = aiplatform.explain.ExplanationMetadata(
    inputs={"features": input_metadata}, outputs={"medv": output_metadata}
)

# ... depoly
endpoint = model.deploy(
    traffic_split={"0": 100},
    machine_type="n1-standard-2",
    explanation_parameters=explain_params,
    explanation_metadata=explain_metadata
)
# actual: 3181.04
test_instance_dict = {
    "n_purchases": 2,
    "avg_purchase_size": 536.5,
    "avg_purchase_revenue": 1132.7,
    "customer_age": 123,
    "days_since_last_purchase": 32,
}
endpoint.predict([test_instance_dict])
explanations = endpoint.explain([test_instance_dict])
pd.DataFrame.from_dict(explanations.explanations[0].attributions[0].feature_attributions, orient='index').plot(kind='barh');
```

## Bigquery
The result will pass back to recency as python variable as type `pandas.core.frame.DataFrame`
```python
%%bigquery recency

SELECT 
  days_since_last_purchase
FROM 
  `online_retail.online_retail_clv_ml`

```


## Depolyment
MODEL_NAME is python variable
```python
%%writefile {MODEL_NAME}/trainer/model.py

%%writefile {MODEL_NAME}/trainer/task.py

%%writefile {MODEL_NAME}/Dockerfile

%%writefile {MODEL_NAME}/requirements.txt

```