import requests
import csv

'''
Function that takes a url as a parameter and the default is set to the GitHub API endpoint for Bootstrap releases.
'''
def fetch_releases(url='https://api.github.com/repos/twbs/bootstrap/releases'):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return {}

    # If the request is successful, parse the JSON data
    if response.status_code == 200:
        releases = response.json()

        if releases:
            return releases

        else:
            print("No releases found.")
    else:
        print(f"Error: {response.status_code}")
    
    return {}

'''
Function to create a csv file that takes a list of releases and a CSV file name as parameters. 
'''
def create_csv_file(releases, csv_file='bs_releases.csv'):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Created Date', 'Tag Name', 'URL'])
            
            # Write each release to CSV file
            for release in releases:
                csv_writer.writerow([release['created_at'], release['tag_name'], release['url']])

        print(f"Data has been writen to {csv_file}")

if __name__ == "__main__":
    releases = fetch_releases()
    if len(releases) > 0:
        create_csv_file(releases)