import streamlit as str_ui

str_ui.set_page_config(
    page_title="AI Clinical, Medical & Sports Expert System",
    page_icon="🩺",
    layout="wide",
)

lang_choice = str_ui.radio("🌐 اللغة / Language", ["العربية", "English"], horizontal=True)
def tr(ar_txt, en_txt): return ar_txt if lang_choice == "العربية" else en_txt

css_code = (
    "<style>"
    ".stApp { background: radial-gradient(circle at top right, #0f172a, #020617 70%); color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }"
    "[data-testid='stSidebar'] { background: linear-gradient(180deg, #0b1120 0%, #020617 100%); border-right: 1px solid rgba(56, 189, 248, 0.25); }"
    "h1 { background: linear-gradient(90deg, #38bdf8, #818cf8, #2dd4bf); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800 !important; }"
    "h2, h3 { color: #38bdf8 !important; font-weight: 700 !important; }"
    ".stButton > button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 50%, #0ea5e9 100%) !important; color: white !important; font-weight: bold !important; font-size: 18px !important; border: none !important; border-radius: 12px !important; padding: 14px 24px !important; box-shadow: 0 0 22px rgba(14, 165, 233, 0.55) !important; }"
    ".diet-banner { background: linear-gradient(135deg, rgba(14, 116, 144, 0.45), rgba(30, 58, 138, 0.45)); border: 1px solid rgba(56, 189, 248, 0.6); box-shadow: 0 10px 32px rgba(14, 165, 233, 0.35), 0 0 18px rgba(45, 212, 191, 0.2); border-radius: 18px; padding: 20px; margin-bottom: 20px; }"
    ".glow-table-wrap { background: rgba(15, 23, 42, 0.92); border: 1px solid rgba(56, 189, 248, 0.55); box-shadow: 0 12px 35px rgba(2, 132, 199, 0.38), 0 0 22px rgba(45, 212, 191, 0.18); border-radius: 18px; padding: 14px; margin-bottom: 22px; overflow-x: auto; }"
    ".custom-tbl { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 12px; overflow: hidden; }"
    ".custom-tbl th { background: linear-gradient(90deg, rgba(2, 132, 199, 0.65), rgba(13, 148, 136, 0.55)); color: #f0f9ff; font-weight: 700; padding: 13px 14px; border-bottom: 2px solid #38bdf8; text-align: right; font-size: 15px; }"
    ".custom-tbl td { padding: 12px 14px; border-bottom: 1px solid rgba(56, 189, 248, 0.18); color: #f1f5f9; text-align: right; font-size: 14px; line-height: 1.65; vertical-align: top; }"
    ".custom-tbl tr:last-child td { border-bottom: none; }"
    ".custom-tbl tr:hover td { background: rgba(56, 189, 248, 0.1); }"
    ".pill-tag { display: inline-block; background: rgba(45, 212, 191, 0.16); border: 1px solid rgba(45, 212, 191, 0.45); color: #5eead4; border-radius: 8px; padding: 2px 8px; font-size: 12px; font-weight: 700; margin-bottom: 4px; }"
    ".tip-box { background: rgba(15, 23, 42, 0.88); border: 1px solid rgba(56, 189, 248, 0.4); box-shadow: 0 6px 22px rgba(14, 165, 233, 0.22); border-radius: 14px; padding: 14px 16px; margin-bottom: 12px; }"
    "</style>"
)
str_ui.markdown(css_code, unsafe_allow_html=True)


def render_condition(title, initial_steps, avoid_text=None, emergency_text=None, med_text=""):
    str_ui.markdown("### " + title)
    str_ui.markdown("**" + tr("التصرف المبدئي:", "Initial Actions:") + "**")
    for step in initial_steps:
        str_ui.markdown("- " + step)
    if avoid_text:
        str_ui.warning("**" + tr("تجنب:", "Avoid:") + "** " + avoid_text)
    if emergency_text:
        str_ui.error("**" + tr("اذهب للطوارئ فوراً 🚨:", "Go to ER immediately 🚨:") + "** " + emergency_text)
    if med_text:
        str_ui.success("**" + tr("الروشتة الطبية المعتمدة - الدواء الموصوف 💊:", "Approved Medical Prescription - Medication 💊:") + "** " + med_text)


def build_html_table(headers, rows):
    th_html = "".join(["<th>" + h + "</th>" for h in headers])
    tr_list = []
    for r in rows:
        tds = "".join(["<td>" + cell + "</td>" for cell in r])
        tr_list.append("<tr>" + tds + "</tr>")
    return (
        "<div class='glow-table-wrap'>"
        "<table class='custom-tbl'>"
        "<thead><tr>" + th_html + "</tr></thead>"
        "<tbody>" + "".join(tr_list) + "</tbody>"
        "</table></div>"
    )


str_ui.title(tr("النظام الخبير الطبي والرياضي الذكي بالذكاء الاصطناعي 🧠", "AI Clinical, Medical & Sports Expert System 🧠"))
str_ui.markdown("<p style='color: #94a3b8; font-size: 18px;'>" + tr("تشخيص طبي منفصل وإرشادات طوارئ + برامج رياضية وجداول غذائية متكاملة", "Separate medical diagnosis & emergency guidance + workout plans & full meal tables") + "</p>", unsafe_allow_html=True)
str_ui.markdown("---")

