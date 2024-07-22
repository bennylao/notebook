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

### To mention (to supervisor)
- models which requires running remote codes during download does not work with fastapi dev
- models are limited to those support pipline only (cannot unify every kind of models, every model requires its own ways to do inference)
- app will only provide a selection of models from hugging face only
    - every model has specific configuration, if we fetch all the models from huggingface, some of them might not be able to work
    - also every model has to be indexed in a particular format and this is difficult to use retreieve automatically
    - better for non-technical users, less choice, they don't have to compare 100+ models
- child model for different nlp tasks under transformer model

### Questions
1. watson model in model index have pipeline tag?

### Issues
- connection issue when downloading models

### meeting notes

## To do

- [x] downlaod hugging face model into custom directory without running it
- [x] data.json use dict format
- [x] sentiment analysis
- [x] translation models
- [ ] speech2text text2speech models
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

