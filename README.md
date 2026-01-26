# AWS-Serverless-Sentiment-Analysis-Pipeline
Proje, tamamiyle yönetilen (managed) servislerden oluşur ve hiçbir sunucu yönetimi gerektirmez.

İşleyiş Adımları:

Amazon S3: Giriş noktasıdır. Kullanıcı analiz edilecek .txt dosyasını yükler.

S3 Event Notifications: Dosya yüklendiği anda bir tetikleyici oluşturur.

AWS Lambda: Tetikleyiciyi yakalar, dosya içeriğini okur ve analiz sürecini yönetir.

Amazon Comprehend: Makine öğrenmesi (NLP) kullanarak metindeki duyguyu (Pozitif, Negatif, Nötr) belirler.

Amazon DynamoDB: Dosya adı, analiz sonucu ve zaman damgası gibi verileri kalıcı olarak saklar.
