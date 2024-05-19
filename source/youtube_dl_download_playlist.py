from yt_dlp.YoutubeDL import YoutubeDL

class YoutubeDLDownloadPlaylist:
    def __init__(self, url: str) -> None:
        self.__url = url

    def download_playlist(self) -> list[dict[str, str]]:
        playlist_videos = self.__get_playlist_urls()
        return playlist_videos

    def __get_playlist_urls(self) -> list[str]:
        ydl_opts = {"quiet": True, "no_warnings": True, "extract_flat": "in_playlist"}
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.__url, download=False)
            playlist_urls = [
                f"https://youtube.com/watch/?v={entry['id']}"
                for entry in info_dict["entries"]
            ]

        return playlist_urls
