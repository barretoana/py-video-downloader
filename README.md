# Video Downloader 

Download and save videos from a JSON with Python's urllib.request. 

## Details
Each data point in the JSON represents a bundle of videos, with name and other caracteristics. 

### JSON Format
```
    { 
        "name": "",
        "src": "",
        "owner": "",
        "details": "", 
        "items": [title, video_url]
    }
```
