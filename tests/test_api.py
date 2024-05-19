from requests import post


def test_api():
    url = "http://localhost:8080/api/video/"
    # Video
    data = {"url": "https://youtu.be/PTqchVeZbx8", "quality": "720p"}
    request = post(url, data)
    json = request.json()
    assert "headers" in json
    assert "url" in json
    assert json["title"] == "Qual é o Mob Mais Forte do Minecraft"
    # Audio
    data = {"url": "https://youtu.be/PTqchVeZbx8", "quality": "mp3"}
    request = post(url, data)
    json = request.json()
    assert "headers" in json
    assert "url" in json
    assert json["title"] == "Qual é o Mob Mais Forte do Minecraft"
    # Playlist
    url = "http://localhost:8080/api/playlist/"
    data = {
        "url": "https://youtube.com/playlist?list=PLRrn6roahEJNwqqpGE_uupQ08yAz9JSAW",
    }
    request = post(url, data)
    json = request.json()
    assert type(json) == list
    video = json[0]
    url = "http://localhost:8080/api/video/"
    ## Video
    data = {"url": video, "quality": "720p"}
    request = post(url, data)
    json = request.json()
    assert "headers" in json
    assert "url" in json
