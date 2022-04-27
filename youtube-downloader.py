from pytube import YouTube
import os

# files will be downloaded here
download_path = os.path.join(os.getcwd(), 'videos')

try:
    os.mkdir(download_path)
except OSError as error:
    print(f'File path {download_path} has already been created')
    
# called when file download is complete
def on_complete(stream, file_path):
    print('Download completed')

# called when file is being in process of download
# this displays a progress bar for the current file being downloaded
def on_progress(stream, chunk, bytes_remaining):
    progress = (bytes_remaining / stream.filesize) * 100
    progress_string = f'{100 - round(progress, 2)}%'
    print(progress_string)

def single_download():
    url = input("Youtube link: ")

    # create a video object, and pass in the video URL as the parameter
    video_object = YouTube(url, on_complete_callback=on_complete,
                        on_progress_callback=on_progress)

    # download options
    print('\nDownload settings: ')
    print('1 - Best | 2 - Audio ')
    download_choice = input('Download setting: ')

    if download_choice == '1':
        video_object.streams.get_highest_resolution().download(download_path)
    elif download_choice == '2':
        video_object.streams.get_audio_only().download(download_path)
    else:
        print('Invalid input')
    
# options of different downloads i.e., single video, playlist, etc
download = True

# main program loop
while(download):
    # ask user for which download option
    print('\nDownload options: ')
    print('1 - Single file | 2 - Multiple files (Playlist) | 3 - Exit')
    download_option = input("Download option: ")
    
    if download_option == '1':
        single_download()
    elif download_option == '2':
        pass
    else:
        print('Program terminating now...')
        break
     
    download_again = input('\nDownload another file? (y/n): ')
    if download_again != 'y' or download_again != 'Y':
        download = False
        print('Program terminating now...\n')