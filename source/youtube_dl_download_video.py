from yt_dlp.YoutubeDL import YoutubeDL


class YoutubeDlDownloadVideo:
    def __init__(
        self,
        url: str,
        quality: str,
    ) -> None:
        # Manager

        # YoutubeDL

        self.__ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "nocheckcertificate": True,  # Fix android ssl bug
        }

        # Video

        self.__video = self.__format_url(url)
        self.__quality = self.__quality_to_itag(quality)

    def download(self) -> dict[str, str]:
        self.__video_infos = self.__get_video_infos()
        self.__video_form = None

        headers = self.__get_headers(self.__quality)
        url = self.__get_video_url(self.__quality)
        title = self.__safe_filename(self.__get_title())
        return {"title": title, "url": url, "headers": headers}

    def __format_url(self, url: str) -> str:
        if "short" in url:
            base_url = r"https://www.youtube.com/watch/?v="
            video_id = url.split("/")[4]
            return f"{base_url}{video_id}"
        else:
            return url

    def __quality_to_itag(self, quality: str) -> str:
        itags = {"720p": "22", "360p": "18", "mp3": "140"}
        if quality in itags:
            return itags[quality]
        return itags["360p"]  # Case don't have 720p

    def __get_video_infos(self) -> dict:
        with YoutubeDL(self.__ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.__video, download=False)
        return info_dict

    def __get_video_url(self, itag: str) -> dict:
        if self.__video_form is not None and self.__video_form["format_id"] == itag:
            return self.__video_form["url"]
        else:
            for form in self.__video_infos["formats"]:
                if form["format_id"] == itag:
                    self.__video_form = form
                    return self.__video_form["url"]

    def __get_headers(self, itag: str) -> dict:
        if self.__video_form is not None and self.__video_form["format_id"] == str(
            itag
        ):
            return self.__video_form["http_headers"]
        else:
            for form in self.__video_infos["formats"]:
                if form["format_id"] == str(itag):
                    self.__video_form = form
                    return self.__video_form["http_headers"]

    def __get_title(self) -> str:
        if self.__video_infos != None:
            return self.__video_infos["title"]
        else:
            self.__video_infos = self.__get_video_infos()
            return self.__video_infos["title"]

    def __safe_filename(self, s: str, max_length: int = 255) -> str:
        """pytube/helpers.py"""
        """Sanitize a string making it safe to use as a filename.

        This function was based off the limitations outlined here:
        https://en.wikipedia.org/wiki/Filename.

        :param str s:
            A string to make safe for use as a file name.
        :param int max_length:
            The maximum filename character length.
        :rtype: str
        :returns:
            A sanitized string.
        """
        # Characters in range 0-31 (0x00-0x1F) are not allowed in ntfs filenames.
        from re import compile, UNICODE

        ntfs_characters = [chr(i) for i in range(0, 31)]
        characters = [
            r'"',
            r"\#",
            r"\$",
            r"\%",
            r"'",
            r"\*",
            r"\,",
            r"\.",
            r"\/",
            r"\:",
            r'"',
            r"\;",
            r"\<",
            r"\>",
            r"\?",
            r"\\",
            r"\^",
            r"\|",
            r"\~",
            r"\\\\",
        ]
        pattern = "|".join(ntfs_characters + characters)
        regex = compile(pattern, UNICODE)
        filename = regex.sub("", s)
        return filename[:max_length].rsplit(" ", 0)[0]
