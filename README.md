
# Ağ Taraması ve ICMP Ping  Scriptleri

 Scapy kütüphanesini kullanarak ağ üzerindeki cihazları keşfetmek için iki farklı Python betiği içerir. 

1. **ARP Taraması**: Belirli bir IP aralığındaki cihazları ARP protokolü ile bulur.
2. **ICMP Ping Taraması**: Belirli bir alt ağdaki cihazların aktif olup olmadığını ICMP ping taraması ile kontrol eder.

## Gereksinimler

- Python 3.x
- Scapy kütüphanesi

Scapy kütüphanesini yüklemek için:

```bash
pip install scapy
```

## ARP Taraması 

### Açıklama

 yerel ağınızdaki cihazları bulmak için ARP (Address Resolution Protocol) kullanır. Hedef IP aralığındaki cihazlara ARP istekleri gönderir ve cevap veren cihazların MAC ve IP adreslerini ekrana yazdırır.

### Kullanım

çalıştırmak için:

1. `arp_scan.py` dosyasını çalıştırın.
2. Terminalde aşağıdaki komutu girin:

```bash
python arp_scan.py
```

### Sonuç

Bu işlem sonucunda, hedef IP aralığındaki cihazların MAC ve IP adresleri listelenecektir.

## ICMP Ping Taraması 

### Açıklama

 belirli bir alt ağda ICMP ping taraması yaparak hangi IP adreslerinin aktif olduğunu belirlemeye yarar. belirlenen IP aralığındaki cihazlara ICMP echo istekleri gönderir ve yanıt veren cihazların IP adreslerini listeye ekler.

### Kullanım

 çalıştırmak için:

1. `ping_sweep.py` dosyasını çalıştırın.
2. Terminalde aşağıdaki komutu girin:

```bash
python ping_sweep.py
```

### Sonuç

Bu işlem sonucunda, belirlenen IP aralığında aktif olan cihazların IP adresleri listelenecektir.

## Notlar


- **ICMP Ping Taraması **: `addr` değişkeni ile taranacak alt ağın başlangıç kısmı belirlenmiştir; ihtiyaçlarınıza göre değiştirilebilir.


