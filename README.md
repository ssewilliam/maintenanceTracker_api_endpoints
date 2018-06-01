## MaintenanceTracker_API_endpoints
[![BuildStatus](https://travis-ci.org/ssewilliam/maintenanceTracker_api_endpoints.svg?branch=api)]
(https://travis-ci.org/travis-ci/travis-web)

## DESCRIPTION
Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

## LINK TO Maintance Tracker Github Pages
### [MaintenanceTracker](https://ssewilliam.github.io/maintenancetracker

## Project API endpoint routes
| REQUEST | ROUTE | ACTION / FUNCTIONALITY |
| ------- | ----- | ---------------------- |
|   GET   | api_v_1_/users/requests | Get all the requests for a logged in user |
|   GET   | api_v_1/users/requests | Get a request for a logged in user |
|   POST  | api_v_1/users/requests | Create a request |
|   PUT   | api_v_1/users/requests | Modify a request |

## BUILT WITH 

*  Flask a Python Framework

## SETTING UP APPLICATION

1. Clone this repository to your computer using 

  **```$ git clone https://github.com/ssewilliam/maintenanceTracker_api_endpoints.git```**

2. Install virtualenv, create and activate anew enviromment inside this folder you've cloned
  **```$ virtualenv maintanance-tracker-env```**
  **```$ source maintanance-tracker-env```**

3. Install all project dependencies using

    **```pip3 install -r requirements.txt```**

## RUNNING APPLICATION

*  To launch the application, run the following command in your terminal

    **```python run.py```**

* To run tests on the application, run the following command in your terminal

    **```python test_requests.py```**

## Author

SSERUBIRI WILLIAM
  
