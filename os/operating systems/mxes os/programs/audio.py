import os
import winsound
music_files=[]
end=False
files=os.listdir("C:\\os\\operating systems\\mxes os")
while len(files)>0:
    file0=files[0]
    if ".wav" in file0:
        music_files.append(file0)
        file0=files[0]
        files.pop(0)
    else:
        file0=files[0]
        files.pop(0)
while len (music_files):
    print(">",music_files[0])
    music_files2=[]
    music_files2.append([0])
    music_files.pop(0)
while not end: 
    file_play=input("> What sound file do you wish to play to exit input e \n> ")
    if file_play=="e":
        end=True
    else:
        winsound.PlaySound(f"C:\\os\\operating systems\\mxes os\\{file_play}",winsound.SND_ASYNC)
        music_op=input("> To stop song input s to exit input e\n> ")
        if music_op.lower()=="s":
            winsound.PlaySound(None, winsound. SND_PURGE)