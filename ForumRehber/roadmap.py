#!/usr/bin/env python3
"""
Watnea Türk Hack Team Roadmap Tool
Türk Hack Team Roadmap 
"""

import webbrowser
import time
import os
import sys


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
    """Ekranı temizle"""
    os.system('clear' if os.name == 'posix' else 'cls')

def typewriter(text, delay=0.03):
    """Daktilo efekti"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_banner():
    """Açılış banner'ını göster"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
██╗    ██╗ █████╗ ████████╗███╗   ██╗███████╗ █████╗ 
██║    ██║██╔══██╗╚══██╔══╝████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║███████║   ██║   ██╔██╗ ██║█████╗  ███████║
██║███╗██║██╔══██║   ██║   ██║╚██╗██║██╔══╝  ██╔══██║
╚███╔███╔╝██║  ██║   ██║   ██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Colors.END}
    """
    print(banner)
    print(f"{Colors.CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                        Türk Hack Team ROADMAP TOOL                                ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}║                    Developed by Watnea for THT Community                    ║{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
    print()

def create_roadmap_html():
    """Türk Hack Team roadmap HTML dosyasını oluştur"""
    html_content = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Watnea - Türk Hack Team Roadmap</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.9)), 
                        url('https://i.hizliresim.com/m367ii8.jpeg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: #ffffff;
            min-height: 100vh;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            padding: 60px 0;
            margin-bottom: 50px;
        }
        
        .hacker-text {
            font-size: 3.5rem;
            color: #00ff88;
            margin-bottom: 15px;
            font-weight: 700;
            text-shadow: 0 0 30px rgba(0, 255, 136, 0.5);
            letter-spacing: 2px;
        }
        
        .subtitle {
            font-size: 1.3rem;
            color: #cccccc;
            font-weight: 400;
        }
        
        .roadmap-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 25px;
            margin-bottom: 50px;
        }
        
        .category {
            background: rgba(20, 20, 30, 0.8);
            border-radius: 15px;
            padding: 0;
            transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            border: 1px solid rgba(0, 255, 136, 0.3);
            overflow: hidden;
            backdrop-filter: blur(10px);
            position: relative;
        }
        
        .category:hover {
            transform: translateY(-8px);
            border-color: rgba(0, 255, 136, 0.6);
            box-shadow: 0 15px 40px rgba(0, 255, 136, 0.3);
        }
        
        .category-header {
            padding: 25px;
            background: rgba(30, 30, 45, 0.9);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
        }
        
        .category-header:hover {
            background: rgba(40, 40, 60, 0.9);
        }
        
        .category-title {
            color: #00ff88;
            font-size: 1.4rem;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 600;
        }
        
        .toggle-icon {
            font-size: 1.2rem;
            transition: transform 0.3s ease;
            color: #00ff88;
        }
        
        .category-content {
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        
        .category-content.expanded {
            padding: 30px;
            max-height: 1000px;
        }
        
        .category-description {
            color: #b0b0b0;
            margin-bottom: 25px;
            font-size: 1.1rem;
            line-height: 1.7;
            font-weight: 400;
        }
        
        .resources {
            margin-top: 20px;
        }
        
        .resources-title {
            color: #00ff88;
            margin-bottom: 20px;
            font-size: 1.2rem;
            font-weight: 600;
            border-bottom: 2px solid rgba(0, 255, 136, 0.3);
            padding-bottom: 10px;
        }
        
        .resource-list {
            list-style: none;
        }
        
        .resource-list li {
            margin: 12px 0;
            padding: 15px 20px;
            background: rgba(30, 30, 45, 0.6);
            border-radius: 10px;
            border-left: 4px solid #00ff88;
            transition: all 0.3s ease;
        }
        
        .resource-list li:hover {
            background: rgba(40, 40, 60, 0.8);
            transform: translateX(8px);
            border-left-color: #66ffaa;
        }
        
        .resource-list a {
            color: #00ff88;
            text-decoration: none;
            font-weight: 500;
            display: block;
            font-size: 1rem;
        }
        
        .resource-list a:hover {
            color: #66ffaa;
        }
        
        .vulnerabilities-section {
            background: rgba(20, 20, 30, 0.8);
            border-radius: 15px;
            padding: 0;
            margin-top: 50px;
            border: 1px solid rgba(255, 0, 100, 0.3);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .vulnerabilities-section:hover {
            border-color: rgba(255, 0, 100, 0.6);
            box-shadow: 0 15px 40px rgba(255, 0, 100, 0.3);
        }
        
        .vuln-header {
            padding: 25px;
            background: rgba(30, 30, 45, 0.9);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.3s ease;
        }
        
        .vuln-header:hover {
            background: rgba(40, 40, 60, 0.9);
        }
        
        .vuln-title {
            color: #ff0064;
            font-size: 1.6rem;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 600;
        }
        
        .vuln-content {
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        
        .vuln-content.expanded {
            padding: 35px;
            max-height: 1000px;
        }
        
        .vuln-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }
        
        .vuln-item {
            background: rgba(30, 30, 45, 0.7);
            padding: 25px 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid rgba(255, 0, 100, 0.3);
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            display: block;
        }
        
        .vuln-item:hover {
            background: rgba(40, 40, 60, 0.9);
            transform: translateY(-5px);
            border-color: rgba(255, 0, 100, 0.6);
            box-shadow: 0 10px 25px rgba(255, 0, 100, 0.4);
        }
        
        .vuln-item h3 {
            color: #ffffff;
            font-size: 1.3rem;
            margin-bottom: 8px;
            font-weight: 600;
        }
        
        .vuln-item p {
            color: #b0b0b0;
            font-size: 0.95rem;
            font-weight: 400;
        }
        
        .footer {
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #888;
        }
        
        .footer p {
            margin: 8px 0;
            font-size: 1.1rem;
            font-weight: 400;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(20, 20, 30, 0.8);
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(0, 255, 136, 0.4);
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 255, 136, 0.6);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .hacker-text {
                font-size: 2.5rem;
            }
            
            .roadmap-container {
                grid-template-columns: 1fr;
            }
            
            .vuln-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .container {
                padding: 15px;
            }
        }
        
        @media (max-width: 480px) {
            .vuln-grid {
                grid-template-columns: 1fr;
            }
            
            .hacker-text {
                font-size: 2rem;
            }
            
            .category-header, .vuln-header {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="hacker-text">Türk Hack Team ROADMAP</h1>
            <p class="subtitle">Watnea tarafından TürkHackTeam topluluğu için hazırlanmıştır</p>
        </div>
        
        <div class="roadmap-container">
            <!-- AĞ -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('network')">
                    <h2 class="category-title">🌐 Network</h2>
                    <span class="toggle-icon" id="network-icon">▼</span>
                </div>
                <div class="category-content" id="network-content">
                    <p class="category-description">Temel ağ protokolleri, TCP/IP modeli, ağ güvenliği, trafik analizi ve network pentesting temelleri</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.turkhackteam.org/konular/http-anatomisi-status-codelari-ne-demek-istiyor-detayli.2076716/" target="_blank">THT - HTTP Anatomisi</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/http-hata-kodlari-ve-anlamlari.1910224/" target="_blank">THT - HTTP Hata Kodları</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/blue-team-stratejisi-bootcamp-bolum-3-network-dedigin-sinyaldir.2061477/" target="_blank">THT - OSİ MODELİ</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/routing-protokolleri-ve-network-topolojisi-1.2061848/" target="_blank">Routing Protokolleri</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/basic-network-bilgisi-2.2059556/" target="_blank">TCP/IP Modeli</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Linux Bash -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('linux')">
                    <h2 class="category-title">🐧 Linux & Bash</h2>
                    <span class="toggle-icon" id="linux-icon">▼</span>
                </div>
                <div class="category-content" id="linux-content">
                    <p class="category-description">Linux komut satırı, bash scripting, sistem yönetimi, process management ve otomasyon</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.turkhackteam.org/konular/linux-shell-script-yazma-egitimi-temel-bilgiler-ve-baslangic-1.2020406/" target="_blank">THT - Linux Shell Script Yazma</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/linux-shell-script-yazma-egitimi-kodlamaya-devam-ve-uygulamalar-2.2020719/" target="_blank">THT - Linux Shell Script Yazma</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- JavaScript -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('javascript')">
                    <h2 class="category-title">⚡ JavaScript</h2>
                    <span class="toggle-icon" id="javascript-icon">▼</span>
                </div>
                <div class="category-content" id="javascript-content">
                    <p class="category-description">Temel JavaScript, ES6+, DOM manipülasyonu, async programming ve web uygulama güvenliği</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.turkhackteam.org/konular/sifirdan-ileriye-javascript-serisi.2065960/" target="_blank">THT - JS SIFIRDAN MAKALE SERİSİ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- PHP -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('php')">
                    <h2 class="category-title">🐘 İleri PHP</h2>
                    <span class="toggle-icon" id="php-icon">▼</span>
                </div>
                <div class="category-content" id="php-content">
                    <p class="category-description">PHP güvenliği, OOP, design patterns, framework'ler, backend geliştirme ve API'ler</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.turkhackteam.org/konular/php-dersleri-1.2020866/" target="_blank">THT - PHP Dersleri #1</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/php-dersleri-2.2021847/" target="_blank">THT - PHP Dersleri #2</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/php-ile-web-uygulama-gelistirme-temel-rehber.2061924/" target="_blank">THT - PHP ile Web</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Python -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('python')">
                    <h2 class="category-title">🐍 Temel Python</h2>
                    <span class="toggle-icon" id="python-icon">▼</span>
                </div>
                <div class="category-content" id="python-content">
                    <p class="category-description">Python programlama, otomasyon, tool geliştirme, güvenlik script'leri ve framework'ler</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.turkhackteam.org/konular/sifirdan-ileri-seviye-python-temeller-1.2076379/" target="_blank">THT - Python Temeller</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/sifirdan-ileri-seviye-python-kosullu-ifader-donguler-2.2076465/" target="_blank">Koşullu İfader & Döngüler</a></li>
                            <li><a href="https://docs.python.org/3/tutorial/" target="_blank">Python Official Tutorial</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Kaynak -->
            <div class="category">
                <div class="category-header" onclick="toggleCategory('sql')">
                    <h2 class="category-title">🗃️ Kaynak Önerisi </h2>
                    <span class="toggle-icon" id="sql-icon">▼</span>
                </div>
                <div class="category-content" id="sql-content">
                    <p class="category-description">Ekstra Kaynak Önerileri</p>
                    <div class="resources">
                        <h3 class="resources-title">Kaynaklar:</h3>
                        <ul class="resource-list">
                            <li><a href="https://www.youtube.com/@ryan_phdsec/videos" target="_blank">Ryan John</a></li>
                            <li><a href="https://book.hacktricks.wiki/en/index.html" target="_blank">Hacktricks</a></li>
                            <li><a href="https://portswigger.net/web-security" target="_blank">Portswigger</a></li>
                            <li><a href="https://www.turkhackteam.org/konular/tht-cyber-star-hacking-hacker-egitim-seti-turkiyede-ilk-ucretsiz.1960243/" target="_blank">ÜCRETSİZ EĞİTİM - HİÇ SAĞ SOLA BAKMA</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Web Zafiyetleri -->
        <div class="vulnerabilities-section">
            <div class="vuln-header" onclick="toggleCategory('vulnerabilities')">
                <h2 class="vuln-title">🔓 WEB ZAFİYETLERİ</h2>
                <span class="toggle-icon" id="vulnerabilities-icon">▼</span>
            </div>
            <div class="vuln-content" id="vulnerabilities-content">
                <p class="category-description">Modern web uygulamalarında karşılaşılan temel güvenlik zafiyetleri ve korunma yöntemleri</p>
                
                <div class="vuln-grid">
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-xss.2038468/" target="_blank" class="vuln-item">
                        <h3>XSS</h3>
                        <p>Cross-Site Scripting</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/temel-olarak-xss-2.1964145/" target="_blank" class="vuln-item">
                        <h3>XSS Temel</h3>
                        <p>Cross-Site Scripting</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-sql-injection.2038449/" target="_blank" class="vuln-item">
                        <h3>SQL Injection</h3>
                        <p>Veritabanı saldırıları</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-command-injection.2038421/" target="_blank" class="vuln-item">
                        <h3>Command Injection</h3>
                        <p>Sistem komut enjeksiyonu</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-idor.2038475/" target="_blank" class="vuln-item">
                        <h3>IDOR</h3>
                        <p>Insecure Direct Object Reference</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-html-injection.2038453/" target="_blank" class="vuln-item">
                        <h3>HTML Injection</h3>
                        <p>HTML enjeksiyon saldırıları</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/ssrf-nedir.2075671/" target="_blank" class="vuln-item">
                        <h3>SSRF</h3>
                        <p>Server-Side Request Forgery</p>
                    </a>
                    <a href="https://www.turkhackteam.org/konular/web-hacking-101-serisi-csrf-final.2038481/" target="_blank" class="vuln-item">
                        <h3>CSRF</h3>
                        <p>Cross-Site Request Forgery</p>
                    </a>
                    <a href="hhttps://www.turkhackteam.org/konular/site-hackleme-rehberi-4.1989338/" target="_blank" class="vuln-item">
                        <h3>RCE</h3>
                    </a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>2025 Watnea - TürkHackTeam Topluluğu</p>
            <p>https://www.turkhackteam.org/uye/watnea.1011624/</p>
        </div>
    </div>

    <script>
        function toggleCategory(categoryId) {
            const content = document.getElementById(categoryId + '-content');
            const icon = document.getElementById(categoryId + '-icon');
            
            if (content.classList.contains('expanded')) {
                content.classList.remove('expanded');
                icon.style.transform = 'rotate(0deg)';
            } else {
                content.classList.add('expanded');
                icon.style.transform = 'rotate(180deg)';
            }
        }
        
        // Sayfa yüklendiğinde ilk kategoriyi açık göster
        document.addEventListener('DOMContentLoaded', function() {
            toggleCategory('network');
        });
    </script>
</body>
</html>
    """
    
    with open("tht_roadmap.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return os.path.abspath("tht_roadmap.html")

def main():
    """Ana program"""
    clear_screen()
    show_banner()
    
    # Yönlendirmeler
    print(f"{Colors.GREEN}Yönlendirme yapılıyor: @watnea{Colors.END}")
    time.sleep(2)
    
    # Web
    print(f"{Colors.YELLOW}TürkHackTeam Roadmap web sitesi oluşturuluyor...{Colors.END}")
    html_file = create_roadmap_html()
    
    print(f"{Colors.GREEN}Web sitesi açılıyor...{Colors.END}")
    time.sleep(1)
    

    webbrowser.open(f'file://{html_file}')
    
    print(f"\n{Colors.CYAN}TürkHackTeam Roadmap başarıyla oluşturuldu ve tarayıcıda açıldı!{Colors.END}")
    print(f"{Colors.WHITE}Dosya konumu: {html_file}{Colors.END}")
    print(f"\n{Colors.YELLOW}Çıkmak için Enter tuşuna basın...{Colors.END}")
    input()

if __name__ == "__main__":
    main()
