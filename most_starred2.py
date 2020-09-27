import pandas as pd
import requests 
from datetime import datetime
df = pd.DataFrame(columns=[ 'name', 'URL', 'created_date', 'number_of_stars'])
results = requests.get('https://api.github.com/search/repositories?q=created:%22%3E2020-08-30%22&sort=stars&order=desc&per_page=100').json()

