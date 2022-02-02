#Kanged From @TroJanZheX
import asyncio
import re
import ast
from Script import script
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, temp
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import(
   del_all,
   find_filter,
   get_filters,
)

BUTTONS = {}


@Client.on_message(filters.user(ADMINS) & filters.private & filters.text)
async def give_filter(client,message):
    group_id = message.chat.id
    name = message.text

    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await message.reply_text(reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await message.reply_text(
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button)
                            )
                    elif btn == "[]":
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or ""
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button)
                        )
                except Exception as e:
                    print(e)
                break 

    else:
        await auto_filter(client, message) 

@Client.on_message(filters.command("nude") & filters.private)
async def nude(client, message):
    await client.send_message(message.chat.id, f""" 
Agatha ve Cinayet Gerçeği (2018) Altyazılı.mp4

Cruella
(Alt yazılı) (2021)

İnjustice (2021) Altyazılı

Free Guy (2021) Altyazılı

Dolittle (2020) Altyazılı

Knives Out (2019) Altyazılı

Shazam (2019) Altyazılı

Kaplan Ve Ejderha  (2000) Dublaj

Kaplan Ve Ejderha 2 (2016) Dublaj

Lucy (2014) Altyazılı

James Bond: Casino Royale (2006) Dublaj

James Bond: Skyfall (2012) Dublaj

İnterstellar (2014) Altyazılı

Old (2021) Altyazılı

Man Of Tai Chi (2013) Dublaj

Extraction (2020) Altyazılı

Kung-fu Killer (2014) Dublaj

13 Suikastçi (2010) Dublaj

Moana (2016) Dublaj

Rurouni Kenshin: Meiji Kenkaku Romantan (2012) Altyazılı

Rurouni Kenshin: Kyoto Cehennemi (2014) Altyazılı

Rurouni Kenshin: The Legend Ends (2014) Altyazılı

Joker (2019) Altyazılı

Rurouni Kenshin: The Final (2021) Altyazılı

Rurouni Kenshin: The Beginning (2021) Altyazılı

Romeo Ve Juliet (1996) Altyazılı

Ong-Bak: The Thai Warrior (2003) Dublaj

Ong-Bak 2 (2008) Dublaj

Ong-Bak 3 (2010) Dublaj

The Suicide Squad (2021)Altyazılı

Shang-Chi: And The Legends Of The Ten Rings (2021) Dublaj
Sinema Çekimi

Star Wars: The Last Jedi (Episode VIII) (2017) Altyazılı

jurassic Park 1 (1993) Dublaj

Jurassic Park Kayıp Dünya (1997) Dublaj

Jurassic Park 3 (2001) Dublaj

Jurassic World (2015) Dublaj

Jurassic World Yıkılmış Krallık - Jurassic World Fallen Kingdom (2018) Dublaj

Godzilla Vs Kong (2021) Dublaj

Ölü Gelin (2005) Dublaj

Space Jam (1996) Dublaj

@quickwasteistek

Space Jam: New Legacy (2021) Altyazılı

@quickwasteistek

Army Of The Dead (2021) Dublaj

Soul (2020) Dublaj

Moonlight (2016) Dublaj

@quickwasteistek

Orphan - Evdeki Düşman (2009) Altyazılı

Caroline ve Gizli Dünya (2009) Dublaj

Koruyucu 2 (2013) Dublaj
@quickwasteistek

Tenet (2020) Altyazılı

Shang-Chi And The Legends Of The Ten Rings kaliteli sinema çekimi Dublaj

The Guilty (2021) Altyazılı

@quickwasteistek

Harley Quinn ve Yırtıcı Kuşlar (2020) Altyazılı

Hayvan Çiftliği (1954) Altyazılı

Hitman's wife's bodyguard 2 - Belalı Tanık 2 (2021) Altyazılı

Power Rangers (2017) Altyazılı

Power Rangers (2017) Dublaj

Snake Eyes: G.I. Joe Origins (2021) Altyazılı

Spiral: From the Book of Saw - Spiral: Testere Devam Ediyor (2021) Altyazılı

Queen Of The Amazon (2021) Altyazılı

Needle in a Timestack (2021) Altyazılı

The Hunted (2020) Altyazılı

White Snake(2019) Altyazılı

Peter Rabbit 2 (2021) Altyazılı

The Power Of The Dog (2021) Altyazılı

The Prodigy (2019) Altyazılı

Venom 2 (2021) Dublaj Sinema Çekimi

Ölümcül Araştırma (2016) Dublaj

Spirit: Özgür Ruh (2021) Altyazılı

Gemini Man (2019) Dublaj

Spirited Away (2001) Altyazılı

Aiyai: Wrathful Soul (2020) Altyazılı

Tom of Finland (2017) Altyazılı

Between Waves (2020) Altyazılı

The Beyond (2017) Altyazılı

After We Leave (2019) Altyazılı

Klaus: Sihirli Plan (2019) Altyazılı

Synapse (2021) Altyazılı

Esaretin Bedeli (1994) Dublaj

Klaus: Sihirli plan (2019) Dublaj

Astra Loco (2021) Altyazılı

Edge Of Tomorrow (2014) Altyazılı

Kimya (2021) Yerli Film

James Bond: Casino Royale (2006) Dublaj

James Bond: Quantum of Solace  (2008) Dublaj

James Bond: Skyfall (2012) Dublaj

James Bond: Spectre (2015) Dublaj

La La Land (2016) Altyazılı

İnception (2010) Dublaj

Shang-Chi (2021) Sinema Çekimi Dublaj

İnception (2010) Altyazılı

Esaretin Bedeli (1994) Altyazılı

The Festival (2018) Altyazılı

Slumber Party Massacre (2021) Altyazılı

After (2019) Altyazılı

Hasat Zamanı (2007) Dublaj

After We Fell (2021) Altyazılı

Gone Girl (2014) Altyazılı

Gerald’s Game (2017) Altyazılı

Found - Kayıp Kökler (2021) Altyazılı

Sinkhole (2021) Altyazılı

Justice League Snyder Cut (2021) Dublaj

I Can't Safe Everyone:
The Blazing World (2021) Altyazılı

The Machinist (2004) Altyazılı

Matrix (1999) Altyazılı Kota Dostu

Matrix 2: Reloaded (2003) Altyazılı Kota dostu

Matrix 3: Revolutions (2003) Altyazılı

Crood’lar 2: Yeni Bir Çağ (2021) Altyazılı

Korsanlar (2012) Dublaj

Sanak (2021) Altyazılı

The Pirates - Korsanlar (2014) Altyazılı

Peter Rabbit 2 (2021) Altyazılı

The Power Of The Dog (2021) Altyazılı

The Prodigy (2019) Altyazılı

Venom 2 (2021) Dublaj Sinema Çekimi

Ölümcül Araştırma (2016) Dublaj

Spirit: Özgür Ruh (2021) Altyazılı

Gemini Man (2019) Dublaj

Spirited Away (2001) Altyazılı

Aiyai: Wrathful Soul (2020) Altyazılı

Tom of Finland (2017) Altyazılı

Between Waves (2020) Altyazılı

The Beyond (2017) Altyazılı

After We Leave (2019) Altyazılı

Klaus: Sihirli Plan (2019) Altyazılı

Synapse (2021) Altyazılı

Esaretin Bedeli (1994) Dublaj

Klaus: Sihirli plan (2019) Dublaj

Astra Loco (2021) Altyazılı

Edge Of Tomorrow (2014) Altyazılı

Kimya (2021) Yerli Film

James Bond: Casino Royale (2006) Dublaj

James Bond: Quantum of Solace  (2008) Dublaj

James Bond: Skyfall (2012) Dublaj

James Bond: Spectre (2015) Dublaj

La La Land (2016) Altyazılı

İnception (2010) Dublaj

Shang-Chi (2021) Sinema Çekimi Dublaj

İnception (2010) Altyazılı

Esaretin Bedeli (1994) Altyazılı

The Festival (2018) Altyazılı

Slumber Party Massacre (2021) Altyazılı

After (2019) Altyazılı

Parasite (2019) Altyazılı

Hasat Zamanı (2007) Dublaj

After We Fell (2021) Altyazılı

Gone Girl (2014) Altyazılı

Gerald’s Game (2017) Altyazılı

Found - Kayıp Kökler (2021) Altyazılı

Sinkhole (2021) Altyazılı

Justice League Snyder Cut (2021) Dublaj

Justice League Snyder Cut (2021) Altyazılı

De slag om de Schelde (2020) Altyazılı

Radium Girls (2018) Altyazılı

Batman Begins (2005) Dublaj

The Dark Knight (2008) Dublaj

The Dark Knight Rises (2012) Dublaj

Dabbe (2006)

Dabbe 2 (2009)

Dabbe 4 (2013)

Dabbe 5 (2014)

Dabbe 6 (2015)

Nomadland (2020) Altyazılı

Black Swan (2010) Altyazılı

Upgrade (2018) Altyazılı

The Avengers (2012) Altyazılı

Avengers: Age Of Ultron (2015) Altyazılı

Avengers: İnfinity War (2018) Altyazılı

Avengers: Endgame (2019) Altyazılı

The Tomorrow War (2021) Altyazılı

Minari (2020) Altyazılı

The Sorcerer and the White Snake (2011) Altyazılı

Monster Family 2 (2021) Altyazılı

Savaşçının Yolu (2010) Dublaj

Aslan Kral (2019) Altyazılı

Megamind (2010) Dublaj

The Corrupted (2019) Altyazılı

Megamind (2010) Altyazılı

Detachment (2011) Altyazılı

Ölümcül Deney 5 (2012) Dublaj

Çılgın Çocuklar 4 (2011) Dublaj

Filth (2013) Altyazılı

Batman V Superman (2016) Dublaj

The Words (2012) Altyazılı

Huzursuz Ruhlar (2006) Dublaj

The Experiment (2001) Altyazılı

Lady Bird (2017) Altyazılı

immortals (2011) Altyazılı

Promising Young Woman (2020) Altyazılı

Upside Down (2012) Altyazılı

I Saw the Devil (2010) Dublaj

X-Men 1 (2000) Altyazılı

X-Men 2 (2003) Altyazılı

X-Men: The Last Stand (2006) Altyazılı

X-Men Origins: Wolverine (2009) Altyazılı

The Halloween-Cadılar Bayramı (2018) Dublaj

Lair (2021) Altyazılı

Nine Days (2020) Altyazılı

Yüzüklerin Efendisi 1 - The Lord of the Rings: The Fellowship of the Ring (2001) Altyazılı

Yüzüklerin Efendisi 2 - The Lord of the Rings: The Two Towers (2002) Altyazılı

Yüzüklerin Efendisi 3 - The Lord of the Rings: The Return of the King (2003) Altyazılı

Harry Potter 1 - Harry Potter and the Sorcerer's Stone (2001) Altyazılı

I Can't Safe Everyone:
Harry Potter 2 - Harry Potter and the Chamber of Secrets (2002) Altyazılı

Hırsızlar Ordusu 2021 TR Dublaj

Love Hard (2020) Altyazılı

Hipnotizma TR Dublaj

Gattaca (1997) Altyazılı

Fractured (2019) Altyazılı

Eternals (2021) Altyazılı sinema çekimi.

@quickwaste

Eternals (2021) Dublaj sinema çekimi

@quickwaste

Sıcak kalpler (2013) Dublaj

Countdown Geri sayım TR dublaj

Frankenstein Ölümsüzlerin Savaşı (2014)  Dublaj

James Bond: No Time To Die (2021) Altyazılı

Shang-Chi And The Legends Of The Ten Rings (2021) Altyazılı

Chennai Express - Aşk Treni (2013) Dublaj

Finch (2021) Altyazılı

Hobbit Beklenmedik Yolculuk (2012) Dublaj

Hobbit 2 (2013) Dublaj

Hobbit 5 Ordunun Savaşı (2014) Dublaj

Yaratık (1979) Altyazılı

Yaratık 2 (1986) Altyazılı

The Call (2020) Altyazılı

Red Notice (2021) Altyazılı

Red Notice (2021) Dublaj

Shang-Chi (2021) Dublaj

Yaratık 3 (1992) Altyazılı

Takip İstanbul - Taken 2 (2012) Altyazılı

Yaratık 4: Diriliş (1997) Altyazılı

Dune (2021) Altyazılı @quickwaste

City Of Ember (2008) Altyazılı

X-Men: The Last Stand (2006) Dublaj

Jungle Cruise (2021) Altyazılı

Split - Parçalanmış (2016) Dublaj

Sihirli Dağ (2009) Dublaj

Knives Out (2019) Dublaj

Hz. Muhammed Allahın Elçisi (2015) Dublaj

Çizgili Pijamalı Çocuk (2008) Dublaj

X-Men: First Class (2011) Altyazılı

X-Men: Apoclypse (2016) Altyazılı

X-Men Dark Phoenix (2019) Altyazılı

X-Men Dark Phoenix (2019) Altyazılı

X-Men: Dark Phoenix (2019) Dublaj

The New Mutants (2020) Altyazılı

Beatiful Boy (2018) Altyazılı

Hızlı Ve Öfkeli 9 (2021) Dublaj

Glass (2019) Altyazılı

Tick, Tick... Boom! (2021) Altyazılı

Tick, Tick... Boom! (2021) Dublaj

Snowpiercer (2013) Altyazılı

Star Wars Episode 1 The Phontom Menace (2000) Altyazılı

Star Wars Episode 2 Attack Of The Clones (2002) Altyazılı

Star Wars Episode 3 Revenge Of The Sith (2005) Altyazılı

Star Wars Episode 4 A New Hope (1977) Altyazılı

Star Wars Episode 4 A New Hope (1977) Altyazılı

Star Wars Episode 5 The Empires Strikes Back (1980) Altyazılı

Star Wars Episode 6 Return Of The Jedi (1983) Altyazılı

Aklım karıştı TR dublaj 1999

Girl interrrupted (1999) Altyazılı

Baby Driver (2017) Altyazılı

Pek Yakında (2014)

Ters Yüz (2015) Dublaj

Vivo (2021) Dublaj

Baby Driver (2017) Dublaj

Fırtına Savaşçıları (2009) Dublaj

Fantastik Dörtlü 1 (2005) Dublaj

Fantastik Dörtlü 2 (2007) Dublaj

Fantastik Dörtlü 3 Reboot (2015) Dublaj

Sleepy Hollow (1999) Altyazılı

Altın Çiceğin Laneti (2006) Dublaj

Hot Summers Nights (2017) Altyazılı

Ben Bir Robotum Ama Sorun Değil (2006) Altyazılı

Vivarium (2019) Altyazılı.mp4

Spencer (2021) Altyazılı

Castle For Christmas (2021) Altyazılı

Fanaa (2006) Altyazılı.mp4

Hıçkırık (2018) Dublaj

Ghajını (2008) Altyazılı

Hint Denizi Korsanları (2008) Dublaj

İnfinite (2021) Altyazılı

The Last Duel (2021) Altyazılı

Bir Geyşa'nın Anıları (2005) Altyazılı

Bir Geyşanın Anıları (2005) Dublaj

Last Night İn Soho (2021) Altyazılı

Savaş Vadisi (2016) Dublaj

Undergods (2020) Altyazılı

Venom 2 (2021) Altyazılı Orijinal Ses Ve Görüntü

The Dictator (2012) Dublaj

Evde Tek Başına (1990) Dublaj

Secret Superstar (2017) Dublaj

Secret Superstar (2017) Altyazılı.mp4

Ella Enchanted (2004) Altyazılı

Anna (2013) Altyazılı

Labirent Alev Deneyleri (2015) Dublaj

Predestination (2014) Altyazılı

Dangal (2016) Dublaj

Yeşil Rehber (2018) Dublaj

Ben Anneyim (2019) Dublaj.mp4

James Bond No Time To Die (2021) Dublaj

Pobochnyi Effekt (2020) Altyazılı

Uyumsuz 3 :  Yandaş Bölüm 1 (2016) Dublaj

The Conjuring: The Devil Made Me Do It (2021) Dublaj

Takip 3 Son Karşılaşma (2014) Altyazılı

5. Dalga (2016) Altyazılı

Uyumsuz Kuralsız (2016) Dublaj

Babil M.S (2008) Dublaj

Amélie (2001) Altyazılı Kota Dostu

Amélie (2001) Altyazılı

Space Jam 2 (2021) Dublaj

Spider-Man No Way Home Sinema Çekimi Dublaj (2021)

Kara Kutu (2021) Altyazılı Sinema Çekimi

Akıl Defteri (2000) Dublaj

The Shack (2017) Altyazılı

Mitchells Vs The Machines (2021) Dublaj

Kodachrome (2017) Altyazılı

Resident Evil : Welcome To Raccoon City (2021) Altyazılı

Being the Ricardos (2021) Altyazılı

The Great Gatsby (2013) Altyazılı

Haberciler 2: Korkuluk (2010) Dublaj

The Unforgivable (2021) Altyazılı

Don't Look Up (2021) Dublaj

Gizemli Geçit (2016) Dublaj

Don't Look Up (2021) Altyazılı

Encounter (2021) Altyazılı

İyi Çocuklar Ağlamaz (2012) Dublaj

Love And Monster (2021) Altyazılı

Ruhlar Bölgesi (2010) Altyazılı

Sylvia (2003) Altyazılı

Enola Holmes (2020) Dublaj

Yeni Grubun İlk Filmi Hayırlı olsun.

Minari (2020) Dublaj

Hilda and the Mountain King (2021) Altyazılı

Old (2021) Dublaj

Enola Holmes (2020) Dublaj .mp4

Minari (2020) Dublaj.mp4

Love Actually (2003) Dublaj.mp4

8-Bit Christmas (2021) Dublaj.mp4

Hilda and the Mountain King (2021) Altyazılı.mp4

Shoplifters (2018) Dublaj

Before I Fall (2017) Altyazılı

The Borrowers (1997) Dublaj.mp4

Ghostbusters Afterlife (2021) Altyazılı.mp4

The Suicide Squad (2021) Dublaj.mp4

Jungle Cruise (2021) Dublaj.mp4

Venom 2 (2021) Dublaj.mp4

Sınavlar Gereği Film atmamız durdurulmuştur lütfen biraz sabırlı olup bekleyiniz.

American Psycho (2000) Altyazılı.mp4

Dirty Grandpa (2016) Altyazılı.mp4

The Wolf Of Wall Street (2013) Altyazılı.mp4

Dirty Grandpa (2016) Dublaj.mp4

Alice İn Wonderland (1966) Altyazılı.mp4

Zola (2021) Altyazılı.mp4

Three Wishes for Cinderella (2021) Altyazılı.mp4

Zola (2020) Dublaj.mp4

Clifford Big Red Dog (2021) Altyazılı.mp4

The God Of Commite (2021) Altyazılı.mp4

The Beast (2021) Altyazılı.mp4

C'mon C'mon (2021) Altyazılı.mp4

Akira (1998) Altyazılı.mp4

Ölümcül Tuzak (2008) Dublaj.mp4

Eternals (2021) Altyazılı.mp4

Free Guy (2021) Dublaj.mp4

Peacemaker 1. Bölüm A Whole New Whirled.mp4

Otel Transilvanya 4: Transformanya (2022) Altyazılı.mp4

Made Of Honor (2008) Altyazılı.mp4

Dude (2018) Altyazılı.mp4

Brazen (2022) Altyazılı.mp4

Gizli Sayılar (2016) Dublaj.mp4

Jingle All The Way (1996) Dublaj.mp4

Yeşil Yılan (2021) Altyazılı.mp4

The Father (2020) Altyazılı.mp4

Holidate (2020) Altyazılı.mp4

Evde Tek Başına (1990) Altyazılı.mp4

Evde Tek Başına 2 (1992) Altyazılı.mp4

Evde Tek Başına 3 (1997) Altyazılı.mp4

Rebelde - Asi Yıllar 1.Sezon 1. Bölüm (dublaj).mp4

Superman And Lois 1. Sezon 1. Bölüm (Altyazılı).mp4

Encanto (2021) Altyazılı.mp4

Karateci Kız (1994) Dublaj.mp4

Ölümcül Güzellik 2 (2012) Dublaj.mp4

Dexter New Blood 1. Sezon 1. Bölüm Dublaj.mp4

How I Met Your Mother 1. Sezon 1. Bölüm - Pilot Bölüm- Altyazılı @anagrupbot.mp4

Stranger Things 1. Sezon 1. Bölüm  (Altyazılı).mp4

Demon Slayer 1. Sezon 1. Bölüm Altyazılı @anagrupbot.mp4

Attack On Titan 1. Sezon 1. Bölüm Altyazılı @anagrupbot.mp4

Vikings 1. Sezon 1. Bölüm Altyazılı @anagrupbot.mp4

Euphoria 1. Sezon 1. Bölüm Altyazılı @anagrupbot.mp4

Spider-Man: Into the Spider-Verse (2018) Altyazılı @anagrupbot.mp4

Matrix Resurrections (2021) Altyazılı@quickwaste.mp4

The Summit If The Gods (2021) Dublaj.mp4

Mad Max 1 (1979) Dublaj @anagrupbot.mp4

Mad Max 2: The Road Warrior (1981) Dublaj @anagrupbot.mp4

Mad Max 3: Beyond Thunderdome (1985) Dublaj @anagrupbot.mp4

Mad Max: Fury Road (2015) Dublaj @anagrupbot.mp4

İnception (2010) Dublaj @anagrupbot.mp4

Scream 5 (2022) Altyazılı Sinema Çekimi @anagrupbot.mp4

Red Rocket (2021) Altyazılı @anagrupbot.mp4

Escape Room Tournament of Champions (2021) Altyazılı @anagrupbot.mp4

The Piona Teacher (2001) Altyazılı @anagrupbot.mp4

Spirit: Özgür Ruh (2021) Dublaj @anagrupbot.mp4

Johnny English Reborn (2011) Altyazılı @anagrupbot.mp4

Rising High (2020) Dublaj @anagrupbot.mp4

Corpse Bride (2005) Altyazılı @anagrupbot.mp4

Terminator 2 Judgment Day (1991) Altyazılı @anagrupbot.mp4

Clean (2022) Altyazılı @anagrupbot.mp4

The 355 (2022) Altyazılı @anagrupbot.mp4

Home Team (2022) Dublaj @anagrupbot.mp4

Home Team (2022) Altyazılı @anagrupbot.mp4

Midnight Swan (2020) Altyazılı @anagrupbot.mp4

Fight Club (1999) Altyazılı @anagrupbot.mp4

The Godfather (1972) Altyazılı @anagrupbot.mp4

The Godfather (1974) Altyazılı @anagrupbot.mp4

Forrest Gump (1994) Altyazılı @anagrupbot.mp4

12 Angry Man - 12 Kızgın Adam (1957) Altyazılı @anagrupbot.mp4

Pulp Fiction (1994) Altyazılı @anagrupbot.mp4

The Good, The Bad And The Ugly (1966) Altyazılı @anagrupbot.mp4

Schindler's List - Schindlerin Listesi (1993) Altyazılı @anagrupbot.mp4

The Dark Knight (2008) Altyazılı @anagrupbot.mp4

One Flew Over the Cuckoo's Nest - Guguk Kuşu (1975) Altyazılı @anagrupbot.mp4

Goodfellas (1990) Altyazılı @anagrupbot.mp4

Saving Private Ryan – Er Ryan’ı Kurtarmak (1998) Altyazılı @anagrupbot.mp4

Parasite (2019) Altyazılı @anagrupbot.mp4

City Of God - Tanrı Kent (2002) Altyazılı @anagrupbot.mp4

Hayat Güzeldir – La Vita è Bella (1997) Altyazılı @anagrupbot.mp4

Yedi - Se7en (1995) Altyazılı @anagrupbot.mp4

Kuzuların Sessizliği – The Silence Of The Lambs (1991) Altyazılı @anagrupbot.mp4

Harakiri (1962) Altyazılı @anagrupbot.mp4

Shichinin No Samurai - Yedi Samuray (1954) Altyazılı @anagrupbot.mp4

Whiplash (2014) Altyazılı @anagrupbot.mp4

The Intouchables – Can Dostum (2011) Altyazılı @anagrupbot.mp4

The Prestige (2006) Altyazılı @anagrupbot.mp4

Şahane Hayat – It’s a Wonderful Life (1946) Altyazılı @anagrupbot.mp4

Titanic - Titanik (1997) Altyazılı @anagrupbot.mp4

The Ice Age Adventures of Buck Wild (2022) Altyazılı @anagrupbot.mp4

American History X – Geçmişin Gölgesinde (1998) Altyazılı @anagrupbot.mp4

The Departed (2006) Altyazılı @anagrupbot.mp4

The Pianist (2002) Altyazılı @anagrupbot.mp4

The Usual Suspects – Olağan Şüpheliler (1995)Altyazılı @anagrupbot.mp4

Gladiator (2000) Altyazılı @anagrupbot.mp4

Leon: The Professional – Sevginin Gücü (1994) Altyazılı @anagrupbot.mp4

The Lion King (1994) Altyazılı @anagrupbot.mp4

Cinema Paradiso – Cennet Sineması (1988) Altyazılı @anagrupbot.mp4

Hotaru No Haka – Ateş Böceklerinin Mezarı (1988) Altyazılı @anagrupbot.mp4

Once Upon a Time in the West – Bir Zamanlar Batıda (1968) Altyazılı @anagrupbot.mp4

Psycho – Sapık (1960) Altyazılı @anagrupbot.mp4

Rear Window – Arka Pencere (1954) Altyazılı @anagrupbot.mp4

Back To The Future (1985) Altyazılı @anagrupbot.mp4

Casablanca – Kazablanka (1942) Altyazılı @anagrupbot.mp4

James Bond: Skyfall (2012) Altyazılı @anagrupbot.mp4

Modern Times (1936) Altyazılı @anagrupbot.mp4

Şehir Işıkları – City Lights (1931) Altyazılı @anagrupbot.mp4

Hamilton (2020) Altyazılı @anagrupbot.mp4

Capernaum – Kefernahum (2018) Altyazılı @anagrupbot.mp4

Joker (2019) Altyazılı @anagrupbot.mp4

Kimi no na wa (2016) Altyazılı @anagrupbot.mp4

Coco (2017) Altyazılı @anagrupbot.mp4

Sleepy Hollow (1999) Altyazılı @anagrupbot.mp4

Spider-Man No Way Home (2021) Altyazılı @anagrupbot.mp4

Hannibal 1. Sezon 1. Bölüm Altyazılı @anagrupbot.mp4

Django Unchained – Zincirsiz (2012) Altyazılı @anagrupbot.mp4

The Dark Knight Rises (2012) Altyazılı @anagrupbot.mp4

WALL·E (2008) Altyazılı @anagrupbot.mp4

3 Idiots – 3 Aptal (2009) Altyazılı @anagrupbot.mp4

The Lives of Others – Başkalarının Hayatı (2006) Altyazılı @anagrupbot.mp4

Taare Zameen Par - Yerdeki Yıldızlar (2007) Altyazılı @anagrupbot.mp4

İhtiyar Delikanlı – Oldeuboi (2003) Altyazılı @anagrupbot.mp4

Memento – Akıl Defteri (2000) Altyazılı @anagrupbot.mp4

Princess Mononoke – Prenses Mononoke (1997) Altyazılı @anagrupbot.mp4

Raiders of The Lost Ark – Kutsal Hazine Avcıları (1981) Altyazılı @anagrupbot.mp4

The Shining – Cinnet (1980) Altyazılı @anagrupbot.mp4

Perfect Blue (1997) Altyazılı @anagrupbot.mp4

Alien - Yaratık (1979) Altyazılı @anagrupbot.mp4

Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964) Altyazılı @anagrupbot.mp4

Apocalypse Now – Kıyamet (1979) Altyazılı @anagrupbot.mp4

Tengoku to jigoku - Yüksek Ve Alçak (1963)Altyazılı @anagrupbot.mp4

Witness for the Prosecution – Beklenmeyen Şahit (1957) Altyazılı @anagrupbot.mp4

Paths of Glory – Zafer Yolları (1957) Altyazılı @anagrupbot.mp4

Sunset Blvd. – Sunset Bulvarı (1950) Altyazılı @anagrupbot.mp4

The Great Dictator – Büyük Diktatör (1940) Altyazılı @anagrupbot.mp4

Jagten – Onur Savaşı (2012) Altyazılı @anagrupbot.mp4

Euphoria 2. Sezon 2. Bölüm @anagrupbot.mp4

Solo: A Star Wars Story (2018) Altyazılı @anagrupbot.mp4

Rogue One: A Star Wars Story (2016) Altyazılı @anagrupbot.mp4

Star Wars: The Rise of Skywalker (Episode IX) (2019) Altyazılı @anagrupbot.mp4

Star Wars: The Last Jedi (Episode VIII) (2017) Altyazılı @anagrupbot.mp4

The Sixth Sense – Altıncı His (1999) Altyazılı @anagrupbot.mp4

Star Wars: The Force Awakens (Episode VII) (2015) Altyazılı @anagrupbot.mp4

War Dogs - Vurguncular (2016) Altyazılı @anagrupbot.mp4

House Of Gucci (2021) Altyazılı @anagrupbot.mp4

Lion Of The Desert - Çöl Aslanı Ömer Muhtar (1981) Altyazılı @anagrupbot.mp4

Borrego (2022) Altyazılı @anagrupbot.mp4

My Best Friend Anne Frank (2021) Altyazılı @anagrupbot.mp4

Titane (2021) Altyazılı @anagrupbot.mp4

Little Women (2019)  Altyazılı @anagrupbot.mp4

The Report (2019) Altyazılı @anagrupbot.mp4
""") 
  

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer("oKda", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("Bunu eski mesajlarımdan biri için kullanıyorsunuz, lütfen isteğinizi tekrar gönderin.",show_alert=True)
        return
    btn=[]

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    if files:
        for file in files:
            file_id = file.file_id
            btn.append(
                [InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'files#{file_id}'), InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'files_#{file_id}')]
                )
    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("⏪ Geri", callback_data=f"next_{req}_{key}_{off_set}"), InlineKeyboardButton(f"📃 Pages {round(int(offset)/10)+1} / {round(total/10)}", callback_data="pages")]
        )
    elif off_set is None:
        btn.append([InlineKeyboardButton(f"🗓 {round(int(offset)/10)+1} / {round(total/10)}", callback_data="pages"), InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("⏪ Geri", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"🗓 {round(int(offset)/10)+1} / {round(total/10)}", callback_data="pages"),
                InlineKeyboardButton("İleri ⏩", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    try:
        await query.edit_message_reply_markup( 
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!",show_alert=True)

    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Thats not for you!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "disconnect" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)

    if query.data.startswith("file"):
        ident, file_id = query.data.split("#")
        files = (await get_file_details(file_id))[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
            except Exception as e:
                    print(e)
            f_caption=f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"
            
        try:
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
                return
            else:
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption
                    )
                await query.answer('Check PM, I have sent files in pm',show_alert = True)
        except UserIsBlocked:
            await query.answer('Unblock the bot mahn !',show_alert = True)
        except PeerIdInvalid:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
        except Exception as e:
            await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")

    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files = (await get_file_details(file_id))[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
            except Exception as e:
                print(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{title}"
        await query.answer()
        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption
            )

    elif query.data == "pages":
        await query.answer()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('➕ Beni Grubuna Ekle ➕', url='http://t.me/anagrupbot?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Ara', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🤖 Güncelle', url='https://t.me/mmagneto')
            ],[
            InlineKeyboardButton('ℹ️ Yardım', callback_data='help'),
            InlineKeyboardButton('😊 Hakkında', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('Manuel Filtre', callback_data='manuelfilter'),
            InlineKeyboardButton('Otomotik Filtre', callback_data='autofilter')
            ],[
            InlineKeyboardButton('Bağlantı', callback_data='coct'),
            InlineKeyboardButton('Extra Mod', callback_data='extra')
            ],[
            InlineKeyboardButton('🏠 Ev', callback_data='start'),
            InlineKeyboardButton('🔮 Durum', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('🤖 Güncelleme', url='https://t.me/mmagneto'),
            InlineKeyboardButton('♥️ Kaynak', callback_data='source')
            ],[
            InlineKeyboardButton('🏠 Ev', callback_data='start'),
            InlineKeyboardButton('🔐 Kapat', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "Kaynak":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help'),
            InlineKeyboardButton('⏹️ Butonlar', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='manuelfilter')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help'),
            InlineKeyboardButton('👮‍♂️ Yönetici', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "Admin":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='extra')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help'),
            InlineKeyboardButton('♻️', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "rfrsh":
        await query.answer("Fetching MongoDb DataBase")
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Geri', callback_data='help'),
            InlineKeyboardButton('♻️', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
      )
    


async def auto_filter(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        files, offset, total_results = await get_search_results(search.lower(), offset=0)
        if files:
            for file in files:
                file_id = file.file_id
                btn.append(
                    [InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'files#{file_id}'), InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'files_#{file_id}')]
                    )
        if not btn:
            return

        if offset != "":
            key = f"{message.chat.id}-{message.message_id}"
            BUTTONS[key] = search
            req = message.from_user.id or 0
            btn.append(
                [InlineKeyboardButton(text=f"🗓 1/{round(int(total_results)/10)}",callback_data="pages"), InlineKeyboardButton(text="İleri ⏩",callback_data=f"next_{req}_{key}_{offset}")]
            )
        else:
            btn.append(
                [InlineKeyboardButton(text="🗓 1/1",callback_data="pages")]
            )
        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            await message.reply_photo(photo=imdb.get('poster'), caption=f"<b>Query: {search}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Başlık: <a href={imdb['url']}>{imdb.get('title')}</a>\n🎭 Tür: {imdb.get('genres')}\n📆 Yıl: <a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n🌟 Puan: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10", reply_markup=InlineKeyboardMarkup(btn))
        elif imdb:
            await message.reply_text(f"<b>Query: {search}</b> \n‌‌‌‌IMDb Bilgisi:\n\n🏷 Başlık: <a href={imdb['url']}>{imdb.get('title')}</a>\n🎭 Tür: {imdb.get('genres')}\n📆 Yıl: <a href={imdb['url']}/releaseinfo>{imdb.get('year')}</a>\n🌟 Puan: <a href={imdb['url']}/ratings>{imdb.get('rating')}</a> / 10", reply_markup=InlineKeyboardMarkup(btn))
        else:
            await message.reply_text(f"<b>İşte sorgunuz için veritabanımda bulduklarım {search} ‌‌‌‌‎ </b>", reply_markup=InlineKeyboardMarkup(btn))
        
