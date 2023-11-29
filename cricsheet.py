from cricsummary import Duranz


 match = Duranz('12345.json')

 match.scorecard(team=1) 

 match.plot_worm() 

 match.plot_manhattan(team=2)

 match.match_info()

match.extras(team=1)
match.fall_of_wickets(team=2)
df_dict = match.teams_df
from cricsummary import json_to_csv
json_to_csv('123.json', output_file=True)
import pandas as pd 
empdata = pd.read_csv('C:\\Users\\XXXXX\\empdata.csv', index_col=False, delimiter = ',') 
empdata.head()
import mysql.connector as msql 
from mysql.connector import Error 
try: 
  conn = msql.connect(host='localhost', user='root', password='root@123')
  cursor = conn.cursor() 
  cursor.execute("CREATE DATABASE cric")
except Error as e: 
  print("Error while connecting to MySQL", e)

csv_data = csv.reader(file('students.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO testcsv(column1, \
          column2, column3 )' \
          'VALUES("%s", "%s", "%s")', 
          row)
cursor.close()
print "Done"
