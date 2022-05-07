# Flystats
This repository demonstrates how to collect data from the flypool API.  

This example points to the Ergo pool API.
[Full API documentation here](https://ergo.flypool.org/api/)

The example contains 2 python scripts: get_data.py and show_data.py

Running get_data regularly will collect data for your miner locally in parquet files, which can then be explored with the show_data script or any other data exploration tool.

The instructiosn below will walk through setting up the scripts to run.

## Requirements
1. Python 3
2. Git (or you can just download the zip)

## Setup Instructions
1. [Install Python 3](https://realpython.com/installing-python/)
2. Clone this repository to your local machine.  Alternatively, use Github's Download ZIP option and unpack the zip folder.
3. Open a terminal window and navigate to your project directory.
4. Run the command
        pip install -r requirements.txt
5. Open get_data.py using any editor.  Set your miner address on line 14
        miner = 'your Ergo address here'
6. That's it!  You can now run get_data.py to collect data and show_data to view an earnings over time chart.
        python get_data.py
        python show_data.py

## Run on a Schedule