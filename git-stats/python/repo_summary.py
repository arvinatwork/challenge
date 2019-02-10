import requests
import argparse

def repo_summary(repo_lists):
    print(repo_lists)


    for repo in repo_lists:
        url = "https://api.github.com/repos/" + repo

        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers)

        # TODO add apierror handling
        # if response.status_code != 200:
            # This means something went wrong.
            # raise ApiError('GET /repos {}'.format(resp.status_code))
        # print(response.json())

        resp_json = response.json()

        # TODO Create Print Object
        print("Name: " + resp_json['name'])
        print("Clone URL: " + resp_json['clone_url'])
        print("SSH URL: " + resp_json['ssh_url'])

        # TODO extract 
        commits_url = url + "/commits"
        commits_resp = requests.get(commits_url, headers=headers)
        commits_resp_json = commits_resp.json()
 
        print("Date: " + commits_resp_json[0]['commit']['author']['date'])
        print("Latest commit: " + commits_resp_json[0]['commit']['message'])
        print("SHA: " + commits_resp_json[0]['sha'])
        print("Author: " + commits_resp_json[0]['commit']['author']['name'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get some git repo summaries.')
    parser.add_argument('repositories', type=str, nargs='+',
                        help='repositories with format $org/$name, e.g. facebook/react')

    args = parser.parse_args()

    repo_summary(args.repositories)