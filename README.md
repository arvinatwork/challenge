# Git Stats Challenge

## How to run

For python:

python git_summarizer.py [-h] repositories [repositories ...]

e.g. 
python git_summarizer.py facebook/react google/clusterfuzz

Use python git_summarizer.py -h for help


## Output
Current output is in CSV format. But it can be easily extended to support other formats.

# Static Site Challenge

## How to run
- Run docker-compose build
- Run docker-compose up

# How to access
Go to these sites:
- Demo site: localhost:80 or **localhost**
- Kibana: **localhost:5601**

# Kibana index pattern setup
Kibana need to setup an index pattern on first run. 
To do that, make sure you've generated some logs for Kibana to have a data to get. 

Then, create the index pattern referencing from the available indexes in the list.

Normally, there should be a **'fluent_xxxx'** index. Just type **'fluent'** and continue with the steps. 

Then you may now go to the **Discover** tab to view the logs.

## How to quit
Run docker-compose down
