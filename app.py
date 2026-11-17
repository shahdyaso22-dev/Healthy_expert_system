import streamlit as str_ui

# إعدادات الصفحة الاحترافية
str_ui.set_page_config(
    page_title="Medical Prescription & Expert System",
    page_icon="🩺",
    layout="centered"
)

# القواميس الشاملة للغات
translations = {
    "English": {
        "title": "🩺 Clinical Expert System & Electronic Prescription",
        "subtitle": "Official Medical Report & Tailored Patient Care Plan",
        "step1": "1. Patient Vital Statistics & Activity",
        "age": "Age (Years)",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "activity": "Activity Level",
        "activities": [
            "Sedentary / Desk Job (Minimal movement)",
            "Lightly Active (Light exercise 1-2 days/week)",
            "Moderately Active (Exercise 3-5 days/week)",
            "Very Active (Intense exercise 6-7 days/week)",
            "Professional Athlete (Daily heavy training)",
            "Low Mobility / Senior (Light daily walking)"
        ],
        "step2": "2. Clinical History, Acute Symptoms & Goals",
        "chronic_label": "Chronic Medical Conditions (Select all that apply):",
        "chronic_options": ["Diabetes", "Hypertension", "Knee Osteoarthritis", "High Cholesterol", "Stomach Pain / Indigestion", "Acid Reflux / GERD", "Irritable Bowel Syndrome (IBS)"],
        "acute_label": "Current Acute Symptoms / Complaints:",
        "acute_options": ["Headache / Migraine", "Common Cold & Flu", "Cough & Sore Throat", "Eye Inflammation / Conjunctivitis"],
        "goal_label": "Primary Health Goal:",
        "goal_options": [
            "Weight Loss & Fat Burning (Cutting)",
            "Maintain Current Weight & Balance",
            "Weight Gain & Muscle Building (Bulking)",
            "Symptom Recovery & Management",
            "Boost Immunity & Daily Energy",
            "Blood Sugar & Pressure Control",
            "Joint Health & Mobility Support"
        ],
        "btn_run": "Issue Official Medical Prescription & Report",
        "report_header": "📋 OFFICIAL MEDICAL PRESCRIPTION & CLINICAL REPORT",
        "patient_info": "Patient Clinical Summary",
        "rx_title": "Rx - Medical Treatment & Directives",
        "diet_title": "🍽️ Daily Meal Plan & Nutritional Table",
        "fit_title": "🏃 Physical Activity & Lifestyle Plan",
        "gold_rules": "⭐ Golden Rules for Fast Results",
        "footer_title": "🌟 Clinical Vision & Professional Care",
        "footer_text": "“Prevention is the master key to lifelong vitality. Investing in your daily health habits today guarantees a stronger, healthier, and happier tomorrow.”\n\n💡 *Note: This expert system is designed as an advanced clinical support tool. Always consult your primary care physician for critical medical decisions.*"
    },
    "العربية": {
        "title": "🩺 النظام الخبير الطبي وإصدار الروشتات الإلكترونية",
        "subtitle": "تقرير طبي معتمد وخطة علاجية وتغذوية مخصصة للمريض",
        "step1": "الخطوة الأولى: القياسات الحيوية ونمط النشاط اليومي",
        "age": "العمر (بالسنوات)",
        "weight": "الوزن (كجم)",
        "height": "الطول (سم)",
        "activity": "مستوى النشاط اليومي (اختر الأنسب)",
        "activities": [
            "قليل جداً / عمل مكتبي (حركة محدودة جداً)",
            "نشاط خفيف (تمرين خفيف 1-2 أيام أسبوعياً)",
            "نشاط معتدل (تمرين 3-5 أيام أسبوعياً)",
            "نشاط عالي (تمرين شاق 6-7 أيام أسبوعياً)",
            "رياضي محترف (تدريبات يومية مكثفة)",
            "حركة محدودة / كبار السن (مشي خفيف يومي)"
        ],
        "step2": "الخطوة الثانية: التاريخ المرضي، الأعراض الحالية، والأهداف",
        "chronic_label": "الأمراض والمشاكل الصحية (إن وجدت - اختر الكل المناسب):",
        "chronic_options": ["مرض السكر", "ارتفاع ضغط الدم", "خشونة الركبة والمفاصل", "ارتفاع الكوليسترول", "وجع المعدة / عسر الهضم", "ارتجاع المريء", "القولون العصبي (IBS)"],
        "acute_label": "الأعراض الحادة الحالية (التي يشكو منها المريض الآن):",
        "acute_options": ["الصداع / الصداع النصفي", "نزلات البرد والإنفلونزا", "الكحة والتهاب الحلق", "التهاب العين والاحمرار"],
        "goal_label": "الهدف العلاجي والصحي الأساسي:",
        "goal_options": [
            "خسارة الوزن وزيادة الحرق (تنشيف / خسارة دهون)",
            "الحفاظ على الوزن الحالي وثباته",
            "زيادة الوزن وبناء العضلات (تضخيم / زيادة الكتلة)",
            "التعافي السريع وإدارة الأعراض",
            "رفع المناعة والطاقة اليومية",
            "ضبط مستويات السكر والضغط بانتظام",
            "دعم صحة المفاصل وتقليل الآلام"
        ],
        "btn_run": "إصدار الروشتة الطبية والتقرير الإكلينيكي الشامل",
        "report_header": "📋 روشتة طبية معتمدة وتقرير إكلينيكي مفصل",
        "patient_info": "ملخص الفحص السريري للمريض",
        "rx_title": "Rx - العلاج الدوائي والإرشادات الطبية المباشرة",
        "diet_title": "🍽️ جدول الوجبات اليومية والنظام الغذائي",
        "fit_title": "🏃 خطة النشاط البدني والحياة اليومية",
        "gold_rules": "⭐ القواعد الذهبية لسرعة النتائج",
        "footer_title": "🌟 رؤية إكلينيكية وعناية صحية متكاملة",
        "footer_text": "“الوقاية هي مفتاح الحيوية الدائمة. استثمارك في صحتك وعاداتك اليومية اليوم هو الضمان الحقيقي لجسم أقوى وحياة أكثر سعادة غداً.”\n\n💡 *تنويه طبي: تم تصميم هذا النظام الخبير كأداة دعم إكلينيكي ذكية، ويُرجى دائماً استشارة الطبيب المختص في الحالات الطبية الطارئة أو الحرجة.*"
    }
}

