# Datasets

Traffic logs collected using tshark. All traffic was over a SSH channel. 

## Collection Strategy:

1. _No interleaved browsing_: Requests for one webpage finish before any other takes place.
2. _Well-demarcated request boundaries_: Start and End of requests for a webpage are known (i.e., we know which requests pertain to a particular webpage though we dont know what the webpage domain is)
3. We have removed very similar webpages (Ex: amazon.de and amazon.in) since they are possibly difficult to distinguish and because we can simply bucket them under the same provider.
4. _Caching Effects_: For each domain, '0.trace' is the cold trace and the remaining are hot traces.
