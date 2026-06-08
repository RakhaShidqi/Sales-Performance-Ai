# Sales Achievement Skill

## Skill Name

Sales Performance Analytics

---

# Base URL

**Port selalu `5000` dan tidak pernah berubah.**
**Yang berubah hanya IP address server — harus dideteksi otomatis setiap sesi.**

Jangan menggunakan `http://127.0.0.1:5000` secara hardcoded.

Aplikasi harus menentukan alamat IP server secara otomatis berdasarkan sistem operasi yang digunakan, kemudian membentuk Base URL dengan format:

```http
http://<IPv4_ADDRESS>:5000
```

## Windows

Jalankan perintah:

```bash
ipconfig
```

Cari nilai **IPv4 Address** pada adapter jaringan yang aktif.

Contoh output:

```text
Ethernet adapter Ethernet:

   IPv4 Address. . . . . . . . . . . : 192.168.18.16
```

Maka Base URL yang digunakan:

```http
http://192.168.18.16:5000
```

---

## Linux

Jalankan perintah:

```bash
ip a
```

atau

```bash
ip addr
```

Cari alamat IPv4 pada interface jaringan yang aktif.

Contoh output:

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
```

Maka Base URL yang digunakan:

```http
http://192.168.18.16:5000
```

---

## Agent Rules

Sebelum melakukan request API:

1. Identifikasi sistem operasi host.
2. Jika Windows, jalankan:

```bash
ipconfig
```

3. Jika Linux, jalankan:

```bash
ip a
```

4. Ambil alamat IPv4 dari interface jaringan aktif.
5. Bentuk Base URL:

```http
http://<IPv4_ADDRESS>:5000
```

6. Gunakan Base URL tersebut untuk seluruh endpoint API.

### Contoh

Jika IPv4 yang ditemukan adalah:

```text
192.168.18.16
```

Maka endpoint:

```http
GET /sales/territory/Retail
```

Menjadi:

```http
GET http://192.168.18.16:5000/sales/territory/Retail
```

### Important

- Jangan menggunakan `127.0.0.1` kecuali IPv4 host memang `127.0.0.1`.
- Selalu gunakan IPv4 hasil deteksi dari sistem operasi.
- Gunakan alamat yang sama untuk seluruh request selama sesi berjalan.
- Jika terdapat lebih dari satu IPv4, prioritaskan alamat jaringan lokal (LAN) yang aktif dan bukan alamat loopback.

---

# Objective

Skill ini digunakan untuk menjawab pertanyaan terkait:

* Sales Achievement
* Sales Performance
* Monthly Achievement
* Quarterly Achievement
* YTD Achievement
* Sales Ranking
* Team Performance
* Head Sales Performance
* Unit Head Performance
* Summary Dashboard
* Database Sales

---

# Available Parameters

| Parameter  | Type    | Description                     |
| ---------- | ------- | ------------------------------- |
| smb        | boolean | Filter data SMB Division        |
| enterprise | boolean | Filter data Enterprise Division |
| headsales  | boolean | Filter data Head Sales          |
| unit_head  | boolean | Filter data Unit Head           |

---

# Territory Classification

## Enterprise

Territory yang termasuk kategori Enterprise:

* Public Sector
* Telco, Media, & Technology
* Financial Services Industry
* Manufacture, Logistic, & Healthcare
* Retail

Gunakan:

```http
?enterprise=true
```

---

## SMB

Territory yang termasuk kategori SMB:

* SMB Bag Utara
* SMB Bag Barat
* SMB Bag Timur
* SMB Bag Selatan

Gunakan:

```http
?smb=true
```

---

## Regional

Territory yang termasuk kategori Regional:

* Reg West Java
* Reg Central Java
* Reg East Java
* Reg Bali
* Reg Sulawesi
* Reg Kalimantan
* Reg Sumatera

---

# Endpoint Selection Rules

## Sales Performance

Gunakan endpoint:

```http
/commercial/sales-performance
```

ketika user bertanya:

* Sales performance
* Achievement sales
* Performance sales
* Progress target sales
* Achievement YTD

---

## Top Ranking

Gunakan endpoint:

```http
/commercial/ranking/top
```

ketika user bertanya:

* Top sales
* Ranking tertinggi
* Best performer
* Sales terbaik
* Top achievement

---

## Bottom Ranking

Gunakan endpoint:

```http
/commercial/ranking/bottom
```

ketika user bertanya:

* Bottom sales
* Ranking terbawah
* Worst performer
* Sales terendah

---

## Summary Dashboard

Gunakan endpoint:

```http
/commercial/summary
```

ketika user meminta:

* Summary
* Dashboard
* Ringkasan performa
* Overview sales

---

---

## Total PO

Gunakan endpoint:

```http
/sales/search/{keyword}/total_po
```

ketika user mencari:
* Total PO

---

---

## Leads On Progress

Gunakan endpoint:

```http
/sales/search/{keyword}/leads_on_progress
```

ketika user mencari:
* Leads On Progress
* Leads yg sedang berjalan

---

## Gap Ach Ytd

Gunakan endpoint:

```http
/sales/search/{keyword}/gap_ach_ytd
```

ketika user mencari:
* Gap Ach Ytd

---

---

## VS Gap

Gunakan endpoint:

```http
/sales/search/{keyword}/vs_gap
```

ketika user mencari:
* VS Gap

---

## Database Sales

Gunakan endpoint:

```http
/database/applicants/search/{keyword}
```

ketika user mencari:

* Nama sales
* Data sales
* Informasi sales
* Territory sales
* Database sales
* Detail Data

---

# Period Mapping

## Default

Jika user tidak menyebutkan periode:

Gunakan YTD.

```http
/commercial/sales-performance
```

---

## Quarterly

| User Mention | Endpoint |
| ------------ | -------- |
| Q1           | /q1      |
| Q2           | /q2      |
| Q3           | /q3      |
| Q4           | /q4      |

---

## Monthly

| Month     | Endpoint |
| --------- | -------- |
| January   | /jan     |
| February  | /feb     |
| March     | /mar     |
| April     | /apr     |
| May       | /may     |
| June      | /jun     |
| July      | /jul     |
| August    | /aug     |
| September | /sep     |
| October   | /oct     |
| November  | /nov     |
| December  | /dec     |

---

# Sales Performance

## Commercial

### YTD

```http
GET /commercial/sales-performance
```

### Quarterly

```http
GET /commercial/sales-performance/q1
GET /commercial/sales-performance/q2
GET /commercial/sales-performance/q3
GET /commercial/sales-performance/q4
```

### Monthly

```http
GET /commercial/sales-performance/jan
GET /commercial/sales-performance/feb
GET /commercial/sales-performance/mar
GET /commercial/sales-performance/apr
GET /commercial/sales-performance/may
GET /commercial/sales-performance/jun
GET /commercial/sales-performance/jul
GET /commercial/sales-performance/aug
GET /commercial/sales-performance/sep
GET /commercial/sales-performance/oct
GET /commercial/sales-performance/nov
GET /commercial/sales-performance/dec
```

---

## SMB Filter

```http
GET /commercial/sales-performance/ytd?smb=true
GET /commercial/sales-performance/q1?smb=true
GET /commercial/sales-performance/q2?smb=true
GET /commercial/sales-performance/q3?smb=true
GET /commercial/sales-performance/q4?smb=true
```

---

## SMB Head Sales

```http
GET /commercial/sales-performance/ytd?smb=true&headsales=true
GET /commercial/sales-performance/q1?smb=true&headsales=true
GET /commercial/sales-performance/q2?smb=true&headsales=true
GET /commercial/sales-performance/q3?smb=true&headsales=true
GET /commercial/sales-performance/q4?smb=true&headsales=true
```

---

## SMB Unit Head

```http
GET /commercial/sales-performance/ytd?smb=true&unit_head=true
GET /commercial/sales-performance/q1?smb=true&unit_head=true
GET /commercial/sales-performance/q2?smb=true&unit_head=true
GET /commercial/sales-performance/q3?smb=true&unit_head=true
GET /commercial/sales-performance/q4?smb=true&unit_head=true
```

---

## Enterprise

```http
GET /commercial/sales-performance/ytd?enterprise=true
GET /commercial/sales-performance/q1?enterprise=true
GET /commercial/sales-performance/q2?enterprise=true
GET /commercial/sales-performance/q3?enterprise=true
GET /commercial/sales-performance/q4?enterprise=true
```

---

## Enterprise Head Sales

```http
GET /commercial/sales-performance/ytd?enterprise=true&headsales=true
GET /commercial/sales-performance/q1?enterprise=true&headsales=true
GET /commercial/sales-performance/q2?enterprise=true&headsales=true
GET /commercial/sales-performance/q3?enterprise=true&headsales=true
GET /commercial/sales-performance/q4?enterprise=true&headsales=true
```

---

## Regional

```http
GET /regional/sales-performance/ytd
GET /regional/sales-performance/q1
GET /regional/sales-performance/q2
GET /regional/sales-performance/q3
GET /regional/sales-performance/q4
```

---

## Regional Head Sales

```http
GET /regional/sales-performance/ytd?headsales=true
GET /regional/sales-performance/q1?headsales=true
GET /regional/sales-performance/q2?headsales=true
GET /regional/sales-performance/q3?headsales=true
GET /regional/sales-performance/q4?headsales=true
```

---

# Top Ranking

Gunakan pola yang sama seperti Sales Performance:

```http
/commercial/ranking/top
/commercial/ranking/top/q1
/commercial/ranking/top/q2
/commercial/ranking/top/q3
/commercial/ranking/top/q4
```

Mendukung:

* smb=true
* enterprise=true
* headsales=true
* unit_head=true

---

# Bottom Ranking

Gunakan pola:

```http
/commercial/ranking/bottom
/commercial/ranking/bottom/q1
/commercial/ranking/bottom/q2
/commercial/ranking/bottom/q3
/commercial/ranking/bottom/q4
```

Mendukung:

* smb=true
* enterprise=true
* headsales=true
* unit_head=true

---

# Summary Dashboard

Gunakan pola:

```http
/commercial/summary/ytd
/commercial/summary/q1
/commercial/summary/q2
/commercial/summary/q3
/commercial/summary/q4
```

Mendukung:

* smb=true
* enterprise=true
* headsales=true
* unit_head=true

---

# Database Sales

## Search Sales

```http
GET /database/applicants/search/{keyword}
```

Contoh:

```http
GET /database/applicants/search/rakha
```

---

# Response Rules

* Selalu gunakan endpoint yang paling spesifik sesuai intent user.
* Jika user menyebut SMB, tambahkan `smb=true`.
* Jika user menyebut Enterprise, tambahkan `enterprise=true`.
* Jika user menyebut Head Sales, tambahkan `headsales=true`.
* Jika user menyebut Unit Head, tambahkan `unit_head=true`.
* Jika user tidak menyebut periode, gunakan YTD.
* Jangan memanggil endpoint ranking ketika user meminta sales performance.
* Jangan memanggil endpoint sales performance ketika user meminta ranking.
* Gunakan endpoint database hanya untuk pencarian sales berdasarkan nama atau keyword.
* Ketika menampilkan data achievement sales, **selalu sertakan kolom Achievement Value** (dalam format Rupiah) bersama kolom Achievement (%) dan Status.
* **Jangan pernah meminta file Excel atau data upload dari user.** Semua data diambil langsung dari API endpoint yang tersedia. Langsung panggil endpoint yang sesuai dengan pertanyaan user.

---

# Output Formatting — Top Sales & Ranking

## Minimum Achievement Threshold

Nilai minimum achievement adalah **17.5%**.

## Aturan Warna & Status di Output Top Sales

Ketika menampilkan **Top Sales** (ranking), terapkan aturan berikut pada setiap baris:

| Kondisi | Status | Format Teks |
|---------|--------|-------------|
| Achievement ≥ 17.5% | ✅ Perform | Tampilkan normal |
| Achievement < 17.5% | ❌Underperform | Tampilkan normal, tanpa HTML styling, tanpa spasi antara ❌ dan teks |

## Contoh Format Output

```
| Rank | Nama | Territory | Achievement | Achievement Value | Status |
|------|------|-----------|-------------|-------------------|--------|
| 1 | Rosita Desiani | FSI | 134.79% | Rp 1.200.000.000 | ✅ Perform |
| 9 | Firdaus Jiemmy | MLH | 10.20% | Rp 80.000.000 | ❌Underperform |
```

## Aturan Penerapan

* Tidak menggunakan HTML styling apapun pada output tabel.
* Aturan ini berlaku untuk semua output Top Sales, Bottom Sales, dan Sales Performance.
* Tampilkan ❌Underperform sebagai plain text tanpa spasi antara ❌ dan kata "Underperform", tanpa tag HTML.

---

# Output Formatting — Detail Data (Database Sales)

Ketika menampilkan **detail data** dari endpoint `/database/applicants/search/{keyword}`, tampilkan hanya kolom berikut:

| Kolom | Keterangan |
|-------|------------|
| Ach Periode | Periode achievement |
| Customer Name | Nama customer |
| Service | Nama produk/layanan |
| Service Description | Deskripsi layanan |

## Contoh Format Output

```
| Periode | Customer | Service | Service Description |
|---------|----------|---------|---------------------|
| JAN | CV. Murni Grace Utama | SMB Access Point Low 2Y | SMB Access Point Low 2Y (LTO) = 1 Unit, Request Instalasi 14 Desember 2025 |
```

* Jangan tampilkan kolom lain (MRC, Revenue, No Inv, dll) kecuali user secara eksplisit memintanya.
* Jika Service Description kosong atau null, tampilkan `-`.

---

# Notes

* Default period adalah YTD.
* Semua endpoint menggunakan metode HTTP GET.
* Base URL berlaku untuk seluruh endpoint.
* Parameter pertama menggunakan `?`.
* Parameter berikutnya menggunakan `&`.
