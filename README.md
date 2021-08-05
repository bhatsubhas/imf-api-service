# API Services

## imf-api-service
A simple Web Service which wraps IMF Exchange Rate Web Service which downloads last 5 days exchange rates for major currencies or a given months exchange rates.

**REST URL Prefix - /api/v1/exchangeRate**

### Exposed REST Endpoints:
* **/health** - to check the health of the service
* **/lastFiveDays** - to get the latest last five days exchange rates file from IMF website
* **/monthly/[yyyy-mm-dd]** - to get the given months exchange rates file from IMF website

## task-api-service
A simple Web Service which keeps track of todo tasks.

**REST URL Prefix - /api/v1/task**

### Exposed REST Endpoints:
* **/health** - to check the health of the service
* **/todo** - to get all the todo tasks and create a todo task
* **/todo/<tsk_id>** - to get one todo task and delete a todo task