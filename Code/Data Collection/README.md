# Data Collection

## Instructions

1. Place list of websites whose traces need to be generated in `final_sites`.
2. Establish SSH tunnel and ensure chrome traffic goes through the tunnel. 
3. Start a chrome browser and kill all other network using applications.
4. Run `python collect_traces.py <# of traces/website> <time/website load> <start_index>`.
5. Collected traces can be found in the `Data/` directory. 