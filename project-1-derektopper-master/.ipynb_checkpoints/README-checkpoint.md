# Project 1: Query Project

- In the Query Project, you will get practice with SQL while learning about
  Google Cloud Platform (GCP) and BiqQuery. You'll answer business-driven
  questions using public datasets housed in GCP. To give you experience with
  different ways to use those datasets, you will use the web UI (BiqQuery) and
  the command-line tools, and work with them in Jupyter Notebooks.

#### Problem Statement

- You're a data scientist at Lyft Bay Wheels (https://www.lyft.com/bikes/bay-wheels), formerly known as Ford GoBike, the
  company running Bay Area Bikeshare. You are trying to increase ridership, and
  you want to offer deals through the mobile app to do so. 
  
- What deals do you offer though? Currently, your company has several options which can change over time.  Please visit the website to see the current offers and other marketing information. Frequent offers include: 
  * Single Ride 
  * Monthly Membership
  * Annual Membership
  * Bike Share for All
  * Access Pass
  * Corporate Membership
  * etc.

- Through this project, you will answer these questions: 

  * What are the 5 most popular trips that you would call "commuter trips"? Not sure yet. 
  
  * What are your recommendations for offers (justify based on your findings)?

- Please note that there are no exact answers to the above questions, just like in the proverbial real world.  This is not a simple exercise where each question above will have a simple SQL query. It is an exercise in analytics over inexact and dirty data. 

- You won't find a column in a table labeled "commuter trip".  You will find you need to do quite a bit of data exploration using SQL queries to determine your own definition of a communter trip.  In data exploration process, you will find a lot of dirty data, that you will need to either clean or filter out. You will then write SQL queries to find the communter trips.

- Likewise to make your recommendations, you will need to do data exploration, cleaning or filtering dirty data, etc. to come up with the final queries that will give you the supporting data for your recommendations. You can make any recommendations regarding the offers, including, but not limited to: 
  * market offers differently to generate more revenue 
  * remove offers that are not working 
  * modify exising offers to generate more revenue
  * create new offers for hidden business opportunities you have found
  * etc. 

#### All Work MUST be done in the Google Cloud Platform (GCP) / The Majority of Work MUST be done using BigQuery SQL / Usage of Temporary Tables, Views, Pandas, Data Visualizations

A couple of the goals of w205 are for students to learn how to work in a cloud environment (such as GCP) and how to use SQL against a big data data platform (such as Google BigQuery).  In keeping with these goals, please do all of your work in GCP, and the majority of your analytics work using BigQuery SQL queries.

You can make intermediate temporary tables or views in your own dataset in BigQuery as you like.  Actually, this is a great way to work!  These make data exploration much easier.  It's much easier when you have made temporary tables or views with only clean data, filtered rows, filtered columns, new columns, summary data, etc.  If you use intermediate temporary tables or views, you should include the SQL used to create these, along with a brief note mentioning that you used the temporary table or view.

In the final Jupyter Notebook, the results of your BigQuery SQL will be read into Pandas, where you will use the skills you learned in the Python class to print formatted Pandas tables, simple data visualizations using Seaborn / Matplotlib, etc.  You can use Pandas for simple transformations, but please remember the bulk of work should be done using Google BigQuery SQL.

#### GitHub Procedures

In your Python class you used GitHub, with a single repo for all assignments, where you committed without doing a pull request.  In this class, we will try to mimic the real world more closely, so our procedures will be enhanced. 

Each project, including this one, will have it's own repo.

Important:  In w205, please never merge your assignment branch to the master branch. 

Using the git command line: clone down the repo, leave the master branch untouched, create an assignment branch, and move to that branch:
- Open a linux command line to your virtual machine and be sure you are logged in as jupyter.
- Create a ~/w205 directory if it does not already exist `mkdir ~/w205`
- Change directory into the ~/w205 directory `cd ~/w205`
- Clone down your repo `git clone <https url for your repo>`
- Change directory into the repo `cd <repo name>`
- Create an assignment branch `git branch assignment`
- Checkout the assignment branch `git checkout assignment`

