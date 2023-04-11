# The final version is on : https://github.com/nogibjj/Huilin-IDS721-Proj4
# Project 4: Serverless Data Engineering Pipeline
In this project, we need to build a serverless data engineering pipeline

## Requirements
* Reproduce the architecture of the example serverless data engineering project or perform something similar using only serverless technologies.
* Enhance the project by extending the functionality of the NLP analysis: adding entity extraction, key phrase extraction, or some other NLP feature or doing Applied Computer Vision.

## week1
### Project Setup
1. Clone the repo and cd into it:
```
$ git clone https://github.com/JuliaJHL/IDS721-Proj4.git
$ cd IDS721-Proj4
```
2. Create and source the virtual environment:
```
$ python3 -m venv env
$ source env/bin/activate
```
3. Install packages
```
$ make install
$ make install ipython
```
### Amazon Comprehend
Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents. It develops insights by recognizing the entities, key phrases, language, sentiments, and other common elements in a document.
* Launch AWS Cloud9
* make install ipython
* use the following command to do sentiment analysis
![comprehend](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/comprehend.png)
* create Lambda function
![lambda](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/lambda.png)
![test](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/test.png)

## week2
In this week, I reproduced the architecture of the example serverless data engineering project.

<img width="500" alt="architecture" src="https://camo.githubusercontent.com/bb29cd924f9eb66730bbf7b0ed069a6ae03d2f1a/68747470733a2f2f757365722d696d616765732e67697468756275736572636f6e74656e742e636f6d2f35383739322f35353335343438332d62616537616638302d353437612d313165392d393930392d6135363231323531303635622e706e67">

### 1. prerequisite
* Create a access role to allow Lambda functions to call AWS services on your behalf.
  ![admin](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/admin.png)
* Create a DynamoDB table called `fang`.
  ![fang](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/fang.png)
* Create a SQS queue called `producer`.
  ![queue](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/queue.png)
* Create a bucket called `comsentiment`.

### 2.Producer Lambda
* Open Cloud9 IDE, create a new Lambda SAM Application called `producer`.
* Modify `app.py` and `requirements.txt`.
* Build and deploy the application.
  ```
  sam build --use-container
  sam deploy --guided
  ```
* Go to AWS Lambda console and click the newly built function.
* Modify the execution role.
* Add an EventBridge (CloudWatch Events) trigger, set the rate as 1 minute.
  ![producer](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/producer.png)
* Check messages of the queue to see the results.
  ![message](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/message.png)
  ![info](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/info.png)

### 3. Consumer Lambda
* Open Cloud9 IDE, create a new Lambda SAM Application called `consumer`.
* Modify `app.py` and `requirements.txt`.
* Build and deploy the application.
  ```
  sam build --use-container
  sam deploy --guided
  ```
* Go to AWS Lambda console and click the newly built function.
* Modify the execution role.
* Add an SQS trigger, choose the `producer` queue.
  ![consumer](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/consumer.png)


## Reference
* [tutorial](https://github.com/noahgift/awslambda)
* [python template](https://github.com/nogibjj/python-template)
* [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)
