# calance

# Instructions:
Create a script that uses the GitHub API to pull information from the Bootstrap repo and write a file.

1. Use the GitHub API to retrieve a list of releases
2. Write the list of releases to a CSV file that includes:
    - Created Date
    - Tag Name
    - URL for the distribution zip file

# Installation & Use:
1. Fork and clone this repo from Github to your local environment
2. Navigate into your local directory and open the contents in your preferred code editor
3. Run `pipenv install` to install dependencies 
4. From the project directory, run `python script.py` to execute the script and create the CSV file.

# References:
[Bootstrap Repo](https://github.com/twbs/bootstrap) <br>
[GitHub REST API Docs](https://docs.github.com/en/rest?apiVersion=2022-11-28) <br>
[Python Requests](https://pypi.org/project/requests/) <br>
[CSV File Writing](https://docs.python.org/3/library/csv.html) <br>