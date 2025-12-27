Kendi yaptığın terminalde kullanabileceğin en temel ve en işlevsel komutları kategorilerine göre aşağıda listeledim. Bunlar hem cmd hem de powershell altyapısında genellikle sorunsuz çalışır:

1. Dosya ve Klasör Yönetimi (Navigasyon)
Bu komutlar, bilgisayarın içinde gezmeni ve dosyaları yönetmeni sağlar.

ls veya dir: Bulunduğun klasördeki her şeyi listeler.

cd <klasör_adı>: Belirlediğin klasörün içine girer (Örn: cd Desktop).

cd ..: Bir üst klasöre geri çıkar.

pwd: Şu an tam olarak hangi klasörde olduğunu gösterir.

mkdir <isim>: Yeni bir klasör oluşturur.

rmdir <isim>: Boş bir klasörü siler.

del <dosya_adı>: Bir dosyayı siler.

2. Sistem Bilgisi ve Durumu
Bilgisayarın donanımı ve çalışan uygulamalar hakkında bilgi verir.

whoami: O an hangi kullanıcı oturumuyla çalıştığını gösterir.

hostname: Bilgisayarın ağdaki adını söyler.

systeminfo: İşlemci, RAM ve Windows sürümü gibi tüm detayları döker.

tasklist: Şu an arkada çalışan tüm programları listeler.

taskkill /IM <program.exe> /F: İstediğin bir programı zorla kapatır.

3. Ağ ve İnternet Komutları
Bağlantı sorunlarını çözmek veya IP öğrenmek için kullanılır.

ipconfig: Yerel IP adresini ve internet kartı bilgilerini gösterir.

ping <site_adı>: Bir siteye paket gönderir, internetin hızını ve kopup kopmadığını test eder (Örn: ping google.com).

getmac: Bilgisayarının fiziksel (MAC) adresini gösterir.

netstat: Bilgisayarının hangi adreslerle iletişim kurduğunu listeler.

4. Terminali Yönetme Komutları
Yaptığın programın ekranını veya sürecini yönetmek için:

cls: Terminal ekranındaki tüm yazıları temizler (Tertemiz bir sayfa açar).

exit: Terminal oturumunu kapatır.

help: Windows'un standart komutları hakkında kısa bir yardım listesi açar.

echo <mesaj>: Ekrana yazdığın mesajı geri basar.

5. Bonus: Renkli ve Havalı Komutlar (Sadece PowerShell)
Programın arka planında PowerShell olduğu için şunları da deneyebilirsin:

Write-Host "Selam" -ForegroundColor Cyan: Ekrana turkuaz renkli yazı yazar.

Get-Service: Bilgisayardaki tüm servislerin (çalışıyor/durdu) listesini verir.

Get-Process | Sort-Object CPU -Descending | Select-Object -First 5: İşlemciyi en çok yoran ilk 5 programı gösterir.