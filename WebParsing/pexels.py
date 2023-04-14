import requests
from secrets import pexels


def download(q: str, p: str):
    header = {"Authorization": pexels}

    url = f"https://api.pexels.com/v1/search?query={q}&per_page={p}"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        _r = r.json()
        print(_r)
        for item in _r.get("photos"):
            print(item.get("url"))
    else:
        print(r.text)


def main() -> None:
    q = input("Query ")
    p = input("Count page ")
    download(q, p)


if __name__ == '__main__':
    main()
