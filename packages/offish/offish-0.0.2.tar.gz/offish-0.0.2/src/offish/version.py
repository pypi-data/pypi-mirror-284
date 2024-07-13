import requests


def get_version(user: str, repository: str, path: str, branch: str = "master") -> str:
    url = "https://raw.githubusercontent.com/{}/{}/{}/{}/__init__.py".format(
        user, repository, branch, path
    )

    r = requests.get(url)
    data = r.text

    version_index = data.index("__version__")
    start_quotation_mark = data.index('"', version_index) + 1
    end_quotation_mark = data.index('"', start_quotation_mark)

    return data[start_quotation_mark:end_quotation_mark]
