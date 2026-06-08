# Sales Achievement Skill

## Skill Name

quarterly_sales_achievement

---

# Objective

Skill ini digunakan untuk menjawab pertanyaan terkait achievement sales yang berjalan berdasarkan data Excel.

Contoh pertanyaan user:

# Quarterly Achievement
* berapa achievement sales quartal ini
* achievement quarter ini
* performance sales quarter ini
* total pencapaian sales quartal ini
* sales achievement Q1
* achievement Q2
* achievement Q3 tahun ini
* pencapaian quarter 4
* performance sales kwartal ini
* total achievement team quarter ini
* quarter ini sudah berapa persen
* pencapaian sales per quartal
* achievement revenue quartal ini
* target vs actual quarter ini
* berapa persen closing quarter ini
* quarter ini sudah achieve berapa
* revenue achievement q1
* revenue quarter ini
* sales quarter ini bagaimana
* summary achievement quarter ini

# Monthly Achievement
* achievement bulan ini
* sales bulan ini berapa
* pencapaian bulan mei
* performance sales bulan ini
* achievement revenue mei
* target bulan ini sudah berapa persen
* actual vs target bulan ini
* achievement MTD
* sales performance monthly
* monthly achievement report
* summary sales bulan ini
* revenue bulan ini
* pencapaian tim bulan ini
* bulan ini sudah closing berapa
* progress target bulan ini
* Yearly / YTD Achievement
* berapa achievement sales tahun ini
* berapa sales YTD

# Achievement YTD
* pencapaian sales tahun berjalan
* revenue tahun ini
* total sales tahun ini
* performance sales yearly
* yearly achievement
* YTD performance
* target vs actual tahun ini
* achievement annual
* annual sales performance
* pencapaian tahunan
* progress target tahunan
* total closing tahun ini
* achievement sampai bulan ini
* revenue YTD berapa
* sales performance sampai saat ini
* Team Achievement
* achievement team sales
* performance team sales
* team sales sudah berapa persen
* siapa top sales bulan ini
* ranking sales bulan ini
* sales terbaik quarter ini
* siapa paling tinggi achievementnya
* siapa top performer
* total achievement seluruh tim
* team performance summary
* ranking revenue sales
* ranking achievement sales
* siapa paling banyak closing
* siapa paling rendah achievement
* summary performa team

# GP Achievement
* GP achievement bulan ini
* gross profit achievement
* achievement GP quarter ini
* GP YTD
* target GP sudah berapa persen
* actual GP bulan ini
* performance GP team
* GP summary
* pencapaian gross profit
* revenue dan GP bulan ini

# Pipeline & Forecast
* pipeline sales bulan ini
* total pipeline quarter ini
* forecast closing bulan ini
* prediksi achievement akhir bulan
* estimasi closing quarter ini
* pipeline terbesar siapa
* deal yang belum closing
* berapa potensi revenue bulan ini
* sales forecast Q2
* prediksi achievement tahunan

# Trend & Comparison
* compare dengan bulan lalu
* compare quarter sebelumnya
* achievement naik atau turun
* trend sales tahun ini
* growth revenue bulan ini
* performance dibanding tahun lalu
* quarter ini lebih baik dari sebelumnya
* perubahan achievement sales
* tren revenue sales
* growth achievement YTD

# Natural Conversation Style
* gimana performa sales sekarang
* sales lagi bagus gak
* target aman gak
* kita udah berapa persen
* closing aman bulan ini?
* sales lagi turun atau naik?
* quarter ini sehat gak?
* kondisi revenue sekarang bagaimana
* progress target bagaimana
* achievement kita sejauh ini bagaimana

---

# Data Source

Source data berasal dari file Excel:

```text
/data/achievement_report2026.xlsx
```

Contoh struktur data:
# Sales Performance Excel Header Description

