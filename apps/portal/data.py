import pandas as pd
from sodapy import Socrata


def getDataframe():
    return pd.read_csv('apps/portal/covid.csv')


def getataframe():
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
  client = Socrata("www.datos.gov.co", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
  dataset = "gt2j-8ykr"
  count = client.get(dataset,select ="COUNT(*)")
  count = count.pop()
  limite = count['COUNT']
  print('Limite: ' + str(limite))

  results = client.get(dataset, limit = limite)

# Convert to pandas DataFrame
  return pd.DataFrame.from_records(results)
