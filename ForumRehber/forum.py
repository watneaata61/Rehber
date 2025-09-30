"""
Siber Güvenlik Forum Rehberi
YEL tarafından geliştirilmiştir
"""

import os
import time
import sys

# Renkler
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def typewriter_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_header():
    header = f"""
{Colors.RED}{Colors.BOLD}
████████╗██╗  ██╗████████╗
╚══██╔══╝██║  ██║╚══██╔══╝
   ██║   ███████║   ██║   
   ██║   ██╔══██║   ██║   
   ██║   ██║  ██║   ██║   
   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
{Colors.END}
    """
    print(header)
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                        HOŞGELDİNİZ! FORUM REHBERİNE                          ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                        Watnea tarafından geliştirilmiştir                        ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()

def print_menu():
    print(f"{Colors.YELLOW}{Colors.BOLD}Kullanılabilir Komutlar:{Colors.END}")
    print(f"  {Colors.GREEN}-yardım{Colors.END}       : Tüm komutları ve amacı göster")
    print(f"  {Colors.GREEN}-onur{Colors.END}        : Onur listesindeki isimleri göster")
    print(f"  {Colors.GREEN}-redteam{Colors.END}     : Red Team hakkında bilgi")
    print(f"  {Colors.GREEN}-blueteam{Colors.END}    : Blue Team hakkında bilgi")
    print(f"  {Colors.GREEN}-moderasyon{Colors.END}  : Moderasyon Ekibi hakkında bilgi")
    print(f"  {Colors.GREEN}-arge{Colors.END}        : Ar-Ge Ekibi hakkında bilgi")
    print(f"  {Colors.GREEN}-medya{Colors.END}       : Medya&Tasarım Ekibi hakkında bilgi")
    print(f"  {Colors.GREEN}-roadmap{Colors.END}     : Siber güvenlik ve web alanında roadmap")
    print(f"  {Colors.GREEN}-çıkış{Colors.END}       : Programdan çık")
    print()

def print_help():
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                                YARDIM MENÜSÜ                                 ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}Bu araç, forumumuzdaki aktif ekipleri, onur listesindeki isimleri ve siber güvenlik")
    print(f"alanında gelişim için roadmap'i kolayca öğrenmenizi sağlar.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Amaç:{Colors.END}")
    print(f"  - Forum yapısını ve ekipleri tanıtmak")
    print(f"  - Siber güvenlik alanında yol haritası sunmak")
    print(f"  - Forumun aktif üyelerini ve ekipleri tanıtmak")
    print()
    print_menu()

def print_honor_list():
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                                ONUR LİSTESİ                                  ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    
    honor_members = [
        "1- ZoRRoKiN",
        "2- Arsenik",
        "3- Veteran 7",
        "4- Mirliva",
        "5- Maveraün Nehr",
        "6- GECEGEZEN",
        "7- META",
        "8- borekaenxd97",
        "9- Baysal",
        "10- 'drose",
        "11- ArchieN",
    ]
    
    for member in honor_members:
        print(f"  {Colors.GREEN}★{Colors.END} {Colors.YELLOW}{member}{Colors.END}")
        time.sleep(0.2)
    
    print()
    print(f"{Colors.WHITE}Bu isimler forumumuza değerli katkılarda bulunmuş ve kendilerini kanıtlamış üyelerimizdir.{Colors.END}")
    print()

def print_redteam_info():
    print(f"{Colors.RED}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}║                                ANKA RED TEAM                                 ║{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}ANKA Red Team; forumumuzun ana dalı olan hacking&siber güvenlik alanında misyonumuza")
    print(f"bağlı olarak ilgili faaliyetleri sürdürür. Adı gibi küllerinden yeniden doğan bir ekiptir.")
    print(f"Bugüne kadar çeşitli sebeplerle dağılan ve tekrar toparlanan bu tim, yeni başvuruların")
    print(f"değerlendirilmesi ile beraber yeni çizgisini belirleyecektir.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Görevleri:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} Penetrasyon testleri")
    print(f"  {Colors.GREEN}•{Colors.END} Zafiyet analizleri")
    print(f"  {Colors.GREEN}•{Colors.END} Güvenlik araştırmaları")
    print(f"  {Colors.GREEN}•{Colors.END} CTF yarışmalarına katılım")
    print()

