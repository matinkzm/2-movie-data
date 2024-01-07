# second project from this link : https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea
import csv
import pandas as pd

# create an empty data frame
movie_dataframe = pd.DataFrame(columns=['movie name', 'year', 'rating'])
# open and read the csv file
with open('imdb_top_250.csv') as file:
    # skip the first line because it is column names
    next(file)
    reader = csv.reader(file)
    index = 0
    for line in reader:
        str_line = str(line)
        # separate the data with comma
        temp_str = [s.strip() for s in str_line.split(',')]
        # add name , year , movie rating into the dataframe
        movie_dataframe.loc[index] = [temp_str[1]] + [temp_str[2]] + [temp_str[7]]
        index += 1

# movie the dataframe into a csv file
movie_dataframe.to_csv("final.csv")