# شريط اختيار اللغة
str_ui.sidebar.title("Settings / الإعدادات")
lang = str_ui.sidebar.selectbox("Language / اللغة", ["العربية", "English"])
t = translations[lang]

# العنوان الرئيسي
str_ui.title(t["title"])
str_ui.markdown(t["subtitle"])
str_ui.divider()

# نموذج الإدخال
with str_ui.form("prescription_form"):
    str_ui.subheader(t["step1"])
    col1, col2, col3 = str_ui.columns(3)
    with col1:
        age = str_ui.number_input(t["age"], min_value=10, max_value=100, value=28)
    with col2:
        weight = str_ui.number_input(t["weight"], min_value=30.0, max_value=200.0, value=75.0)
    with col3:
        height = str_ui.number_input(t["height"], min_value=100.0, max_value=220.0, value=170.0)
        
    activity_level = str_ui.selectbox(t["activity"], t["activities"])

    str_ui.subheader(t["step2"])
    selected_chronic = str_ui.multiselect(t["chronic_label"], t["chronic_options"])
    selected_acute = str_ui.multiselect(t["acute_label"], t["acute_options"])
    health_goal = str_ui.selectbox(t["goal_label"], t["goal_options"])

    submitted = str_ui.form_submit_button(t["btn_run"])

