# API Services

## IMF Endpoints
A simple Web Service which wraps IMF Exchange Rate Web Service which downloads last 5 days exchange rates for major currencies or a given months exchange rates.

**REST URL Prefix - /api/v1/exchangeRate**

### Exposed REST Endpoints:
* GET **/lastFiveDays** - to get the latest last five days exchange rates file from IMF website
* GET **/monthly/[yyyy-mm-dd]** - to get the given months exchange rates file from IMF website

## Task Endpoints
A simple Web Service which keeps track of todo tasks.

**REST URL Prefix - /api/v1/task**

### Exposed REST Endpoints:
* GET **/todo** - to get all the todo tasks
* POST **/todo** - create a todo task where task details are passed in body, Sample body: `{"task":"task name", "is_pending": "Yes"}`
* GET **/todo/<tsk_id>** - to get one todo task
* DELETE **/todo/<tsk_id>** - delete a todo task

## Health Check Endpoint
* GET **/health** - to check the health of the service