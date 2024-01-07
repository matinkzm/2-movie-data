import csv
import pandas as pd

movie_dataframe = pd.DataFrame(columns=['movie name', 'year', 'rating'])

with open('imdb_top_250.csv') as file:
    next(file)
    reader = csv.reader(file)
    index = 0
    for line in reader:
        str_line = str(line)
        temp_str = [s.strip() for s in str_line.split(',')]
        movie_dataframe.loc[index] = [temp_str[1]] + [temp_str[2]] + [temp_str[7]]
        index += 1


movie_dataframe.to_csv("final.csv")
