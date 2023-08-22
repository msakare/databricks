import sys
import os
from github import Github

def attach_reports(token, pr_number, comment):
    g = Github(token)
    repo = g.get_repo("msakare/databricks")  # Replace with your repository info

    pull_request = repo.get_pull(pr_number)
    pull_request.create_issue_comment(comment)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python attach_reports.py <PAT_TOKEN> <comment> <pr_number>")
        sys.exit(1)

    pat_token = sys.argv[1]
    comment = sys.argv[2]
    pr_number = os.getenv("GITHUB_REF").split("/")[-1]  # Fetch the pull request number from GITHUB_REF

    attach_reports(pat_token, pr_number, comment)


# import os
# from github import Github

# def attach_reports(token):
#     g = Github(token)
#     repo = g.get_repo("msakare/databricks")
#     pr_number = 28  # Replace with the actual PR number

#     comment = """
#     **JUnit Test Report:**\n
#     [Download JUnit Report](https://github.com/msakare/databricks/actions/artifacts/28/junit)\n
#     **Security Scan Report:**\n
#     [Download Security Scan Report](https://github.com/msakare/databricks/actions/artifacts/28/security-scan)
#     """

#     pull_request = repo.get_pull(pr_number)
#     pull_request.create_issue_comment(comment)

# if __name__ == "__main__":
#     import sys

#     if len(sys.argv) != 2:
#         print("Usage: python attach_reports.py <PAT_TOKEN>")
#         sys.exit(1)

#     pat_token = sys.argv[1]
#     attach_reports(pat_token)
