# Deployment Data Collection

## Instructions:

1. Empty the `Test_Data` directory.
2. Place list of websites to be tested in test_sites.
3. Establish SSH tunnel and ensure all traffic on chrome is tunneled via SSH.
4. Close all other applications using the network.
5. Run `python collect_traces.py <time_per_page> <i>` (i is start index in list, run once with each index).
6. All collected traces can be found in `Test_Data`.