| Header            | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| No.               | Role Akses                                                                |
| Name              | Nama sales / account manager / person in charge                           |
| Join Date         | Tanggal bergabung sales ke perusahaan                                     |
| Teritory          | Area atau wilayah penjualan yang ditangani                                |
| Status            | Status sales, contoh: Active, Resign, Probation                           |
| JAN               | Total revenue / achievement bulan Januari                                 |
| Jan %             | Persentase achievement Januari terhadap target                            |
| FEB               | Total revenue / achievement bulan Februari                                |
| Feb %             | Persentase achievement Februari terhadap target                           |
| MAR               | Total revenue / achievement bulan Maret                                   |
| Mar %             | Persentase achievement Maret terhadap target                              |
| APR               | Total revenue / achievement bulan April                                   |
| Apr %             | Persentase achievement April terhadap target                              |
| MAY               | Total revenue / achievement bulan Mei                                     |
| May %             | Persentase achievement Mei terhadap target                                |
| JUN               | Total revenue / achievement bulan Juni                                    |
| Jun %             | Persentase achievement Juni terhadap target                               |
| JUL               | Total revenue / achievement bulan Juli                                    |
| Jul %             | Persentase achievement Juli terhadap target                               |
| AUG               | Total revenue / achievement bulan Agustus                                 |
| Aug %             | Persentase achievement Agustus terhadap target                            |
| SEP               | Total revenue / achievement bulan September                               |
| Sep %             | Persentase achievement September terhadap target                          |
| OCT               | Total revenue / achievement bulan Oktober                                 |
| Oct %             | Persentase achievement Oktober terhadap target                            |
| NOV               | Total revenue / achievement bulan November                                |
| Nov %             | Persentase achievement November terhadap target                           |
| DEC               | Total revenue / achievement bulan Desember                                |
| Dec %             | Persentase achievement Desember terhadap target                           |
| Total YTD         | Total akumulasi revenue / achievement Year To Date                        |
| YTD %             | Persentase total achievement Year To Date terhadap target tahunan         |
| ACH Q1            | Total achievement Quarter 1 (Jan-Mar)                                     |
| ACH Q2            | Total achievement Quarter 2 (Apr-Jun)                                     |
| Total PO          | Total Purchase Order / total deal yang berhasil closing                   |
| GAP Ach YTD       | Selisih antara target YTD dan actual YTD                                  |
| Leads On Progress | Jumlah leads / opportunity yang masih dalam proses                        |
| VS GAP            | Perbandingan leads/pipeline terhadap kekurangan target                    |
| ACH FY 2025       | Total achievement full year 2025                                          |
| FY'25             | Target full year 2025                                                     |
| Expenses          | Total biaya / operational cost sales                                      |
| Ratio             | Rasio performance tertentu, biasanya revenue vs expense atau profit ratio |

---

# Sample Data Interpretation - Sales Performance

## Raw Data

| Name | Join Date | Territory | Status | JAN | Jan % | FEB | Feb % | MAR | Mar % | APR | Apr % | MAY | May % | JUN | Jun % | JUL | Jul % | AUG | Aug % | SEP | Sep % | OCT | Oct % | NOV | Nov % | DEC | Dec % | Total YTD | YTD % | ACH Q1 | ACH Q2 | Total PO | GAP Ach YTD | Leads On Progress | VS GAP | ACH FY 2025 | FY'25 | Expenses | Ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Previna Clara Surjahadi | 5-Apr-2021 | Public Sector | Active | 13,860,960 | 3.0% | 4,615,200 | 1.1% | 0 | 0.0% | 62,394,461 | 18.0% | 48,676,809 | 15.8% | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% | 0 | 0.0% | 129,547,430 | 4.3% | 1.46% | 12.03% | 8 | -2,062,760,263 | 4,870,000,000 | 236.1% | 819,058,142 | 30.9% | 2.9% |

---

# Human Readable Summary

## Employee Information

