from os.path import exists, join
from os import system, mkdir, remove
from pathlib import Path
from io import BytesIO
from urllib.request import Request, urlopen


def download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(request) as response:
        file: bytes = b""
        length = response.getheader("content-Length")
        block_size = 1000000  # 1MB Default

        if length:
            length = int(length)
            block_size = max(4096, length // 20)

        buffer_all = BytesIO()
        size = 0

        print("Start Download!")

        while True:
            buffer_now = response.read(block_size)
            file += buffer_now

            if not buffer_now:
                break

            buffer_all.write(buffer_now)
            size += len(buffer_now)

            if length:
                percent = int((size / length) * 100)
                print(f"{percent}%", end=" ")
    print()
    return file


def save_file(file: bytes, save_path: str, name: str) -> None:
    if not exists(save_path):
        mkdir(save_path)

    with open(join(save_path, name), "wb") as f:
        f.write(file)


def extract_module(path_to_file: str) -> None:
    # Install dependencies
    print("Start extract module!")

    print("Start extract file")

    system(f"7z x {path_to_file}")

    print("Finished extract")

    # Delete 7z

    remove(path_to_file)


def get_url_to_downloader_dmyrn(repository: str) -> str:
    # Get url to downloader dmyrn 7z
    from json import loads

    file = download(
        f"https://api.github.com/repos/JoaoEmanuell/{repository}/releases/latest"
    )
    dictionary = loads(file)
    return dictionary["assets"][0]["browser_download_url"]  # Download link to 7z


if __name__ == "__main__":
    absolute_path = join(Path().absolute(), "")
    tmp_path = join(absolute_path, "tmp")
    path_to_download = join(absolute_path)

    # yt-dlp dmyrn

    youtube_dl_7z_name = r"yt_dlp.7z"
    url_youtube_dl = get_url_to_downloader_dmyrn("yt-dlp-dmyrn")
    file_youtube_dl = download(url_youtube_dl)
    save_file(
        file=file_youtube_dl,
        save_path=tmp_path,
        name=youtube_dl_7z_name,
    )
    extract_module(path_to_file=join(tmp_path, youtube_dl_7z_name))