def print_blueteam_info():
    print(f"{Colors.BLUE}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}║                                  BLUE TEAM                                   ║{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}Blue Team; sistemlerin ve ağların güvenliğini sağlamak, olası saldırıları tespit")
    print(f"etmek ve önlemek için çalışan savunma odaklı ekiptir. Red Team'in saldırılarına karşı")
    print(f"savunma stratejileri geliştirir ve sistemlerin güvenliğini artırmak için çalışır.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Görevleri:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} SIEM yönetimi")
    print(f"  {Colors.GREEN}•{Colors.END} Log analizi")
    print(f"  {Colors.GREEN}•{Colors.END} Güvenlik duvarı yönetimi")
    print(f"  {Colors.GREEN}•{Colors.END} Olay müdahale")
    print()

def print_moderation_info():
    print(f"{Colors.PURPLE}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.PURPLE}{Colors.BOLD}║                             MODERASYON EKİBİ                               ║{Colors.END}")
    print(f"{Colors.PURPLE}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}Moderasyon Ekibi; forumun temel düzenini sağlayan, forum/kategori kurallarına")
    print(f"aykırı konu/mesaj/profil mesajı.vb gibi içerikleri tespit ederek müdahale eden ekiptir.")
    print(f"Ayrıca forumun kategorilerini sürekli güncel tutmak ve canlandırmak için yeni konular açar.")
    print(f"Forumumuzun can damarı Yardım Merkezi'mizde üyelerimize elinden geldiğince yardımcı olur.")
    print(f"Forumumuza ait kategori/kategorilerde temel bilgi birikimine sahip herkes bu görevi")
    print(f"rahatlıkla yapabilir.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Görevleri:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} Forum kurallarının uygulanması")
    print(f"  {Colors.GREEN}•{Colors.END} İçerik moderasyonu")
    print(f"  {Colors.GREEN}•{Colors.END} Kullanıcı yardımı")
    print(f"  {Colors.GREEN}•{Colors.END} Forum aktivitesinin artırılması")
    print()

def print_arge_info():
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                                AR-GE EKİBİ                                  ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}Forumun yazılım ekibidir. Bir yandan kişisel projelerini diğer yandan ise forum")
    print(f"için çeşitli uygulamalar üretmektedirler. Bu ekibe giriş için, en az bir yazılım dilinde")
    print(f"uzmanlaşmış olmak, bilgiye ve araştırmaya açık olmanız gerekmektedir.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Görevleri:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} Forum yazılımı geliştirme")
    print(f"  {Colors.GREEN}•{Colors.END} Özel araçlar geliştirme")
    print(f"  {Colors.GREEN}•{Colors.END} Otomasyon scriptleri yazma")
    print(f"  {Colors.GREEN}•{Colors.END} Teknoloji araştırmaları")
    print()

