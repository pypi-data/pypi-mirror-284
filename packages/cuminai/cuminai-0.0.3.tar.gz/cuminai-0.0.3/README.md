# cuminai

This package contains the Cumin AI Python SDK. Cumin AI is a Managed LLM Context Service. This package provides integration with Langchain.

## Installation

```bash
pip install cuminai
```

## Usage

The `cuminai` class helps easily access the Cumin AI Context store.

```python
# Setup API key
import os
from getpass import getpass

CUMINAI_API_KEY = getpass("Enter Cumin AI API Key: ")
os.environ["CUMINAI_API_KEY"] = CUMINAI_API_KEY
```

```python
# Access Cumin AI Client
from cuminai import CuminAI

embedding =  ... # use a LangChain Embeddings class

client = CuminAI(
    source="<Cumin AI Context Source>",
    embedding_function = embedding
)
```

```python
# Get Langchain retreiver for Appending to Chain.
num_docs_to_retrieve = ... # number of docs to retrieve. Defaults to 4
retriever = client.as_retriever(search_kwargs={"k": num_docs_to_retrieve})
```

```python
# Get Langchain retreiver with document with at least one of the tags.
num_docs_to_retrieve = ... # number of docs to retrieve. Defaults to 4
has_any_of_these_tags = ["<document tag 1>", "<document tag 2>"] # only docs with at lease one of these tags will be returned from Cumin AI knowledge base
retriever = client.as_retriever(search_kwargs={"k": num_docs_to_retrieve, "cuminai_tags": has_any_of_these_tags})
```

## For Creators
Publishing knowledge is simple with Cumin AI. Currently we support the following knowledge types:
- Links - scrapable URLs can be given as input
- Text files - .txt and .md files can be given as input. The text files should be in the same directory where `CUMINFILE.yaml` exists.

To upload knowledge to Cumin AI, the creators must first create a `CUMINFILE.yaml` in their project directory.

Sample CUMINFILE.yaml for getting started:
```yaml
name: "<name of knowledge source>"
kind: LINK
version:
    tag: <tag name>
    latest: true
type: PUBLIC
embedding: ollama/nomic-embed-text:v1.5
tag:
    type: global
chunkstrategy:
    size: 1024
    overlap: 100
knowledge:
    - source: "<enter url for first link source>"
    - source: "<enter url for second link source>"
    - source: "<enter url for third link source>"
```

For text based knowledge sample CUMINFILE is given below:
```yaml
name: "<name of knowledge source>"
kind: TEXT
version:
    tag: v1
    latest: true
type: PRIVATE
embedding: ollama/nomic-embed-text:v1.5
tag:
    type: local
    minoccurances: 1
chunkstrategy:
    size: 1024
    overlap: 100
knowledge:
    - 
        source: "<enter name with extension for first text file>"
        metadata:
            tags:
                - <document tag 1>
                - <document tag 2>
    - source: "<enter name with extension for second text file>"
    - source: "<enter name with extension for third text file>"
```

Then make sure you have latest version of cuminai
```bash
pip install cuminai
```

Subsequently login into Cumin AI using your username and api key obtained from Cumin AI dashboard. 
```bash
cuminai login --username <username> --apikey <Cumin AI API Key>
```

once you have authenticated, go to the project directory and validate your `CUMINFILE.yaml` by running the following command from your terminal
```bash
cuminai validate
```

then once the validation is successful, you can deploy your knowledge to Cumin AI using the below command
```bash
cuminai deploy
```

Post deployment your knowledge will be available for Cumin AI users at
```
@<username>/<name of knowledge source>
```

this knowledge source can be accessed in python
```python
# Access Cumin AI Client
from cuminai import CuminAI

embedding =  ... # use a LangChain Embeddings class

client = CuminAI(
    source="@<username>/<name of knowledge source>:<version of knowledge>",
    embedding_function = embedding
)
```
if `<version of knowledge>` is left empty then the latest version of knowledge is used.

you can logout of Cumin AI by typing the below on your terminal
```
cuminai logout
```

## Release
Currently Cumin AI is in `pre-release` mode. We have exciting things planned. You can check out our [roadmap](https://roadmap.cuminai.com) to know more.

## License
[Apache 2.0](./LICENSE)