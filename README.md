# AWS-Serverless-Sentiment-Analysis-Pipeline
Proje, tamamiyle yönetilen (managed) servislerden oluşur ve hiçbir sunucu yönetimi gerektirmez.

İşleyiş Adımları:
1.Amazon S3: Giriş noktasıdır. Kullanıcı analiz edilecek .txt dosyasını yükler.

2.S3 Event Notifications: Dosya yüklendiği anda bir tetikleyici oluşturur.

3.AWS Lambda: Tetikleyiciyi yakalar, dosya içeriğini okur ve analiz sürecini yönetir.

4.Amazon Comprehend: Makine öğrenmesi (NLP) kullanarak metindeki duyguyu (Pozitif, Negatif, Nötr) belirler.

5.Amazon DynamoDB: Dosya adı, analiz sonucu ve zaman damgası gibi verileri kalıcı olarak saklar.
