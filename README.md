# TrafficLeak

## Side Channel Attack on Encryted Web Traffic

This project aims to detect the domain to which encrypted communication takes place via network log information. 

For this purpose, we assume the communication occurs over an SSH channel and the network logs of the client are available.

## Assumptions:

1. _Closed World Assumption_: We assume only certain webpages from our list are accessed.
2. _No interleaved browsing_: Requests for one webpage finish before any other takes place.
3. _Well-demarcated request boundaries_: Start and End of requests for a webpage are known (i.e., we know which requests pertain to a particular webpage though we dont know what the webpage domain is)
4. We have removed very similar webpages (Ex: amazon.de and amazon.in) since they are possibly difficult to distinguish and because we can simply bucket them under the same provider.
5. _Webpage fingerprinting_ is done (not website) (can be extended)
6. _Caching effects_: We use hot traces for webpages rather than cold traces. Cold traces are easier to distinguish due to larger number of differing requests.
