import pandas as pd

scraper = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

'''print(scraper) 
#this will give us too much information'''

'''for idx, table in enumerate(scraper):
    print("********************************")
    print(idx)
    print(table)'''

#the table we are interested at, would be Distribution in index 3
mytable_dist_index3 = scraper[3]
print(mytable_dist_index3)