def print_media_info():
    print(f"{Colors.YELLOW}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║                           MEDYA&TASARIM EKİBİ                             ║{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    print(f"{Colors.WHITE}Medya&Tasarım Ekibi; forumumuza ait sosyal medya hesapların kontrolü ile sosyal")
    print(f"medya hesaplarında paylaşılacak içeriklerin üretimini yapan ayrıca forumumuzda bulunan")
    print(f"Sosyal Medya Kategorisi'nin düzenini sağlayan yöneticilerimizin bulunduğu ekiptir.")
    print(f"Tasarım Alanında görev alacak hem kendini hem de forumumuzu geliştirecek Grafiker")
    print(f"olarak görevlendirilecek ekip arkadaşları aramaktayız.{Colors.END}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}Görevleri:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} Sosyal medya yönetimi")
    print(f"  {Colors.GREEN}•{Colors.END} Grafik tasarım")
    print(f"  {Colors.GREEN}•{Colors.END} İçerik üretimi")
    print(f"  {Colors.GREEN}•{Colors.END} Marka bilinirliğini artırma")
    print()

def print_roadmap():
    print(f"{Colors.GREEN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}║                                 ROADMAP                                     ║{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                           SİBER GÜVENLİK YOL HARİTASI                        ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    
    cybersecurity_steps = [
        f"{Colors.YELLOW}1. TEMEL BİLGİLER:{Colors.END}",
        "   • Ağ temelleri (TCP/IP, OSI modeli)",
        "   • İşletim sistemleri (Linux, Windows)",
        "   • Programlama temelleri (Python, Bash)",
        "",
        f"{Colors.YELLOW}2. SİBER GÜVENLİK TEMELLERİ:{Colors.END}",
        "   • Güvenlik kavramları (CIA üçlüsü)",
        "   • Tehdit modelleri ve saldırı vektörleri",
        "   • Temel kriptografi",
        "",
        f"{Colors.YELLOW}3. AĞ GÜVENLİĞİ:{Colors.END}",
        "   • Ağ protokolleri ve zafiyetleri",
        "   • Güvenlik duvarları ve IDS/IPS",
        "   • VPN ve ağ izolasyonu",
        "",
        f"{Colors.YELLOW}4. UYGULAMA GÜVENLİĞİ:{Colors.END}",
        "   • Web uygulama güvenliği (OWASP Top 10)",
        "   • Mobil uygulama güvenliği",
        "   • API güvenliği",
        "",
        f"{Colors.YELLOW}5. PENETRASYON TESTİ:{Colors.END}",
        "   • Keşif ve bilgi toplama",
        "   • Zafiyet tarama ve analiz",
        "   • Exploit geliştirme",
        "   • Post-exploitation",
        "",
        f"{Colors.YELLOW}6. DEFANSİF GÜVENLİK:{Colors.END}",
        "   • SIEM kullanımı",
        "   • Log analizi",
        "   • Olay müdahale",
        "   • Forensic analiz",
    ]
    
    for step in cybersecurity_steps:
        print(f"   {step}")
        time.sleep(0.05)
    
    print()
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                              WEB GELİŞTİRME YOL HARİTASI                     ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()
    
    webdev_steps = [
        f"{Colors.YELLOW}1. TEMEL TEKNOLOJİLER:{Colors.END}",
        "   • HTML5 (Semantik yapı, formlar)",
        "   • CSS3 (Flexbox, Grid, Animasyonlar)",
        "   • JavaScript (ES6+, DOM manipülasyonu)",
        "",
        f"{Colors.YELLOW}2. FRONTEND GELİŞTİRME:{Colors.END}",
        "   • React.js / Vue.js / Angular",
        "   • State yönetimi (Redux, Vuex)",
        "   • Modern CSS framework'leri",
        "",
        f"{Colors.YELLOW}3. BACKEND GELİŞTİRME:{Colors.END}",
        "   • Node.js / Python (Django/Flask) / PHP",
        "   • RESTful API geliştirme",
        "   • Veritabanları (SQL, NoSQL)",
        "",
        f"{Colors.YELLOW}4. VERİTABANI:{Colors.END}",
        "   • MySQL / PostgreSQL",
        "   • MongoDB / Redis",
        "   • ORM kullanımı",
        "",
        f"{Colors.YELLOW}5. DEVOPS & DEPLOYMENT:{Colors.END}",
        "   • Git ve GitHub",
        "   • Docker ve containerization",
        "   • CI/CD pipeline'ları",
        "   • Cloud servisleri (AWS, Azure, GCP)",
        "",
        f"{Colors.YELLOW}6. GÜVENLİK:{Colors.END}",
        "   • Authentication & Authorization",
        "   • Input validation ve sanitization",
        "   • HTTPS ve SSL/TLS",
        "   • Güvenlik başlıkları (CSP, HSTS)",
    ]
    
    for step in webdev_steps:
        print(f"   {step}")
        time.sleep(0.05)
    
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}ÖNERİLEN KAYNAKLAR:{Colors.END}")
    print(f"  {Colors.GREEN}•{Colors.END} Siber Güvenlik: https://www.turkhackteam.org/forumlar/siber-guvenlik.538/")
    print(f"  {Colors.GREEN}•{Colors.END} Web & Server Güvenliği: https://www.turkhackteam.org/forumlar/web-server-guvenligi-ve-zafiyetler.13/")
    print(f"  {Colors.GREEN}•{Colors.END} Blue Team Hizmet #Hacking'in Mavi Tarafı: https://www.turkhackteam.org/konular/hackingin-mavi-tarafi-ucretsiz-327-sayfa-egitim-kitabi.1996702/")
    print(f"  {Colors.GREEN}•{Colors.END} BLue Team Hizmet #Siber Güvelik Saldır: https://www.turkhackteam.org/konular/blue-team-siber-guvelik-saldiri-savunma-kitabi.2048375/")
    print(f"  {Colors.GREEN}•{Colors.END} Red Team Hizmet #Hacking Eğitimi TR'de İlk: https://www.turkhackteam.org/konular/tht-cyber-star-hacking-hacker-egitim-seti-turkiyede-ilk-ucretsiz.1960243/page-18")
    print(f"  {Colors.GREEN}•{Colors.END} Red Team Hizmet #Web Hacking Serisi: https://www.turkhackteam.org/konular/site-hackleme-rehberi-1.1987722/")
    print(f"  {Colors.GREEN}•{Colors.END} Tüm detayları ile Anonim Olmak: https://www.turkhackteam.org/konular/tum-detaylari-ile-internette-anonim-kalmak.1977297/")
    print()

def main():
    clear_screen()
    
    # Açılış KIsmı
    print(f"{Colors.RED}{Colors.BOLD}Sistem başlatılıyor...{Colors.END}")
    time.sleep(1)
    
    for i in range(3):
        progress_bar = "=" * (i + 1) + " " * (2 - i)
        print(f"{Colors.YELLOW}[{progress_bar}] %{((i+1)*33)}{Colors.END}")
        time.sleep(0.5)
    
    clear_screen()
    print_header()
    
    
    welcome_msg = f"{Colors.GREEN}Merhaba değerli türkhackteam üyeleri. Yardım için '-yardım' yazabilirsiniz.{Colors.END}"
    typewriter_effect(welcome_msg)
    print()
    
    
    while True:
        try:
            command = input(f"{Colors.BLUE}{Colors.BOLD}forum@rehber~$ {Colors.END}").strip().lower()
            
            if command == '-yardım' or command == '-help':
                print_help()
            elif command == '-onur':
                print_honor_list()
            elif command == '-redteam':
                print_redteam_info()
            elif command == '-blueteam':
                print_blueteam_info()
            elif command == '-moderasyon':
                print_moderation_info()
            elif command == '-arge':
                print_arge_info()
            elif command == '-medya':
                print_media_info()
            elif command == '-roadmap':
                print_roadmap()
            elif command == '-çıkış' or command == '-exit':
                print(f"{Colors.GREEN}Görüşmek üzere! İyi günler.{Colors.END}")
                break
            elif command == '':
                continue
            else:
                print(f"{Colors.RED}Geçersiz komut: '{command}'. Yardım için '-yardım' yazın.{Colors.END}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.GREEN}Görüşmek üzere! İyi günler.{Colors.END}")
            break

if __name__ == "__main__":
    main()