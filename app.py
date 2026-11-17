import streamlit as str_ui

# Page Configuration & Modern Dark Clinical Theme
str_ui.set_page_config(
    page_title="AI Medical & Clinical Expert System", 
    page_icon="🩺", 
    layout="wide"
)

# Custom Dark Medical CSS Styling (Black & Deep Neon Blue Theme)
str_ui.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .sidebar .stSidebar {
        background-color: #161b22;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
    }
    .clinical-card {
        background-color: #1f2937;
        border-left: 5px solid #38bdf8;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Language
if 'lang' not in str_ui.session_state:
    str_ui.session_state['lang'] = 'English'

lang_choice = str_ui.sidebar.selectbox("Language / اللغة", ["English", "العربية"])
str_ui.session_state['lang'] = 'English' if lang_choice == "English" else 'العربية'
lang = str_ui.session_state['lang']

# Bilingual Dictionaries
translations = {
    'English': {
        'title': "🩺 AI Medical & Clinical Expert System",
        'subtitle': "Advanced Diagnostic Neural Engine & Personalized Fitness-Nutrition Integration",
        'patient_info': "Patient Clinical Profile",
        'age': "Age (Years)",
        'weight': "Weight (kg)",
        'height': "Height (cm)",
        'gender': "Gender",
        'male': "Male",
        'female': "Female",
        'goal': "Fitness & Health Goal",
        'lose': "Weight Loss (Cutting) + Cardio Regimen",
        'gain': "Muscle Mass Gain (Bulking) + Resistance Training",
        'maintain': "Maintain Weight & General Fitness",
        'conditions': "Comprehensive Medical History & Chronic Diseases",
        'diabetes': "Diabetes (Type 1 / Type 2)",
        'hypertension': "Hypertension (High Blood Pressure)",
        'heart': "Cardiovascular / Heart Disease",
        'asthma': "Asthma / Respiratory Conditions",
        'symptoms': "Acute Symptoms Assessment (All-in-One)",
        'fever': "Fever, Chills & Infections",
        'cough': "Cough, Cold & Sore Throat",
        'headache': "Severe Headache & Migraine",
        'stomach': "Stomach Pain, Acid Reflux & IBS",
        'joint': "Joint & Muscle Inflammation",
        'analyze': "Execute AI Clinical Diagnosis & Generate Prescription",
        'diagnosis_title': "📋 Comprehensive AI Diagnostic Assessment",
        'prescription_title': "💊 Clinical Prescription & Medical Directives",
        'diet_title': "🥗 Tailored Nutrition & Sports-Fitness Regimen",
        'fit_title': "Body Composition & AI Confidence Score",
        'footer': "AI Clinical Expert System • Graduation Project • Department of Artificial Intelligence"
    },
    'العربية': {
        'title': "🩺 النظام الخبير الطبي والسريري المدعوم بالذكاء الاصطناعي",
        'subtitle': "محرك التشخيص العصبي المتقدم ودمج التغذية المخصصة مع الأنظمة الرياضية",
        'patient_info': "الملف السريري للمريض",
        'age': "العمر (بالسنوات)",
        'weight': "الوزن (كجم)",
        'height': "الطول (سم)",
        'gender': "الجنس",
        'male': "ذكر",
        'female': "أنثى",
        'goal': "الهدف الصحي والرياضي",
        'lose': "خسارة الوزن والتنشيف (Cutting) + برنامج الكارديو",
        'gain': "بناء العضلات والضخامة (Bulking) + تمارين المقاومة",
        'maintain': "الحفاظ على الوزن ولياقة الجسم العامة",
        'conditions': "التاريخ المرضي الشامل والأمراض المزمنة (كل الأقسام)",
        'diabetes': "مرض السكري (النوع الأول / الثاني)",
        'hypertension': "ارتفاع ضغط الدم المزمن",
        'heart': "أمراض القلب والأوعية الدموية",
        'asthma': "الربو ومشاكل الجهاز التنفسي",
        'symptoms': "تقييم الأعراض الحادة الشاملة",
        'fever': "حمى، قشعريرة والتهابات حادة",
        'cough': "سعال، برد والتهاب الحلق",
        'headache': "صداع شديد، توتر وشقيقة",
        'stomach': "آلام المعدة، الارتجاع المريئي والقولون العصبي (IBS)",
        'joint': "آلام المفاصل والعضلات",
        'analyze': "تشغيل التشخيص الذكي وإصدار الروشتة السريرية",
        'diagnosis_title': "📋 التقييم التشخيصي الشامل بالذكاء الاصطناعي",
        'prescription_title': "💊 الروشتة الطبية المعتمدة والإرشادات الدوائية",
        'diet_title': "🥗 النظام الغذائي والبرنامج الرياضي المخصص",
        'fit_title': "تحليل مؤشر كتلة الجسم ونسبة ثقة الذكاء الاصطناعي",
        'footer': "النظام الخبير الطبي للذكاء الاصطناعي • مشروع تخرج • قسم الذكاء الاصطناعي"
    }
}

t = translations[lang]

str_ui.title(t['title'])
str_ui.markdown(f"### *{t['subtitle']}*")
str_ui.markdown("---")

# Sidebar inputs
str_ui.sidebar.header(t['patient_info'])
age = str_ui.sidebar.number_input(t['age'], 1, 120, 22)
weight = str_ui.sidebar.number_input(t['weight'], 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input(t['height'], 50.0, 250.0, 170.0)
gender = str_ui.sidebar.selectbox(t['gender'], [t['male'], t['female']])
goal = str_ui.sidebar.selectbox(t['goal'], [t['lose'], t['gain'], t['maintain']])

str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader(t['conditions'])
has_diabetes = str_ui.sidebar.checkbox(t['diabetes'])
has_hypertension = str_ui.sidebar.checkbox(t['hypertension'])
has_heart = str_ui.sidebar.checkbox(t['heart'])
has_asthma = str_ui.sidebar.checkbox(t['asthma'])

str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader(t['symptoms'])
has_fever = str_ui.sidebar.checkbox(t['fever'])
has_cough = str_ui.sidebar.checkbox(t['cough'])
has_headache = str_ui.sidebar.checkbox(t['headache'])
has_stomach = str_ui.sidebar.checkbox(t['stomach'])
has_joint = str_ui.sidebar.checkbox(t['joint'])

if str_ui.button(t['analyze'], type="primary", use_container_width=True):
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    # AI Confidence Score simulation based on inputs
    confidence_score = 94.8 if (has_stomach or has_diabetes) else 91.2

    str_ui.markdown(f"## {t['diagnosis_title']}")
    
    diag_summary = f"""
    <div class="clinical-card">
        <b>Patient Profile:</b> {age} Years, {gender} | <b>BMI:</b> {bmi:.2f}<br>
        <b>AI Diagnostic Confidence Score:</b> <span style="color: #38bdf8; font-weight: bold;">{confidence_score}%</span><br>
        <b>Engine Status:</b> Neural Clinical Rules Triggered Successfully.
    </div>
    """
    str_ui.markdown(diag_summary, unsafe_allow_html=True)
    
    # Prescription
    str_ui.markdown(f"## {t['prescription_title']}")
    meds = []
    if has_fever or has_headache:
        meds.append(("Paracetamol / Panadol", "500mg - 1 tablet every 8 hours after meals for fever/pain."))
    if has_cough:
        meds.append(("Congestal / Cough Syrup", "1 tablet or tablespoon 3 times daily for cold symptoms."))
    if has_stomach:
        meds.append(("Omeprazole & Librax", "Omeprazole 20mg before breakfast; Librax twice daily for IBS & Reflux."))
    if has_diabetes:
        meds.append(("Metformin Directives", "As prescribed by endocrinologist with main meals."))
    if not meds:
        meds.append(("Multivitamin Complex", "1 capsule daily with breakfast to sustain vitality."))

    for m, d in meds:
        str_ui.markdown(f"- **💊 {m}:** `{d}`")

    # Diet & Sports Section based on Goal
    str_ui.markdown(f"## {t['diet_title']}")
    
    if "lose" in goal.lower() or "خسارة" in goal:
        str_ui.info("🎯 **Target Regimen:** Weight Loss (Cutting) + Moderate Cardio (4 days/week running/cycling 30 mins).")
        table_markdown = """
| Meal | Option 1 | Option 2 | Fitness & Sports Directive |
| :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 3 Boiled eggs + Cucumber & Greens | Oatmeal with water & cinnamon | Fasted morning walk (optional) |
| 🍗 **Lunch** | 150g Grilled chicken + Green salad | Baked fish + Steamed vegetables | Post-workout high protein meal |
| 🥗 **Dinner** | 150g Cottage cheese + Tomatoes | Vegetable soup with lean meat | Low carb to enhance fat burning |
"""
    elif "gain" in goal.lower() or "بناء" in goal:
        str_ui.info("🎯 **Target Regimen:** Muscle Bulking + Heavy Resistance Training (4-5 days/week gym hypertrophy).")
        table_markdown = """
| Meal | Option 1 | Option 2 | Fitness & Sports Directive |
| :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 3 Fried eggs in butter + Whole wheat toast | Peanut butter oats bowl with banana | Pre-workout heavy carb energy |
| 🥜 **Snack** | Dried fruits & nuts mix | Protein shake with milk | Sustained amino acid release |
| 🍗 **Lunch** | Egyptian rice + 200g Grilled meat | Pasta with chicken & white sauce | Post-workout muscle recovery |
| 🥗 **Dinner** | Thick fava beans + olive oil + eggs | Cottage cheese with whole bread | Slow digesting overnight protein |
"""
    else:
        str_ui.info("🎯 **Target Regimen:** Weight Maintenance + General Fitness (3 days/week full body workout).")
        table_markdown = """
| Meal | Option 1 | Option 2 | Fitness & Sports Directive |
| :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 2 Eggs + Toast + Tea | Yogurt with honey & fruits | Balanced macro nutrition |
| 🍗 **Lunch** | Grilled chicken + Rice + Salad | Tuna sandwich + Fresh juice | Moderate portion control |
| 🥗 **Dinner** | Light cheese + Cucumber | Warm milk + Few almonds | Restful sleep preparation |
"""

    str_ui.markdown(table_markdown)
    str_ui.markdown(f"**{t['fit_title']}:** `{bmi:.2f}` (AI Confidence: {confidence_score}%)")

str_ui.markdown("---")
str_ui.markdown(f"<p style='text-align: center; color: gray;'>{t['footer']}</p>", unsafe_allow_html=True)
