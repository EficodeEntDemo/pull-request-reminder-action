import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    server_url = os.environ["GITHUB_SERVER_URL"]
    print(f"Hello repo: {server_url}/{repo}")

    pull_requests_url = "{server_url}/{repo}/pulls?state=open&per_page=100".format(
                server_url=server_url,
                repo=repo
            )

    while pull_requests_url:
        result = get_pull_request_page(pull_requests_url, self.github_cfg)
        pull_requests_url = result[0]
        for pull_request in result[1]:
            print(f"Pull request: {pull_request}")

if __name__ == "__main__":
    main()
