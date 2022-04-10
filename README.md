# Optimizing an ML Pipeline in Azure
## by Cristian Alberch as part of Udacity Nanodegree "Machine Learning Engineer with Azure"

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project, we build an automated Azure ML pipeline to:
- Authenticate
- Create a ML model
- Deploy the best model
- Consume and interact with the model


## Architectural Diagram

![Architectural Diagram of project](readme_arch.png)


## Key Steps

### Step 1: Authentication

A Service Principal is created to limit the scope of the resource group.
![Step 1](screenshots\1.1-az_ms_ws_share.jpg)

Allow the Service Principal access to the Workspace:
![Step 1](screenshots\1.2-az_ms_ws_share.jpg)


### Step 2: Automated ML Experiment
A ML Experiment is created:
![Step 2](screenshots\2.1-registered_datasets.png)

And the ML Experiment is completed:
![Step 2](screenshots\2.2-completed-experiment.png)


### Step 3: Deploy the Best Model

- The best model is selected for deployment.
- Model is deployed using Azure Container Instance.

### Step 4: Enable Logging
Application insights is enabled:
![Step 4](screenshots\4-application-insights-enabled.png)
And the output can be monitored:
![Step 4](screenshots\4-application-insights-output.png)

The logs can be seen running script "logs.py":
![Step 4](screenshots\4-logs-py-output.png)


### Step 5: Swagger Documentation

Swagger is used to document and consum RESTful web service:
![Step 5](screenshots\5-swagger-output.png)

Swagger provides information on types of HTTP requests that an API can consume POST: and GET: with details on the data:
![Step 5](screenshots\5-swagger-output-2.png)


### Step 6: Consume Model Endpoints

![Step 6](screenshots\6-consume_endpoints_test_terminal.png)

![Step 6](screenshots\6.1-consume_endpoints_test.png)


### Step 7: Create, Publish, and Consume
A AutoML Pipeline is started with a Experiment created:
![Step 7](screenshots\7.1-pipelines-list.png)

The pipeline includes a automl_module that incorporates the AutoML pipeline in SDK.
![Step 7](screenshots\7.2-pipeline-created.png)

The AutoML pipeline is published with a REST endpoint created for consumption.
![Step 7](screenshots\7.3-published-pipeline.png)

The published pipeline can be run on demand:
![Step 7](screenshots\7.4-widget-finished.png)

## Screen Recording
https://youtu.be/pocQQJ9NJb0

## Next Steps
The following could be used to improve the work:
1. Hyperparameter tuning could be used to improve the accuracy further.
2. The ML pipeline could be automated to run on scheduled and/or trigger events.
3. Azure Kubernetes could be used to improve the performance of the pipeline and ability to handle additional data.


