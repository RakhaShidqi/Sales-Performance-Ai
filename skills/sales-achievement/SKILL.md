# Sales Achievement Skill

## Skill Name

Sales Performance Analytics

---

# Base URL

```http
http://10.180.70.78:5000
```

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

---

# Notes

* Default period adalah YTD.
* Semua endpoint menggunakan metode HTTP GET.
* Base URL berlaku untuk seluruh endpoint.
* Parameter pertama menggunakan `?`.
* Parameter berikutnya menggunakan `&`.
