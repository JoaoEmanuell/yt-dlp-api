- [Apis](#apis)
  - [Video](#video)
    - [POST](#post)
  - [Playlist](#playlist)
    - [POST](#post-1)


# Apis

**Base url to requests:**

```
<endpoint>/api
```

## Video

### POST

```
/api/videos/
```

**Body**

```
{
    "url": "www.youtube.com/watch?v=exampleUrl&si=si,
    "quality": "mp3" | "360" | "720"
}
```

**Return**

```
{
    "headers": <json_with_html_headers>,
    "title":"Title",
    "url": <url_to_download>
}
```

If *headers* or *url* is equal **null**, remake the request.

## Playlist

### POST

```
/api/playlist/
```

**Body**

```
{
    "url": "www.youtube.com/watch?v=exampleUrl&si=si"
}
```

**Return**

```
{
    [
        "www.youtube.com/watch?v=exampleUrl&si=si",
        "www.youtube.com/watch?v=exampleUrl&si=si"
        . . .
    ]
}
```