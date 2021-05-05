# imf-api-service
A simple Web Service which wraps IMF Exchange Rate Web Service which downloads last 5 days exchange rates for major currencies or a given months exchange rates.

**REST URL Prefix - /api/v1**

## Exposed REST Endpoints:
* **/health** - to check the health of the service
* **/exchangeRate/lastFiveDays** - to get the latest last five days exchange rates file from IMF website
* **/exchangeRate/monthly/[yyyy-mm-dd]** - to get the given months exchange rates file from IMF website
