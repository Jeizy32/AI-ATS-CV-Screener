from flask import Blueprint, request, jsonify
from app.utils.pdf_helper import extract_text_from_pdf
import google.generativeai as genai
import os

generator_bp = Blueprint('generator', __name__)
KUMPULAN_API_KEYS = [k.strip() for k in os.getenv("GEMINI_API_KEYS", "").split(",") if k.strip()]

@generator_bp.route('/generate-bullet', methods=['POST'])
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

@generator_bp.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    # 1. Ambil file CV dan teks JD
    if 'cv_file' not in request.files or 'jd_text' not in request.form:
        return jsonify({"error": "Data tidak lengkap"}), 400
    
    file = request.files['cv_file']
    jd_text = request.form['jd_text']
    cv_text = extract_text_from_pdf(file) # Pakai fungsi yang udah ada!
    
    # 2. Prompt untuk Cover Letter
    prompt = f"""
    Buatkan surat lamaran kerja (Cover Letter) yang profesional, persuasif, dan ATS-friendly berdasarkan data berikut:
    CV Kandidat: {cv_text}
    Job Description: {jd_text}
    
    Format:
    - Gunakan bahasa Indonesia yang formal.
    - Tekankan pengalaman yang paling relevan dengan posisi tersebut.
    - Jangan terlalu panjang (maksimal 3 paragraf).
    - Berikan tempat untuk [Nama], [Alamat], dan [Tanggal].
    - BERIKAN HASILNYA SAJA TANPA KATA PENGANTAR.
    """

    hasil_surat = None
    
    # 3. Looping API Key (Sama seperti fitur sebelumnya)
    for key in KUMPULAN_API_KEYS:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-flash-latest")
            response = model.generate_content(prompt)
            hasil_surat = response.text.replace("*", "").strip()
            print(f"✅ [Cover Letter] Berhasil pakai key: ...{key[-4:]}")
            break
        except Exception as e:
            print(f"❌ Key ...{key[-4:]} gagal. Mencoba berikutnya...")
            continue

    if hasil_surat:
        return jsonify({"cover_letter": hasil_surat})
    else:
        return jsonify({"cover_letter": "Maaf, semua kuota AI sedang sibuk. Coba lagi nanti."}), 500
    pass