The previous steps only need to be done once.  Once you your clone is on the assignment branch it will remain on that branch unless you checkout another branch.

The project workflow follows this pattern, which may be repeated as many times as needed.  In fact it's best to do this frequently as it saves your work into GitHub in case your virtual machine becomes corrupt:
- Make changes to existing files as needed.
- Add new files as needed
- Stage modified files `git add <filename>`
- Commit staged files `git commit -m "<meaningful comment about your changes>"`
- Push the commit on your assignment branch from your clone to GitHub `git push origin assignment`

Once you are done, go to the GitHub web interface and create a pull request comparing the assignment branch to the master branch.  Add your instructor, and only your instructor, as the reviewer.  The date and time stamp of the pull request is considered the submission time for late penalties. 

If you decide to make more changes after you have created a pull request, you can simply close the pull request (without merge!), make more changes, stage, commit, push, and create a final pull request when you are done.  Note that the last data and time stamp of the last pull request will be considered the submission time for late penalties.

---

## Parts 1, 2, 3

We have broken down this project into 3 parts, about 1 week's work each to help you stay on track.

**You will only turn in the project once  at the end of part 3!**

- In Part 1, we will query using the Google BigQuery GUI interface in the cloud.

- In Part 2, we will query using the Linux command line from our virtual machine in the cloud.

- In Part 3, we will query from a Jupyter Notebook in our virtual machine in the cloud, save the results into Pandas, and present a report enhanced by Pandas output tables and simple data visualizations using Seaborn / Matplotlib.

---

## Part 1 - Querying Data with BigQuery

### SQL Tutorial

Please go through this SQL tutorial to help you learn the basics of SQL to help you complete this project.

SQL tutorial: https://www.w3schools.com/sql/default.asp

### Google Cloud Helpful Links

Read: https://cloud.google.com/docs/overview/

BigQuery: https://cloud.google.com/bigquery/

Public Datasets: Bring up your Google BigQuery console, open the menu for the public datasets, and navigate to the the dataset san_francisco.

- The Bay Bike Share has two datasets: a static one and a dynamic one.  The static one covers an historic period of about 3 years.  The dynamic one updates every 10 minutes or so.  THE STATIC ONE IS THE ONE WE WILL USE IN CLASS AND IN THE PROJECT. The reason is that is much easier to learn SQL against a static target instead of a moving target.

- (USE THESE TABLES!) The static tables we will be using in this class are in the dataset **san_francisco** :

  * bikeshare_stations

  * bikeshare_status

  * bikeshare_trips

- The dynamic tables are found in the dataset **san_francisco_bikeshare**

### Some initial queries

Paste your SQL query and answer the question in a sentence.  Be sure you properly format your queries and results using markdown. 

- What's the size of this dataset? (i.e., how many trips)
```sql
select count(*) from `bigquery-public-data.san_francisco.bikeshare_trips`
```
  - 983648

- What is the earliest start date and time and latest end date and time for a trip?
```sql
select min(time), max(time) from `bigquery-public-data.san_francisco.bikeshare_status`
```
  - Earliest: 2013-08-29 12:06:01 UTC, Latest: 2016-08-31 23:58:59 UTC

- How many bikes are there?
```sql
select count(distinct bike_number) from `bigquery-public-data.san_francisco.bikeshare_trips`
```
  - 700

### Questions of your own
- Make up 3 questions and answer them using the Bay Area Bike Share Trips Data.  These questions MUST be different than any of the questions and queries you ran above.

- Question 1: What is the most common trip and how many trips were taken?

  * Answer: From 'Harry Bridges Plaza (Ferry Building)' to 'Embarcadero at Sansome' and there were 9150 trips.
  
  * SQL query: 
 ```sql
select start_station_name, end_station_name,       count(start_station_name) as count2 from `bigquery-public-    data.san_francisco.bikeshare_trips` group by start_station_name, end_station_name order by count(start_station_name) desc limit 1
```


