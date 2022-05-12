# kibana-8-training

This Kibana 8 training is based on Elastic Certified Analyst Exam [syllabus](https://www.elastic.co/training/elastic-certified-analyst-exam)). So running through these lessons should place you very well to complete this certification.

The basis of the training is pulled from the [elastic.co](https://www.elastic.co) website (so all the rights and praise goes to them). There is also a sprinkle of my own experience in the training. The sample data used comes straight from Wikipedia.

The current `Elastic Certified Analyst Exam Prep` syllabus is provided below for reference.

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

You will need an Elasticsearch and Kibana instance to run through this training. I have written up some instructions on how to set up a cloud instance [here](https://www.swarmee.net/swagger%204%20es/elasticsearch-cloud-instance-setup/). Alternatively there is a ```docker-compose.yml``` file within this repo that you can use to run a elasticsearch and kibana instance locally. 

---

### Lesson 1. Kibana Data View and Discover Tab
__Dataset : Top Selling Books__

__Video Run Through__: [youtube link](https://youtu.be/3Rh6gBkuyNQ)

<details><summary>Objectives</summary>
<p>

- Load data into elasticsearch through kibana.
- Modify the default `data view` (new name for index template).
- Format data display using the discovery tab.
- Perform various serarches.

</p>
</details>

<details><summary>Steps</summary>
<p>

Steps :

- Download dataset to your computer - `1-top-selling-books.ndjson` file from the datasets folder in this repo.
- Login to Kibana and click the `Upload a file` link on the home page.
- Upload dataset into Kibana. The wizard will guide you through creating the `mapping` and `data view` (replace the default mapping with mapping provided below).
- Once the dataset is created in Kibana we can modify the data view:
  - Set a custom format for the `yearFirstPublished` field (YYYY).
  - Create a scripted field to google search the books title (template = https://www.google.com.au/search?q={{value}} , script = doc['Book.keyword'].value)
- Open the dataset in the discover tab - note the impact of the data view changes we made - i.e. additional fields.
- Format the display in the discovery tab. Noting that the rows can be expanded to see all the details.
- Save the "search" - so it can be revisited later.
- Perform following searches kql (Kibana's query language) and Lucene query language:
  - Simple text search (J. K. Rowling) - noting that search terms are `OR`ed together. Can be `AND`ed together.
  - Field Specific search (Book : wild).
  - Phase Search (Author : "Stephen Hawking")
  - Boolean operator ( yearFirstPublished : 1988 AND Book : (The AND Alchemist) )
  - Range Search with Boolean operator (yearFirstPublished >= 1980 and yearFirstPublished < 1991)
  - Lucene syntax Search for fuzzy matches (Woma~1). Edit distance of 1.
  - Lucene syntax Search for fuzzy phase matches ("The Woman"~1). Word order distance of 1.
- Create a simple filter and see how it can be turned on/off and inverted ("OriginalLanguage": "Norwegian" ). Note that the filters are actually generating elastic DSL queries.
- Review the inspect tab which provides details of the requests and responses from elasticsearch.

</p>
</details>

<details><summary>Top Sellings Books Data Mapping</summary>
<p>

```JSON
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
```

</p>
</details>

---

### Lesson 2. Simple Visualistions (lens and classic methods)
__Dataset : World's Tallest Towers__

__Video Run Through__: [youtube link](https://www.youtube.com/embed/i9W07cUt1qs)


<details><summary>Objectives</summary>
<p>

- Load data into elasticsearch through kibana - 80 documents.
- Create Visualisations from Discover Tab (using `lens`)
- Create Visualisations manually (using `lens`)
- Create Visualisations manually (using `classic` method)

The `classic` visualisation method - basically following a structured approach where you need to select the index and the chart type first.
The `lens` visualisation approach - allows you to change the chart type and index at any point during the creation of the visualisation.

</p>
</details>

<details><summary>Steps</summary>
<p>

- Download dataset to your computer - `2 - world-tallest-towers.ndjson` file from the datasets folder in this repo.
- Login to Kibana and click the `Upload a file` link on the home page.
- Upload dataset into Kibana. The wizard will guide you through loading the data - replace the generated `mapping` with the below ```mapping```. And untick the create data view (we will do it manually in the next step). 
- Once the data has been loaded - create the data view manually setting the time field as `yearBuilt` - and set the format for `yearBuilt` to __YYYY__.
- Open the dataset in the discover tab - switch to the new `Field Statistics` view and then __action__ the `cityName.keyword` field to create a create visualisation in `lens`. Note `lens` allows you to change the chart type and index at any point during the creation of the visualisation. Create the following charts:

  - Bar Horizontal Country by Count.
  - Bar Horizontal Country by Max Height.
  - Bar Vertical Stacked Height vs Records by country.

- Create a Visualisations manually using `lens` and the `classic` method.

</p>
</details>

<details><summary>Mapping</summary>
<p>

```JSON
{
  "properties": {
    "buildingName": {
      "type": "text",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "cityName": {
      "type": "text",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "countryName": {
      "type": "text",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "floors": {
      "type": "long"
    },
    "heightMeters": {
      "type": "double"
    },
    "heightFeet": {
      "type": "long"
    },
    "rank": {
      "type": "long"
    },
    "yearBuilt": {
        "type":   "date",
        "format": "yyyy"
    },
    "countryGeoPoint" : {"type" : "geo_point"},
    "countryCode" : {"type" : "keyword"}
  }
}
```

</p>
</details>


<details><summary>Source Data Script</summary>
<p>

```python
import pandas as pd
import json
import requests


df = pd.read_html('https://en.wikipedia.org/wiki/List_of_tallest_buildings')[1]
df =df.drop(['Image', 'Notes'], axis=1)



#df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
df.reset_index()
df.columns = [ 'rank'     ,   'buildingName',           'cityName',    'countryName',              'heightMeters',           'heightFeet',           'floors',          'yearBuilt']

df['floors'] = df['floors'].str.replace(r"\(.*\)","") 
df['floors'] = df['floors'].str.replace(r"\[.*\]","") 

df['floors'] = df['floors'].str.strip()

df = df.to_dict('records')

for record in df:
    r = requests.get ('https://www.swarmee.net/country/' + record['countryName'].upper())
    r = r.json()
    record["countryGeoPoint"] =  [ r['latlng'][1], r['latlng'][0] ]
    record["countryCode"]    = r["cca2"]
    print(json.dumps(record))

```



</p>
</details>


---

### Lesson 3. Simple Map Visualistions
__Dataset: Fastest 100m Runners__

__Video Run Through__: [youtube link](https://www.youtube.com/embed/ps_tO2Tuwew)

<details><summary>Objectives</summary>
<p>

- Load 102 documents into elasticsearch through kibana.
- Create Map Visualisations from Discover Tab.
- Select different map visualisation options and layers

</p>
</details>

<details><summary>Output Screenshot</summary>
<p>

<img src="./images/3 - fastest-humans-over-100m.png" alt="Screenshot">

</p>
</details>

<details><summary>Steps</summary>
<p>

- Download dataset to your computer - `3 - fastest-humans-over-100m.ndjson` file from the datasets folder in this repo.
- Login to Kibana and click the `Upload a file` link on the home page.
- Upload dataset into Kibana using the wizard.
  - Replace the default `mapping` with mapping provided below.
  - Deselect the automatic creation of the data view (it needs to be created manually afterwards - so a date/time field can be selected)
- Once the dataview is created then set the display format for the date field to be ```YYYY-MM-DD```
- Once the data is successfully uploaded manually create the data view selecting `date` as the datetime field.
- Open the dataset in the discover tab - select the - select `athleteCountryGeoPoint` field from the left hand table, go to field statistics and click action. Because it is a geo point field it will open the maps visualisation app. By default a document Geo Point Map. 
- Select different map visualisation options. I.e. -  Choropleth (World Countries EMS boundaries) and Heat Maps. 
- Hide / Unhide Layers
- Add timeslider

</p>
</details>

<details><summary>Mapping</summary>
<p>

```JSON
{
  "properties": {
    "athlete": {
      "type": "text",
      "fielddata": "true",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "athleteCountry": {
      "type": "text",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "athleteCountryGeoPoint" : {
      "type": "geo_point"
    },
    "date": {
      "type": "date",
      "format": "iso8601"
    },
    "location": {
      "type": "text",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "athleteCountryCode": {
      "type": "keyword"
    },
    "manWoman": {
      "type": "keyword"
    },
    "performance": {
      "type": "long"
    },
    "time": {
      "type": "double"
    },
    "wind": {
      "type": "double"
    }
  }
}
```

</p>
</details>

<details><summary>Source Data Script</summary>
<p>

```python
#### MEN

import pandas as pd
import json
import requests


def fiddle_with_data(Athlete,Nation ):
  if Athlete.startswith('Blake'):
    return 'Yohan Blake', 'Jamaica'
  if Athlete.startswith('Bolt'):
    return 'Usain Bolt', 'Jamaica'
  if Athlete.startswith('Gay'):
    return 'Tyson Gay', 'United States'
  if Athlete.startswith('Gatlin'):
    return 'Justin Gatlin', 'United States'
  if Athlete.startswith('Powell'):
    return 'Asafa Powell', 'Jamaica'
  if Athlete.startswith('Bromell'):
    return 'Trayvon Bromell', 'United States'
  if Athlete.startswith('Bolt'):
    return 'Usain Bolt', 'Jamaica'
  return Athlete, Nation



def wind_fiddle(wind):
  if wind.startswith('+'):
    return wind[1:]
  elif wind.startswith('−') or wind.startswith('−'):
    return '-' + wind[1:]
  else:
    return '0.0'

df = pd.read_html('https://en.wikipedia.org/wiki/100_metres')[2]
df["Date"]= pd.to_datetime(df["Date"])
df =df.drop(['Ref', 'Ath.#', "Perf.#"], axis=1)
df['Time (s)'] = df['Time (s)'].str.replace(r"\[.*\]","")

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

df['Wind (m/s)'] = df['Wind (m/s)'].apply(lambda x: wind_fiddle(x))

df[['Athlete', 'Nation']] = df.apply(lambda x: fiddle_with_data(x['Athlete'],x['Nation']),axis=1, result_type="expand")

df['performance'] = df.index
df.columns = ['time', 'wind', 'athlete', 'athleteCountry', 'date', 'location', 'performance']

df['manWoman'] = 'man'
df = df.to_dict('records')

for record in df:
    r = requests.get ('https://www.swarmee.net/country/' + record['athleteCountry'].upper())
    r = r.json()
    record["athleteCountryGeoPoint"] =  [ r['latlng'][1], r['latlng'][0] ]
    record["athleteCountryCode"]    = r["cca2"]
    print(json.dumps(record))

### WOMEN

import pandas as pd
import json
import requests


def fiddle_with_data(Athlete,Nation ):
  if Athlete.startswith('Griffith-Joyner'):
    return 'Griffith-Joyner', 'United States'
  if Athlete.startswith('Thompson-Herah'):
    return 'Elaine Thompson-Herah', 'Jamaica'
  if Athlete.startswith('Fraser-Pryce'):
    return 'Shelly-Ann Fraser-Pryce', 'Jamaica'
  if Athlete.startswith('Jeter'):
    return 'Carmelita Jeter', 'United States'
  if Athlete.startswith('Jones'):
    return 'Marion Jones', 'United States'
  return Athlete, Nation

def wind_fiddle(wind):
  if wind.startswith('+'):
    return wind[1:]
  elif wind.startswith('−') or wind.startswith('−'):
    return '-' + wind[1:]
  else:
    return '0.0'

df = pd.read_html('https://en.wikipedia.org/wiki/100_metres')[3]
df["Date"]= pd.to_datetime(df["Date"])
df =df.drop(['Ref', 'Ath.#', "Perf.#"], axis=1)
df['Time (s)'] = df['Time (s)'].str.replace(r"\[.*\]","")

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

df['Wind (m/s)'] = df['Wind (m/s)'].apply(lambda x: wind_fiddle(x))

df[['Athlete', 'Nation']] = df.apply(lambda x: fiddle_with_data(x['Athlete'],x['Nation']),axis=1, result_type="expand")

df['performance'] = df.index
df.columns = ['time', 'wind', 'athlete', 'athleteCountry', 'date', 'location', 'performance']

df['manWoman'] = 'woman'
df = df.to_dict('records')

for record in df:
    r = requests.get ('https://www.swarmee.net/country/' + record['athleteCountry'].upper())
    r = r.json()
    record["athleteCountryGeoPoint"] =  [ r['latlng'][1], r['latlng'][0] ]
    record["athleteCountryCode"]    = r["cca2"]
    print(json.dumps(record))


```

</p>
</details>

---

### Lesson 4. Simple Dashboard
__Dataset: Highest Grossing Animated Films__

__Video Run Through__: [youtube link](https://www.youtube.com/embed/ps_tO2Tuwew)

<details><summary>Objectives</summary>
<p>

- Load data into elasticsearch through kibana.
- Create Visualisations from Discover Tab (using `lens`)
- Create Visualisations manually (using `lens`)
- Create Visualisations manually (using `classic` method)

</p>
</details>

<details><summary>Output Screenshot</summary>
<p>

<img src="./images/4 - highest-grossing-animated-films.png" alt="Screenshot">

</p>
</details>

<details><summary>Steps</summary>
<p>

- Download dataset to your computer - `4 - highest-grossing-animated-films.ndjson` file from the datasets folder in this repo.
- Login to Kibana and click the `Upload a file` link on the home page.
- Upload dataset into Kibana. The wizard will guide you through loading the data into elasticsearch. Please use the mapping provided below. And select not to create the data view automatically - will create it manually after.
- Once the data is loaded we now create the data view manually, selecting `yearReleased` as the time field. 
- We now tweak the dataview to change the display of ;
  - yearReleased to `YYYY`, and
  - grossRevenue to `$0,0`.
- Open the dataset in the discover tab - select fields on the left to create a list view presentation of the data. 
- Now create a dashboard and add in 4 visualisations and the list view of the data (saved in the previous step).


</p>
</details>

<details><summary>Mapping</summary>
<p>

```JSON
{
  "properties": {
    "grossRevenue": {
      "type": "long"
    },
    "movieTitle": {
      "type": "text",
      "fielddata": "true",
      "fields": {
          "keyword": {
            "type":  "keyword"
          }
        }
    },
    "rank": {
      "type": "long"
    },
    "yearReleased": {
        "type":   "date",
        "format": "yyyy"
    }
  }
}
```

</p>
</details>

<details><summary>Source Data Script</summary>
<p>

```python
import pandas as pd
import json

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_highest-grossing_animated_films')[0]  ### Download first table on wiki page

df =df.drop(['Reference(s)'], axis=1) ### remove reference column
df["Worldwide gross"] = df["Worldwide gross"].replace('[\$\,\.]',"",regex=True).astype(int)  ### convert amount string to float
df['Rank'] = df['Rank'].str.replace(r"\[.*\]","")  ### remove square brackets
df['Title'] = df['Title'].str.replace(r"\[.*\]","")
df.columns = ['rank', 'movieTitle', 'grossRevenue', 'yearReleased']  ### rename columns
df = df.to_dict('records')

for record in df:
    print(json.dumps(record))
```

</p>
</details>
