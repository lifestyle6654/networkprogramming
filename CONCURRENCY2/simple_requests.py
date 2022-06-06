# 2개의 사이트를 번갈아 가면서 총 160번의 웹 페이지 요청/응답 수신
# 1개의 요청/응답 수신 후, 다음 요청/응답 수신을 수행함

import requests
import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr",
        "https://www.google.co.kr",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")