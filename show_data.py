from datetime import datetime
import pytz
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
import pyarrow as pa
import plotly.express as px


data_directory = 'data/'

#  Read parquet directories, convert to dataframes, drop duplicates
blocks = pq.read_table(f'{data_directory}blocks/').to_pandas()
blocks.drop_duplicates(inplace=True)
rounds = pq.read_table(f'{data_directory}rounds/').to_pandas()
rounds.drop_duplicates(inplace=True)

#  join blocks and miner rounds data
df = pd.merge(blocks,rounds,how="left", left_on="number",right_on="block")

#  convert amount from nano Erg to Erg
df['amount'] = df['amount'] / pow(10,9)

#  set up timezones
df['time'] = df['time'].astype(int)
est = pytz.timezone('US/Eastern')

# at timestamp to dataframe
df['timestamp'] = df['time'].astype(int).apply(lambda x: datetime.utcfromtimestamp(x).astimezone(est))
df['date'] = df['time'].astype(int).apply(lambda x: datetime.utcfromtimestamp(x).astimezone(est).date())

df2 = df[['block','timestamp','date','amount']].nunique()

# Aggregate to show amount earned per day
df2 = df.groupby('date').agg(
    date = pd.NamedAgg(column='date',aggfunc='min'),
    income=pd.NamedAgg(column='amount',aggfunc='sum')
)

# create and show chart
fig = px.bar(df2,x="date",y="income",title="Income over time")
fig.show()