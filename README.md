# CV ATS Screener

**CV ATS Screener** adalah aplikasi berbasis web yang dirancang untuk membantu pengguna menganalisis dan mengukur tingkat kesesuaian Curriculum Vitae (CV) mereka terhadap standar *Applicant Tracking System* (ATS) yang sering digunakan oleh HRD.

## Tampilan Antarmuka
<img width="459" height="243" alt="Image" src="https://github.com/user-attachments/assets/9baf48d5-8ae4-4638-8da6-2e5003622a50" />
<img width="1333" height="386" alt="Image" src="https://github.com/user-attachments/assets/e8c71317-a6cc-4b09-9cee-bdce9f56833b" />
<img width="1327" height="607" alt="Image" src="https://github.com/user-attachments/assets/2463b517-3630-46a7-9cb9-3631f5a1d35c" />
<img width="1366" height="619" alt="Image" src="https://github.com/user-attachments/assets/45ce7e91-0b55-410d-9548-2900637347c7" />


## Alur Sistem (System Architecture)
Aplikasi ini tidak hanya memindai teks, tetapi juga memproses struktur dokumen dengan alur berikut:
1. **Input:** Pengguna memasukkan data CV (teks/dokumen).
2. **Ekstraksi Data:** Sistem memproses input untuk mengenali entitas penting seperti keahlian (skills), pengalaman, dan pendidikan.
3. **Scoring Engine:** Algoritma mencocokkan hasil ekstraksi dengan kata kunci standar industri dan menghitung persentase kesesuaian.
4. **Rekomendasi:** Sistem menampilkan hasil analisis beserta saran perbaikan format dan tata letak dokumen secara real-time.

## Teknologi yang Digunakan (Tech Stack)
* **Backend:** [Flask / Node.js]
* **Frontend:** [HTML, CSS, JavaScript / Tailwind CSS]
* **Pustaka Tambahan:** [Sebutkan jika ada, misal: PyPDF2, NLTK, dll]

## Cara Menjalankan Aplikasi di Lokal
Bagi yang ingin mencoba menjalankan aplikasi ini di environment lokal, ikuti langkah berikut:

1. Clone repository ini:
   ```bash
   git clone [https://github.com/Jeizy32/AI-ATS-CV-Screener](https://github.com/Jeizy32/AI-ATS-CV-Screener)

2. Masuk ke direktori proyek:
    cd cv-ats-screener

3.  Install semua depencies:
    pip install -r requirements.txt

4. Jalankan server aplikasi:
    python app.py
