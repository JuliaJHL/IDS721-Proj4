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



## Reference
* [tutorial](https://github.com/noahgift/awslambda)
* [python template](https://github.com/nogibjj/python-template)
* [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)
