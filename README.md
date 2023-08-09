# DjangoBlogProject UPOD Projesi
Proje Amacı: Kullanıcının kendi postlarını görebildiği, 
yeni post ekleyebildiği, 
var olan postlarını güncelleyebildiği/silebildiği 
bir web uygulamasını Django(Python) ile yazınız.

Postlar başlık, 
açıklama ve resim alanlarına sahiptir. 
Başlık ve açıklama alanlarının olması zorunludur. 
Resim eklenebilmesi artı puan getirecek ve yapılmadığında puan kırılmayacak bir görevdir.

Adım 1: Proje amacını gerçekleştirecek olan web uygulamasının veri tabanı işlemlerini(CRUD) yapınız. 
Admin panel kullanarak postlara bakılabilmeli, 
eklenebilmeli ve güncellenebilmelidir. 
(shell kullanarak da yapılabilir)

Adım 2: Postlarda silme işlemi, 
veri tabanından kalıcı bir silme şeklinde yapılmasın. 
Her post is_deleted isimli bir alana sahip olsun. 
Silinen postların is_deleted alanı True yapılsın. 
Ve silinenler gösterilmesin.

Adım 3: Kullanıcının login ve register olabildiği arayüzü yapınız. 
Kullanıcı yalnız kendi postlarını görsün ve güncellesin. 
Son kullanıcılar tüm postlari görebilir ama duzenleyemez. 
Eğer login olduysa kendi postlarini duzenleyebilir.


Projeyi indirdikten sonra çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Terminali açın ve proje dizinine (projenizin manage.py dosyasının bulunduğu dizine) gidin:

`cd /path/to/your/project`

Sanal ortamınızı etkinleştirin (eğer etkinleştirmediyseniz):

`source venv/bin/activate`

Projenizi çalıştırın:

`python manage.py runserver`

Bu komut, sunucuyu başlatacaktır. Sunucu başladığında, terminalde bir çıktı görünecektir. 
Genellikle http://127.0.0.1:8000/ veya http://localhost:8000/ adresine giderek projenizin çalıştığını görebilirsiniz.

Tarayıcınızı açın ve projenizi belirtilen adreste görüntüleyin.



