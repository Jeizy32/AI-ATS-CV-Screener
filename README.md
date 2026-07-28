# ATS Resume AI Screener

**Deskripsi Singkat:**
ATS Resume AI Screener adalah aplikasi web berbasis *Artificial Intelligence* yang dirancang untuk membantu para pencari kerja menganalisis tingkat kecocokan Curriculum Vitae (CV) mereka terhadap standar *Applicant Tracking System* (ATS). Dilengkapi dengan fitur pemrosesan dokumen cerdas dan generator surat lamaran otomatis (*Cover Letter*).

## Tampilan Antarmuka
![Tampilan Web ATS Resume AI Screener]
<img width="459" height="243" alt="Image" src="https://github.com/user-attachments/assets/6a9cef34-7dbc-4234-96c2-db78d39a9675"/>
<img width="1333" height="386" alt="Image" src="https://github.com/user-attachments/assets/d77e43e8-6ec1-4c15-90e4-a606e94f8542" />
<img width="1327" height="607" alt="Image" src="https://github.com/user-attachments/assets/b5e721d5-889a-4fe4-9130-256bd1ac0fc9"/>
<img width="1366" height="619" alt="Image" src="https://github.com/user-attachments/assets/ec4a87a3-8a23-473c-9ad0-17d29644feac" />

## Fitur Utama
* **Smart PDF Parsing:** Mengekstraksi teks dari dokumen CV berformat PDF secara akurat dan bersih.
* **Keyword Matching:** Menganalisis kata kunci penting dalam CV dan mencocokkannya dengan kriteria deskripsi pekerjaan.(Deskripsi pekerjaan dan spesifikasi requirement bisa di copy dari job portal dan di copy disini)
* **ATS Compatibility Score:** Memberikan metrik persentase kecocokan yang jelas untuk mengukur kesiapan CV.
* **Draft AI:** Fitur cerdas yang otomatis menghasilkan teks perbaikan yang sesuai dengan kekurangan pada cv.
* **AI Cover Letter Generator:** Fitur cerdas yang otomatis menghasilkan draf surat lamaran kerja (*cover letter*) berdasarkan analisis CV dan posisi yang dilamar.

## Arsitektur & Teknologi (Tech Stack)
* **Backend:** Flask / Python
* **Generative AI:** Google Generative AI (Gemini API)
* **PDF Processing:** PyPDF2
* **Environment Management:** python-dotenv
* **Frontend:** HTML, CSS, JavaScript

## Konfigurasi Environment (Penting untuk Fitur AI)
Karena aplikasi ini memanfaatkan kecerdasan buatan dari Google Gemini, Anda wajib menyiapkan *API Key* sebelum menjalankan fitur analisis:

1. Buat file baru bernama `.env` di dalam direktori utama proyek (`ATS-Resume-AI-Screener`).
2. Masukkan konfigurasi API Key Anda dengan format berikut:
   ```env
   GEMINI_API_KEY=masukkan_api_key_google_gemini_anda_disini

*Panduan Instalasi & Menjalankan (How to Run)*
Bagi pengguna atau pengembang yang ingin menjalankan sistem ini di komputer lokal, ikuti langkah-langkah berikut:

1. Clone repository ini:
git clone [https://github.com/Jeizy32/ATS-Resume-AI-Screener.git](https://github.com/Jeizy32/ATS-Resume-AI-Screener.git)

2. Masuk ke direktori proyek:
Bash
cd ATS-Resume-AI-Screener

3. Instalasi Dependencies:
Install semua modul pendukung yang dibutuhkan melalui terminal:
Bash
pip install -r requirements.txt

4. Jalankan Aplikasi:
Bash
python run.py
(Buka browser Anda dan akses tautan: http://127.0.0.1:5000/)

*Pengembang*
Muhammad Rijal

System Integrator & Technical Documentation Enthusiast

www.linkedin.com/in/muhammad-rijal-6b7613288
