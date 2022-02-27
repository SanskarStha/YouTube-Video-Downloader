import pytube

print("Enter video url:")
link = input()

yt = pytube.YouTube(link)
all_streams = yt.fmt_streams

val = input("1.Audio\n2.Video\n")
if val == '1' or val == '2':
    down_index = 0
    for s in all_streams:
        if val == '2':
            if s.type == "video":
                print(s.resolution + " " + s.subtype)
        elif val == '1':
            if s.type == "audio":
                print(s.type)
            else:
                down_index += 1
    choice = 0
    if val == '2':
        choice = int(input("Enter the appropriate resolution and type:"))
    else:
        choice = int(input("Enter the appropriate type:"))
        choice = choice + down_index

    choice -= 1
    output_path = input("Enter the output location:")
    all_streams[choice].download(output_path)