- Question 2: Did more trips come from subscribers or from customers?
  * Answer: Customers took 136,809 trips, while Subscribers took 846,839 trips.

  * SQL query: 
```sql
select distinct(subscriber_type) as user, count(subscriber_type) as count2 from `bigquery-public-data.san_francisco.bikeshare_trips` group by subscriber_type
```

- Question 3: When were the first stations installed? 
  * Answer: The earliest stations were installed on 2013-08-05
  * SQL query: 
```sql
select min(installation_date) as minDate from `bigquery-public-data.san_francisco.bikeshare_stations` group by installation_date order by installation_date limit 1
```

### Bonus activity queries (optional - not graded - just this section is optional, all other sections are required)

The bike share dynamic dataset offers multiple tables that can be joined to learn more interesting facts about the bike share business across all regions. These advanced queries are designed to challenge you to explore the other tables, using only the available metadata to create views that give you a broader understanding of the overall volumes across the regions(each region has multiple stations)

We can create a temporary table or view against the dynamic dataset to join to our static dataset.

Here is some SQL to pull the region_id and station_id from the dynamic dataset.  You can save the results of this query to a temporary table or view.  You can then join the static tables to this table or view to find the region:
```sql
#standardSQL
select distinct region_id, station_id
from `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info`
```

- Top 5 popular station pairs in each region

- Top 3 most popular regions(stations belong within 1 region)

- Total trips for each short station name in each region

- What are the top 10 used bikes in each of the top 3 region. these bikes could be in need of more frequent maintenance.

---

## Part 2 - Querying data from the BigQuery CLI 

- Use BQ from the Linux command line:

  * General query structure

    ```
    bq query --use_legacy_sql=false '
        SELECT count(*)
        FROM
           `bigquery-public-data.san_francisco.bikeshare_trips`'
    ```

### Queries

1. Rerun the first 3 queries from Part 1 using bq command line tool (Paste your bq
   queries and results here, using properly formatted markdown):

  * What's the size of this dataset? (i.e., how many trips)
  
  ```
  bq query --use_legacy_sql=false '
  SELECT count(*) as trips
  FROM
      `bigquery-public-data.san_francisco.bikeshare_trips`'
      
    +--------+
    | trips  |
    +--------+
    | 983648 |
    +--------+
  ```
  
  * What is the earliest start time and latest end time for a trip?
  ```
  bq query --use_legacy_sql=false '
  SELECT min(time) as EarliestRide, max(time) as LatestRide
  FROM
      `bigquery-public-data.san_francisco.bikeshare_status`'
      
    +---------------------+---------------------+
    |    EarliestRide     |     LatestRide      |
    +---------------------+---------------------+
    | 2013-08-29 12:06:01 | 2016-08-31 23:58:59 |
    +---------------------+---------------------+
  ```

  * How many bikes are there?
  ```
  bq query --use_legacy_sql=false '
  SELECT count(distinct bike_number) 
  FROM 
      `bigquery-public-data.san_francisco.bikeshare_trips`'
      
    +--------+
    | bikes  |
    +--------+
    |  700   |
    +--------+
  ```




2. New Query (Run using bq and paste your SQL query and answer the question in a sentence, using properly formatted markdown):

  * How many trips are in the morning vs in the afternoon?
  - ***In the San Francisco Bikeshare trips, there were 516,839 trips in the afternoon, from the time frame of 12pm to 8pm, while there were 406.317 trips in the morning from 4 am to 12 pm.***
  
  ```
  bq query --use_legacy_sql=false '
  SELECT 
    case when EXTRACT(Hour FROM start_date ) >= 4 and EXTRACT(Hour FROM start_date ) < 12 then "Morning"
    when EXTRACT(Hour FROM start_date ) >= 12 and EXTRACT(Hour FROM start_date ) < 20 then "Afternoon"
    else "Night" end as time_of_day,  
    count(case when EXTRACT(Hour FROM start_date ) >= 4 and EXTRACT(Hour FROM start_date ) < 12 then "Morning"
    when EXTRACT(Hour FROM start_date ) >= 12 and EXTRACT(Hour FROM start_date ) < 20 then "Afternoon"
    else "Night" end) as num_trips
  FROM `bigquery-public-data.san_francisco.bikeshare_trips`
  group by time_of_day'
  
+-------------+-----------+
| time_of_day | num_trips |
+-------------+-----------+
| Afternoon   |    516839 |
| Morning     |    406317 |
| Night       |     60492 |
+-------------+-----------+
  
  ```


