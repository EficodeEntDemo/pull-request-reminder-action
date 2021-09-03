import os
import json
from requests import get, post  # noqa We are just importing this to prove the dependency installed correctly
import logging as log
from datetime import datetime
from datetime import timezone

log.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log.root.setLevel(log.DEBUG)


def utc_now():
    return datetime.now(timezone.utc)


def get_next_page_url(link_header):
    if link_header:
        log.debug("Parsing header {}".format(link_header))
        links = link_header.split(",")
        for link in links:
            parts = link.split(";")
            if len(parts) >= 2 and parts[1].strip() == "rel=\"next\"":
                return parts[0].strip().strip("<").strip(">")
    return None


def get_pull_request_page(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = get(url, headers=headers, verify=True)
    if response.status_code == 200:
        link_header = response.headers.get("Link", None)
        next_url = get_next_page_url(link_header)
        return next_url, json.loads(response.text)
    else:
        log.debug(f"{response.__dict__}")


def send_pull_request_notification(server_url, owner, repo, pull_request, github_token):
    url = f"{server_url}/repos/{owner}/{repo}/issues/{pull_request['number']}/comments"
    headers = {"Authorization": f"Bearer {github_token}"}
    response = post(url, headers=headers, verify=True, json={
        'owner': owner,
        'repo': repo,
        'issue_number': pull_request['id'],
        'body': 'Please do something about this, nothing is going on @EficodeEntDemo/root-rnd-enterprise'
    })
    if response.status_code != 201:
        log.debug(f"{response.__dict__}")


# Return True if it is ok, False if in need of notification
def check_the_pull_request(pull_request):
    title = pull_request.get('title', None)
    created_at = pull_request.get('created_at', None)
    updated_at = pull_request.get('updated_at', None)

    log.debug(f"Created {created_at}")
    log.debug(f"Updated {updated_at}")
    return False # Always in need of notification

def main():
    github_token = os.environ["INPUT_GITHUB_TOKEN"]
    server_url = os.environ["GITHUB_API_URL"]
    owner = os.environ["GITHUB_REPOSITORY_OWNER"]
    repo = os.environ["GITHUB_REPOSITORY"]

    log.debug(f"Hello repo: {server_url}/{repo}")
    log.debug("Hello repo: %s", github_token[0:4])

    pull_requests_url = f"{server_url}/repos/{owner}/{repo}/pulls?state=open&per_page=100"

    count_of_pages = 0
    while pull_requests_url:
        count_of_pages += 1
        result = get_pull_request_page(pull_requests_url, github_token)
        log.debug(f"Complete result: {result}")
        pull_requests_url = result[0]
        pull_request_count = 0
        for pull_request in result[1]:
            if not check_the_pull_request(pull_request):
                send_pull_request_notification(server_url, owner, repo, pull_request, github_token)
            pull_request_count += 1
            log.debug(f"Pull requests {pull_request_count}: {pull_request}")

        log.debug(f"We got {pull_request_count} pull requests")
        log.debug(f"We got {count_of_pages} pages")


if __name__ == "__main__":
    os.environ["INPUT_GITHUB_TOKEN"] = "your-token-here"
    os.environ["GITHUB_API_URL"] = "https://api.github.com"
    os.environ["GITHUB_REPOSITORY_OWNER"] = "EficodeEntDemo"
    os.environ["GITHUB_REPOSITORY"] = "pluto-the-beginning"

    main()

