from flask import Blueprint, request, jsonify
import json
import google.generativeai as genai
from app.utils.pdf_helper import extract_text_from_pdf
import os

analyzer_bp = Blueprint('analyzer', __name__)

kumpulan_keys_string = os.getenv("GEMINI_API_KEYS", "")
KUMPULAN_API_KEYS = [key.strip() for key in kumpulan_keys_string.split(",") if key.strip()]

@analyzer_bp.route('/analyze', methods=['POST'])
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
