import requests
import csv

def fetch_releases(url):
    response = requests.get(url)

    if response.status_code == 200:
        releases = response.json()

        if releases:
            csv_file = 'bs_releases.csv'

            create_csv_file(csv_file, releases)

            print(f"Data has been writen to {csv_file}")
        else:
            print("No releases found.")
    else:
        print(f"Error: {response.status_code}")

def create_csv_file(csv_file, releases):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Created Date', 'Tag Name', 'URL'])

            for release in releases:
                created_date = release['created_at']
                tag_name = release['tag_name']
                url = release['url']

                csv_writer.writerow([created_date, tag_name, url])

def main():
    url = 'https://api.github.com/repos/twbs/bootstrap/releases'

    fetch_releases(url)

if __name__ == "__main__":
    main()