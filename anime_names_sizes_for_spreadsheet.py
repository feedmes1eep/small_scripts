'''
ok. Before you use this or even go through the code let me tell you something. I am still new to programminng e.e
Aight now thats out of the way, open Powershell and cd to the folder where you collection fo anime is (or whereever you want, all up to you). 
Copy this into the text area (script lines i took from http://woshub.com/powershell-get-folder-sizes/ )

gci -force 'C:\Users'-ErrorAction SilentlyContinue | ? { $_ -is [io.directoryinfo] } | % {
$len = 0
gci -recurse -force $_.fullname -ErrorAction SilentlyContinue | % { $len += $_.length }
$_.fullname, '{0:N2} GB' -f ($len / 1Gb)
}

after the dirs and Sizes show up select all of it with your mouse (drop from the beginning to the end, if you know a better way to select the text in a shell you can do that. and pfft hmu and lemme know that trick too ;)).
Copy them. Run this python script and paste them in the input area. For the last one press enter and then type 'q' and then enter.
You should have files in the directory where you ran this python script in. Now go use them for spreadsheet columns :^)
'''

animes=[]
sizes=[]
full_thing=[]
end=0

while end == 0:
    end=input(":=")
    if end == "q":
        break
    else:
        full_thing.append(end)
        end=0
end=0
for thing in full_thing:
    thingsmolp = thing.split(" ")
    for smol in thingsmolp:
        while end==0:
            if smol.find('.') == True:
                sizes.append(smol)
                thingsmolp.remove(smol)
                if len(thingsmolp) > 1:
                    thingsmolp=" ".join(thingsmolp)
                    animes.append(thingsmolp)
                    break
                else:
                    animes.append(thingsmolp[0])
                    break
            else:
                break

with open('anime.txt','w') as f:
    for anime in animes:
        anime = anime.split('/')
        f.write(anime[3])
        f.write('\n')

with open('size.txt','w') as f:
    for size in sizes:
        f.write(size+" GB")
        f.write('\n')