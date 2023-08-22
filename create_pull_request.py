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
    comment = f"""
    **JUnit Test Report:**

    {junit_report}

    **Security Scan Report:**

    {security_scan_report}
    """

    # Create the pull request comment
    pull_request = repo.get_pull(pr_number)
    pull_request.create_issue_comment(comment)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python create_pull_request_comment.py <PAT_TOKEN> <PR_NUMBER> <JUNIT_REPORT_PATH> <SECURITY_SCAN_REPORT_PATH>")
        sys.exit(1)

    pat_token = sys.argv[1]
    pr_number = int(sys.argv[2])
    junit_report_path = sys.argv[3]
    security_scan_report_path = sys.argv[4]

    create_pull_request_comment(pat_token, pr_number, junit_report_path, security_scan_report_path)

