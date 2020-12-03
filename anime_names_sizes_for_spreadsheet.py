'''
+ok. Before you use this or even go through the code let me tell you something. I am still new to programminng e.e
Aight now thats out of the way, let us start using the script. Here are the steps:

=================================================================================================================

1. Open Powershell
2. use the 'cd' or 'Set-Location' command to go into the directory that has all the anime folders. eg: Set-Location H:\pathto\directorythat\'has all the anime folders'\
3. Copy the lines from 14 to 19
4. Paste them in the powershell window you opened and press enter

---------------------------- lines to get the anime directories in the working-directory and their size --------------------------------

$location = Get-Location
gci -force $location -ErrorAction SilentlyContinue | ? { $_ -is [io.directoryinfo] } | % {
$len = 0
gci -recurse -force $_.fullname -ErrorAction SilentlyContinue | % { $len += $_.length }
$_.fullname, '{0:N0} MB' -f ($len / 1Mb)
} > output.txt

after the dirs and Sizes show up select all of it with your mouse (drop from the beginning to the end, if you know a better way to select the text in a shell you can do that. and pfft hmu and lemme know that trick too ;)).
Copy them. Run this python script and paste them in the input area. For the last one press enter and then type 'q' and then enter.
You should have files in the directory where you ran this python script in. Now go use them for spreadsheet columns :^)
------------------------------ script lines i took from http://woshub.com/powershell-get-folder-sizes/ -----------------------------------

5. After the directories and Sizes show up select all of it with your mouse (drop from the beginning to the end, if you know a better way to select the text in a shell you can do that. and pfft hmu and lemme know that trick too ;)).
6. Copy them. 
7. Run this python script and paste them into input area. 
8. For the last one press enter 
9. After you're done copying the directories and sizes, Type 'q' and then press enter.
10. Lastly, You should have a csv file ready for you in whichever directory that you ran the script in
You can open it using Microsoft Excel or import it to a google spreadsheet. Have fun :)

====================================================================================================================
Now go use them for spreadsheet columns :^)
i know that you can create csv's with python and use them for database usage. I'm just taking my time in learning these things and also i am a slow learner when theres no1 to really teach me kek.
'''
import string,csv
animes=[]
sizes=[]
directories=[]
end=0

while end == 0: 
    end=input(r":=")
    if end == "q":
        break
    else:
        directories.append(end)
        end=0
end=0
for directory in directories:
    small_directory = directory.split(" ")
    for smol in small_directory:
        while end==0:
            if str.isdigit(smol) or smol.find(',') > -1:
                sizes.append(smol)
                small_directory.remove(smol)
                if len(small_directory) > 1:
                    small_directory=" ".join(small_directory)
                    animes.append(small_directory)
                    break
                else:
                    animes.append(small_directory[0])
                    break
            else:
                break

for anime in animes:
    i = animes.index(anime)
    animes.remove(anime)
    anime = anime.replace('MB','')
    animes.insert(i,anime)

for size in sizes:
    if len(size) > 3:
        i = sizes.index(size)
        temp_size = size
        sizes.remove(temp_size)
        size = size.replace(',','.')
        temp_size=list(size)
        for x in range(2):
            temp_size.pop(-1)
        temp_size = ''.join(temp_size)
        sizes.insert(i,temp_size)

# with open('anime.txt','w') as f:
#     for anime in animes:
#         anime = anime.split('\\')
#         f.write(anime[3])
#         f.write('\n')

# with open('size.txt','w') as f:
#     for size in sizes:
#         if size.find('.') > -1:
#             f.write(size+' GB')
#             f.write('\n')
#         else:
#             f.write(size+' MB')
#             f.write('\n')

with open('anime_folderandsizes.csv','w',newline='') as file:
    header = ['Anime','Size']
    writer = csv.DictWriter(file,fieldnames=header)

    writer.writeheader()
    for anime in animes:
        i = animes.index(anime)
        anime = anime.split('\\')

        if sizes[i].find('.') > -1:
            size = sizes[i] + ' GB'
        else:
            size = sizes[i] + ' MB'
            
        anime_size = {
            'Anime': anime[3],
            'Size': size
        }

        writer.writerow(anime_size)