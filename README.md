# WatchDog-ile-Calismak
WatchDog kütüphanesi kullanılarak bir uygulama geliştirildi

**🔨 Kurulum Adımları**
* Bilgisayarımızda python -m venv venv adında yeni bir sanal ortam oluşturmalısınız
* Ardından sanal ortamı venv\Scripts\activate diyerek aktif etmelisiniz
* Sonra da Kullanıdığınız mevcut IDE'da (VS Code or Pycharm) Select Interpeter diyerek Projemizde az önce oluşturduğumuz venv dosyasını seçmelisiniz
* Sonra da terminal ekranına pip install -r requirements.txt yazarak projemiz için gerekli paketleri kurmalısınız

**🚀 Projemiz Nasıl Çalışıyor**
* İlk olarak watchdog_education.py dosyasını çalıştırınız 
* Dosyayı çalıştırdıktan sonra observer ile sistemi izleyeceğiz 
* Dizine bir dosya kaydettiğiniz zaman on_created fonksiyonu çalışacaktır 
* Dizinden bir dosya sildiğiniz zaman on_deleted fonksiyonu çalışacaktır 
* Dizindeki bir dosyayı başka bir yere taşıdığınız zaman on_moved fonksiyonu çalışacaktır 
* Dizindeki bir dosyayı güncellediğiniz zaman on_modified fonksiyonu çalışacaktır 

**⚠️ Projemizdeki Diğer Önemli Husus** 
Bu proje geliştiricinin daha önce watchdog kütüphanesini kullandığını göstermek için yaratıldı

 
