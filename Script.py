class script(object):
    START_TXT = """Merhaba {},
Ben <a href='https://t.me/Anagrupbot'>Ana Grup Bot</a>, İnline Modda (Satır içi) çalışıyorum ve size film sağlamaya çalışıyorum. 
Eğer senin de bota eklenmesini istediğin film veya dizi önerin varsa <a href='https://t.me/Anagrupp'>İstek Ve Sohbet</a> Grubuna Beklerim."""
    HELP_TXT = """Merhaba {}
İşte Komutlarım İçin Yardım ."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: Quickwaste Film Botu
✯ Yaratıcı: ali
✯ Kütüphane: Pyrogram
✯ Dil: Python 3
✯ Veri Tabanı: Mongo db
✯ Bot 𝚂unucusu: Heroku
✯ Yapı Durumu: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria açık kaynaklı bir projedir. 
- Source - https://t.me/mmagneto

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOT:</b>
1. Eva Maria'nın yönetici privillage'ı olmalı.
2. Bir sohbete yalnızca yöneticiler filtre ekleyebilir.
3. Uyarı düğmelerinin sınırı 64 karakterdir. 

<b>Komutlar Ve Kullanım:</b>
• /filter - <code>Sohbet için bir filtre ekle</code>
• /filters - <code>Tüm Filtrelerin listesi</code>
• /del - <code>sohbette belirli bir filtreyi silme</code>
• /delall - <code>sohbetteki tüm filtreleri silme (Sohbet Kurucusu Sadece)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Quickwaste Film Botu Hem URL hem de uyarı satır içi düğmelerini destekler .

<b>NOT:</b>
1. Telegram herhangi bir içerik olmadan düğme göndermenize izin vermez, bu nedenle içerik zorunludur.
2. Quickwaste Film Botu, herhangi bir telegram medya türüne sahip düğmeleri destekler.
3. Düğmeler markdown biçimi olarak düzgün bir şekilde ayrıştırılmalıdır

<b>URL butonları:</b>
<code>[Button Text](buttonurl:https//t.me/QuickwasteBot)</code>

<b>Uyarı Butonları:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Yardım: <b>Auto Filter</b>

<b>NOT:</b>
1. Özelse beni kanalınızın yöneticisi yap.
2. Kanalınızın kam rip, porno ve sahte dosyalar içermediğinden emin olun.
3. Son mesajı bana alıntılarla iletin.
 O kanaldaki tüm dosyaları veritabanıma ekleyeceğim. ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Filtreleri yönetmek için botu PM'ye bağlamak için kullanılır 
- gruplar halinde spam'leri önlemeye yardımcı olur. 

<b>NOT:</b>
1. Yalnızca yöneticiler bağlantı ekleyebilir .
2. Send <code>/connect</code> for connecting me to ur PM

<b>Komutlar Ve Kullanım:</b>
• /connect  - <code>belirli bir sohbeti özel sohbetinize bağlama</code>
• /disconnect  - <code>sohbetten Bağlantıyı Kopartma</code>
• /connections - <code>Tüm Bağlantılarının Listesi</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOT:</b>
bunlar TESSA'nın ekstra özellikleridir

<b>Commands and Usage:</b>
• /id - <code>Belirli Bir kullanıcının İd sini getirir.</code>
• /info  - <code>Kulanıcıların Bilgisini Getirir.</code>
• /imdb  - <code>İmdb Kaynağından Film Bilgisi getirir.</code>
• /search  - <code>film bilgilerini çeşitli kaynaklardan almak.</code>"""
    ADMIN_TXT = """Help: <b>Admin modu0</b>

<b>NOT:</b>
Bu modül yalnızca yöneticim için çalışır. 

<b>Commands and Usage:</b>
• /logs - <code>rescent hatalarını almak için</code>
• /stats - <code>DB'deki dosyaların durumunu almak için.</code>
• /users - <code>kullanıcılarımın ve kimliklerimin listesini almak için.</code>
• /chats - <code>sohbetlerimin ve kimliklerimin listesini almak için</code>
• /leave  - <code>sohbetten ayrılmak için.</code>
• /disable  -  <code>sohbeti devre dışı bırakma.</code>
• /ban  - <code>kullanıcıyı yasaklamak için.</code>
• /unban  - <code>Kullanıcının Banını Açma.</code>
• /channnel - <code>toplam bağlı kanalların listesini almak için</code>
• /broadcast - <code>tüm TSSA kullanıcılarına mesaj yayınlamak için</code>"""
    STATUS_TXT = """★ Toplam Dosya: <code>{}</code>
★ Toplam Kullanıcı: <code>{}</code>
★ 𝚃𝙾plam Sohbetler: <code>{}</code>
★ Kullanılan Depolama: <code>{}</code> 𝙼𝚒𝙱
★ Boş Depolama: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Grup = {}(<code>{}</code>)
Toplam Üyeler = <code>{}</code>
Eklendi tarafından - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
ADI - {}
"""
