# TrafficLeak

## Side Channel Attack on Encryted Web Traffic

This project aims to detect the domain to which encrypted communication takes place via network log information. 

For this purpose, we assume the communication occurs over an SSH channel and the network logs of the client are available.

## Assumptions:

1. __Closed World Assumption__: We assume only certain webpages from our list are accessed.
2. __No interleaved browsing__: Requests for one webpage finish before any other takes place.
3. __Well-demarcated request boundaries__: Start and End of requests for a webpage are known (i.e., we know which requests pertain to a particular webpage though we dont know what the webpage domain is)
4. We have removed very similar webpages (Ex: amazon.de and amazon.in) since they are possibly difficult to distinguish and because we can simply bucket them under the same provider.
5. __Webpage fingerprinting__ is done (not website) (can be extended)
6. __Caching effects__: We use hot traces for webpages rather than cold traces. Cold traces are easier to distinguish due to larger number of differing requests.

## Reference

Cai, Xiang, et al. "Touching from a distance: Website fingerprinting attacks and defenses." Proceedings of the 2012 ACM conference on Computer and communications security. ACM, 2012.