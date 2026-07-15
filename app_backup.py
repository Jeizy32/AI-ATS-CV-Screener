from flask import Flask, render_template, request, jsonify
import PyPDF2
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
kumpulan_keys_string = os.getenv("GEMINI_API_KEYS", "")
KUMPULAN_API_KEYS = [key.strip() for key in kumpulan_keys_string.split(",") if key.strip()]

app = Flask(__name__)

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'cv_file' not in request.files or 'jd_text' not in request.form:
        return jsonify({"error": "Data tidak lengkap"}), 400
    
    file = request.files['cv_file']
    jd_text = request.form['jd_text']
    
    if file.filename == '':
        return jsonify({"error": "File CV belum dipilih"}), 400

    try:
        cv_text = extract_text_from_pdf(file)
        
        prompt = f"""
        Kamu adalah Senior Tech Recruiter dan ahli sistem ATS (Applicant Tracking System).
        Tugasmu adalah menganalisis teks CV kandidat dan membandingkannya dengan Job Description (JD).

        Teks CV: {cv_text}
        Teks Job Description: {jd_text}

        Lakukan analisis dan kembalikan response HANYA dalam format JSON dengan struktur berikut:
        {{
          "ats_score": (angka 0-100),
          "category_scores": [
            {{"category": "teknikal & Tools", "score": (angka 0-100)}},
            {{"category": "Pengalaman Kerja", "score": (angka 0-100)}},
            {{"category": "Pendidikan", "score": (angka 0-100)}},
            {{"category": "Soft Skills", "score": (angka 0-100)}}
            ],
          "matching_keywords": ["keyword 1", "keyword 2"],
          "missing_keywords": ["keyword 3", "keyword 4"],
          "role_title_optimization": [
            {{
              "original_title": "(jabatan di CV)",
              "suggested_title": "(jabatan alternatif)",
              "reason": "(alasan)"
            }}
          ],
          "general_feedback": "(Saran singkat)"
        }}
        """
        
        # --- PERBAIKAN: Definisikan model untuk fungsi analyze ---
        genai.configure(api_key=KUMPULAN_API_KEYS[0]) # Pakai key pertama dari list
        model = genai.GenerativeModel('gemini-flash-latest')
        
        response = model.generate_content(prompt)
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        result = json.loads(cleaned_text)
        return jsonify(result)
        
    except Exception as e:
        import traceback
        print(f"Error: {e}")
        traceback.print_exc()
        print("========================")
        return jsonify({"error": str(e)}), 500

@app.route('/generate-bullet', methods=['POST'])
def generate_bullet():
    data = request.json
    keyword = data.get('keyword', '')
    job_title = data.get('job_title', '')
    
    # Tambahin instruksi caps lock biar AI-nya nurut
    prompt = f"""Tuliskan 1 kalimat bullet point resume yang profesional, ATS-friendly, dan berdampak untuk melamar posisi '{job_title}'. 
    Kalimat ini harus menonjolkan keahlian dalam hal '{keyword}'. 
    Gunakan action verb di awal kalimat dan bahasa Indonesia yang formal.
    
    ATURAN SANGAT PENTING: 
    Berikan HANYA kalimat hasil akhirnya saja. 
    DILARANG memberikan kata pengantar, penjelasan, atau basa-basi apa pun.
    DILARANG menggunakan simbol bullet atau tanda kutip."""
    
    hasil_teks = None
    
    # --- PERBAIKAN: Posisi indentasi disesuaikan ---
    for key in KUMPULAN_API_KEYS:
        try:
            genai.configure(api_key=key)  
            model = genai.GenerativeModel("gemini-flash-latest")
            
            response = model.generate_content(prompt)
            hasil_teks = response.text.replace("*","").strip()
            
            print(f"✅ [Draft AI] Berhasil pakai key berakhiran: ...{key[-4:]}")
            break  
        except Exception as e:
            print(f"❌ [Draft AI] Key berakhiran ...{key[-4:]} limit/error: {e}. Mencoba key berikutnya...")
            continue
            
    # Harus sejajar dengan FOR, agar dipanggil setelah loop selesai
    if hasil_teks:
        return jsonify({"bullet": hasil_teks})
    else:
        return jsonify({"bullet": "Maaf, semua kuota AI server sedang penuh. Coba lagi nanti."}), 500

if __name__ == '__main__':
    app.run(debug=True)