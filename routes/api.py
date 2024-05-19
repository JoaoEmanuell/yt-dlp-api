from flask import request, jsonify, Blueprint

from source import YoutubeDlDownloadVideo, YoutubeDLDownloadPlaylist

api = Blueprint("api", __name__, template_folder="api")


@api.route("/video/", methods=["POST"])
def video():
    data = request.get_json()
    url = str(data["url"]).strip()
    quality = str(data["quality"]).strip()
    youtube_dl = YoutubeDlDownloadVideo(url, quality)
    video = youtube_dl.download()
    return jsonify(video)


@api.route("/playlist/", methods=["POST"])
def playlist():
    data = request.get_json()
    url = str(data["url"]).strip()
    youtube_dl = YoutubeDLDownloadPlaylist(url)
    playlist = youtube_dl.download_playlist()
    return jsonify(playlist)
