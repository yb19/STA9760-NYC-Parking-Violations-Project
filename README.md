# STA9760-NYC-Parking-Violations-Project
This is the NYC parking violations analysis project for the Big Data Technology course (STA9760).

## Description:
First, you can use this container to extract the Open Parking and Camera Violations (OPCV) data from NYC Open Data (https://opendata.cityofnewyork.us/). You can specify the number of rows (of data) on each page, the number of pages you want to load, and whether to print out the data to stdout or write the data to the file that you speficy. 

Second, besides downloading the data, you can also use the container to load it into your elasticsearch instance so that you can search and analyze data quickly and in near real time.

Third, you can stand up an instance of Kibana on top of the ElasticSearch instance to visualize and analyze your dataset so that you can extract insights from dataset.

## Outline
This project is divided into four parts:
- Part 1: Python Scripting
- Part 2: Loading into ElasticSearch
- Part 3: Visualizing and Analysis on Kibana
- Part 4: Deploying to EC2 Instance

## Part 1 Python Scripting:
### Instructions
After pulling this container, you can use the following command to run the container:

`$ docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json`

### Arguments
YOUR_APP_KEY is your [APP TOKEN](https://data.cityofnewyork.us/login?return_to=%2Fprofile%2Fedit%2Fdeveloper_settings) for the NYC Open Data API.

--page_size=your_page_size is the number of rows (of data) on each page. This command line argument is required.

--num_pages=you_num_pages is the number of pages you want to load. If omitted, the container will continue requesting data until the entirety of the content has been exhausted.

--output=file_name.file_format is the file that the container will write the data to. If omiited, the container will simply print data to stdout.

### Warning:
If you want to spycify more than one command line argument (i.e., num_pages, output), you should follow the order of arguments specified above.
