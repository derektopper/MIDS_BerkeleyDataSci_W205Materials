# template-activity-01

## Assignment 01: Set up and prerequisites

1. Git
- Install git.
https://git-scm.com/downloads

- You may see references to the stand alone app for git on your desktop. That's not what we're using for this course.

- Watch the videos in this series that you need to watch (seriously, even if you've been working with git for a while, it's sometimes handy to revisit, e.g., the difference between git and Github). They are on youtube. If you don't have a subscription, it will pop up with short ads. Sorry, but these are really decent videos. There's about 30 min total.

https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD

- Follow the instructions to do what the videos walk you through.



2. Data Engineering Jobs

- Google "data engineering jobs"
- Read ads (between 5 & 10)
- What are companies looking for in skills, experience, competencies?

* Answer: I looked at 5 job postings and these were some of the skills and requirements I found.
  * Most of the companies wanted some level of experience with data engineering. They seemed to also want someone who was comfortable writing SQL statements.
  * They typically wanted someone who had worked with a big data technology like Snowflake, Redshift or Python, as well as experience using a MapReduce schema.
  * Some posting also mention knowing how to use streaming data pipelines using Kafka, or Spark.
  * Postings also mention a preference for those working with a major cloud provider such as AWS or Azure. They also mention experience with Airflow.
  * Postings also reference familiarity with deploying data notebook and analytic environments such as Jupyter and Databricks and binary data serialization formats such as Parquet, Avro, and Thrift
  
* Postings
  
* Amazon: Data Engineer, Analytics and Insights
  - 3+ years of experience as a Data Engineer
  - Experience in SQL
  - A track record of manipulating, processing, and extracting value from large datasets and demonstrated strength in data modeling, data-pipelines development, and data warehousing.
  - Experience with a data warehouse technology
  - Experience using big data technologies (S3, MPP database, Spark/Scala, EMR, Redshift/Spectrum, Python, etc.)
  - Experience using business intelligence reporting tools (Tableau, Business Objects, Cognos, etc.)
  - Experience working with cloud computing and infrastructure (AWS, Google Cloud, Azure)
  - Knowledge of distributed systems as it pertains to data storage and computing
  
* Facebook: Data Engineer, Analytics
  - 4+ years experience in the data warehouse space.
  - 4+ years experience in custom ETL design, implementation and maintenance.
  - 4+ years experience working with either a Map Reduce or an MPP system.
  - 4+ years experience with schema design and dimensional data modeling.
  - 4+ years experience in writing SQL statements.
  - Communication skills including the ability to identify and communicate data driven insights.
  - Ability in managing and communicating data warehouse plans to internal clients.
  - Manage data warehouse plans for a product or a group of products.
  - Design, build and launch new data extraction, transformation and loading processes in production.
  - Define and manage SLA for all data sets in allocated areas of ownership.
  - Work with data infrastructure to triage infra issues and drive to resolution.

* Goldman Sachs: Junior Data Engineer, Investment Banking
  - Minimum 3 years of experience building distributed systems in a scale-out micro-service architecture using Java or Python.
  - Minimum 1 year production experience with Kafka, Kinesis or equivalent as a Data Bus / Work Queue
  - S. or higher in Computer Science (or equivalent work experience)
  - Comfort with Agile operating models that emphasize automated testing

* Away Travel: Data Engineer
  - 2-5 years of experience building data pipelines using Python
  - 2-5 years of experience with distributed data storage systems/formats & data stores such as Snowflake, Redshift or other Big data systems
  - SQL knowledge is required, Linux/Unix experience preferred
  - Experience working with batch processing/real-time systems using various open source technologies like Spark, MapReduce, NoSQL, Hive, etc.
  - Experience working with messaging frameworks such as Kafka or Kinesis
  - Experience with Airflow is a nice to have
  - Have worked with a major cloud provider such as AWS or Azure
  - Knowledge in data modeling, data access, and data storage techniques for big data platforms
  - Exposure to Continuous Integration/Continuous Deployment & Test Driven Development preferred
  - Hard-working with a "no task is too small" attitude

* Disney Streaming Services

  - 3-5 years of experience developing in object oriented Python
  - Experience deploying and running AWS-based data solutions and familiar with tools such as Cloud Formation, IAM, Athena, and Kinesis
  - Experience engineering big-data solutions using technologies like EMR, S3, Spark and an in-depth understanding of data partitioning and sharding techniques
  - Familiar with metadata management, data lineage, and principles of data governance
  - Experience loading and querying cloud-hosted databases such as Redshift and Snowflake
  - Building streaming data pipelines using Kafka, Spark, or Flink
  - Familiarity with binary data serialization formats such as Parquet, Avro, and Thrift
  - Experience deploying data notebook and analytic environments such as Jupyter and Databricks
  - Knowledge of the Python data ecosystem using pandas and numpy
  - Experience building and deploying ML pipelines: training models, feature development, regression testing
  - Experience with graph-based data workflows using Apache Airflow Bachelor’s degree in Computer Science or related field or equivalent work experience Disney Streaming Services is a place for the creative and the bold.
  - Experience deploying and running AWS-based data solutions and familiar with tools such as Cloud Formation, IAM, Athena, and Kinesis
  - Experience engineering big-data solutions using technologies like EMR, S3, Spark and an in-depth understanding of data partitioning and sharding techniques
  - Familiar with metadata management, data lineage, and principles of data governance
  - Ability to design and build and deploy streaming and batch data pipelines capable of processing and storing petabytes of data quickly and reliably
  - Ability to maintain dimensional data warehouses in support of business intelligence tools

3. Submit a PR for this assignment.
- You changed this `README.md` in part 2;

- Commit your changes.

- Submit a PR with this `README.md` changed.
(following the instructions from the synchronous session)


4. You should know a few things about Markdown, the markup language that  determines how things look when you view them on the Github web interface. That is what we see when we review your work, so you should always check to see how your `README.me` file looks before you submit. You might check out [this cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for some pointers.

Markdown is designed to look pretty much in plain text the way that you might guess it would look when made into pretty HTML.

### Here are some basics.

Use `#`, `##`, `###`, and so on to indicate headers. The header above is `###`.

```
Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

[This is a link](https://www.google.com)

```

Look like this:

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

[This is a link](https://www.google.com)

#### Formatting Code

Since much of what we'll be doing is showing code and output, it's important to know how to display that such that it is readable.

    Inline `code` has `back-ticks around` it.

Inline `code` has `back-ticks around` it.


Blocks of code can be indicated by indenting with 4 spaces or with three back-ticks (<code>```</code).


    ```sql
    SELECT this, that, the_other
    FROM my_table
    ```

```sql
SELECT this, that, the_other
FROM my_table;
```

    ```
    col1               col2               col3
    fun                dog                cat
    mouse              rat                banana
    ```

```
col1               col2               col3
fun                dog                cat
mouse              rat                banana
```
without the backticks, that sql would look like:

SELECT this, that, the_other
FROM my_table;


and that pretty table would look like this (please don't do this!!):

col1               col2               col3
fun                dog                cat
mouse              rat                banana
