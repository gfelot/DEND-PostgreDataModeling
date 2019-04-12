# Song Play Analysis
## FLAT FILES INTO POSTGRE DATA MODEL FOR ANALYSIS

The purpose of this project is to build an adapted data model thanks to python to load data in a JSON file format and wrangle them into a star schema (see the ERD) for a **Postgre database**.

### Prerequisite

1. Install [Python 3.x](https://www.python.org/).

2. This project is build with **conda** instead of **pip**.
Install [anaconda](https://www.anaconda.com/distribution/) or modify the script to make use of pip.

3. You need also to have a **Postgre database** up and running. This project is configured to use the database on **localhost**. See the query string in the script to configure your instance or modify it to suit your installation.

4. To understand the concept and logic of this project you can read an run the **.ipynb** files with [Jupyter Notebook](https://jupyter.org/).

> You will not be able to run **test.ipynb**, **etl.ipynb**, or **etl.py** until you have run **create_tables.py** at least once to create the sparkifydb database, which these other files connect to.

### Main Goal
The compagny Sparkify need to analyses theirs data to better know the way users (free/paid) use theirs services. With this data model we will be able to ask question like When? Who? Where? and What? about the data.

### Data Model
![Song ERD](./Song_ERD.png)

This data model is called a **start schema** data model. At it's aim is a **Fact Table -songplays-** that containg fact on song play like user agent, location, session or user's level and then have columns of **foreign keys (FK)** of **4 dimension tables** :

* **Songs** table with data about songs
* **Artists** table
* **Users** table
* **Time** table

This model enable search with the minimum **SQL JOIN** possible and enable fast read queries.

### Run it
Few steps

1. Launch **create_tables.py** to prepare the database
2. Run **etl.py** to wrangle the data