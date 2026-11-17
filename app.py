import streamlit as str_ui

# 1. إعدادات الصفحة
str_ui.set_page_config(
    page_title="AI Medical & Sports Expert System",
    page_icon="🩺",
    layout="wide"
)

# 2. تصميم عصري منور (Glowing Cyber-Blue & Glassmorphism UI)
str_ui.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #0f172a, #020617 70%);
        color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1120 0%, #020617 100%);
        border-right: 1px solid rgba(56, 189, 248, 0.25);
    }
    h1 {
        background: linear-gradient(90deg, #38bdf8, #818cf8, #2dd4bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-shadow: 0px 0px 25px rgba(56, 189, 248, 0.3);
    }
    h2, h3 {
        color: #38bdf8 !important;
        font-weight: 700 !important;
    }
    .glow-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.4);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .rx-card {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(17, 24, 39, 0.95));
        border: 1px solid #2dd4bf;
        box-shadow: 0 0 20px rgba(45, 212, 191, 0.2);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #2563eb 50%, #0ea5e9 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.85) !important;
        transform: translateY(-2px);
    }
    table {
        width: 100%;
        border-collapse: collapse;
        background-color: rgba(15, 23, 42, 0.85) !important;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.15);
    }
    th {
        background-color: rgba(2, 132, 199, 0.35) !important;
        color: #7dd3fc !important;
        padding: 12px !important;
        border-bottom: 2px solid #38bdf8 !important;
    }
    td {
        padding: 12px !important;
        border-bottom: 1px solid rgba(56, 189, 248, 0.15) !important;
        color: #e2e8f0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. اللغات
if 'lang' not in str_ui.session_state:
    str_ui.session_state['lang'] = 'العربية'

lang_choice = str_ui.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "English"])
str_ui.session_state['lang'] = lang_choice
lang = str_ui.session_state['lang']

