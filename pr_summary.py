import requests
import json
import datetime
import sys
from prettytable import PrettyTable

# Get the arguments repo_url, email_to and number of days to fetch the pull requests
days_to_fetch = int(sys.argv[1])
repo_url = sys.argv[2]
email_to = sys.argv[3]

# Parse repository URL to get owner and repository name
url_parts = repo_url.split('/')
owner = url_parts[-2]
repo_name = url_parts[-1]

# Get current date and previous date from which we want to get the details
current_date = datetime.datetime.utcnow()
previous_date = current_date - datetime.timedelta(days=days_to_fetch)

# Set up API request headers and parameters
api_request = f'https://api.github.com/repos/{owner}/{repo_name}/pulls?state=all'
headers = {'Accept': 'application/vnd.github+json'}

# Make API request and parse response JSON
response = requests.get(api_request, headers=headers)
pull_requests = json.loads(response.content)
summary = PrettyTable(["PR Number", "Title", "State", "Draft", "Created At", "Closed At"])
for pr in pull_requests:
    open_date = datetime.datetime.strptime(pr['created_at'].split('T')[-2], '%Y-%m-%d')
    closed_date = previous_date - datetime.timedelta(days=1)
    if (pr['closed_at']):
        closed_date = datetime.datetime.strptime(pr['closed_at'].split('T')[-2], '%Y-%m-%d')
    if open_date >= previous_date or closed_date >= previous_date:
        summary.add_row([pr['number'], pr['title'], pr['state'], pr['draft'], pr['created_at'], pr['closed_at']])

# Format email message
from_email = 'you@example.com'
to_email = email_to
subject = f'GitHub pull request summary for {owner}/{repo_name}'
body = 'Please find the GitHub pull request summary attached below:\n\n'
email = f'From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}\n{summary}'

# Print email details to console
print(email)
