import os
import requests
from github import Github

# GitHub access token
access_token = os.environ.get('GITHUB_TOKEN')

# Repository information
repo_owner = 'msakare'
repo_name = 'databricks'
pr_number = 11  # Replace with the actual PR number

# Read JUnit and security scan reports
junit_report = open('junit/test-report.xml', 'r').read()
security_scan_report = open('junit/security-scan-report.xml', 'r').read()

# Comment body
comment = updatedreport
**JUnit Test Report:**

