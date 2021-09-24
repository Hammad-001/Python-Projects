from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

# creating interface of App
root = Tk()
root.geometry("500x600")  # setting width and height of root window
root.title("YT Video Downloader")  # giving title to window
root.resizable(False, False)  # setting resizable to false for both x and y
root.configure(bg="black")  # setting background color to black

# making folder icon global as we need it in our different functions
folder = ""


# for getting file location on selecting path
def file_location():
    """ This function runs on clicking button choose path
    this function is made to get folder in which we wanna
    save our downloaded files.
    """

    # informing user to stay patient as download takes time
    download_wait_label.config(text="Just be Calm and wait if system shows not responding during download!")
    download_name_label.config(text="")  # setting Name of file label Empty
    download_size_label.config(text="")  # setting size label empty
    download_path_label.config(text="")  # setting storage path label empty

    # accessing global variable folder for change in path
    global folder

    folder = filedialog.askdirectory()  # asking the selected directory
    path_add_label.config(text=folder)  # setting the selected folder in the label


# this method runs on clicking on download button
def download_video():
    """ It runs when download button is pressed,
    It finds video on youtube, and download its
    corresponding resolution video/audio.
    """

    # getting link and quality from link entry and choices box
    url = link_enter.get()
    quality = choices_box.get()

    # checking either if user has entered the folder path or not
    if len(folder) < 1:
        path_add_label.config(text="Please select path where to download!")

    # checking whether the link is provided or not
    if len(url) > 1:
        link_error_label.config(text="Please Enter a URL of Youtube Video.")

        try:
            # creating selected corresponding youtube video's object
            yt = YouTube(url)

            # checking video quality
            if quality == choices[0]:  # for high resolution
                video = yt.streams.get_highest_resolution()

            elif quality == choices[1]:  # for low resolution
                video = yt.streams.filter(progressive=True, file_extension="mp4").first()

            elif quality == choices[2]:  # for audio quality
                video = yt.streams.filter(only_audio=True).first()

            try:
                # start downloading
                video.download(folder)

                # after downloading clearing the link from box
                link_enter.delete(0, "end")

                # resetting link text
                link_error_label.config(text="^ Paste Video Link Above ^")

                # resetting path label text
                path_add_label.config(text="Please select path of download!")

                # download complete label
                download_wait_label.config(text="Download Complete!")

                # fetching video title from video's object
                name = video.title

                # fetching file size from video's object
                size = round(video.filesize / 1024000, 1)

                # setting attributes on app
                download_name_label.config(text="Name: " + name)
                download_size_label.config(text="Size: " + str(size) + "Mb")
                download_path_label.config(text="Path: " + folder)

            except:
                download_wait_label.config(text="Download Failed!!!")

        except:
            path_add_label.config(text="Please enter a valid path!!!")

    else:
        link_error_label.config(text="Please enter URL of video in above box ^^ !!")


# padx = padding x
# pady = padding y
# anchor center = align center

# Downloader Name label
downloader_label = Label(root, text="Youtube Video Downloader", bg="black", fg="white", font="Arial 15 bold")
downloader_label.pack(anchor="center", pady=8)

# link word label
link_label = Label(root, text="URL: ", bg="black", fg="white", font="arial 10")
link_label.pack(anchor="nw", padx=30, pady=20)

# link input entry
link = StringVar()
link_enter = Entry(root, width=62, textvariable=link)
link_enter.place(x=90, y=68)

# show Error in link label
link_error_label = Label(root, text="^ Paste Video Link Above ^", bg="black", fg="white", font="arial 10")
link_error_label.pack(anchor="center")

# Save destination path label
path_label = Label(root, text="Path", bg="black", fg="white", font="arial 10")
path_label.pack(anchor="nw", padx=30, pady=25)

# chosen path label
path_add_label = Label(root, text="Please select path of download!", width=30, fg="black", font="arial 10")
path_add_label.place(x=90, y=153)

# open file location button
path_button = Button(root, width=13, text="Select Path", bg="black", fg="white", font="arial 10",
                     command=file_location)
path_button.place(x=351, y=151)

# Quality label
quality_label = Label(root, text="Select Video Quality:", bg="black", fg="white", font="arial 10")
quality_label.pack(anchor="nw", padx=30)

# Combobox for choices
choices = ["High Quality", "Low Quality", "Audio Only"]
choices_box = ttk.Combobox(root, width=35, values=choices)
choices_box.current(0)
choices_box.place(x=230, y=203)

# Download button
download_button = Button(root, width=30, text="Download", bg="black", fg="white", font="arial 10",
                         command=download_video)
download_button.pack(anchor="center", pady=50)

# download wait label
download_wait_label = Label(root, text="", width=70, bg="black", fg="white",
                            font="arial 10")
download_wait_label.pack(anchor="nw", padx=30, pady=10)

# download name label
download_name_label = Label(root, text="", width=50, bg="black", fg="white",
                            font="arial 10")
download_name_label.pack(anchor="center", pady=10)

# download size label
download_size_label = Label(root, text="", width=60, padx=30, bg="black", fg="white",
                            font="arial 10")
download_size_label.pack(anchor="center", pady=10)

# download path label
download_path_label = Label(root, text="", width=50, bg="black", fg="white",
                            font="arial 10")
download_path_label.pack(anchor="center", padx=30, pady=10)

# developer label
developer_label = Label(root, text="Developer: Muhammad Hammad Faisal", bg="black", fg="white", font="arial 12 bold")
developer_label.pack(anchor="center", padx=30, pady=20)

# running interface
root.mainloop()
