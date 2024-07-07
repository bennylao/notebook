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

## Random Note
- problem statement
- Map: who why how
- end user, persona, customer journey, 

- watsonx is super expensive
- offline model that can run locally (model with much lower requirements) 

- presentations
- road map, figma, proejct goal, conceptual design, plan, ...

- small model extract the important info from the doc and then offload it into watsonx

## To-do

- Auto fetching LLM models
- .NET MAUI
- Integration between Python and .NET

## meeting notes



## Weekly Notes

### Week 1
Understand project brief

### Week 2
- tech review
    - Frontend: Electron, Tkinter, .NET MAUI
    - Backend: Flask, FastAPI
    - Python Library: Flask, FastAPI, transformer (hugging face)

### Week 3

### Week 4
- UI design

### Week 5
- subprocess for each model (free up memory, track system resource usage)

### Report Writing

plan content list
first draft of intro

### To mention
- dict or array



### To do

- downlaod hugging face model into custom directory without running it
- put fastapi into dotnet
- prompt tuning
- Rag
- hugging face model card
- data.json use dict format

- abstract and interface
- access type
- 