import requests
import time
from bs4 import BeautifulSoup
import os


def main():
    failed_file = []
    print("Paste in the download path.")
    path_parent = str(input())
    URL = "http://www.ghibli.jp/works/"
    res_parent = requests.get(URL)
    soup_parent = BeautifulSoup(res_parent.text, "html.parser")
    links_parent = [
        h1_obj.get("href") for h1_obj in soup_parent.select("h1.post-header a")
    ]
    for link in links_parent:
        split_link = link.split("/")
        save_path = os.path.join(path_parent, split_link[-2])
        links = scrape_links(link)
        print(links)
        if len(links) > 0:
            if os.path.isdir(path_parent) and not os.path.isdir(save_path):
                os.mkdir(save_path)
                time.sleep(2.0)
                dl_img_files(links, save_path, failed_file, split_link)

    if len(failed_file) > 0:
        output_dl_failed_file(path_parent, failed_file)


def output_dl_failed_file(path: str, failed_file: str):
    with open(os.path.join(path, "failed_file.log"), "w") as f:
        for i in failed_file:
            f.write("".join([i, "\n"]))


def scrape_links(link: str) -> list:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    links = [url.get("href") for url in soup.select("a.panelarea")]
    # print(links)
    return links


def dl_img_files(links: list, save_path: str, failed_file: list, split_link: list):
    for img_url in links:
        time.sleep(5.0)
        file_name = os.path.basename(img_url)
        dst_path = os.path.join(save_path, file_name)
        try:
            image = requests.get(img_url)
            open(dst_path, "wb").write(image.content)
            print("Downloaded", dst_path)
        except ValueError:
            print("ValueError", img_url)
            valerr_str = img_url.split("/")
            failed_file.append("".join(["ValueError : ", valerr_str[-1]]))
        except ConnectionResetError:
            print("ConnectionResetError", img_url)
            reset_str = img_url.split("/")
            failed_file.append("".join([split_link[-2], " : ", reset_str[-1]]))


if __name__ == "__main__":
    main()
