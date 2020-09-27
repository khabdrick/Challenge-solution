import pandas as pd
import requests 
from datetime import datetime
df = pd.DataFrame(columns=[ 'name', 'URL', 'created_date', 'number_of_stars'])
results = requests.get('https://api.github.com/search/repositories?q=created:%22%3E2020-08-30%22& \
sort=stars&order=desc&per_page=100').json()

for repo in results['items'][0:100]:
        d_tmp = {
                'name': repo['name'],
                'URL': repo['html_url'],
                'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),


                'number_of_stars': repo['stargazers_count']}
       


        print (d_tmp)