# STA9760-NYC-Parking-Violations-Project
This is the NYC parking violations analysis project for the Big Data Technology course (STA9760).

## Description
This project aims to use big data technology to extract, store, and analyze big volumns of data. Specifically, the project can be used to extract parking violations data from NYC Open Data source, then store it in Elasticsearch, and finally analyze it on Kibana.

## Dataset
The dataset used in the project is the Open Parking and Camera Violations (OPCV) data from NYC Open Data (https://opendata.cityofnewyork.us/). 

## Outline
This project is divided into four parts:
- Part 1: Python Scripting
- Part 2: Loading into ElasticSearch
- Part 3: Visualizing and Analysis on Kibana
- Part 4: Deploying to EC2 Instance

## Part 1: Python Scripting
In this part, you can use this container to extract parking violations data from NYC Open Data. You can specify the number of rows (of data) on each page, the number of pages you want to load, and whether to print out the data to stdout or write the data to the file that you speficy. 

### Instructions
After pulling the container, run the container using:

```
$ docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
```

You can also run the container on AWS EC2 using:

```
$ sudo docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
```

### Arguments
- **YOUR_APP_KEY** is your [APP TOKEN](https://data.cityofnewyork.us/login?return_to=%2Fprofile%2Fedit%2Fdeveloper_settings) for the NYC Open Data API.

- **--page_size=your_page_size** is the number of rows (of data) on each page. This command line argument is required.

- **--num_pages=you_num_pages** is the number of pages you want to load. If omitted, the container will continue requesting data until the entirety of the content has been exhausted.

- **--output=file_name.file_format** is the file that the container will write the data to. If omiited, the container will simply print data to stdout.

### Warning:
If you want to spycify more than one command line argument (i.e., num_pages, output), you should follow the order of arguments specified above.

## Part 2: Loading into ElasticSearch
In this part, besides downloading the data, you can also use the container to load it into your elasticsearch instance so that you can search and analyze data quickly and in near real time.

### Instructions
1. After pulling the container, spin up the entire service (bigdata1, Elasticsearch, Kibana) using:

```
$ docker-compose up -d
```

2. Download data from NYC Open Data and store it to Elasticsearch using:

```
docker-compose run -e APP_TOKEN=${YOUR_APP_TOKEN} pyth python main.py --page_size=2 --num_pages=2 --output=result.txt
```

3. View data by typing "localhost:5601" in your browser or using:

```
$ curl http://localhost:9200/bigdata1/parkviolates/_search?q=state:NJ&size=1
```

4. After finishing the whole process, turn off the service using:

```
$ docker-compose down
```

## Part 3: Visualizing and Analysis on Kibana
In this part, you can stand up an instance of Kibana on top of the ElasticSearch instance to visualize and analyze your dataset so that you can extract insights from dataset.

### Instructions
1. After pushing data into Elasticsearch, view data on Kibana by typing "localhost:5601" in your browser.

2. Click "Index Patterns" under Management column on the left.

3. Copy "bigdata1" into blank box and click "Next step" on the bottom right.

4. Select "issue_date" as the Time Filter field name and click "Create index pattern" on the bottom right.

5. View data under Discover column on the left and select "Last 2 years" under Time Range on the top right.

6. Create visuals under Visualize column or dashboard under Dashboard column on the left.

### Visualizations
#### 1. Number of Violations by Month
![](Part%203/images/lineplot.png)

#### 2. Top 5 Popular Violations
![](Part%203/images/pieplot.png)

#### 3. Average Reduction Amount by County
![](Part%203/images/barplot.png)

#### 4. Relationship Between Violation Type and Penalty Amount
![](Part%203/images/heatmap.png)

### Dashboard
![](Part%203/images/dashboard.png)