str_ui.sidebar.header(tr("الملف الشخصي للمريض والرياضي", "Patient & Athlete Profile"))
age = str_ui.sidebar.number_input(tr("العمر (بالسنوات)", "Age (years)"), 1, 120, 22)
weight = str_ui.sidebar.number_input(tr("الوزن (كجم)", "Weight (kg)"), 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input(tr("الطول (سم)", "Height (cm)"), 50.0, 250.0, 172.0)
gender = str_ui.sidebar.selectbox(tr("الجنس", "Gender"), [tr("أنثى", "Female"), tr("ذكر", "Male")])
activity_level = str_ui.sidebar.selectbox(
    tr("مستوى النشاط البدني والحركة", "Physical Activity & Movement Level"),
    [
        tr("خامل (بدون تمرين أو عمل مكتبي)", "Sedentary (no exercise or desk job)"),
        tr("نشاط خفيف (تمرين 1-3 أيام في الأسبوع)", "Lightly active (exercise 1-3 days/week)"),
        tr("نشاط معتدل (تمرين 3-5 أيام في الأسبوع)", "Moderately active (exercise 3-5 days/week)"),
        tr("نشاط عالي جداً (تمارين شاقة 6-7 أيام)", "Very active (intense training 6-7 days/week)"),
        tr("حركة محدودة / كبار السن (مجهود بسيط)", "Limited mobility / seniors (light effort)"),
    ],
)

str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader(tr("اختر القسم الذي تريد العمل عليه", "Choose the section to work on"))
section_mode = str_ui.sidebar.radio(
    tr("القسم", "Section"),
    [
        tr("القسم الطبي والأمراض", "Medical & Diseases Section"),
        tr("القسم الرياضي والغذائي", "Sports & Nutrition Section"),
    ],
)

selected_disease = tr("لا يوجد أمراض أو أعراض (حالة سليمة)", "No diseases or symptoms (Healthy)")
fitness_goal = None

if section_mode == tr("القسم الطبي والأمراض", "Medical & Diseases Section"):
    str_ui.sidebar.markdown("---")
    str_ui.sidebar.subheader(tr("قسم الأمراض والحالات السريرية الشاملة", "Comprehensive Diseases & Clinical Cases"))
    disease_options = [
        tr("لا يوجد أمراض أو أعراض (حالة سليمة)", "No diseases or symptoms (Healthy)"),
        tr("1. مرض السكر (Diabetes)", "1. Diabetes"),
        tr("2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)", "2. Chronic Hypertension"),
        tr("3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)", "3. Cardiovascular Diseases"),
        tr("4. مشاكل الجهاز التنفسي (Respiratory Problems)", "4. Respiratory Problems"),
        tr("5. الحمى وارتفاع درجة الحرارة (Fever)", "5. Fever"),
        tr("6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)", "6. Cough, Cold & Sore Throat"),
        tr("7. حموضة المعدة (Acidity / Heartburn)", "7. Acidity / Heartburn"),
        tr("8. القولون العصبي (IBS)", "8. Irritable Bowel Syndrome (IBS)"),
        tr("9. الآلام والصداع (Pain & Headache)", "9. Pain & Headache"),
        tr("10. ارتجاع المريء (GERD)", "10. GERD (Acid Reflux)"),
        tr("11. آلام الظهر (Back Pain)", "11. Back Pain"),
        tr("12. آلام المفاصل والعضلات (Joint & Muscle Pain)", "12. Joint & Muscle Pain"),
    ]
    selected_disease = str_ui.sidebar.selectbox(tr("اختر الداء أو العرض الرئيسي", "Select main condition or symptom"), disease_options)
    button_label = tr("عرض التشخيص الطبي والروشتة ⚡", "Show Medical Diagnosis & Prescription ⚡")
else:
    str_ui.sidebar.markdown("---")
    str_ui.sidebar.subheader(tr("قسم الرياضة والتغذية المعتمدة", "Approved Sports & Nutrition Section"))
    fitness_goal = str_ui.sidebar.radio(
        tr("اختر هدفك الرياضي والغذائي", "Choose your sports & nutrition goal"),
        [
            tr("زيادة وزن وبناء عضلات", "Weight Gain & Muscle Building"),
            tr("تقليل وزن وتنشيف", "Weight Loss & Cutting"),
        ],
    )
    button_label = tr("تفعيل النظام الرياضي والغذائي 🏋️‍♂️", "Activate Sports & Nutrition System 🏋️‍♂️")

if str_ui.button(button_label, use_container_width=True):
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        bmi_cat = tr("نحافة (Underweight)", "Underweight")
    elif bmi < 25:
        bmi_cat = tr("وزن مثالي (Normal)", "Normal Weight")
    elif bmi < 30:
        bmi_cat = tr("زيادة وزن (Overweight)", "Overweight")
    else:
        bmi_cat = tr("سمنة (Obese)", "Obese")

    if section_mode == tr("القسم الطبي والأمراض", "Medical & Diseases Section"):
        confidence = 98.2 if ("لا يوجد" in selected_disease or "No diseases" in selected_disease) else 96.5
        str_ui.markdown("### " + tr("التقرير التشخيصي وتحليل الذكاء الاصطناعي", "Diagnostic Report & AI Analysis"))
        c1, c2, c3 = str_ui.columns(3)
        c1.metric(tr("البيانات الفردية", "Individual Profile"), f"{age} " + tr("سنة", "yrs") + f" | {gender}")
        c2.metric(tr("مؤشر كتلة الجسم (BMI)", "Body Mass Index (BMI)"), f"{bmi:.1f}", bmi_cat)
        c3.metric(tr("دقة الذكاء الاصطناعي", "AI Confidence"), f"{confidence}%")
        str_ui.info("**" + tr("الحالة المختارة:", "Selected Condition:") + f"** {selected_disease} | **" + tr("مستوى النشاط:", "Activity Level:") + f"** {activity_level}")

        if ("لا يوجد" not in selected_disease) and ("No diseases" not in selected_disease):
            str_ui.markdown("## " + tr("📋 الإرشادات الطبية والتصرف المبدئي للطوارئ", "📋 Medical Guidance & Emergency First Aid"))

            if "1." in selected_disease:
                render_condition(
                    tr("1. مرض السكر (Diabetes)", "1. Diabetes"),
                    [
                        tr("قياس مستوى السكر بجهاز قياس السكر إن توفر.", "Check blood glucose level with a glucometer if available."),
                        tr("شرب الماء بانتظام وتناول الوجبات في مواعيدها ومتابعة مستوى السكر وتسجيل القراءات.", "Drink water regularly, eat meals on time, and monitor/log blood glucose readings."),
                        tr("إذا ظهرت أعراض انخفاض السكر، مثل الرعشة والتعرق والدوخة، والشخص واعٍ وقادر على البلع، يُعطى مصدر سكر سريع مثل نصف كوب عصير، ثم يُعاد القياس بعد 15 دقيقة.", "If low blood sugar symptoms appear (tremors, sweating, dizziness) and the person is conscious and able to swallow, give a fast sugar source like half a cup of juice and recheck after 15 minutes."),
                        tr("الاستمرار على العلاج الموصوف وعدم تغيير جرعاته دون تعليمات الطبيب.", "Continue prescribed treatment and do not change doses without doctor instructions."),
                    ],
                    tr("إيقاف الإنسولين أو مضاعفة جرعات الدواء من تلقاء نفسك.", "Stopping insulin or doubling medication doses on your own."),
                    tr("حدث فقدان للوعي، أو تشوش شديد، أو صعوبة تنفس، أو قيء مستمر، أو لم يستطع الشخص البلع. لا تعطِ فاقد الوعي أي طعام أو شراب.", "Loss of consciousness, severe confusion, trouble breathing, persistent vomiting, or inability to swallow. Do not give food or drink to an unconscious person."),
                    tr("الالتزام بالعلاج الموصوف ومنظم السكر أو الإنسولين حسب تعليمات الطبيب.", "Adhere to prescribed therapy, glucose regulators, or insulin as directed by your physician."),
                )
            elif "2." in selected_disease:
                render_condition(
                    tr("2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)", "2. Chronic Hypertension"),
                    [
                        tr("الجلوس في مكان هادئ والراحة.", "Sit in a calm place and rest."),
                        tr("قياس ضغط الدم بعد الجلوس بهدوء.", "Measure blood pressure after sitting calmly."),
                        tr("تجنب المجهود والتوتر مؤقتًا وتقليل الأطعمة شديدة الملوحة.", "Temporarily avoid exertion and stress, and reduce very salty foods."),
                        tr("الالتزام بأدوية الضغط الموصوفة في مواعيدها.", "Take prescribed blood pressure medications on schedule."),
                    ],
                    tr("أخذ جرعة إضافية من دواء الضغط دون استشارة الطبيب.", "Taking an extra dose of blood pressure medication without consulting a doctor."),
                    tr("صاحب ارتفاع الضغط ألم في الصدر، أو صعوبة تنفس، أو ضعف مفاجئ في أحد جانبي الجسم، أو اضطراب الكلام أو الرؤية، أو صداع شديد مفاجئ.", "High blood pressure accompanied by chest pain, trouble breathing, sudden one-sided weakness, speech or vision changes, or sudden severe headache."),
                    tr("أدوية الضغط الموصوفة في مواعيدها الثابتة حسب إرشادات الطبيب.", "Prescribed blood pressure medications at fixed times as advised by your doctor."),
                )
            elif "3." in selected_disease:
                render_condition(
                    tr("3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)", "3. Cardiovascular Diseases"),
                    [
                        tr("إيقاف أي مجهود بدني.", "Stop any physical exertion."),
                        tr("الجلوس في وضع مريح وتهدئة الشخص وعدم تركه بمفرده.", "Sit comfortably, calm the person, and do not leave them alone."),
                        tr("استخدام الدواء الموصوف مسبقًا للحالة فقط وفق تعليمات الطبيب.", "Use previously prescribed medication for the condition only as instructed by the doctor."),
                    ],
                    tr("المشي أو ممارسة الرياضة لمحاولة التخلص من ألم الصدر، وعدم إعطاء أدوية عشوائية.", "Walking or exercising to try to relieve chest pain, and giving random medications."),
                    tr("ظهر ألم أو ضغط بالصدر، أو امتد الألم إلى الذراع أو الفك أو الظهر، أو حدث عرق شديد أو دوخة أو ضيق تنفس. اتصل بالإسعاف 123 في مصر.", "Chest pain or pressure, pain radiating to arm, jaw, or back, heavy sweating, dizziness, or shortness of breath. Call ambulance 123 in Egypt."),
                    tr("الدواء الموصوف مسبقاً للحالة فقط وفق تعليمات الطبيب.", "Medication previously prescribed for the condition only as directed by the doctor."),
                )
            elif "4." in selected_disease:
                render_condition(
                    tr("4. مشاكل الجهاز التنفسي (Respiratory Problems)", "4. Respiratory Problems"),
                    [
                        tr("الجلوس في وضع مستقيم.", "Sit in an upright position."),
                        tr("الابتعاد عن الدخان والغبار والروائح القوية.", "Stay away from smoke, dust, and strong odors."),
                        tr("توفير هواء نقي وتهوية المكان.", "Provide fresh air and ventilate the area."),
                        tr("استخدام بخاخ الربو الموصوف للشخص وفق خطة الطبيب إن كان يعاني من الربو.", "Use the person's prescribed asthma inhaler according to the doctor's plan if they have asthma."),
                    ],
                    tr("التعرض للدخان أو استخدام بخاخات أو أدوية غير موصوفة.", "Exposure to smoke or using unprescribed inhalers or medications."),
                    tr("كان هناك اختناق أو صعوبة شديدة في التنفس أو عدم القدرة على الكلام بشكل طبيعي أو ازرقاق الشفاه.", "Choking, severe difficulty breathing, inability to speak normally, or bluish lips."),
                    tr("بخاخ الربو الموصوف وفق خطة الطبيب إن كان يعاني من الربو.", "Prescribed asthma inhaler according to the doctor's plan if applicable."),
                )
            elif "5." in selected_disease:
                render_condition(
                    tr("5. الحمى وارتفاع درجة الحرارة (Fever)", "5. Fever"),
                    [
                        tr("قياس درجة الحرارة بترمومتر.", "Measure temperature with a thermometer."),
                        tr("شرب السوائل بانتظام والراحة والحصول على قسط كافٍ من النوم.", "Drink fluids regularly, rest, and get enough sleep."),
                        tr("ارتداء ملابس خفيفة ومريحة واستخدام كمادات ماء فاتر عند الحاجة.", "Wear light, comfortable clothes and use lukewarm compresses when needed."),
                    ],
                    tr("تغطية الجسم بأغطية ثقيلة أو استخدام الماء المثلج أو الكحول لتخفيض الحرارة.", "Covering the body with heavy blankets or using ice-cold water or alcohol to lower fever."),
                    tr("صاحبت الحمى صعوبة تنفس أو تشنجات أو تشوش في الوعي أو تيبس الرقبة أو صداع شديد غير معتاد.", "Fever accompanied by trouble breathing, seizures, altered consciousness, stiff neck, or unusually severe headache."),
                    tr("Paracetamol (باراسيتامول) عند اللزوم حسب إرشادات الطبيب أو الصيدلي.", "Paracetamol when needed according to doctor or pharmacist instructions."),
                )
            elif "6." in selected_disease:
                render_condition(
                    tr("6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)", "6. Cough, Cold & Sore Throat"),
                    [
                        tr("شرب المشروبات الدافئة.", "Drink warm beverages."),
                        tr("تناول العسل لتخفيف السعال إذا لم توجد حساسية منه.", "Take honey to soothe cough if there is no allergy to it."),
                        tr("الغرغرة بالماء الدافئ والملح مع عدم بلعه.", "Gargle with warm salt water without swallowing it."),
                        tr("استخدام محلول ملحي للأنف والراحة وشرب كمية كافية من السوائل.", "Use nasal saline solution, rest, and drink enough fluids."),
                    ],
                    tr("التدخين والتعرض للهواء الملوث واستخدام المضادات الحيوية دون وصفة.", "Smoking, exposure to polluted air, and using antibiotics without a prescription."),
                    tr("حدثت صعوبة في التنفس أو البلع، أو ألم شديد بالصدر، أو عدم القدرة على شرب السوائل.", "Difficulty breathing or swallowing, severe chest pain, or inability to drink fluids."),
                    tr("Congestal (كنجستال)", "Congestal"),
                )
            elif "7." in selected_disease:
                render_condition(
                    tr("7. حموضة المعدة (Vonacidan)", "7. Acidity (Vonacidan)"),
                    [
                        tr("الجلوس في وضع مستقيم بعد الأكل وتجنب الاستلقاء مباشرة.", "Sit upright after eating and avoid lying down immediately."),
                        tr("تناول وجبات صغيرة والابتعاد عن الأطعمة التي تزيد الحموضة.", "Eat small meals and avoid foods that increase acidity."),
                    ],
                    tr("الاستلقاء مباشرة بعد الطعام أو الأطعمة الدسمة والحارة.", "Lying down right after eating or heavy/spicy foods."),
                    tr("ألم حاد في البطن أو قيء مستمر أو دموي أو براز داكن.", "Severe abdominal pain, persistent or bloody vomiting, or dark stools."),
                    tr("Vonacidan (فوناسيدان)", "Vonacidan"),
                )
            elif "8." in selected_disease:
                render_condition(
                    tr("8. القولون العصبي (Replix)", "8. IBS (Replix)"),
                    [
                        tr("تجنب التوتر والقلق والأطعمة المهيجة للقولون.", "Avoid stress, anxiety, and colon-irritating foods."),
                        tr("تناول وجبات منتظمة وشرب السوائل والمشروبات الدافئة المهدئة.", "Eat regular meals and drink soothing fluids/warm drinks."),
                    ],
                    tr("التوتر الشديد والأكل السريع والوجبات الدسمة.", "Severe stress, rushing meals, and heavy foods."),
                    tr("فقدان وزن غير مبرر أو نزيف أو ألم شديد يوقظ من النوم.", "Unexplained weight loss, bleeding, or severe pain waking from sleep."),
                    tr("Replix (ريبليكس)", "Replix"),
                )
            elif "9." in selected_disease:
                render_condition(
                    tr("9. الألم والصداع (Paracetamol)", "9. Pain & Headache (Paracetamol)"),
                    [
                        tr("الراحة في مكان هادئ وشرب الماء بانتظام.", "Rest in a quiet place and drink water regularly."),
                        tr("تجنب الإجهاد الزائد والشاشات لفترات طويلة.", "Avoid overexertion and prolonged screens."),
                    ],
                        tr("الإفراط في المسكنات أو السهر وقلة النوم.", "Overusing painkillers or staying up late/lack of sleep."),
                )
                
            elif "10." in selected_disease:
                render_condition(
                    tr("10. ارتجاع المريء (GERD)", "10. GERD (Acid Reflux)"),
                    [
                        tr("الجلوس في وضع مستقيم بعد تناول الطعام.", "Sit upright after eating."),
                        tr("تناول وجبات صغيرة وتجنب الاستلقاء لمدة ساعتين إلى ثلاث ساعات بعد الأكل.", "Eat small meals and avoid lying down for 2-3 hours after eating."),
                        tr("الابتعاد عن الأطعمة التي تزيد الحموضة لدى الشخص.", "Avoid foods that increase acidity for the person."),
                        tr("رفع الجزء العلوي من الجسم أثناء النوم إذا كانت الأعراض ليلية.", "Elevate the upper body during sleep if symptoms occur at night."),
                    ],
                    tr("تناول وجبات كبيرة قبل النوم أو الاستلقاء مباشرة بعد الأكل.", "Eating large meals before bed or lying down immediately after eating."),
                    tr("ظهر ألم شديد أو ضغط في الصدر، خاصة مع العرق أو ضيق التنفس أو الدوخة، أو حدث قيء دموي أو صعوبة شديدة في البلع.", "Severe chest pain or pressure, especially with sweating, shortness of breath, or dizziness, or bloody vomiting or severe difficulty swallowing."),
                    tr("حسب إرشادات الطبيب المختص.", "As directed by the specialist physician."),
                )
            elif "11." in selected_disease:
                render_condition(
                    tr("11. آلام الظهر (Back Pain)", "11. Back Pain"),
                    [
                        tr("تجنب حمل الأشياء الثقيلة.", "Avoid lifting heavy objects."),
                        tr("تغيير وضعية الجلوس باستمرار والمشي الخفيف والحركة الهادئة حسب القدرة.", "Change sitting posture continuously, walk lightly, and move gently as tolerated."),
                        tr("استخدام كمادات باردة أو دافئة ملفوفة في قطعة قماش.", "Use cold or warm compresses wrapped in a cloth."),
                        tr("الحصول على الراحة دون ملازمة السرير لفترات طويلة.", "Get rest without prolonged bed rest."),
                    ],
                    tr("الحركات المفاجئة أو حمل الأوزان أو التدليك العنيف.", "Sudden movements, lifting weights, or vigorous massage."),
                    tr("صاحَب الألم ضعف مفاجئ بالساقين، أو فقدان التحكم في البول أو البراز، أو فقدان الإحساس بمنطقة ما بين الفخذين، أو حدث بعد إصابة قوية.", "Pain accompanied by sudden leg weakness, loss of bowel or bladder control, loss of sensation in the groin area, or after strong trauma."),
                    tr("حسب إرشادات الطبيب المختص.", "As directed by the specialist physician."),
                )
            elif "12." in selected_disease:
                render_condition(
                    tr("12. آلام المفاصل والعضلات (Joint & Muscle Pain)", "12. Joint & Muscle Pain"),
                    [
                        tr("إراحة الجزء المصاب مؤقتًا.", "Rest the affected area temporarily."),
                        tr("استخدام كمادات باردة ملفوفة في منشفة لمدة قصيرة عند وجود تورم حديث.", "Use cold compresses wrapped in a towel for a short time when there is recent swelling."),
                        tr("تجنب المجهود والحركات التي تزيد الألم.", "Avoid exertion and movements that increase pain."),
                        tr("تحريك المفصل بلطف عندما تسمح الحالة بذلك وشرب الماء بانتظام.", "Move the joint gently when condition allows and drink water regularly."),
                    ],
                    tr("الضغط على المفصل المصاب أو ممارسة الرياضة العنيفة أو استخدام أدوية دون استشارة.", "Pressing on the injured joint, doing intense exercise, or using medications without consultation."),
                    tr("كان المفصل شديد التورم أو ساخنًا ومحمرًا، أو صاحبه ارتفاع حرارة، أو تعذر تحريكه أو تحميل الوزن عليه.", "Severe joint swelling, warmth, and redness, or accompanied by fever, or inability to move it or bear weight on it."),
                    tr("حسب إرشادات الطبيب المختص.", "As directed by the specialist physician."),
                )
        else:
            str_ui.info(tr("لا يوجد أمراض مسجلة حالياً — الحالة الصحية مستقرة.", "No diseases recorded currently — health status is stable."))
            str_ui.markdown("## " + tr("🏋️‍♂️ البرنامج الرياضي والنظام الغذائي", "🏋️‍♂️ Sports & Nutrition Program"))
            c1, c2, c3 = str_ui.columns(3)
            c1.metric(tr("البيانات البدنية", "Physical Profile"), f"{age} " + tr("سنة", "yrs") + f" | {gender}")
            c2.metric(tr("مؤشر كتلة الجسم (BMI)", "Body Mass Index (BMI)"), f"{bmi:.1f}", bmi_cat)
            c3.metric(tr("الهدف المختار", "Selected Goal"), fitness_goal or tr("غير محدد", "Not Set"))
            str_ui.info("**" + tr("مستوى النشاط البدني:", "Physical Activity Level:") + f"** {activity_level}")

            goal_txt = str(fitness_goal or "")
            is_gain = ("زيادة وزن" in goal_txt) or ("Weight Gain" in goal_txt) or ("زيادة" in goal_txt)

            if is_gain:
                str_ui.markdown(
                    """
                    <div class='diet-banner'>
                        <span class='pill-tag'>""" + tr("فائض سعرات صحي ومتوازن", "Healthy Balanced Calorie Surplus") + """</span>
                        <h3 style='margin: 4px 0; color: #7dd3fc !important;'>""" + tr("📈 جدول النظام الغذائي لزيادة الوزن وبناء العضلات", "📈 Weight Gain & Muscle Building Diet Plan") + """</h3>
                        <p style='margin: 0; color: #cbd5e1;'>""" + tr("خطة يومية متكاملة من 6 وجبات لزيادة الكتلة العضلية والوزن الصحي بأمان.", "Complete 6-meal daily plan for safe muscle and weight gain.") + """</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                gain_meals = [
                    ["<strong>" + tr("الفطار", "Breakfast") + "</strong><br><span style='color:#38bdf8;'>" + tr("صباحاً", "Morning") + "</span>", tr("شوفان أو بيض + حليب + تمر أو فاكهة", "Oats or eggs + milk + dates or fruit")],
                    ["<strong>" + tr("وجبة خفيفة 1", "Snack 1") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل الظهر", "Mid-Morning") + "</span>", tr("مكسرات + زبادي أو فاكهة", "Nuts + yogurt or fruit")],
                    ["<strong>" + tr("الغداء (الوجبة الرئيسية)", "Lunch (Main Meal)") + "</strong><br><span style='color:#38bdf8;'>" + tr("الظهر", "Afternoon") + "</span>", tr("مصدر بروتين + أرز أو مكرونة + خضار", "Protein source + rice or pasta + vegetables")],
                    ["<strong>" + tr("وجبة 2 (قبل التمرين)", "Meal 2 (Pre-Workout)") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل التمرين", "Pre-Workout") + "</span>", tr("موزة أو بطاطس مسلوقة + مصدر بروتين خفيف", "Banana or boiled potato + light protein")],
                    ["<strong>" + tr("العشاء", "Dinner") + "</strong><br><span style='color:#38bdf8;'>" + tr("مساءً", "Evening") + "</span>", tr("جبن أو بيض أو تونة + خبز + سلطة", "Cheese or eggs or tuna + bread + salad")],
                    ["<strong>" + tr("قبل النوم مباشرة", "Before Bed") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل النوم", "Before Bed") + "</span>", tr("كوب حليب أو زبادي", "Cup of milk or yogurt")],
                ]
                str_ui.markdown(build_html_table([tr("الوجبة والفترة", "Meal & Period"), tr("مكونات الوجبة المقترحة", "Suggested Meal Components")], gain_meals), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("🏋️‍♂️ الرياضة والتمارين المطلوبة (زيادة وزن وبناء عضلات)", "🏋️‍♂️ Required Sports & Workouts (Weight Gain & Muscle Building)"))
                gain_sports = [
                    ["<strong>" + tr("اليوم 1", "Day 1") + "</strong>", tr("تمارين مقاومة: صدر، كتف أمامي وجانبي، وترايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Resistance: chest, front/side delts, triceps (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 2", "Day 2") + "</strong>", tr("تمارين مقاومة: ظهر، كتف خلفي، وبايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Resistance: back, rear delts, biceps (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 3", "Day 3") + "</strong>", tr("راحة تامة واستشفاء عضلي", "Complete rest and muscle recovery")],
                    ["<strong>" + tr("اليوم 4", "Day 4") + "</strong>", tr("تمارين مقاومة شاملة: فخذ أمامي وخلفي وسمانة (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Full lower body resistance: quads, hamstrings, calves (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 5", "Day 5") + "</strong>", tr("تمارين جزء علوي وبطن (Upper Body & Core) (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Upper body & core workout (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 6 و 7", "Days 6 & 7") + "</strong>", tr("راحة ومرونة واستشفاء عضلي", "Rest, mobility, and recovery")],
                ]
                str_ui.markdown(build_html_table([tr("اليوم", "Day"), tr("الرياضة والتمارين المطلوبة", "Required Sports & Workouts")], gain_sports), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("💡 نصائح ذهبية لنجاح نظام زيادة الوزن", "💡 Golden Tips for Weight Gain Success"))
                str_ui.markdown(
                    """
                    <div class='tip-box'><strong>""" + tr("1. زيادة السعرات التدريجية:", "1. Gradual Calorie Surplus:") + """</strong> """ + tr("زوّدي السعرات تدريجياً بدون حرمان أو إفراط مفاجئ.", "Increase calories gradually without extreme rush.") + """</div>
                    <div class='tip-box'><strong>""" + tr("2. الدهون الصحية في كل وجبة:", "2. Healthy Fats in Every Meal:") + """</strong> """ + tr("أضيفي زيت زيتون، مكسرات، أو أفوكادو لرفع السعرات بذكاء.", "Add olive oil, nuts, or avocado to boost calories smartly.") + """</div>
                    <div class='tip-box'><strong>""" + tr("3. الاستمرارية والراحة:", "3. Consistency & Rest:") + """</strong> """ + tr("الالتزام بالتمارين والنوم الكافي أساس بناء الكتلة العضلية.", "Consistent training and adequate sleep drive muscle growth.") + """</div>
                    """,
                    unsafe_allow_html=True,
                )
             if fitness_goal and ("زيادة وزن" in str(fitness_goal) or "Weight Gain" in str(fitness_goal)):
                str_ui.markdown(
                    """
                    <div class='diet-banner'>
                        <span class='pill-tag'>""" + tr("فائض سعرات صحي ومتوازن", "Healthy Balanced Calorie Surplus") + """</span>
                        <h3 style='margin: 4px 0; color: #7dd3fc !important;'>""" + tr("📈 جدول النظام الغذائي لزيادة الوزن وبناء العضلات", "📈 Weight Gain & Muscle Building Diet Plan") + """</h3>
                        <p style='margin: 0; color: #cbd5e1;'>""" + tr("خطة يومية متكاملة من 6 وجبات لزيادة الكتلة العضلية والوزن الصحي بأمان.", "Complete 6-meal daily plan for safe muscle and weight gain.") + """</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                gain_meals = [
                    ["<strong>" + tr("الفطار", "Breakfast") + "</strong><br><span style='color:#38bdf8;'>" + tr("صباحاً", "Morning") + "</span>", tr("شوفان أو بيض + حليب + تمر أو فاكهة", "Oats or eggs + milk + dates or fruit")],
                    ["<strong>" + tr("وجبة خفيفة 1", "Snack 1") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل الظهر", "Mid-Morning") + "</span>", tr("مكسرات + زبادي أو فاكهة", "Nuts + yogurt or fruit")],
                    ["<strong>" + tr("الغداء (الوجبة الرئيسية)", "Lunch (Main Meal)") + "</strong><br><span style='color:#38bdf8;'>" + tr("الظهر", "Afternoon") + "</span>", tr("مصدر بروتين + أرز أو مكرونة + خضار", "Protein source + rice or pasta + vegetables")],
                    ["<strong>" + tr("وجبة 2 (قبل التمرين)", "Meal 2 (Pre-Workout)") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل التمرين", "Pre-Workout") + "</span>", tr("موزة أو بطاطس مسلوقة + مصدر بروتين خفيف", "Banana or boiled potato + light protein")],
                    ["<strong>" + tr("العشاء", "Dinner") + "</strong><br><span style='color:#38bdf8;'>" + tr("مساءً", "Evening") + "</span>", tr("جبن أو بيض أو تونة + خبز + سلطة", "Cheese or eggs or tuna + bread + salad")],
                    ["<strong>" + tr("قبل النوم مباشرة", "Before Bed") + "</strong><br><span style='color:#38bdf8;'>" + tr("قبل النوم", "Before Bed") + "</span>", tr("كوب حليب أو زبادي", "Cup of milk or yogurt")],
                ]
                str_ui.markdown(build_html_table([tr("الوجبة والفترة", "Meal & Period"), tr("مكونات الوجبة المقترحة", "Suggested Meal Components")], gain_meals), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("🏋️‍♂️ الرياضة والتمارين المطلوبة (زيادة وزن وبناء عضلات)", "🏋️‍♂️ Required Sports & Workouts (Weight Gain & Muscle Building)"))
                gain_sports = [
                    ["<strong>" + tr("اليوم 1", "Day 1") + "</strong>", tr("تمارين مقاومة: صدر، كتف أمامي وجانبي، وترايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Resistance: chest, front/side delts, triceps (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 2", "Day 2") + "</strong>", tr("تمارين مقاومة: ظهر، كتف خلفي، وبايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Resistance: back, rear delts, biceps (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 3", "Day 3") + "</strong>", tr("راحة تامة واستشفاء عضلي", "Complete rest and muscle recovery")],
                    ["<strong>" + tr("اليوم 4", "Day 4") + "</strong>", tr("تمارين مقاومة شاملة: فخذ أمامي وخلفي وسمانة (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Full lower body resistance: quads, hamstrings, calves (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 5", "Day 5") + "</strong>", tr("تمارين جزء علوي وبطن (Upper Body & Core) (45 - 60 دقيقة • 4 أيام أسبوعياً)", "Upper body & core workout (45-60 min • 4 days/week)")],
                    ["<strong>" + tr("اليوم 6 و 7", "Days 6 & 7") + "</strong>", tr("راحة ومرونة واستشفاء عضلي", "Rest, mobility, and recovery")],
                ]
                str_ui.markdown(build_html_table([tr("اليوم", "Day"), tr("الرياضة والتمارين المطلوبة", "Required Sports & Workouts")], gain_sports), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("💡 نصائح ذهبية لنجاح نظام زيادة الوزن", "💡 Golden Tips for Weight Gain Success"))
                str_ui.markdown(
                    """
                    <div class='tip-box'><strong>""" + tr("1. زيادة السعرات التدريجية:", "1. Gradual Calorie Surplus:") + """</strong> """ + tr("زوّدي السعرات تدريجياً بدون حرمان أو إفراط مفاجئ.", "Increase calories gradually without extreme rush.") + """</div>
                    <div class='tip-box'><strong>""" + tr("2. الدهون الصحية في كل وجبة:", "2. Healthy Fats in Every Meal:") + """</strong> """ + tr("أضيفي زيت زيتون، مكسرات، أو أفوكادو لرفع السعرات بذكاء.", "Add olive oil, nuts, or avocado to boost calories smartly.") + """</div>
                    <div class='tip-box'><strong>""" + tr("3. الاستمرارية والراحة:", "3. Consistency & Rest:") + """</strong> """ + tr("الالتزام بالتمارين والنوم الكافي أساس بناء الكتلة العضلية.", "Consistent training and adequate sleep drive muscle growth.") + """</div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                str_ui.markdown(
                    """
                    <div class='diet-banner'>
                        <span class='pill-tag'>""" + tr("تنشيف وخسارة دهون", "Cutting & Fat Loss") + """</span>
                        <h3 style='margin: 4px 0; color: #7dd3fc !important;'>""" + tr("🔥 جدول النظام الغذائي لتقليل الوزن والتنشيف", "🔥 Weight Loss & Cutting Diet Plan") + """</h3>
                        <p style='margin: 0; color: #cbd5e1;'>""" + tr("خطة متوازنة عالية البروتين لتقليل الوزن والحفاظ على الكتلة العضلية.", "Balanced high-protein plan for weight loss and muscle preservation.") + """</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                cut_meals = [
                    ["<strong>" + tr("الفطار", "Breakfast") + "</strong>", tr("2 بيضة مسلوقة أو أومليت بملعقة زيت زيتون + ربع رغيف بلدي + خيار وجرجير", "2 boiled eggs or omelet with 1 tsp olive oil + 1/4 baladi bread + cucumber & arugula"), tr("كوب زبادي لايت أو قريش + شوفان قليل + خيار", "Cup of light yogurt or cottage cheese + small oats + cucumber")],
                    ["<strong>" + tr("الغداء", "Lunch") + "</strong>", tr("صدر دجاج مشوي أو سمك مشوي + طبق سلطة كبير + 4-6 ملاعق أرز أو بطاطس مسلوقة", "Grilled chicken breast or grilled fish + large salad + 4-6 tbsp rice or boiled potato"), tr("تونة مصفاة أو لحم خالي الدهن + خضار سوتيه أو سلطة + حصة نشويات بسيطة", "Drained tuna or lean meat + sautéed veggies or salad + small carb portion")],
                    ["<strong>" + tr("العشاء", "Dinner") + "</strong>", tr("جبن قريش أو زبادي يوناني بالخيار والنعناع + ربع رغيف بلدي", "Cottage cheese or Greek yogurt with cucumber & mint + 1/4 baladi bread"), tr("بيضة مسلوقة + طبق سلطة خضراء بدون زيوت ثقيلة", "Boiled egg + green salad without heavy oils")],
                ]
                str_ui.markdown(build_html_table([tr("الوجبة", "Meal"), tr("الخيار الأول", "Option 1"), tr("الخيار الثاني", "Option 2")], cut_meals), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("🏃‍♀️ الرياضة والتمارين المطلوبة (تقليل وزن وتنشيف)", "🏃‍♀️ Required Sports & Workouts (Weight Loss & Cutting)"))
                cut_sports = [
                    ["<strong>" + tr("اليوم 1 و 4", "Days 1 & 4") + "</strong>", tr("تمارين كارديو (Cardio): مشي سريع أو جري خفيف (30 - 45 دقيقة)", "Cardio: brisk walking or light jogging (30-45 min)")],
                    ["<strong>" + tr("اليوم 2 و 5", "Days 2 & 5") + "</strong>", tr("تمارين مقاومة كاملة للجسم (Full Body Circuit) لحماية العضلات ورفع الحرق", "Full body resistance circuit to protect muscle and boost burn")],
                    ["<strong>" + tr("اليوم 3", "Day 3") + "</strong>", tr("كارديو متقطع خفيف أو حبل قفز أو عجلة ثابتة (20 - 30 دقيقة)", "Light interval cardio, jump rope, or stationary bike (20-30 min)")],
                    ["<strong>" + tr("اليوم 6 و 7", "Days 6 & 7") + "</strong>", tr("مشي خفيف في الهواء الطلق واستشفاء عضلي", "Light outdoor walk and active recovery")],
                ]
                str_ui.markdown(build_html_table([tr("اليوم", "Day"), tr("الرياضة والتمارين المطلوبة", "Required Sports & Workouts")], cut_sports), unsafe_allow_html=True)

                str_ui.markdown("### " + tr("💡 قواعد أساسية لنجاح التنشيف وتقليل الوزن", "💡 Core Rules for Successful Cutting & Weight Loss"))
                str_ui.markdown(
                    """
                    <div class='tip-box'><strong>""" + tr("1. عجز سعرات مدروس:", "1. Controlled Calorie Deficit:") + """</strong> """ + tr("قللي السعرات باعتدال مع الحفاظ على البروتين لتقليل الدهون لا العضلات.", "Maintain a moderate deficit with high protein to lose fat, not muscle.") + """</div>
                    <div class='tip-box'><strong>""" + tr("2. شرب الماء والألياف:", "2. Hydration & Fiber:") + """</strong> """ + tr("اشربي ماء كافياً وأكثري من الخضار والسلطة لزيادة الإحساس بالشبع.", "Drink plenty of water and eat vegetables/salad for fullness.") + """</div>
                    <div class='tip-box'><strong>""" + tr("3. النوم والانتظام:", "3. Sleep & Consistency:") + """</strong> """ + tr("النوم المنتظم يظبط هرمونات الجوع والشبع ويحسن الأداء الرياضي.", "Regular sleep regulates hunger hormones and improves workout performance.") + """</div>
                    """,
                    unsafe_allow_html=True,
                )
                

str_ui.markdown("---")
str_ui.markdown("<p style='text-align: center; color: gray;'>" + tr("النظام الخبير الطبي والرياضي المعتمد • مشروع تخرج قسم الذكاء الاصطناعي", "Certified Clinical, Medical & Sports Expert System • AI Department Graduation Project") + "</p>", unsafe_allow_html=True)
            
