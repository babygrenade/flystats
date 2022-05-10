#  flystats
#  script to collect miner and block data from flypool api
#  API documentation can be found at https://ergo.flypool.org/api/

#  import dependencies
from datetime import datetime
import pyarrow.parquet as pq
from pyarrow import Table as patb
import pandas as pd
import requests
import os

#  set configuration
#  Set your miner address here.
miner = '9iHLQWxPoQaFq2Hg5APGNT9sD8HZKPp2UUxYZSBcbmksrBsrqLq'
base_url = 'https://api-ergo.flypool.org/'
rounds_url = f'{base_url}miner/{miner}/rounds'
blocks_url = f'{base_url}blocks'
data_directory = 'data/'
rounds_directory = f'{data_directory}rounds/'
blocks_directory = f'{data_directory}blocks/'

# set datetime for filename
d1 = datetime.now().strftime("%Y-%m-%d-%H-%M")

#  function to get round data for your specific miner address
def get_rounds(miner):
    url = ''.join([base_url,'miner/',miner,'/rounds'])
    r = requests.get(url)
    return r.json()

#  function to get block detail data to be combined with miner specific data
def get_blocks():
    url = base_url + 'blocks'
    r = requests.get(url)
    return r.json()

# call get_rounds and convert json data to dataframe
rounds = pd.DataFrame(get_rounds(miner)['data'])
# call get_blocks and convert json data to dataframe
blocks = pd.DataFrame(get_blocks()['data'])

# check if directories exist and create them if not

if not os.path.exists(rounds_directory):
    os.makedirs(rounds_directory)

if not os.path.exists(blocks_directory):
    os.makedirs(blocks_directory)

# write dataframes as parquet files in repsective directories
pq.write_table(patb.from_pandas(rounds),f'{rounds_directory}{d1}.parquet')
pq.write_table(patb.from_pandas(blocks),f'{blocks_directory}{d1}.parquet')