### Project Questions
Identify the main questions you'll need to answer to make recommendations (list
below, add as many questions as you need).

CAN WE FIND OPEN DOCKS IN CERTAIN AREAS? NO SPOTS TO DOCK OR BIKES TO TAKE?

- Question 1: What are the 5 most popular trips between 6am and 11am on Weekdays?

- Question 2: What are the 5 most popular trips between 3pm and 8pm on Weekdays?

- Question 3: Do the stations involved in the 5 most popular trips have enough bikes for users to take?

- Question 4: Do the stations involved in the 5 most popular trips have enough docks for users to dock at?

- Question 5: How many trips occurred from subscribers vs customers on weekday mornings from 6am to 11am?

- Question 6: How many trips occurred from subscribers vs customers on weekday afternoons from 3pm and 8pm?

- ...

- Question n: 

### Answers

Answer at least 4 of the questions you identified above You can use either
BigQuery or the bq command line tool.  Paste your questions, queries and
answers below.

- Question 1: How many trips occurred from subscribers vs customers on weekday mornings from 6am to 11am?
 
  * Answer: About 95% of these trips occurred from subscribers, who made 324,219 trips  on weekday mornings from 6am to 11am, while customers made just 15,662 trips. This is notably higher than the data without filters, where about 85% of trips were made by subscribers.
  
  * SQL query:
```
SELECT subscriber_type, count(subscriber_type) as count
FROM `bigquery-public-data.san_francisco.bikeshare_trips`
WHERE EXTRACT(Hour FROM start_date ) >= 6  and EXTRACT(Hour FROM start_date ) < 11 and
      EXTRACT(DAYOFWEEK FROM start_date) <> 1 and EXTRACT(DAYOFWEEK FROM start_date) <> 7
GROUP BY subscriber_type
```

- Question 2: How many trips occurred from subscribers vs customers on weekday afternoons from 3pm and 8pm?
  * Answer: About 91% of these trips occurred from subscribers, who made 318,350 trips on weekday afternoons from 3pm and 8pm, while customers made just 31,178 trips. This is notably higher than the data without filters, where about 85% of trips were made by subscribers.
  * SQL query:
  
```
SELECT subscriber_type, count(subscriber_type) as count
FROM `bigquery-public-data.san_francisco.bikeshare_trips`
WHERE EXTRACT(Hour FROM start_date ) >= 15 and EXTRACT(Hour FROM start_date ) < 20 and
  EXTRACT(DAYOFWEEK FROM start_date) <> 1 and EXTRACT(DAYOFWEEK FROM start_date) <> 7 
GROUP BY subscriber_type
```

- Question 3: What are the 5 most popular trips between 6am and 11am on Weekdays?
  * Answer: The 5 most popular weekday morning trips are the Ferry Building to 2nd at Townsend, which saw 4,904 trips; San Francisco Caltrain to the Temporary Transbay Terminal, which saw 4,310 trips; San Francisco Caltrain 2 to Townsend at 7th, which saw 4,203 trips; Steuart at Market to the Embarcadero at Folsom, whcih saw 4,125 trips; and San Francisco Caltrain to Steuart at Market, which saw 3,705 trips. A table with this information is shown below.

```
+-----------------------------------------+----------------------------------------------+-----------+
|           start_station_name            |           end_station_name                   |      count|
+-----------------------------------------+----------------------------------------------+-----------+
| Harry Bridges Plaza (Ferry Building)    | 2nd at Townsend                              |      4904 |
| San Francisco Caltrain (Townsend at 4th)| Temporary Transbay Terminal (Howard at Beale)|      4310 |
| San Francisco Caltrain 2 (330 Townsend) | Townsend at 7th                              |      4203 |
| Steuart at Market                       | Embarcadero at Folsom                        |      4125 |
| San Francisco Caltrain (Townsend at 4th)| Steuart at Market                            |      3705 |
+-----------------------------------------+----------------------------------------------+-----------+
```

  * SQL query:
