import csv,feedparser,re,time as t,datetime as dt,random
from discord_webhook import DiscordWebhook,DiscordEmbed

details_list = []
entry_list = []
colors = [16711680, 16777215, 16776960, 255, 65535, 12632256, 8421504, 65280, 16766720, 4915330, 8388736, 15631086, 16761035, 16119260, 10824234]
loop = 0
webhook_link = ' =======  Your Webhook Link Here ======= '

while True:
    loop += 1
    with open ('anime_list.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            details_list.append(row)

    try:
        feed = feedparser.parse('https://animepahe.com/feed/')
    except:
        loop -= 1
        break

    for entry in feed['entries']:
        if entry['title'] in entry_list:
            break
        elif re.search('{',entry['title']) == None:
            title = entry['title']
            subgrup = re.search(r'\[[^\]]*\]',title).group()
            title = title.replace(subgrup,'')
            for anime_detail in details_list:
                if re.search('{}'.format(anime_detail['title']),title):
                    i = details_list.index(anime_detail)
                    entry_list.append(entry['title'])
                    
                    webhook = DiscordWebhook(webhook_link)
                    embed = DiscordEmbed(title='Series Update: {}'.format(title),color=random.choice(colors))
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    webhook.execute()

                    print('Series_Update: {}:: {}'.format(title,dt.datetime.now())) 

        else:
            title = entry['title'].split(' - ')[0]
            if re.search(r'de":\d+',entry['title'].split(' - ')[1]):
                details = entry['title'].split(' - ')[1]
            else:
                details = entry['title'].split(' - ')[2]
                title = title + ' - ' + entry['title'].split(' - ')[1]
            
            episode = re.search(r'de":\d+',details).group()
            episode = re.search(r'\d+',episode).group()
            link = re.search(r'anime_id":\d+',details).group()
            link = 'https://pahe.win/a/'+re.search(r'\d+',link).group()

            for anime_detail in details_list:
                if re.search('{}'.format(anime_detail['title']),title):
                    if int(episode) > int(anime_detail['episode']):
                        i = details_list.index(anime_detail)
                        entry_list.append(entry['title'])

                        anime_detail = {
                            'title': title,
                            'episode': episode,
                            'link': link + '/' + episode
                        }
                        details_list[i].update({'episode': episode,'link': anime_detail['link']})
                        
                        webhook = DiscordWebhook(webhook_link)
                        embed = DiscordEmbed(title='{} - Episode {}'.format(anime_detail['title'],anime_detail['episode']),url=anime_detail['link'],color=random.choice(colors))
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()

                        print('New: {} - Episode {} :: {}'.format(anime_detail['title'],anime_detail['episode'],dt.datetime.now()))
    
    with open('anime_list.csv','w',newline='') as csvfile:
        headers = ['title','episode','link']
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        for detail in details_list:
            writer.writerow(detail)

    details_list.clear()
    print(loop,' :: ',dt.datetime.now().strftime('%H:%M:%S'))
    t.sleep(300)
