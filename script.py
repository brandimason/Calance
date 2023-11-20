import requests
import csv

url = 'https://api.github.com/repos/twbs/bootstrap/releases'

response = requests.get(url)

# if response.status_code == 200:
#     releases = response.json()

#     if releases:  # Check if the list is not empty
#         csv_file = 'bs_releases.csv'

#         with open(csv_file, 'w', newline='') as file:
#             csv_writer = csv.writer(file)
#             csv_writer.writerow(['Created Date', 'Tag Name', 'URL'])

#             for release in releases:
#                 created_date = release['created_at']
#                 tag_name = release['tag_name']
#                 url = release['url']

#                 csv_writer.writerow([created_date, tag_name, url])
#             print(f"Data has been writen to {csv_file}")

#     else:
#         print("No releases found.")
# else:
#     print(f"Error: {response.status_code}")


releases = response.json()

csv_file = 'bs_releases.csv'

with open(csv_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Created Date', 'Tag Name', 'URL'])

    for release in releases:
        created_date = release['created_at']
        tag_name = release['tag_name']
        url = release['url']

        csv_writer.writerow([created_date, tag_name, url])
    print(f"Data has been writen to {csv_file}")