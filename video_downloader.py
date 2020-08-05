def create_new_folder(name):
    '''
    Create folder in current directory
    @params
        name    - Required: Name of Folder (Str)
    '''
    try:
        os.mkdir(name)
    except FileExistsError: 
        print("Ops, looks like you've done that already!")
    except: 
        print("Hum... something went wrong with the folder.")
    else: 
        print('Yay! Folder Created Succesfully.')

    return name

def create_txt_details(info, dir): 
    '''
    Create .txt file with information
    @params 
        info      - Required: The information to be saved (Any)
        dir       - Required: Directory address (Str)
    '''

    with open('{}/info.txt'.format(dir), 'w') as details: 
        details.write(json.dumps(info, sort_keys=True, indent=4))

def download_video(dir, name, url):
    ''' 
    Download video file from external source
    @params
        dir       - Required: output directory address (Str)
        name      - Required: output filename (Str)
        url       - Required: url to request video, must be the direct address of the file (Str)
        res       - Optional: video resolution, can be 360, 480, 720(default) or 1080 when available (Int)
    '''

    print ("Fetching file: {}/{}".format(dir, name)) 
    try:
        urllib.request.urlretrieve(url, '{}/{}.mp4'.format(dir, name), reporthook=download_progress)
    except: 
        print('\n ! Vish, unable to download file: {}'.format(url))
    else: 
        print (" ***** Iha, Video Downloaded Succesfully.")
    time.sleep(0.1)


def download_progress(block_num, block_size, total_size):
    '''
    Show download progress percentage
    @params 
        block_num   - Required: Current Download Block Number (Int)
        block_size  - Required: Current Download Block Size (Int)
        total_size  - Required: File total size (Int)
    '''

    downloaded = block_num * block_size
    progress = int((downloaded/total_size)*100)
    print ("\r \tDownload Progress",str(progress),"%", end='')


import urllib.request
import json, os, re, time
 
with open('test_links.json') as f:
    data = json.load(f) 

for item in data: 
    folder_name = create_new_folder(item['owner'] + ' - ' + item['name'])
    create_txt_details(item, folder_name)
    
    for each in item['videos']: 
        try: 
            download_video(folder_name, each[0], each[-1])
        except: 
            print('Check your JSON format, something might be wrong.')
    