```
SELECT start_station_name, end_station_name, count(*) as count
FROM `bigquery-public-data.san_francisco.bikeshare_trips`
WHERE EXTRACT(Hour FROM start_date ) >= 6 and EXTRACT(Hour FROM start_date ) < 11 and
  EXTRACT(DAYOFWEEK FROM start_date) <> 1 and EXTRACT(DAYOFWEEK FROM start_date) <> 7 
GROUP BY start_station_name, end_station_name 
ORDER BY count desc
LIMIT 5
```
  
- Question 4:  What are the 5 most popular trips between 3pm and 7pm on Weekdays?
  * Answer:
  
```
+---------------------------------------------+-----------------------------------------+-----------+
|           start_station_name                |           end_station_name              |      count|
+---------------------------------------------+-----------------------------------------+-----------+
| 2nd at Townsend                              | Harry Bridges Plaza (Ferry Building)   |      5041 |
| Embarcadero at Folsom                        | San Francisco Caltrain (Townsend at 4th)|     4877 |
| Embarcadero at Sansome                       | Steuart at Market                       |     4400 |
| Temporary Transbay Terminal (Howard at Beale)| San Francisco Caltrain (Townsend at 4th)|     4130 |
| Steuart at Market                            | San Francisco Caltrain (Townsend at 4th)|     4052 |
+----------------------------------------------+-----------------------------------------+----------+
```
  
  
  * SQL query:
```
SELECT start_station_name, end_station_name, count(*) as count
FROM `bigquery-public-data.san_francisco.bikeshare_trips`
WHERE EXTRACT(Hour FROM start_date ) >= 15 and EXTRACT(Hour FROM start_date ) < 20 and
  EXTRACT(DAYOFWEEK FROM start_date) <> 1 and EXTRACT(DAYOFWEEK FROM start_date) <> 7 
GROUP BY start_station_name, end_station_name 
ORDER BY count desc
limit 5
```
  
- ...

- Question n:
  * Answer:
  * SQL query:

---

## Part 3 - Employ notebooks to synthesize query project results

### Get Going

Create a Jupyter Notebook against a Python 3 kernel named Project_1.ipynb in the assignment branch of your repo.

#### Run queries in the notebook 

At the end of this document is an example Jupyter Notebook you can take a look at and run.  

You can run queries using the "bang" command to shell out, such as this:

```
! bq query --use_legacy_sql=FALSE '<your-query-here>'
```

- NOTE: 
- Queries that return over 16K rows will not run this way, 
- Run groupbys etc in the bq web interface and save that as a table in BQ. 
- Max rows is defaulted to 100, use the command line parameter `--max_rows=1000000` to make it larger
- Query those tables the same way as in `example.ipynb`

Or you can use the magic commands, such as this:

```sql
%%bigquery my_panda_data_frame

select start_station_name, end_station_name
from `bigquery-public-data.san_francisco.bikeshare_trips`
where start_station_name <> end_station_name
limit 10
```

```python
my_panda_data_frame
```

#### Report in the form of the Jupter Notebook named Project_1.ipynb

- Using markdown cells, MUST definitively state and answer the two project questions:

  * What are the 5 most popular trips that you would call "commuter trips"? 
  
  * What are your recommendations for offers (justify based on your findings)?

- For any temporary tables (or views) that you created, include the SQL in markdown cells

- Use code cells for SQL you ran to load into Pandas, either using the !bq or the magic commands

- Use code cells to create Pandas formatted output tables (at least 3) to present or support your findings

- Use code cells to create simple data visualizations using Seaborn / Matplotlib (at least 2) to present or support your findings

### Resource: see example .ipynb file 

[Example Notebook](example.ipynb)

