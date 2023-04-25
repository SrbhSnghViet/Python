# Python
This python script is using GitHub API to retrieve a summary of all opened, closed, and in draft pull requests in the last week for a given repository and send a summary email to a configurable email address. Script pr_summary.py accepts three arguments:

1. Number of days to fetch pull requests.
2. Repository URL and
3. Email Id where you need to send the report.

For example:
```
python pr_summary.py 7 https://github.com/SrbhSnghViet/Demo srbhkmrsngh@gmail.com
```
### Note:
This script will print the email content on the console as SMTP details are required to send the email.
