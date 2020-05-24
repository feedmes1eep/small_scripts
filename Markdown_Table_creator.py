# commented parts are an attempt to make a prettified table. was in the process of doing this when i noticed that you can just make an inline version of it
# and i like to save things to might as well keep it in here :)


# def longest_everything(names,unames,mnumbers,dIDs):
#     longest_name=0
#     longest_uname=0
#     longest_mnumber=0
#     longest_dID=0
#     for name in names:
#         if name == names[0]:
#             longest_name=len(name)
#         elif len(name) > longest_name:
#             longest_name=len(name)
#     for uname in unames:
#         if uname == unames[0]:
#             longest_uname=len(uname)
#         elif len(uname) > longest_uname:
#             longest_uname=len(uname)
#     for mnumber in mnumbers:
#         if mnumber == mnumbers[0]:
#             longest_mnumber=len(mnumber)
#         elif len(mnumber) > longest_mnumber:
#             longest_mnumber=len(mnumber)
#     for dID in dIDs:
#         if dID == dIDs[0]:
#             longest_dID=len(dID)
#         elif len(dID) > longest_dID:
#             longest_dID=len(dID)
#     return longest_name,longest_uname,longest_mnumber,longest_dID

T1names=[]
T1uplay_names=[]
T1mobile_numbers=[]
T1discord_ids=[]
T2names=[]
T2uplay_names=[]
T2mobile_numbers=[]
T2discord_ids=[]
headings=['Names', 'Uplay Nmaes', 'Discord IDs', 'Mobile Number']
print("---------------F33DM3N3ZUK0 Details---------------")
for x in range(6):
    name=input('Full name: ')
    uplay_name=input('Uplay name: ')
    mobile_number=input('Mobile number: ')
    discord_id=input('Discord Name with #ID: ')
    T1names.append(name)
    T1uplay_names.append(uplay_name)
    T1mobile_numbers.append(mobile_number)
    T1discord_ids.append(discord_id)
print("\n---------------AlphoofFTW Details---------------")
for x in range(6):
    name=input('Full name: ')
    uplay_name=input('Uplay name: ')
    mobile_number=input('Mobile number: ')
    discord_id=input('Discord Name with #ID: ')
    T2names.append(name)
    T2uplay_names.append(uplay_name)
    T2mobile_numbers.append(mobile_number)
    T2discord_ids.append(discord_id)

# # lname,luplay_name,lmobile_number,ldiscord_id=longest_everything(names,uplay_names,mobile_numbers,discord_ids)
star = "*"*2
print("# F33DM3N3ZUK0")
for heading in headings:
    if heading == headings[-1]:
        print(star+heading+star)
    elif heading == heading[0]:
        print(star+heading+star,end=" | ")
    else:
        print(star+heading+star,end=" | ")
for x in headings:
    if x == headings[-1]:
        print(" --- ")
    else:
        print(" --- ",end="|")

for x in range(len(T1names)):
    print(T1names[x],end=" | ")
    print(T1uplay_names[x],end=" | ")
    print(T1discord_ids[x],end=" | ")
    print(T1mobile_numbers[x])

print("# AlphoofFTW")
for heading in headings:
    if heading == headings[-1]:
        print(star+heading+star)
    elif heading == heading[0]:
        print(star+heading+star,end=" | ")
    else:
        print(star+heading+star,end=" | ")
for x in headings:
    if x == headings[-1]:
        print(" --- ")
    else:
        print(" --- ",end="|")

for x in range(len(T2names)):
    print(T2names[x],end=" | ")
    print(T2uplay_names[x],end=" | ")
    print(T2discord_ids[x],end=" | ")
    print(T2mobile_numbers[x])