# قاعدة المعرفة الطبية والروشتات الاحترافية
medical_knowledge = {
    "مرض السكر": {
        "rx": "1. منظم السكر الموصوف (مثل جلوكوفاج / Metformin) بعد الأكل، أو التزام بجرعات الأنسولين (Insulin) حسب إرشادات الطبيب.\n2. قياس السكر بانتظام صائم وفاطر.\n3. الاحتفاظ بمصدر سكريات سريع تحسباً لأي هبوط.",
        "fit": "المشي المنتظم لمدة 30 إلى 45 دقيقة يومياً لتحسين حساسية الأنسولين."
    },
    "Diabetes": {
        "rx": "1. Prescribed oral hypoglycemic agents (e.g., Glucophage) or Insulin therapy as directed.\n2. Regular blood glucose monitoring.\n3. Keep fast-acting glucose sources nearby.",
        "fit": "Brisk walking for 30-45 minutes daily to improve insulin sensitivity."
    },
    "ارتفاع ضغط الدم": {
        "rx": "1. الالتزام بأدوية خفض ضغط الدم في موعدها الثابت.\n2. قياس الضغط يومياً وتدوين القراءات.\n3. تجنب الانفعالات العصبية وتقليل الملح.",
        "fit": "المشي الهادئ، تمارين التنفس العميق والاسترخاء."
    },
    "Hypertension": {
        "rx": "1. Strict adherence to prescribed antihypertensive medications.\n2. Daily blood pressure logging.\n3. Stress management and low sodium intake.",
        "fit": "Calm walking, deep breathing exercises."
    },
    "خشونة الركبة والمفاصل": {
        "rx": "1. جل موضعي مسكن ومضاد للالتهاب (مثل فليكدان أو فريزودين).\n2. مكملات غذائية لصحة الغضاريف (أوميغا 3 وجلوكوزامين).\n3. تجنب الجلوس الخاطئ على الأرض.",
        "fit": "السباحة، تمارين تقوية عضلات الساقين بدون تحميل على المفصل."
    },
    "Knee Osteoarthritis": {
        "rx": "1. Topical anti-inflammatory gel during pain flare-ups.\n2. Joint health supplements (Omega-3, Glucosamine).\n3. Avoid prolonged sitting on the floor.",
        "fit": "Swimming, seated leg strengthening exercises."
    },
    "ارتفاع الكوليسترول": {
        "rx": "1. أدوية خفض الدهون (الستاتينات مثل أتورفاستاتين) إن وصفها الطبيب.\n2. إجراء تحليل دهون شامل كل 3 إلى 6 أشهر.",
        "fit": "تمارين كارديو منتظمة (جري خفيف، مشي سريع، سباحة)."
    },
    "High Cholesterol": {
        "rx": "1. Statin therapy as prescribed.\n2. Periodic lipid profile testing.",
        "fit": "Regular cardio exercises (jogging, brisk walking)."
    },
    "وجع المعدة / عسر الهضم": {
        "rx": "1. مسكن آلام خفيف (باراسيتامول / بنادول) عند الحاجة الملحة.\n2. مضادات حموضة (مثل مالوكس أو رانتاج) ومشروبات مهدئة (بابونج أو نعناع).\n3. تجنب الوجبات الدسمة والمقليات.",
        "fit": "الراحة التامة وتجنب النوم مباشرة بعد الأكل."
    },
    "Stomach Pain / Indigestion": {
        "rx": "1. Mild analgesic (Paracetamol) if needed.\n2. Antacids (e.g., Maalox) and soothing warm herbal drinks.\n3. Avoid heavy, spicy, and fried meals.",
        "fit": "Physical rest and avoiding lying down right after meals."
    },
    "ارتجاع المريء": {
        "rx": "1. أدوية مثبطات مضخة البروتون (مثل أوميبرازول / بانتوبرازول) قبل الأكل.\n2. تجنب النوم بعد الأكل مباشرة ورفع مستوى الرأس أثناء النوم.\n3. الابتعاد عن الشاي، القهوة، والوجبات الحارة.",
        "fit": "المشي الخفيف الهادئ بعد الوجبات بمدة كافية."
    },
    "Acid Reflux / GERD": {
        "rx": "1. Proton Pump Inhibitors (e.g., Omeprazole) before meals.\n2. Elevate the head during sleep and avoid lying down post-meals.\n3. Avoid caffeine, citrus, and spicy foods.",
        "fit": "Light walking well after meals."
    },
    "القولون العصبي (IBS)": {
        "rx": "1. منظم لحركة الأمعاء ومضاد للتقلصات (مثل ليبراكس - Librax أو كولوفورمين).\n2. الإكثار من الألياف السائلة وشرب الأعشاب المهدئة (شمر ويانسون).\n3. الابتعاد عن التوتر العصبي والأكلات المهيجة للقولون.",
        "fit": "ممارسة تمارين الاسترخاء واليوجا أو المشي المنتظم."
    },
    "Irritable Bowel Syndrome (IBS)": {
        "rx": "1. Antispasmodics and bowel regulators (e.g., Librax as prescribed).\n2. High soluble fiber intake and soothing teas (fennel).\n3. Stress management and avoiding trigger foods.",
        "fit": "Relaxation exercises and regular walking."
    },
    "الصداع / الصداع النصفي": {
        "rx": "1. مسكن آلام فعال (باراسيتامول أو بنادول إكسترا) عند حدوث النوبة.\n2. الجلوس في غرفة مظلمة وهادئة تماماً.\n3. شرب كميات وافرة من الماء.",
        "fit": "إراحة الجسم تماماً أثناء النوبة."
    },
    "Headache / Migraine": {
        "rx": "1. Over-the-counter mild analgesic (Paracetamol / Panadol).\n2. Rest in a dark, quiet room.\n3. Adequate hydration.",
        "fit": "Complete physical rest during attacks."
    },
    "نزلات البرد والإنفلونزا": {
        "rx": "1. أقراص علاج البرد المتكاملة (مثل كونجستال - Congestal أو كومتركس) كل 8 ساعات.\n2. خافض حرارة ومسكن (باراسيتامول / بنادول فلو).\n3. فيتامين سي، سوائل دافئة وراحه تامة.",
        "fit": "راحة تامة في السرير وعدم ممارسة أي مجهود بدني."
    },
    "Common Cold & Flu": {
        "rx": "1. Cold medication (e.g., Congestal or Comtrex) every 8 hours.\n2. Antipyretic and analgesic (Panadol Cold & Flu).\n3. Vitamin C, warm fluids, and bed rest.",
        "fit": "Absolute bed rest with zero physical exertion."
    },
    "الكحة والتهاب الحلق": {
        "rx": "1. شراب مهدئ للسعال أو مذيب للبلغم (مثل تريوسلف أو برونكوهيل).\n2. أقراص استحلاب ملطفة للحلق (مثل ستربرسلز).\n3. الغرغرة بالماء الدافئ والملح.",
        "fit": "الراحة الصوتية والبدنية، وتجنب الهواء البارد والأتربة."
    },
    "Cough & Sore Throat": {
        "rx": "1. Appropriate cough syrup or mucolytic.\n2. Soothing throat lozenges.\n3. Warm saltwater gargles.",
        "fit": "Vocal and physical rest."
    },
    "التهاب العين والاحمرار": {
        "rx": "1. قطرات عيون مرطبة أو مضادة للحساسية والالتهاب (مثل توبرادكس أو افامايسين بوصف طبي).\n2. كمادات باردة أو دافئة نظيفة.\n3. تجنب فرك العين نهائياً وغسل اليدين باستمرار.",
        "fit": "إراحة العين تماماً من الشاشات."
    },
    "Eye Inflammation / Conjunctivitis": {
        "rx": "1. Prescribed lubricating or anti-inflammatory eye drops.\n2. Clean compresses.\n3. Strictly avoid rubbing the eyes.",
        "fit": "Complete screen rest for the eyes."
    }
}

