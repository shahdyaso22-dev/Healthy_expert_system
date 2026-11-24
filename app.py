import streamlit as st

st.set_page_config(
    page_title="AI Clinical, Medical & Sports Expert System",
    page_icon="🧠",
    layout="wide",
)

# ==========================================
# 1. إعداد اللغة والترجمة الشاملة (عربي / إنجليزي)
# ==========================================
lang_choice = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True,
)


def tr(ar_txt: str, en_txt: str) -> str:
    return ar_txt if lang_choice == "العربية" else en_txt


is_ar = lang_choice == "العربية"

# ==========================================
# 2. التنسيق البصري والألوان الداكنة
# ==========================================
st.markdown(
    f"""
    <style>
        .stApp {{
            background: radial-gradient(circle at top right, #0f172a, #020617 70%);
            color: #f8fafc;
            direction: {"rtl" if is_ar else "ltr"};
            text-align: {"right" if is_ar else "left"};
        }}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #0b1120 0%, #020617 100%);
            border-{"left" if is_ar else "right"}: 1px solid rgba(56, 189, 248, 0.25);
        }}
        h1, h2, h3 {{
            background: linear-gradient(90deg, #38bdf8, #818cf8, #2dd4bf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700 !important;
        }}
        .stButton > button {{
            background: linear-gradient(90deg, #0284c7 0%, #2563eb 50%, #0ea5e9 100%) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 10px 20px !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 18px rgba(14, 165, 233, 0.35) !important;
        }}
        .stButton > button:hover {{
            transform: translateY(-1px);
            box-shadow: 0 6px 22px rgba(56, 189, 248, 0.5) !important;
        }}
        .hero-sub {{
            color: #94a3b8;
            font-size: 16px;
            margin-top: -8px;
            margin-bottom: 16px;
        }}
        .section-banner {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 58, 138, 0.45));
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 16px;
            padding: 18px 20px;
            margin: 14px 0 18px 0;
            box-shadow: 0 8px 24px rgba(2, 6, 23, 0.65);
        }}
        .pill-badge {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.16);
            border: 1px solid rgba(56, 189, 248, 0.45);
            color: #7dd3fc;
            padding: 3px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        .glow-table-wrap {{
            background: rgba(15, 23, 42, 0.92);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 14px;
            overflow-x: auto;
            margin: 12px 0 20px 0;
            box-shadow: 0 6px 24px rgba(2, 6, 23, 0.7);
        }}
        table.custom-tbl {{
            width: 100%;
            border-collapse: collapse;
            min-width: 540px;
        }}
        table.custom-tbl th {{
            background: linear-gradient(90deg, #0369a1, #0f766e);
            color: #f0f9ff;
            padding: 13px 14px;
            font-weight: 700;
            text-align: {"right" if is_ar else "left"};
            border-bottom: 1px solid rgba(125, 211, 252, 0.3);
        }}
        table.custom-tbl td {{
            padding: 12px 14px;
            color: #e2e8f0;
            border-bottom: 1px solid rgba(148, 163, 184, 0.15);
            vertical-align: top;
            line-height: 1.6;
        }}
        table.custom-tbl tr:last-child td {{
            border-bottom: none;
        }}
        table.custom-tbl tr:hover td {{
            background: rgba(56, 189, 248, 0.07);
        }}
        .tip-card {{
            background: rgba(15, 23, 42, 0.88);
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-{"right" if is_ar else "left"}: 4px solid #38bdf8;
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 10px;
            color: #e2e8f0;
        }}
        .med-card {{
            background: rgba(6, 78, 59, 0.35);
            border: 1px solid rgba(16, 185, 129, 0.45);
            border-radius: 12px;
            padding: 14px 16px;
            margin: 12px 0;
            color: #d1fae5;
        }}
        .em-card {{
            background: rgba(127, 29, 29, 0.38);
            border: 1px solid rgba(248, 113, 113, 0.55);
            border-radius: 12px;
            padding: 14px 16px;
            margin: 12px 0;
            color: #fee2e2;
        }}
        .footer-note {{
            text-align: center;
            color: #64748b;
            font-size: 13px;
            padding-top: 14px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


def build_html_table(headers: list[str], rows: list[list[str]]) -> str:
    th_cells = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = []
    for row in rows:
        td_cells = "".join(f"<td>{cell}</td>" for cell in row)
        body_rows.append(f"<tr>{td_cells}</tr>")
    return (
        "<div class='glow-table-wrap'>"
        "<table class='custom-tbl'>"
        f"<thead><tr>{th_cells}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table>"
        "</div>"
    )


# ==========================================
# 3. بيانات الحالات الطبية الـ 12
# ==========================================
DISEASES_DATA = [
    {
        "key": "1.",
        "label": tr("1. مرض السكر (Diabetes)", "1. Diabetes"),
        "steps": [
            tr("قياس مستوى السكر في الدم بجهاز القياس إن توفر.", "Check blood glucose level with a glucometer if available."),
            tr("شرب الماء بانتظام وتناول وجبات متوازنة ومراقبة مستوى السكر وتسجيل القراءات.", "Drink water regularly, eat balanced meals, and log glucose readings."),
            tr("الاستمرار على العلاج الموصوف وعدم تغيير جرعاته دون تعليمات الطبيب.", "Continue prescribed treatment and do not alter doses without doctor advice."),
        ],
        "avoid": tr(
            "إيقاف الإنسولين أو مضاعفة جرعات الدواء من تلقاء نفسك، أو تجاهل أعراض هبوط السكر الشديد أو الدوخة أو صعوبة التنفس.",
            "Stopping insulin or doubling medication doses on your own, or ignoring severe hypoglycemia, dizziness, or breathing difficulty.",
        ),
        "emergency": tr(
            "إذا حدث فقدان وعي أو تشنجات أو قيء مستمر أو تنفس سريع مع رائحة أسيتون أو هبوط سكر حاد لا يتحسن بعد كوب عصير.",
            "Loss of consciousness, seizures, persistent vomiting, rapid breathing with fruity odor, or severe low blood sugar not improving after juice.",
        ),
        "med": tr(
            "الالتزام بالعلاج الموصوف ومنظم السكر أو الإنسولين حسب تعليمات الطبيب.",
            "Adhere to prescribed therapy, oral hypoglycemics, or insulin as directed by the physician.",
        ),
    },
    {
        "key": "2.",
        "label": tr("2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)", "2. Chronic Hypertension"),
        "steps": [
            tr("الجلوس في مكان هادئ والراحة التامة.", "Sit calmly in a quiet place and rest."),
            tr("قياس ضغط الدم بعد الجلوس بهدوء لعدة دقائق.", "Measure blood pressure after sitting quietly for several minutes."),
            tr("تجنب المجهود والتوتر وتقليل الأملاح والمشروبات المنبهة.", "Temporarily avoid exertion and stress; reduce salt and caffeine."),
        ],
        "avoid": tr(
            "أخذ جرعة إضافية من دواء الضغط دون استشارة الطبيب أو ممارسة مجهود شاق أثناء ارتفاع الضغط.",
            "Taking an extra dose of blood pressure medication without consulting a doctor or doing strenuous exercise during high readings.",
        ),
        "emergency": tr(
            "إذا كان هناك ألم شديد في الصدر أو صعوبة في التنفس أو ضعف مفاجئ في أحد جانبي الجسم أو اضطراب في الكلام أو الرؤية.",
            "Severe chest pain, shortness of breath, sudden one-sided weakness, or speech/vision disturbances.",
        ),
        "med": tr(
            "الالتزام بأدوية الضغط الموصوفة في مواعيدها الثابتة حسب إرشادات الطبيب.",
            "Take prescribed antihypertensive medications on schedule as directed by the physician.",
        ),
    },
    {
        "key": "3.",
        "label": tr("3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)", "3. Cardiovascular Diseases"),
        "steps": [
            tr("التوقف الفوري عن أي مجهود بدني والجلوس أو الاستلقاء بوضعية مريحة.", "Stop physical exertion immediately and sit or rest comfortably."),
            tr("فك الملابس الضيقة حول الرقبة والصدر والتنفس بهدوء.", "Loosen tight clothing around neck and chest and breathe calmly."),
            tr("مراقبة الأعراض والالتزام بالمتابعة الدورية مع طبيب القلب.", "Monitor symptoms and keep regular follow-up with your cardiologist."),
        ],
        "avoid": tr(
            "بذل مجهود بدني أو صعود السلالم بسرعة أو إهمال الأعراض الصدرية أو التوقف المفاجئ عن أدوية القلب.",
            "Physical exertion, climbing stairs rapidly, ignoring chest symptoms, or abruptly stopping heart medications.",
        ),
        "emergency": tr(
            "ألم أو ضغط أو ثقل في الصدر يمتد للذراع أو الفك أو الظهر، أو ضيق تنفس شديد أو تعرق بارد أو إغماء.",
            "Chest pain, pressure, or tightness radiating to arm, jaw, or back, severe dyspnea, cold sweat, or fainting.",
        ),
        "med": tr(
            "الالتزام بالأدوية القلبية الموصوفة بدقة حسب خطة الطبيب المختص.",
            "Follow prescribed cardiac medications strictly according to the specialist's plan.",
        ),
    },
    {
        "key": "4.",
        "label": tr("4. مشاكل الجهاز التنفسي (Respiratory Problems)", "4. Respiratory Problems"),
        "steps": [
            tr("الجلوس في وضع مستقيم ومريح لتسهيل التنفس.", "Sit upright in a comfortable position to ease breathing."),
            tr("الابتعاد عن الدخان والغبار والروائح النفاذة وتهوية المكان جيداً.", "Stay away from smoke, dust, and strong odors; ventilate the room."),
            tr("شرب السوائل الدافئة إذا لم يكن هناك مانع طبي.", "Drink warm fluids unless medically contraindicated."),
        ],
        "avoid": tr(
            "التعرض للدخان أو مسببات الحساسية أو استخدام بخاخات أو أدوية غير موصوفة.",
            "Exposure to smoke or allergens, or using unprescribed inhalers or medications.",
        ),
        "emergency": tr(
            "اختناق أو صعوبة شديدة في التنفس أو عدم القدرة على إكمال جملة بوضوح أو ازرقاق الشفاه والأظافر.",
            "Choking, severe difficulty breathing, inability to speak in full sentences, or bluish lips/nails.",
        ),
        "med": tr(
            "استخدام بخاخ الربو أو العلاج التنفسي الموصوف وفق خطة الطبيب.",
            "Use prescribed rescue/controller inhalers or respiratory therapy as directed by the physician.",
        ),
    },
    {
        "key": "5.",
        "label": tr("5. الحمى وارتفاع درجة الحرارة (Fever)", "5. Fever"),
        "steps": [
            tr("قياس درجة الحرارة بدقة باستخدام الترمومتر.", "Measure body temperature accurately with a thermometer."),
            tr("شرب السوائل بانتظام والراحة والحصول على قسط كافٍ من النوم.", "Drink fluids regularly, rest, and get adequate sleep."),
            tr("ارتداء ملابس خفيفة ومريحة واستخدام كمادات ماء فاتر عند الحاجة.", "Wear light comfortable clothes and use lukewarm water compresses when needed."),
        ],
        "avoid": tr(
            "تغطية الجسم ببطانيات ثقيلة أثناء ارتفاع الحرارة أو استخدام الماء المثلج أو الكحول لتخفيض الحرارة.",
            "Covering the body with heavy blankets during fever, or using ice-cold water or alcohol to cool down.",
        ),
        "emergency": tr(
            "ارتفاع حرارة شديد مستمر أو مصحوب بتيبس الرقبة أو صداع حاد أو طفح جلدي أو تشنجات أو جفاف شديد.",
            "Persistently very high fever, neck stiffness, severe headache, rash, seizures, or severe dehydration.",
        ),
        "med": tr(
            "خافض حرارة مناسب مثل الباراسيتامول (Paracetamol) عند اللزوم وفق إرشادات الطبيب أو الصيدلي.",
            "Appropriate antipyretic such as Paracetamol when needed per doctor or pharmacist guidance.",
        ),
    },
    {
        "key": "6.",
        "label": tr("6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)", "6. Cough, Cold & Sore Throat"),
        "steps": [
            tr("شرب المشروبات الدافئة والراحة والترطيب الجيد.", "Drink warm beverages, rest, and stay well hydrated."),
            tr("الغرغرة بالماء الدافئ والملح (دون بلعه) وتناول عسل للبالغين إذا لم توجد حساسية.", "Gargle with warm salt water (spit out) and take honey (for adults without allergy) if suitable."),
            tr("استخدام محلول ملحي للأنف عند الاحتقان.", "Use saline nasal spray or rinse for congestion."),
        ],
        "avoid": tr(
            "التدخين أو التعرض للهواء الملوث أو استخدام المضادات الحيوية دون وصفة طبية.",
            "Smoking, exposure to polluted air, or taking antibiotics without a prescription.",
        ),
        "emergency": tr(
            "حدوث صعوبة في التنفس أو نهجان أو ألم حاد في الصدر أو ارتفاع حرارة مستمر أو صفير مسموع مع التنفس.",
            "Difficulty breathing, shortness of breath, sharp chest pain, persistent fever, or audible wheezing.",
        ),
        "med": tr(
            "مسكن ومهدئ مناسب عند الحاجة مثل الكونجستال (Congestal) أو حسب إرشادات الطبيب.",
            "Symptomatic relief such as Congestal when appropriate or as advised by a physician.",
        ),
    },
    {
        "key": "7.",
        "label": tr("7. حموضة المعدة (Acidity / Heartburn)", "7. Acidity / Heartburn"),
        "steps": [
            tr("الجلوس في وضع مستقيم بعد الأكل وتجنب الاستلقاء مباشرة.", "Sit upright after eating and avoid lying down immediately."),
            tr("تناول وجبات صغيرة ومتوازنة والابتعاد عن الأطعمة التي تزيد الحموضة.", "Eat smaller balanced meals and avoid trigger foods that increase acidity."),
            tr("شرب الماء باعتدال وتجنب القهوة والمشروبات الغازية على معدة فارغة.", "Drink water moderately and avoid coffee or sodas on an empty stomach."),
        ],
        "avoid": tr(
            "الاستلقاء مباشرة بعد الطعام أو تناول الأطعمة الدسمة والحارة والمقلية بكثرة.",
            "Lying down right after meals or eating heavy, spicy, or fried foods heavily.",
        ),
        "emergency": tr(
            "ألم حاد في البطن أو قيء مستمر أو دموي أو براز داكن أو صعوبة في البلع.",
            "Severe abdominal pain, persistent or bloody vomiting, black stools, or difficulty swallowing.",
        ),
        "med": tr(
            "مضاد حموضة مناسب مثل الفوناكيدان (Vonacidan) عند الحاجة أو حسب تعليمات الطبيب.",
            "Suitable antacid such as Vonacidan when needed or per physician instructions.",
        ),
    },
    {
        "key": "8.",
        "label": tr("8. القولون العصبي (IBS)", "8. IBS"),
        "steps": [
            tr("تجنب التوتر والقلق ومحاولة تنظيم أوقات الوجبات اليومية.", "Reduce stress and anxiety and keep regular meal times."),
            tr("شرب الماء بانتظام وتناول ألياف مناسبة وتدوين الأطعمة المهيجة للقولون.", "Drink water regularly, eat suitable fiber, and note trigger foods."),
            tr("ممارسة حركة خفيفة ومريحة تساعد على الهضم وتقليل الانتفاخ.", "Do gentle light movement that supports digestion and reduces bloating."),
        ],
        "avoid": tr(
            "الإفراط في البقوليات أو الأطعمة الدسمة والمنبهات أو تناول الطعام بسرعة كبيرة.",
            "Overeating legumes, fatty foods, or stimulants, or eating meals too quickly.",
        ),
        "emergency": tr(
            "فقدان وزن غير مبرر أو نزيف شرجي أو ألم بطني شديد مفاجئ أو إسهال مصحوب بحمى.",
            "Unexplained weight loss, rectal bleeding, sudden severe abdominal pain, or diarrhea with fever.",
        ),
        "med": tr(
            "علاج داعم مناسب مثل الريبلس (Replex) أو حسب إرشادات الطبيب المختص.",
            "Supportive therapy such as Replex when appropriate or as guided by a specialist.",
        ),
    },
    {
        "key": "9.",
        "label": tr("9. آلام والصداع (Pain & Headache)", "9. Pain & Headache"),
        "steps": [
            tr("الراحة في مكان هادئ وإضاءة مريحة وشرب الماء بانتظام.", "Rest in a quiet, comfortably lit room and drink water regularly."),
            tr("تجنب إجهاد العين والنظر الطويل للشاشات دون راحة.", "Avoid eye strain and prolonged screen time without breaks."),
            tr("الحصول على قسط كافٍ من النوم المنتظم.", "Get sufficient regular sleep."),
        ],
        "avoid": tr(
            "الإفراط في المسكنات أو السهر وقلة النوم أو تخطي الوجبات لفترات طويلة.",
            "Overusing painkillers, staying up late with poor sleep, or skipping meals for long hours.",
        ),
        "emergency": tr(
            "صداع مفاجئ حاد جداً أو مصحوب بتيبس الرقبة أو اضطراب الرؤية أو ضعف في الأطراف أو بعد إصابة في الرأس.",
            "Sudden thunderclap headache, neck stiffness, vision changes, limb weakness, or head trauma.",
        ),
        "med": tr(
            "مسكن ألم مناسب مثل الباراسيتامول (Paracetamol) عند اللزوم دون تجاوز الجرعة الآمنة.",
            "Appropriate analgesic such as Paracetamol when needed without exceeding safe limits.",
        ),
    },
    {
        "key": "10.",
        "label": tr("10. ارتجاع المريء (GERD)", "10. GERD (Acid Reflux)"),
        "steps": [
            tr("الجلوس في وضع مستقيم بعد تناول الطعام.", "Sit upright after eating."),
            tr("تناول وجبات صغيرة وتجنب الاستلقاء لمدة ساعتين إلى ثلاث ساعات بعد الأكل.", "Eat smaller meals and avoid lying down for 2–3 hours after eating."),
            tr("رفع الجزء العلوي من الجسم أثناء النوم إذا كانت الأعراض ليلية.", "Elevate the upper body during sleep if nighttime symptoms occur."),
        ],
        "avoid": tr(
            "تناول وجبات كبيرة قبل النوم أو الاستلقاء مباشرة بعد الأكل أو الإكثار من الحمضيات والنعناع والدهون.",
            "Eating large meals before bed, lying down right after eating, or heavy citrus, mint, and fatty foods.",
        ),
        "emergency": tr(
            "ظهور ألم شديد أو ضغط في الصدر خاصة مع العرق أو ضيق التنفس أو الدوخة، أو حدوث قيء دموي أو صعوبة شديدة في البلع.",
            "Severe chest pain or pressure especially with sweating, shortness of breath, or dizziness, or bloody vomiting / severe dysphagia.",
        ),
        "med": tr(
            "حسب إرشادات الطبيب المختص.",
            "As directed by the specialist physician.",
        ),
    },
    {
        "key": "11.",
        "label": tr("11. ألم الظهر (Back Pain)", "11. Back Pain"),
        "steps": [
            tr("تجنب حمل الأشياء الثقيلة أو الانحناء المفاجئ.", "Avoid lifting heavy objects or sudden bending."),
            tr("تغيير وضعية الجلوس باستمرار والمشي الخفيف والحركة الهادئة حسب القدرة.", "Change sitting posture continuously with light walking and gentle movement as tolerated."),
            tr("استخدام كمادات باردة أو دافئة ملفوفة في قطعة قماش والحصول على راحة دون ملازمة السرير لفترات طويلة.", "Use cold or warm compresses wrapped in a cloth and rest without prolonged bed rest."),
        ],
        "avoid": tr(
            "الحركات المفاجئة أو حمل الأوزان أو التدليك العنيف على منطقة الألم.",
            "Sudden movements, lifting heavy weights, or vigorous massage over the painful area.",
        ),
        "emergency": tr(
            "وجود ألم ضعف مفاجئ بالساقين، أو فقدان التحكم في البول أو البراز أو فقدان الإحساس بمنطقة ما بين الفخذين، أو حدث بعد إصابة قوية.",
            "Sudden leg weakness, loss of bowel or bladder control, saddle numbness between the thighs, or trauma.",
        ),
        "med": tr(
            "حسب إرشادات الطبيب المختص.",
            "As directed by the specialist physician.",
        ),
    },
    {
        "key": "12.",
        "label": tr("12. ألم المفاصل والعضلات (Joint & Muscle Pain)", "12. Joint & Muscle Pain"),
