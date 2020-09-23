from bs4 import BeautifulSoup
import os
import requests
import sys
import time


def main():
    failed_file = []
    path_parent = ""
    while not os.path.isdir(path_parent):
        print("Type or paste the download path below.")
        path_parent = str(input())
        if not os.path.isdir(path_parent):
            print("The path you specified does not exist.")

    links_parent = search_works_url()

    for link in links_parent:
        save_path = os.path.join(path_parent, list(link.split("/"))[-2])
        links = scrape_links(link)
        # print(links)
        if len(links) > 0:
            if os.path.isdir(path_parent) and not os.path.isdir(save_path):
                os.mkdir(save_path)
                time.sleep(2.0)
                dl_img_files(links, save_path, failed_file)

    if len(failed_file) > 0:
        output_dl_failed_file(path_parent, path_parent, failed_file)
    sys.exit(0)


def output_dl_failed_file(path: str, path_parent: str, failed_file: str):
    with open(os.path.join(path, "failed_file.log"), "w") as f:
        for i in failed_file:
            f.write("".join([i, "\n"]))
        print("\nSome of the image(s) failed to download.")
        print("If you want to check this, see", path_parent, "\\failed_file.log\n")
        input("Press Enter(Return) to exit.")


def search_works_url() -> list:
    print("Preparing for download...")
    URL = "http://www.ghibli.jp/works/"
    res_parent = requests.get(URL)
    soup_parent = BeautifulSoup(res_parent.text, "html.parser")
    return [h1_obj.get("href") for h1_obj in soup_parent.select("h1.post-header a")]


def scrape_links(link: str) -> list:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    links = [url.get("href") for url in soup.select("a.panelarea")]
    # print(links)
    return links


def dl_img_files(links: list, save_path: str, failed_file: list):
    print("Downloading now...")
    for img_url in links:
        time.sleep(5.0)
        file_name = list(img_url.split("/"))[-1]
        dst_path = os.path.join(save_path, file_name)
        msg = ""
        try:
            image = requests.get(img_url)
            open(dst_path, "wb").write(image.content)
            msg = "Downloaded " + file_name + " to " + save_path
        except ValueError:
            msg = "Failed to download " + file_name + " : reason->ValueError"
            failed_file.append("".join["ValueError : ", file_name])
        except ConnectionResetError:
            msg = "Failed to download " + file_name + " : reason->ConnectionResetError"
            failed_file.append("".join["ConnectionResetError : ", file_name])
        print(msg)


if __name__ == "__main__":
    main()