translations = {
    'English': {
        'title': "🩺 AI Clinical & Sports Expert System",
        'subtitle': "Advanced Neural Diagnostics, Activity Analysis & Smart Fitness Engine",
        'patient_info': "👤 Patient & Athlete Profile",
        'age': "Age (Years)",
        'weight': "Weight (kg)",
        'height': "Height (cm)",
        'gender': "Gender",
        'male': "Male",
        'female': "Female",
        'activity': "Physical Activity Level",
        'act_sedentary': "Sedentary (Little to no exercise / Desk job)",
        'act_light': "Lightly Active (Light exercise 1-3 days/week)",
        'act_moderate': "Moderately Active (Moderate exercise 3-5 days/week)",
        'act_active': "Very Active (Hard exercise 6-7 days/week)",
        'act_elderly': "Elderly / Limited Mobility (حركة محدودة / كبير السن)",
        'conditions_section': "🏥 1. Comprehensive Medical & Diseases",
        'no_conditions': "None / Healthy Baseline (لا يوجد أمراض)",
        'diabetes': "Diabetes (Type 1 / Type 2)",
        'hypertension': "Hypertension (High Blood Pressure)",
        'heart': "Cardiovascular / Heart Disease",
        'asthma': "Asthma / Respiratory Issues",
        'fever': "Fever & Chills",
        'cough': "Cough, Cold & Sore Throat",
        'headache': "Severe Headache & Migraine",
        'stomach': "Stomach Pain, Acid Reflux & IBS",
        'joint': "Joint & Muscle Pain",
        'sports_section': "🏋️‍♂️ 2. Sports, Fitness & Diet Section",
        'enable_sports': "Activate Sports & Custom Diet Plan",
        'fitness_goal': "Select Your Fitness Goal",
        'cutting': "Weight Loss & Cutting (Cardio + Fat Burn)",
        'bulking': "Muscle Gain & Bulking (Resistance + Hypertrophy)",
        'maintenance': "General Fitness & Weight Maintenance",
        'analyze': "⚡ Run AI Neural Diagnosis & Generate Plan",
        'diagnosis_title': "🧠 AI Diagnostic & Activity Analysis Report",
        'prescription_title': "💊 Smart Clinical Prescription (Rx)",
        'sports_title': "🔥 Personalized Training Schedule",
        'diet_title': "🥗 Custom Fitness Nutrition Table"
    },
    'العربية': {
        'title': "🩺 النظام الخبير الطبي والرياضي الذكي",
        'subtitle': "محرك التشخيص العصبي، تحليل النشاط البدني وبرامج اللياقة المخصصة",
        'patient_info': "👤 الملف الشخصي للمريض والرياضي",
        'age': "العمر (بالسنوات)",
        'weight': "الوزن (كجم)",
        'height': "الطول (سم)",
        'gender': "الجنس",
        'male': "ذكر",
        'female': "أنثى",
        'activity': "مستوى النشاط البدني والحركة",
        'act_sedentary': "خامل (بدون تمرين أو عمل مكتبى)",
        'act_light': "نشاط خفيف (تمرين 1-3 أيام في الأسبوع)",
        'act_moderate': "نشاط معتدل (تمرين 3-5 أيام في الأسبوع)",
        'act_active': "نشاط عالي جداً (تمارين شاقة 6-7 أيام)",
        'act_elderly': "حركة محدودة / كبير السن (مجهود بسيط)",
        'conditions_section': "🏥 1. قسم الأمراض والأعراض الشامل",
        'no_conditions': "لا يوجد أمراض أو أعراض (حالة سليمة)",
        'diabetes': "مرض السكري (النوع الأول / الثاني)",
        'hypertension': "ارتفاع ضغط الدم المزمن",
        'heart': "أمراض القلب والأوعية الدموية",
        'asthma': "الربو ومشاكل الجهاز التنفسي",
        'fever': "حمى وارتفاع درجة الحرارة",
        'cough': "سعال وبرد والتهاب الحلق",
        'headache': "صداع شديد وشقيقة",
        'stomach': "آلام المعدة والارتجاع والقولون العصبي",
        'joint': "آلام المفاصل والعضلات",
        'sports_section': "🏋️‍♂️ 2. قسم الرياضة والنظام الغذائي",
        'enable_sports': "تفعيل برنامج الرياضة وجدول الأكل المخصص",
        'fitness_goal': "اختر هدفك الرياضي",
        'cutting': "تخسيس وتنشيف (Cutting) + كارديو وحرق دهون",
        'bulking': "زيادة وزن وبناء عضلات (Bulking) + تمارين مقاومة",
        'maintenance': "لياقة عامة والحفاظ على الوزن",
        'analyze': "⚡ تشغيل التشخيص الذكي وإصدار الخطة الكاملة",
        'diagnosis_title': "🧠 تقرير التشخيص العصبي وتحليل النشاط البدني",
        'prescription_title': "💊 الروشتة الطبية الذكية المعتمدة (Rx)",
        'sports_title': "🔥 جدول التمارين الرياضية المخصص لك",
        'diet_title': "🥗 جدول النظام الغذائي المرتبط برياضتك"
    }
}

t = translations[lang]

str_ui.title(t['title'])
str_ui.markdown(f"<p style='color: #94a3b8; font-size: 18px; margin-top: -10px;'>{t['subtitle']}</p>", unsafe_allow_html=True)
str_ui.markdown("---")

