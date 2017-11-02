# TrafficLeak

## Side Channel Attack on Encryted Web Traffic

This project aims to detect the domain to which encrypted communication takes place via network log information. 

For this purpose, we assume the communication occurs over an SSH channel and the network logs of the client are available.

## Assumptions:

1. Closed World Assumption: We assume only certain webpages from our list are accessed.
2. No interleaved browsing. Requests for one webpage finish before any other takes place.
3. Start and End of requests for a webpage are known (i.e., we know which requests pertain to a particular webpage though we dont know what the webpage domain is)
4. For dataset, we have removed very similar webpages (Ex: amazon.de and amazon.in) since they are possibly difficult to distinguish and because we can simply bucket them under the same provider.
5. Webpage fingerprinting is done (not website) (can be extended)
6. Caching (hot and cold pages) effect
7. Interference in data collection?

