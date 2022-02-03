import os
import logging
import random
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp

logger = logging.getLogger(__name__)

@Client.on_message(filters.command("start"))
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons =[
            [
                InlineKeyboardButton('Ara 🔍', switch_inline_query_current_chat=''),
                InlineKeyboardButton('Bot Nasıl Kullanılır?', url='https://t.me/anagrupp/7402')
            ],
            [
                InlineKeyboardButton('Bot Destek', url=f"https://t.me/mmagneto"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
            protect_content=True
        )
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id, message.from_user.first_name)
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "Grubuma katıl!", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton(" 🔄 Tekrar Dene", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**Lütfen Grubuma Katıl Botu Kullanabilmek İçin**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if message.command[1] in ["subscribe", "error", "okay"]:
        return
    file_id = message.command[1]
    print(file_id)
    files = (await get_file_details(file_id))[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=get_size(size), file_caption=f_caption)
        except Exception as e:
            print(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


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

The Report (2019) Altyazılı @anagrupbot.mp4""")
                    

@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Işleniyor...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('Desteklenmeyen Mesaj Tipi')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('Dosya Başarı ile Veritabanından Silindi.')
    else:
        await msg.edit('Veri tabanında dosya bulunamadı')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'Bu tüm kayıtlı dosyaları silecek.\nDevam etmek istiyor musun??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Tüm Kayıtlı Dosyalar Başarı ile silindi.')

@Client.on_message(filters.command('about'))
async def delete(bot, message):
    """Yardım Mesajı"""