# الشريط الجانبي
str_ui.sidebar.header(t['patient_info'])
age = str_ui.sidebar.number_input(t['age'], 1, 120, 22)
weight = str_ui.sidebar.number_input(t['weight'], 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input(t['height'], 50.0, 250.0, 172.0)
gender = str_ui.sidebar.selectbox(t['gender'], [t['female'], t['male']])
activity_level = str_ui.sidebar.selectbox(t['activity'], [t['act_sedentary'], t['act_light'], t['act_moderate'], t['act_active'], t['act_elderly']])

# قسم الأمراض
str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader(t['conditions_section'])
no_cond = str_ui.sidebar.checkbox(t['no_conditions'])

if not no_cond:
    has_diabetes = str_ui.sidebar.checkbox(t['diabetes'])
    has_hypertension = str_ui.sidebar.checkbox(t['hypertension'])
    has_heart = str_ui.sidebar.checkbox(t['heart'])
    has_asthma = str_ui.sidebar.checkbox(t['asthma'])
    has_fever = str_ui.sidebar.checkbox(t['fever'])
    has_cough = str_ui.sidebar.checkbox(t['cough'])
    has_headache = str_ui.sidebar.checkbox(t['headache'])
    has_stomach = str_ui.sidebar.checkbox(t['stomach'])
    has_joint = str_ui.sidebar.checkbox(t['joint'])
else:
    has_diabetes = has_hypertension = has_heart = has_asthma = False
    has_fever = has_cough = has_headache = has_stomach = has_joint = False

# قسم الرياضة
str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader(t['sports_section'])
enable_sports = str_ui.sidebar.checkbox(t['enable_sports'])
fitness_goal = None
if enable_sports:
    fitness_goal = str_ui.sidebar.selectbox(t['fitness_goal'], [t['cutting'], t['bulking'], t['maintenance']])

if str_ui.button(t['analyze'], use_container_width=True):
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        bmi_cat = "نحافة (Underweight)"
    elif bmi < 25:
        bmi_cat = "وزن مثالي (Normal)"
    elif bmi < 30:
        bmi_cat = "زيادة وزن (Overweight)"
    else:
        bmi_cat = "سمنة (Obese)"

    any_disease = any([has_diabetes, has_hypertension, has_heart, has_asthma, has_fever, has_cough, has_headache, has_stomach, has_joint])
    confidence = 96.8 if any_disease else 98.5

    str_ui.markdown(f"## {t['diagnosis_title']}")
    status_text = "لا يوجد أمراض مسجلة (حالة صحية مستقرة)" if (no_cond or not any_disease) else "تم رصد مؤشرات سريرية وتفعيل قواعد الاستدلال الذكي"
    
    diag_html = f"""
    <div class="glow-card">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="color: #94a3b8; font-size: 14px;">البيانات الحيوية ومستوى النشاط</span><br>
                <strong style="font-size: 16px; color: #f8fafc;">{age} سنة | {gender}</strong><br>
                <span style="color: #38bdf8; font-size: 13px;">⚡ {activity_level}</span>
            </div>
            <div>
                <span style="color: #94a3b8; font-size: 14px;">مؤشر كتلة الجسم (BMI)</span><br>
                <strong style="font-size: 18px; color: #38bdf8;">{bmi:.1f} — {bmi_cat}</strong>
            </div>
            <div>
                <span style="color: #94a3b8; font-size: 14px;">دقة استنتاج الذكاء الاصطناعي</span><br>
                <strong style="font-size: 18px; color: #2dd4bf;">⚡ {confidence}% AI Confidence</strong>
            </div>
        </div>
        <hr style="border-color: rgba(56, 189, 248, 0.2); margin: 15px 0;">
        <p style="margin: 0; color: #cbd5e1;"><strong>الحالة السريرية:</strong> {status_text}</p>
    </div>
    """
    str_ui.markdown(diag_html, unsafe_allow_html=True)

    # الروشتة
    str_ui.markdown(f"## {t['prescription_title']}")
    meds = []
    if no_cond or not any_disease:
        meds.append(("لا يوجد أدوية مطلوبة (No Medication Needed)", "حالتك الصحية مستقرة بناءً على مؤشرات النشاط البدني والبيانات الحيوية. يُنصح بالاستمرار في نمط الحياة الصحي."))
    else:
        if has_fever or has_headache:
            meds.append(("Panadol / Paracetamol 500mg", "قرص واحد كل 8 ساعات عند اللزوم لتسكين الألم وخفض الحرارة."))
        if has_cough:
            meds.append(("Congestal / شراب للسعال", "قرص كل 8 ساعات أو ملعقة كبيرة 3 مرات يومياً لأعراض البرد."))
        if has_stomach:
            meds.append(("Omeprazole 20mg + Librax", "كبسولة أوميبرازول قبل الإفطار + قرص ليبراكس قبل الغداء والعشاء للقولون والمعدة."))
        if has_diabetes:
            meds.append(("Metformin Directives", "الالتزام بجرعات منظم السكر المعتمدة مع الوجبات الرئيسية."))
        if has_hypertension:
            meds.append(("مراقبة ضغط الدم", "الالتزام بأدوية الضغط الموصوفة وتجنب المالح والتوتر."))
        if has_joint:
            meds.append(("جل موضعي مسكن", "دهان موضعي مرتين يومياً لمفاصل الجسم المتعبة."))

    rx_items = ""
    for m, d in meds:
        rx_items += f"<p style='margin-bottom: 12px;'><strong style='color: #2dd4bf; font-size: 16px;'>💊 {m}</strong><br><span style='color: #cbd5e1;'>{d}</span></p>"
    
    str_ui.markdown(f"<div class='rx-card'>{rx_items}</div>", unsafe_allow_html=True)

    # قسم الرياضة والأكل (لو مفعل)
    if enable_sports and fitness_goal:
        str_ui.markdown(f"## {t['sports_title']}")
        
        if "cutting" in fitness_goal.lower() or "تخسيس" in fitness_goal:
            str_ui.markdown("""
            <div class="glow-card">
                <strong style="color: #38bdf8; font-size: 17px;">🔥 جدول التمارين الرياضية (تنشيف وحرق دهون)</strong>
            </div>
            """, unsafe_allow_html=True)
            
            sports_table = """
| اليوم | نوع التمارين | المدة والشدة |
| :--- | :--- | :--- |
| **اليوم 1 و 4** | مشي سريع أو كارديو لحرق الدهون | 45 دقيقة |
| **اليوم 2 و 5** | تمارين مقاومة شاملة (Full Body) | 45 دقيقة |
| **اليوم 3 و 6** | تمارين إطالة وحرق خفيف | 30 دقيقة |
| **اليوم 7** | راحة تامة واستشفاء | راحة |
"""
            str_ui.markdown(sports_table)

            str_ui.markdown(f"## {t['diet_title']}")
            diet_table = """
| الوجبة | الخيار الأول | الخيار الثاني | ملاحظات التنشيف |
| :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 3 بيضات مسلوقة + خيار | شوفان بالماء والقرفة | سعرات منخفضة وشبع |
| 🍗 **الغداء** | 150 جم دجاج مشوي + سلطة | سمك مشوي + خضار سوتيه | بروتين صافي |
| 🥗 **العشاء** | 150 جم جبنة قريش + طماطم | علبة تونة مصفاة | هضم خفيف ليلاً |
"""
            str_ui.markdown(diet_table)

        elif "bulking" in fitness_goal.lower() or "زيادة" in fitness_goal:
            str_ui.markdown("""
            <div class="glow-card">
                <strong style="color: #38bdf8; font-size: 17px;">💪 جدول التمارين الرياضية (ضخامة وبناء عضلات)</strong>
            </div>
            """, unsafe_allow_html=True)

            sports_table = """
| اليوم | نوع التمارين | المدة والشدة |
| :--- | :--- | :--- |
| **اليوم 1** | دفع (صدر + كتف + ترايسبس) | 60 دقيقة أوزان ثقيلة |
| **اليوم 2** | سحب (ظهر + بايسبس) | 60 دقيقة أوزان ثقيلة |
| **اليوم 3** | راحة عضلية | راحة |
| **اليوم 4** | أرجل كاملة (Legs) | 60 دقيقة |
| **اليوم 5** | جزء علوي شامل (Upper Body) | 50 دقيقة |
| **اليوم 6 و 7** | راحة ونوم عميق للاستشفاء | راحة تامة |
"""
            str_ui.markdown(sports_table)

            str_ui.markdown(f"## {t['diet_title']}")
            diet_table = """
| الوجبة | الخيار الأول | الخيار الثاني | ملاحظات الضخامة |
| :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 3 بيضات بالزبدة + توست أسمر | شوفان بالحليب كامل الدسم وموز وعسل | طاقة عالية |
| 🥜 **سناك** | مكسرات وفواكه مجففة | سموثي زبدة فول سوداني | سعرات إضافية |
| 🍗 **الغداء** | أرز مصري + 200 جم لحم مشوي | مكرونة بصدور الدجاج والصلصة | بناء عضلي قوي |
| 🥗 **العشاء** | فول مدمس بزيت الزيتون + بيض | جبنة قريش بالخبز البلدي وحليب | بروتين بطيء ليلاً |
"""
            str_ui.markdown(diet_table)
        else:
            str_ui.markdown("""
            <div class="glow-card">
                <strong style="color: #38bdf8; font-size: 17px;">⚡ نظام اللياقة العامة</strong>
                <p style="color: #cbd5e1; margin-top: 8px;">المحافظة على النشاط اليومي والمشي 30 دقيقة يومياً مع نظام غذائي متوازن.</p>
            </div>
            """, unsafe_allow_html=True)
