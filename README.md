# Hi!

This repository consists REST API testing framework that I made via 'PyTest' & 'Requests' libraries. Here you can find a instruction how to execute my code:

1. Download repository.
2. Download all required packages (from the setup.py file)
3. To run tests you need to use console command: pytest tests/test_options.py (make sure you are in the repository REST_API_automation )

Note:
- in the config file you can change the base you test
- in the data.json file you can find the whole list of users that you can use for tests
- in the helpers.py file you can find references to:
  - all libs that used for run tests
  - class HttpRequests that include methods get,post,delete,put,patch. All tests using these methods via instance 'http_methods'
  - generate_random function that using for patch/put tests to generate new values
  - context managers that help to read json files config.json and data.json