| Field     | Value                   |
| --------- | ----------------------- |
| Name      | Previna Clara Surjahadi |
| Join Date | 5 April 2021            |
| Teritory | Public Sector           |
| Status    | Active                  |

---

# Monthly Achievement Summary

| Month    | Revenue       | Achievement % |
| -------- | ------------- | ------------- |
| January  | Rp 13,860,960 | 3.0%          |
| February | Rp 4,615,200  | 1.1%          |
| March    | Rp 0          | 0.0%          |
| April    | Rp 62,394,461 | 18.0%         |
| May      | Rp 48,676,809 | 15.8%         |
| June     | Rp 0          | 0.0%          |

---

# Quarterly Achievement

| Quarter | Achievement |
| ------- | ----------- |
| Q1      | 1.46%       |
| Q2      | 12.03%      |

---

# YTD Performance

| Metric              | Value          |
| ------------------- | -------------- |
| Total YTD Revenue   | Rp 129,547,430 |
| YTD Achievement     | 4.3%           |
| FY 2025 Achievement | Rp 819,058,142 |
| FY 2025 Percentage  | 30.9%          |

---

# Pipeline & Gap Analysis

| Metric              | Value            |
| ------------------- | ---------------- |
| Total PO            | 8                |
| GAP Achievement YTD | Rp 2,062,760,263 |
| Leads On Progress   | Rp 4,870,000,000 |
| VS GAP              | 236.1%           |

---

# Expense & Ratio

| Metric   | Value    |
| -------- | -------- |
| Expenses | Rp 30.9% |
| Ratio    | 2.9%     |

---

# Formula Reference & Business Rules

* Jika user bertanya terkait achievement quartal (Q1, Q2, Q3, atau Q4), maka sistem menggunakan formula berikut:

```text id="u41f64"
Average Ach Q =
SUM(Ach Q WHERE No. != 1 AND Ach Q != 0)
/
COUNT(Name WHERE No. != 1 AND Ach Q != 0)
```

Dengan `Ach Q` menyesuaikan header quartal yang ditanyakan user seperti:

* `ACH Q1`
* `ACH Q2`
* `ACH Q3`
* `ACH Q4`

---

* Jika user bertanya terkait achievement secara umum dan bukan berdasarkan quartal tertentu, maka sistem akan menggunakan `YTD %` sebagai default achievement report tahun berjalan.

Formula:

```text id="kqaq76"
Average ACH YTD =
SUM(YTD % WHERE No. != 1 AND YTD % != 0)
/
COUNT(Name WHERE No. != 1 AND YTD % != 0)
```

Default report mengacu pada Achievement Report 2026.

---

* `Join Date` digunakan sebagai pertimbangan tambahan dalam analisa performance sales.

Jika sales memiliki masa kerja yang masih baru berdasarkan `Join Date`, maka sistem akan memberikan catatan tambahan seperti:

```text id="n4aq7g"
Notes:
Sales masih dalam masa adaptasi karena baru bergabung.
```

---

* `VS GAP` digunakan untuk menganalisa potensi pencapaian target berdasarkan pipeline yang masih berjalan.

Contoh:
Jika sales sudah memiliki pencapaian besar pada quartal sebelumnya (misalnya sudah closing Rp1 Miliar dengan target Rp300 Juta), maka selisih achievement tersebut dianggap sebagai “tabungan achievement”.

Tabungan achievement masih dapat digunakan pada quartal berikutnya dengan syarat:

```text id="3ah1x0"
Minimum achievement YTD tetap harus >= 100% terhadap target YTD.
```

---

* Jika user bertanya terkait sales performance, maka sistem akan menampilkan seluruh data performance sales.

Namun sistem juga akan memberikan notes atau insight tambahan untuk masing-masing sales, seperti:

* Sales dengan performance baik
* Sales dengan achievement rendah
* Sales yang memiliki pipeline besar
* Sales baru join
* Sales yang masih memiliki potensi closing tinggi



