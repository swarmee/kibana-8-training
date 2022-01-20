# kibana-8-training

This Kibana 8 training is based on Elastic Certified Analyst Exam [syllabus](https://www.elastic.co/training/elastic-certified-analyst-exam)). So running through these lessons should place you very well to complete this certification. 

The basis of the training is pulled from the [elastic.co](https://www.elastic.co) website (so all the rights and praise goes to them). There is also a sprinkle of my own experience in the training. The sample data used comes straight from Wikipedia.  

The current ```Elastic Certified Analyst Exam Prep``` syllabus is provided below for reference. 

<details><summary>Syllabus @ 31/12/2021</summary>
<p>

<i>

### Topics
To be fully prepared for the Elastic Certified Analyst exam, candidates should be able to complete all of the following exam objectives with **only the assistance of the Elastic documentation**:

#### Searching Data:
  - Define an index pattern with or without a Time Filter field
  - Set the time filter to a specified date or time range
  - Use the Kibana Query Language (KQL) in the search bar to display only documents that match a specified criteria
  - Create and pin a filter based on a search criteria
  - Apply a search criteria to a visualization or dashboard

#### Visualizing Data:
  - Create a Metric or Gauge visualization that displays a value satisfying a given criteria
  - Create a Lens visualization that satisfies a given criteria
  - Create an Area, Line, Pie, Vertical Bar or Horizontal Bar visualization that satisfies a given criteria
  - Split a visualization using sub-bucket aggregations
  - Create a visualization that computes a moving average, derivative, or serial diff aggregation
  - Customize the format and colors of a line chart or bar chart
  - Using geo data, create an Elastic map that satisfies a given criteria
  - Create a visualization using the Time Series Visual Builder (TSVB) that satisfies a given set of criteria
  - Define multiple line or bar charts on a single TSVB visualization
  - Create a chart that displays a filter ratio, moving average, or mathematical computation of two fields
  - Define a metric, gauge, table or Top N visualization in TSVB
  - Create a Tag Cloud visualization on a keyword field of an index
  - Create a Data Table visualization that satisfies a given criteria
  - Create a Markdown visualization
  - Define and use an Option List or Range Slider control
  - Create a Dashboard that consists of a collection of visualizations

#### Analyzing Data:
  - Answer questions about a given dataset using search and visualizations
  - Use visualizations to find anomalies in a dataset
  - Define a single metric, multi-metric, or population Machine Learning job
  - Define and use a scripted field for an index
  - Define and use a Space in Kibana
</i>

</p>
</details>

#### Prerequisites

You will need an Elasticsearch and Kibana instance to run through this training. I have written up some instructions on how to set one up [here](https://www.swarmee.net/swagger%204%20es/elasticsearch-cloud-instance-setup/)

### Lesson 1. Kibana Data View and Discover Tab
Dataset: Top Selling Books of All Time
[Youtube Video](www.youtube.com). 

Objectives :
- Load data into elasticsearch through kibana.
- Modify the default index ```data view``` (new name for index template). 
- Format data display using the discovery tab.  
- Perform various serarches.  

<details><summary>Steps</summary>
<p>

Steps : 
- Download dataset to your computer - ```1-top-selling-books.ndjson``` file from the datasets folder in this repo. 
- Login to Kibana and click the ```Upload a file``` link on the home page. 
- Upload dataset into Kibana. The wizard will guide you through creating the ```mapping``` and ```data view``` (replace the default mapping with mapping provided below). 
- Once the dataset is created in Kibana we can modify the data view:
   - Set a custom format for the ```yearFirstPublished``` field (YYYY). 
   - Create a scripted field to google search the books title (template = https://www.google.com.au/search?q={{value}} , script = doc['Book.keyword'].value)
- Open the dataset in the discover tab - note the impact of the data view changes we made - i.e. additional fields.  
- Format the display in the discovery tab. Noting that the rows can be expanded to see all the details. 
- Save the "search" - so it can be revisited later.  
- Perform following searches kql (Kibana's query language) and Lucene query language:
   - Simple text search (J. K. Rowling) - noting that search terms are ```OR```ed together. Can be ```AND```ed together. 
   - Field Specific search (Book : wild). 
   - Phase Search  (Author : "Stephen Hawking")
   - Boolean operator ( yearFirstPublished : 1988 AND Book : (The AND Alchemist) )   
   - Range Search with Boolean operator (yearFirstPublished >= 1980 and yearFirstPublished < 1991)
   - Lucene syntax Search for fuzzy matches (Woma~1). Edit distance of 1.    
   - Lucene syntax Search for fuzzy phase matches ("The Woman"~1). Word order distance of 1. 
- Create a simple filter and see how it can be turned on/off and inverted ("OriginalLanguage": "Norwegian" ). Note that the filters are actually generating elastic DSL queries. 
- Review the inspect tab which provides details of the requests and responses from elasticsearch. 


<details><summary>Top Sellings Books Data Mapping</summary>
<p>

{
  "properties": {
    "Author": {
      "type": "text",
      "fields": {
          "keyword": { 
            "type":  "keyword"
          }
        }      
    },
    "Book": {
      "type": "text",
      "fields": {
          "keyword": { 
            "type":  "keyword"
          }
        } 
    },
    "OriginalLanguage": {
      "type": "keyword"
    },
    "millionOfSales": {
      "type": "double"
    },
    "yearFirstPublished": {
        "type":   "date",
        "format": "yyyy"
    }
  }
}
</p>
</details>

</p>
</details>


### Lesson 2. Simple Visualistions  
Dataset: Fastest Humans Over 100m

Objectives :
- Load data into elasticsearch through kibana.
- Create Visualisations from Discover Tab (using ```lens```)
- Create Visualisations manually (using ```lens```)
- Create Visualisations manually (using ```classic``` method)


Steps : 
- Download dataset to your computer - ```2-fastest-humans-over-100m.ndjson``` file from the datasets folder in this repo. 
- Login to Kibana and click the ```Upload a file``` link on the home page. 
- Upload dataset into Kibana. The wizard will guide you through creating the ```mapping``` and ```data view``` (replace the default mapping with mapping provided below). 
- Open the dataset in the discover tab - select fields on the left to automatically create visuslisations in ```lens```. Note ```lens``` allows you to change the chart type and index at any point during the creation of the visualization. 


note the impact of the data view changes we made - i.e. additional fields.  
- Format the display in the discovery tab. Noting that the rows can be expanded to see all the details. 
- Save the "search" - so it can be revisited later.  
- Perform following searches kql (Kibana's query language) and Lucene query language:
   - Simple text search (J. K. Rowling) - noting that search terms are ```OR```ed together. Can be ```AND```ed together. 
   - Field Specific search (Book : wild). 
   - Phase Search  (Author : "Stephen Hawking")
   - Boolean operator ( yearFirstPublished : 1988 AND Book : (The AND Alchemist) )   
   - Range Search with Boolean operator (yearFirstPublished >= 1980 and yearFirstPublished < 1991)
   - Lucene syntax Search for fuzzy matches (Woma~1). Edit distance of 1.    
   - Lucene syntax Search for fuzzy phase matches ("The Woman"~1). Word order distance of 1. 
- Create a simple filter and see how it can be turned on/off and inverted ("OriginalLanguage": "Norwegian" ). Note that the filters are actually generating elastic DSL queries. 
- Review the inspect tab which provides details of the requests and responses from elasticsearch. 



<details><summary>Fastest Humans Over 100m Data Mapping</summary>
<p>


{
  "properties": {
    "athlete": {
      "type": "text",
      "fields": {
          "keyword": { 
            "type":  "keyword"
          }
        } 
    },
    "date": {
      "type": "date",
      "format": "iso8601"
    },
    "manOrWoman": {
      "type": "keyword"
    },
    "raceLocation": {
      "type": "geo_point"
    },
    "raceLocationName": {
      "type": "text",
      "fields": {
          "keyword": { 
            "type":  "keyword"
          }
        } 
    },
    "rank": {
      "type": "long"
    },
    "runnerNation": {
      "type": "text",
      "fields": {
          "keyword": { 
            "type":  "keyword"
          }
        } 
    },
    "runnerNationLocation": {
      "type": "geo_point"
    },
    "time": {
      "type": "double"
    },
    "wind": {
      "type": "double"
    }
  }
}
</p>
</details>











- Create visualizations using ```classic``` method - basically following a structured approach where you need to select the index and the chart type first. 
- Create visualizations using ```lens``` - which allows you to change the chart type and index at any point during the creation of the visualization. 

library of charts. 
- Create Dashboard with ```classic``` visulisation 




Video 2. 

#### Searching Data:
  - Define an index pattern with or without a Time Filter field
  - Set the time filter to a specified date or time range
  - Use the Kibana Query Language (KQL) in the search bar to display only documents that match a specified criteria
  - Create and pin a filter based on a search criteria
  - Apply a search criteria to a visualization or dashboard

#### Visualizing Data:
  - Create a Metric or Gauge visualization that displays a value satisfying a given criteria
  - Create a Lens visualization that satisfies a given criteria
  - Create an Area, Line, Pie, Vertical Bar or Horizontal Bar visualization that satisfies a given criteria
  - Split a visualization using sub-bucket aggregations
  - Create a visualization that computes a moving average, derivative, or serial diff aggregation
  - Customize the format and colors of a line chart or bar chart
  - Using geo data, create an Elastic map that satisfies a given criteria
  - Create a visualization using the Time Series Visual Builder (TSVB) that satisfies a given set of criteria
  - Define multiple line or bar charts on a single TSVB visualization
  - Create a chart that displays a filter ratio, moving average, or mathematical computation of two fields
  - Define a metric, gauge, table or Top N visualization in TSVB
  - Create a Tag Cloud visualization on a keyword field of an index
  - Create a Data Table visualization that satisfies a given criteria
  - Create a Markdown visualization
  - Define and use an Option List or Range Slider control
  - Create a Dashboard that consists of a collection of visualizations

#### Analyzing Data:
  - Answer questions about a given dataset using search and visualizations
  - Use visualizations to find anomalies in a dataset
  - Define a single metric, multi-metric, or population Machine Learning job
  - Define and use a scripted field for an index
  - Define and use a Space in Kibana
</p>
</details>










# swagger-4-es

`swagger-4-es` provides a Swagger UI page for the key elasticsearch (and Opensearch) endpoints. It's aimed at being a training resource to engineers starting off with 
elasticsearch. You may also consider customising the openapi specification (additional endpoints and notes) to become a training resource specific to your organisation.   

See [https://www.swarmee.net/swagger 4 es](https://www.swarmee.net/swagger%204%20es/) for further details. 

### Screenshot
[![Swagger UI Screenshot](./docs/Swagger-UI-Screenshot.png)](./docs/Swagger-UI-Screenshot.png)

### Local Setup
FolloThe following steps run you through running ```swagger-4-es``` swagger UI locally.

#### Prerequisite

The following software and configuration is required on your computer to boot up the containers:

- `docker`. See these [docs](https://docs.docker.com/get-docker/) for instructions.
- `docker-compose`. See these [docs](https://docs.docker.com/compose/install/) for instructions.
- Increase the `mmap` count on linux systems. See these [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html) for instructions.


#### Usage

```shell
docker-compose up
```

Then open [https://localhost/index.html](https://localhost/index.html) to see the Swagger UI page. The nginx container is setup to forward all to elasticsearch except for URLs ending in ```.json``` or ```.html```. 

**Noting**:

- The Elasticsearch instance will take a little while to boot up - at least 15 seconds (you should see the messages scrolling through on your terminal as it starts up).
- The container starts a nginx reverse proxy to host the Swagger UI page, it generates a self signed certificate so you will need to accept the warning message in your browser. I.e. it is expected to see a `Warning: Potential Security Risk Ahead` message when you open the Swagger UI link (Click Accept Risk and Proceed).
- No authentication is required for the local instance. 

The local instance is also avaliable directly at [http://localhost:9200](http://localhost:9200)






"text", "fields": { "keyword" : { "type" : "keyword"}}