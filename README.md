# 2-Day-Data-Real-Estate-Processing-Project

## Project
the project is similar to a real life data science task, although I would argue this project would take longer than the given time period. we were each given 2 dataset API's to extract datasets from, and merge them into a single dataset. we are required to clean the data from null values and duplicates, fix the datatypes, and choose a model that best suites the dataset

## API:
initially I used:
* https://www.rentcast.io/api
* https://www.datafiniti.co/data/property-data

but after finding out the unavailablility and unreliability of the datasets, despite doing my best cleaning them, 
I used the following instead:
* https://www.attomdata.com/solutions/property-data-api/
* Local API(generated dataset)

## Compramise
* Using my initial 2 Datasets, even after cleaning the combined dataset, I wasn't provided with the data required for my models to run at high accuracy, there are too many null values, and the data is too random and unrelated. It would have taken more than a week to fix if I did use such dataset for my assignment

* I used another dataset from a different API as a compramise to this, Although it was harder to access than my initial API datasets, It was at least provided and more complete in comparison

## Preprocessing
1. Ran the API and extracted property data in JSON format.
2. genrated dummy data
3. used fast api to extract the generated dataset
4. filtered the required columns from the unnecessary ones
5. Merged data from both APIs.
6. Cleaned the data from nulls and duplicates.
7. Changed data types when required.
8. Filled missing columns.
9. Deleted and dropped unwanted data.

## Modeling
* I chose Decision Tree, Random Forest, and XGBoost regression modeling algorithms
* Random Forest gave the best results
