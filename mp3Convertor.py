try:
    from pytube import YouTube
    import os

    # url
    yt = (input("Please enter the URL of the Youtube Video for MP3 Conversion: "))
    # mp3 extraction
    video = yt.streams.filter(only_audio=True).first
    print('Enter the audio destination or leave blank for current directory')
    destination = str(input('>')) or '.'
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # results
    print(yt.title, 'has successfully downloaded in .mp3 format')
except AttributeError:
    print('Error converting the link')


