# imf-api-service
A simple Web Service which wraps IMF Exchange Rate Web endpoint to download:
* Last 5 days exchange rates for major currencies
* Get exchange rates for all the published dates in a given month

**REST URL Prefix - /api/v1/exchangeRate**

## Exposed REST Endpoints:
* **/health** - to check the health of the service
* **/lastFiveDays** - to get the latest last five days exchange rates in a file
* **/monthly/[yyyy-mm-dd]** - to get the given month's exchange rates for all the published date in a file
