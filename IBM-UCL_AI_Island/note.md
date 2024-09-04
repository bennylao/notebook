# IBM-UCL AI Islands Theme: Local AI Index for NLP on WatsonX

Create an offline NLP AI index system that can be used off-line and 
enable selection of different AI models, for testing, 
benchmarking and passing through to systems integration points. 
APIs are needed to be designed with enterprise design patterns in mind for MLOps. 
Provision this as an extension for WatsonX under the IBM-UCL AI-Islands name. 

## Tech Review

- InstructLab
    - use of LAB method to find tune and improve the performance of LLMs with an even smaller set of human-generated data
    - https://www.redhat.com/en/topics/ai/what-is-instructlab
- RAG
    - cost-efficient method for supplementing an LLM with domain-specific knowledge that wasn’t part of its pretraining. RAG makes it possible for a chatbot to accurately answer questions related to a specific field or business without retraining the model. Knowledge documents are stored in a vector database, then retrieved in chunks and sent to the model as part of user queries

## Related URLs

- watsonx models: 
    - https://www.ibm.com/products/watsonx-ai
    - https://eu-gb.dataplatform.cloud.ibm.com/wx/home?context=wx&apps=data_science_experience,watson_machine_learning,cos&nocache=true&onboarding=true&quick_start_target=watsonx
- watson service: https://cloud.ibm.com/developer/watson/dashboard
- SkillsBuild: https://academic.ibm.com/a2mt/downloads
- .NET MAUI: https://learn.microsoft.com/en-gb/dotnet/maui/what-is-maui?view=net-maui-8.0

- pydantic Annotated: https://docs.pydantic.dev/latest/concepts/json_schema/#generating-json-schema
- huggingface languages: https://huggingface.co/languages

## Hugging Face
load a model card from the hub

```python
from huggingface_hub import ModelCard

card = ModelCard.load('nateraw/vit-base-beans')
```

## Types of models added to the application
- text classification (sentiment analysis, product rating)
- zero shot classification (custom labels)
- reranker
- translation
- speech2text
- text2speech

## Weekly Notes

### Week 1 (03 June - 09 June)
Understand project brief

### Week 2 (10 June - 16 June)
- tech review
    - Frontend: Electron, Tkinter, .NET MAUI
    - Backend: Flask, FastAPI
    - Python Library: Flask, FastAPI, transformer (hugging face)

### Week 3 (17 June - 23 June)
- after liaison with client, we decided to use dotnet as frontend and fastapi as backend


### Week 4 (24 June - 30 June)
- UI design

### Week 5 (01 July - 07 July)
- subprocess for each model (free up memory, track system resource usage)
- class design
- project structure

### Week 7 (08 July - 14 July)
- persona, use case
- real time speech to text issue


### Week 8 (15 July - 21 July)
- pytest
- trust remote code
- another library for reranker
- child child process works on production model but not in dev mode
- updated model control for new data structure
- adding different types of nlp models into the application

- models are limited to those support pipline only (cannot unify every kind of models, every model requires its own ways to do inference)

- app will only provide a selection of models from hugging face only
    - every model has specific configuration, they have to be indexed in a particular format. 
    if we fetch all the models from huggingface, some of them might not be able to work 
    - better for non-technical users, as many of the models on hugging face are actually fine tune from the same base model, 
    as the result, they don't have to compare 100+ models that are very similar

- models which requires running remote codes during download does not work with fastapi dev

### Week 9 (22 July - 28 July)
- added speech2text, text2speech models and zero shot classification models
- research on training
- training dataset is not uploaded into the application. the dataset has to be tokenised before training but the tokeniser used for each models are different. storing the datasets in the application is not useful and cannot be reused. unlike rag dataset and image datasets.


## playground config
first attempt: new observableCollection for playground config and bind the picker to each row
however it leads to unexpected error

## Notes

### Report Writing
plan content list
first draft of intro

### To mention (to group)
- fastapi route should use annotated [reference link](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#__tabbed_6_1)

- list all the possible config parameters with its default value in model index
    - some models requires extra default config to run
    - there should be a place to record all possible config parameters, otherwise dev or user would not know which and what parameters they can modify
    - unless they look into the model card

- what does generator do?

- task in config
- sentence prefix

### To mention (to supervisor)
- looked into huggingface accelerator
the accelerator allows the models to run faster and use less system memory.
it is particularly useful for large model like LLMs, as it significantly reduce the computational time for model prediction. hence we decided to apply it on every model.

- added more categories of nlp models, including text to speech and zero shot classification. 

zero shot classification is similar to sentiment analysis model, but instead of outputing only 
positive negatie and neutral, it allows custom topics and labels. for example

text to speech model takes texts as input and generate an audio file
since different text2speech models take different config and the ways to use them are also very different,
so it took me a bit of time to test those model.

some of the text2speech models requires speaker embedding to generate audio. 
speaker embedding is like a array recoding the characteristics of the speaker.
currently, i have saved a speaker embedding in the app and served as a default embedding.

later in this week, i will make the functionality for user to select4 different speaker embedding from the dataset upload their own speaker embedding if they have one

- model training
- it only supports text classifcation and translation.
- it supports some of the text to speech models
- most of the other models require custom script for training and it is very difficult to unify the codes for types of training
- training is only allow for sentiment analysis model and translation model

### Questions


### Issues
- connection issue when downloading models

### meeting notes

## To do

- [x] downlaod hugging face model into custom directory without running it
- [x] data.json use dict format
- [x] sentiment analysis
- [x] translation models
- [x] speech2text text2speech models
- [ ] realtime speech2text


### Random Note
- problem statement
- Map: who why how
- end user, persona, customer journey, 

- watsonx is super expensive
- offline model that can run locally (model with much lower requirements) 

- presentations
- road map, figma, proejct goal, conceptual design, plan, ...

- small model extract the important info from the doc and then offload it into watsonx

