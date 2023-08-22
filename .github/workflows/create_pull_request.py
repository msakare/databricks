import os
from github import Github

def create_pull_request(token):
    g = Github(token)
    repo = g.get_repo("msakare/databricks")

    base = "Release"  # The base branch you want to create the pull request against
    head = "feature"  # The source branch of the pull request
    title = "Automated PR: SecurityScan"
    body = "This pull request is automatically generated to trigger security scanning."

    # Create the pull request
    pull_request = repo.create_pull(
        title=title,
        body=body,
        base=base,
        head=head,
    )

    # Add reviewers to the pull request (GitHub usernames or team names)
    reviewers = ["pankajadas", "yashuonfire"]
    pull_request.create_review_request(reviewers=reviewers)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python create_pull_request.py <PAT_TOKEN>")
        sys.exit(1)

    pat_token = sys.argv[1]
    create_pull_request(pat_token)