# عند الضغط على زر التشغيل
if submitted:
    h_m = height / 100.0
    bmi = weight / (h_m ** 2)
    
    if bmi < 18.5:
        bmi_status = "Underweight / نحيف"
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal Weight / وزن مثالي وطبيعي"
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight / زيادة في الوزن"
    else:
        bmi_status = "Obese / سمنة مفرطة"

    str_ui.success(t["report_header"])
    
    str_ui.markdown(f"### 🏥 {t['patient_info']}")
    c1, c2, c3 = str_ui.columns(3)
    c1.metric(label="BMI", value=f"{bmi:.2f}")
    c2.write(f"**العمر / Age:** {age} سنة")
    c3.write(f"**الوزن / الطول:** {weight}كغ / {height}سم")
    
    str_ui.info(f"📌 **التصنيف الصحي:** {bmi_status} \n\n🎯 **الهدف العلاجي المختار:** {health_goal} | ⚡ **النشاط:** {activity_level}")

    str_ui.divider()

    all_selected = selected_chronic + selected_acute

    if not all_selected:
        str_ui.warning("⚠️ لم يتم تحديد أي أمراض أو أعراض. إليك الروشتة والتوجيهات العامة:")
        all_selected = ["التوجيهات العامة"]
        medical_knowledge["التوجيهات العامة"] = {
            "rx": "1. لا توجد أدوية مطلوبة حالياً.\n2. الفحص الدوري الروتيني وشرب الماء بانتظام.",
            "fit": "المشي اليومي لمدة 30 دقيقة للحفاظ على اللياقة."
        }

    for item in all_selected:
        rec = medical_knowledge.get(item, {
            "rx": "استشر الطبيب المختص لتحديد العلاج المناسب.",
            "fit": "ممارسة النشاط البدني الخفيف المنتظم."
        })
        
        with str_ui.expander(f"🩺 روشتة وتقرير حالة: **{item}**", expanded=True):
            
            str_ui.markdown(f"#### {t['rx_title']}")
            str_ui.code(rec["rx"], language=None)
            
            # جدول الأكل الاحترافي (حسب هدف المريض: زيادة وزن أو خسارة وزن)
            str_ui.markdown(f"#### {t['diet_title']}")
            
            is_bulking = "زيادة الوزن" in health_goal or "Bulking" in health_goal
            
            if lang == "العربية":
                if is_bulking:
                    table_markdown = """
| الوجبة | الخيار الأول | الخيار الثاني | الخيار الثالث | ملاحظات هامة |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 3 بيضات مقلية في الزبدة + رغيف خبز بلدي أو شريحتين توست بر + كوب حليب كامل الدسم مع تمرات + معلقة كبيرة زبدة فول سوداني | طبق فول بزيت الزيتون والبطاطس المسلوقة + رغيف بلدي + جبنة قريش | فطير مشلتت خفيف أو توست أبيض مع عسل وطحينة + كوب حليب | طاقة عالية لزيادة الوزن وبناء العضلات بأمان |
| 🥪 **سناك (1)** | سلطة فواكه مجففة ومكسرات (عين جمل، لوز، زبيب) | كوب عصير مانجو أو موز بالحليب كامل الدسم مع العسل | توست بزبده الفول السوداني والموز | سعرات مركزة وسهلة الهضم وغنية بالدهون الصحية |
| 🍗 **الغداء** | طبق خبز أرز مصري أو مكرونة (مطهي بالسمن أو الزبدة) + صدرين دجاج أو قطعة لحم ضأن/بقري متوسطة الحجم + طبق خضار مطهي مع مرقة ودسم صحي + سلطة خضراء مع زيت الزيتون | صينية مكرونة بشاميل أو رقاق باللحمة المفرومة + سلطة خضراء + قطعة لحم دسمة | سمك مقلي أو مشوي بزيت ذرة + أرز صيادية كبير + سلطة خضراء | وجبة أساسية مليئة بالبروتين والكربوهيدرات المعقدة |
| 🥪 **سناك (2)** | سندوتش زبدة الفول السوداني والموز مع العسل | طبق شوفان بالحليب والعسل والمكسرات | فطيرة صغيرة بالجبنة أو التمر | تمدك بطاقة عالية جداً قبل أي مجهود أو التمرين |
| 🥗 **العشاء** | طبق فول بزيت الزيتون والطحينة الكثيفة + جبنة كاملة الدسم (قريش مع قشطة أو جبنة بيضاء دسمة) + رغيف خبز بلدي | علبة تونة مصفاة تماماً + طبق سلطة خضراء كبير | كوب زبادي يوناني بالعسل والمكسرات | بروتين بطيء الهضم جداً يغذي الجسم طوال النوم |
| 🌙 **قبل النوم** | كوب حليب دافئ كامل الدسم مع معلقة عسل ومكسرات مطحونة | كوب زبادي كامل الدسم مع تمرات مقطعة | وجبة خفيفة من المكسرات والزبيب | يساعد على الاسترخاء ويزيد السعرات في آخر اليوم |
"""
                else:
                    table_markdown = """
| الوجبة | الخيار الأول | الخيار الثاني | الخيار الثالث | ملاحظات هامة |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 3 بيضات مستوية أو مقلية بمعلقة زيت زيتون + ربع رغيف بلدي + خيار وجرجير | 4 ملاعق فول بزيت زيتون وكمون + ربع رغيف بلدي + بيضة مسلوقة أو قطعة جبنة قريش | عجة بيض بالخضروات وفلفل رومي + ربع رغيف بلدي | بداية نشطة ومشبع لفترة طويلة |
| 🍗 **الغداء** | 150-200 جم صدور فراخ مشوية أو مسلوقة أو لحم مفروم قليل الدهن + 5 ملاعق أرز أو مكرونة + طبق خضار سوتيه + سلطة خضراء | 2 سمكة مشوية + ربع رغيف بلدي كامل أو 5 ملاعق أرز + طبق سلطة خضراء كبير | بروتين (علبة تونة مصفاة من الزيت) + نشويات (رغيف بلدي كامل أو 5 ملاعق مكرونة) + خضار (طبق خضار سوتيه + سلطة) | معلقة زيت زيتون وليمون فقط على السلطة |
| 🥗 **العشاء** | 150 جم جبنة قريش بالطماطم والخيار ورشة زعتر + ربع رغيف بلدي | علبة تونة مصفاة تماماً + طبق سلطة خضراء | كوب زبادي يوناني (أو عادي) + نص معلقة عسل نحل + معلقة بذور كتان أو شيا | وجبة خفيفة ومناسبة قبل النوم |
"""
            else:
                if is_bulking:
                    table_markdown = """
| Meal | Option 1 | Option 2 | Option 3 | Important Notes |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 3 fried eggs in butter + whole bread or toast + full-fat milk with dates & peanut butter | Fava beans with olive oil & boiled potatoes + bread + cottage cheese | Light flaky pastry or white toast with honey & tahini + milk | High energy for weight gain and muscle building |
| 🥪 **Snack (1)** | Dried fruits and nuts salad (walnuts, almonds, raisins) | Mango or banana milkshake with honey | Toast with peanut butter and banana | Dense calories, easy digestion, healthy fats |
| 🍗 **Lunch** | Egyptian rice or pasta (cooked with ghee/butter) + 2 chicken breasts or beef + cooked veggies with healthy fat + green salad with olive oil | Bechamel pasta or lasagna + green salad + meat piece | Fried/grilled fish + large riced fish + green salad | Essential protein and complex carbs for mass |
| 🥪 **Snack (2)** | Peanut butter and banana sandwich with honey | Oatmeal bowl with milk, honey, and nuts | Small cheese or date pastry | High energy boost pre-workout |
| 🥗 **Dinner** | Thick fava beans with olive oil & tahini + full-fat cheese + whole bread | Drained canned tuna + large green salad | Greek yogurt with honey and nuts | Slow-digesting protein overnight |
| 🌙 **Before Sleep**| Warm full-fat milk with honey and ground nuts | Full-fat yogurt with chopped dates | Small handful of nuts and raisins | Aids relaxation and boosts daily calories |
"""
                else:
                    table_markdown = """
| Meal | Option 1 | Option 2 | Option 3 | Important Notes |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 3 fried/boiled eggs with olive oil + quarter bread + cucumber & arugula | 4 spoons fava beans with olive oil + quarter bread + egg or cottage cheese | Vegetable egg omelet with quarter bread | Active start, long satiety |
| 🍗 **Lunch** | 150-200g grilled chicken/lean meat + 5 spoons rice/pasta + sautéed veggies + salad | 2 grilled fish + quarter bread or 5 spoons rice + large green salad | Tuna (drained) + whole bread or pasta + vegetable soup + salad | Only olive oil and lemon on salad |
| 🥗 **Dinner** | 150g cottage cheese with tomatoes, cucumber, thyme + quarter bread | Drained canned tuna + green salad | Greek/regular yogurt + half spoon honey + flax/chia seeds | Light meal suitable before bed |
"""
            str_ui.markdown(table_markdown)
            
            str_ui.markdown(f"#### {t['fit_title']}")
            str_ui.write(f"🚶 {rec['fit']}")
            
        str_ui.write("")

    # القواعد الذهبية لسرعة النتائج
    str_ui.info(f"""...""")
### {t['gold_rules']}
💧 **شرب المياه:** من 2.5 إلى 3 لتراً يومياً لزيادة معدل الحرق ومنع الإحساس الوهمي بالجوع.  
🚶 **الحركة الخفيفة:** المشي 15-20 دقيقة في منتصف اليوم أو بعد الغداء لتحسين الهضم والدورة الدموية.  
🚫 **السكر والمشروبات:** استبدال السكر الأبيض بسكر دايت ومنع العصائر المعلبة ت
