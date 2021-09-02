import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    server_url = os.environ["GITHUB_SERVER_URL"]
    print(f"Hello repo: {server_url}/{repo}")


if __name__ == "__main__":
    main()
