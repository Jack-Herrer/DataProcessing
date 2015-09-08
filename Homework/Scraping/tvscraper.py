#!/usr/bin/env python
# Name: Michiel van der List
# Student number: 10363521
'''
This script scrapes IMDB and outputs a CSV file with highest ranking tv series.
'''
# IF YOU WANT TO TEST YOUR ATTEMPT, RUN THE test-tvscraper.py SCRIPT.
import csv

from pattern.web import URL, DOM

TARGET_URL = "http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating,desc&start=1&title_type=tv_series"
BACKUP_HTML = 'tvseries.html'
OUTPUT_CSV = 'tvseries.csv'


def extract_tvseries(dom):
    '''
    Extract a list of highest ranking TV series from DOM (of IMDB page).

    Each TV series entry should contain the following fields:
    - TV Title
    - Ranking
    - Genres (comma separated if more than one)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    '''

    # Get html data from local file and convert to text
    def get_dom(start_val):    
        html_data = requests.get(BACKUP_HTML).text
        dom=web.Element(html_data)
        return dom

    #
    def parse_dom(dom):
        result=[]
        for tv_series in dom.by_tag('td.title'):    
            title = tv_series.by_tag('a')[0].content
            genres = tv_series.by_tag('span.genre')[0].by_tag('a')
            genres = "|".join([g.content for g in genres])
            try:
                runtime = tv_series.by_tag('span.runtime')[0].content
            except:
                runtime = "NA"
            rating = tv_series.by_tag('span.value')[0].content
            artists = tv_series.by_tag('span.credit')[0].by_tag('a')
            artists = "|".join([a.content for a in artists])
            temp_res=[]
            temp_res.extend([title, genres, runtime, rating, artists])
            result.append(temp_res)
        return result
    

    # ADD YOUR CODE HERE TO EXTRACT THE ABOVE INFORMATION ABOUT THE
    # HIGHEST RANKING TV-SERIES
    # NOTE: FOR THIS EXERCISE YOU ARE ALLOWED (BUT NOT REQUIRED) TO IGNORE
    # UNICODE CHARACTERS AND SIMPLY LEAVE THEM OUT OF THE OUTPUT.

    return []  # replace this line as well as appropriate


def save_csv(f, tvseries):
    '''
    Output a CSV file containing highest ranking TV-series.
    '''
    for row in tvseries:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Ranking', 'Genre', 'Actors', 'Runtime'])
    # ADD SOME CODE OF YOURSELF HERE TO WRITE THE TV-SERIES TO DISK

if __name__ == '__main__':
    # Download the HTML file
    url = URL(TARGET_URL)
    html = url.download()

    # Save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in testing / grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # Parse the HTML file into a DOM representation
    dom = DOM(html)

    # Extract the tv series (using the function you implemented)
    tvseries = extract_tvseries(dom)

    # Write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'wb') as output_file:
        save_csv(output_file, tvseries)
