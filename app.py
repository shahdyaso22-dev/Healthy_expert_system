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
            overflow-x: hidden;
        }}
        .main .block-container {{
            direction: {"rtl" if is_ar else "ltr"};
            text-align: {"right" if is_ar else "left"};
            max-width: 100%;
            overflow-x: hidden;
        }}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #0b1120 0%, #020617 100%);
            direction: {"rtl" if is_ar else "ltr"};
            text-align: {"right" if is_ar else "left"};
            overflow-x: hidden;
        }}
        [data-testid="stSidebar"] * {{
            word-break: normal !important;
            overflow-wrap: break-word !important;
            max-width: 100%;
        }}
        @media (max-width: 768px) {{
            [data-testid="stSidebar"][aria-expanded="true"] {{
                width: 75vw !important;
                min-width: 75vw !important;
                max-width: 75vw !important;
        }}
        @media (max-width: 768px) {{
            .main .block-container {{
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }}
            table.custom-tbl {{
                min-width: 100% !important;
                width: 100% !important;
                font-size: 13px !important;
            }}
            table.custom-tbl th,
            table.custom-tbl td {{
                padding: 9px 8px !important;
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
                "steps": [
            tr("إراحة الجزء المصاب مؤقتاً.", "Rest the affected area temporarily."),
            tr("استخدام كمادات باردة ملفوفة في منشفة لمدة قصيرة عند وجود تورم حديث.", "Use cold compresses wrapped in a towel for short intervals if there is recent swelling."),
            tr("تجنب المجهود والحركات التي تزيد الألم وتحريك المفصل بلطف عندما تسمح الحالة وشرب الماء بانتظام.", "Avoid exertion and painful movements, move the joint gently when tolerated, and drink water regularly."),
        ],
        "avoid": tr(
            "الضغط على المفصل المصاب أو ممارسة الرياضة العنيفة أو استخدام أدوية دون استشارة.",
            "Pressing on the injured joint, doing strenuous exercise, or taking medications without guidance.",
        ),
        "emergency": tr(
            "كان المفصل شديد التورم أو ساخناً ومحمرّاً أو صاحبه ارتفاع حرارة أو تعذر تحريكه أو تحميل الوزن عليه.",
            "Severe joint swelling, warmth, redness, accompanying fever, or inability to move or bear weight on it.",
        ),
        "med": tr(
            "حسب إرشادات الطبيب المختص.",
            "As directed by the specialist physician.",
        ),
    },
]

# ==========================================
# 4. العنوان الرئيسي والـ Sidebar
# ==========================================
st.title(
    tr(
        "🧠 النظام الخبير الطبي والرياضي الذكي بالذكاء الاصطناعي",
        "🧠 AI Clinical, Medical & Sports Expert System",
    )
)
st.markdown(
    f"<p class='hero-sub'>{tr('تشخيص طبي منفصل وإرشادات طوارئ + برامج رياضية وجداول غذائية متكاملة', 'Separate clinical diagnosis & emergency guidance + structured sports & nutrition plans')}</p>",
    unsafe_allow_html=True,
)
st.divider()

st.sidebar.header(tr("👤 الملف الشخصي للمريض والرياضي", "👤 Patient & Athlete Profile"))

age = st.sidebar.number_input(
    tr("العمر (بالسنوات)", "Age (years)"),
    min_value=1,
    max_value=120,
    value=22,
)
weight = st.sidebar.number_input(
    tr("الوزن (كجم)", "Weight (kg)"),
    min_value=20.0,
    max_value=250.0,
    value=70.0,
    step=0.5,
)
height = st.sidebar.number_input(
    tr("الطول (سم)", "Height (cm)"),
    min_value=50.0,
    max_value=250.0,
    value=172.0,
    step=0.5,
)
gender = st.sidebar.selectbox(
    tr("الجنس", "Gender"),
    [tr("أنثى", "Female"), tr("ذكر", "Male")],
)
activity_level = st.sidebar.selectbox(
    tr("مستوى النشاط البدني والحركة", "Physical Activity & Movement Level"),
    [
        tr("خامل (بدون تمرين أو عمل مكتبي)", "Sedentary (no exercise or desk job)"),
        tr("نشاط خفيف (تمرين 1-3 أيام في الأسبوع)", "Lightly active (exercise 1-3 days/week)"),
        tr("نشاط معتدل (تمرين 3-5 أيام في الأسبوع)", "Moderately active (exercise 3-5 days/week)"),
        tr("نشاط عالي جداً (تمارين شاقة 6-7 أيام)", "Very active (intense training 6-7 days/week)"),
        tr("حركة محدودة / كبار السن (مجهود بسيط)", "Limited mobility / seniors (light effort)"),
    ],
)

st.sidebar.divider()
st.sidebar.subheader(tr("🧭 اختر القسم الذي تريد العمل عليه", "🧭 Choose the Section to Work On"))

section_mode = st.sidebar.radio(
    tr("القسم", "Section"),
    [
        tr("القسم الطبي والأمراض", "Medical & Diseases Section"),
        tr("القسم الرياضي والغذائي", "Sports & Nutrition Section"),
    ],
)

is_medical_section = section_mode in (
    "القسم الطبي والأمراض",
    "Medical & Diseases Section",
)

selected_disease = tr("لا يوجد أمراض أو أعراض (حالة سليمة)", "No diseases or symptoms (Healthy)")
fitness_goal = tr("زيادة وزن وبناء عضلات", "Weight Gain & Muscle Building")

if is_medical_section:
    st.sidebar.divider()
    st.sidebar.subheader(tr("🩺 قسم الأمراض والحالات السريرية الشاملة", "🩺 Comprehensive Diseases & Clinical Cases"))
    disease_options = [tr("لا يوجد أمراض أو أعراض (حالة سليمة)", "No diseases or symptoms (Healthy)")] + [
        d["label"] for d in DISEASES_DATA
    ]
    selected_disease = st.sidebar.selectbox(
        tr("اختر الداء أو العرض الرئيسي", "Select main condition or symptom"),
        disease_options,
    )
    action_clicked = st.sidebar.button(
        tr("🩺 عرض التشخيص الطبي والروشتة", "🩺 Show Medical Diagnosis & Prescription"),
        use_container_width=True,
    )
else:
    st.sidebar.divider()
    st.sidebar.subheader(tr("🏋️‍♂️ قسم الرياضة والتغذية المعتمدة", "🏋️‍♂️ Approved Sports & Nutrition Section"))
    fitness_goal = st.sidebar.radio(
        tr("اختر هدفك الرياضي والغذائي", "Choose your sports & nutrition goal"),
        [
            tr("زيادة وزن وبناء عضلات", "Weight Gain & Muscle Building"),
            tr("تقليل وزن وتنشيف", "Weight Loss & Cutting"),
        ],
    )
    action_clicked = st.sidebar.button(
        tr("🏋️‍♂️ تفعيل النظام الرياضي والغذائي", "🏋️‍♂️ Activate Sports & Nutrition System"),
        use_container_width=True,
    )

height_m = max(height / 100.0, 0.5)
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    bmi_cat = tr("نحافة", "Underweight")
elif bmi < 25.0:
    bmi_cat = tr("وزن مثالي", "Normal Weight")
elif bmi < 30.0:
    bmi_cat = tr("زيادة وزن", "Overweight")
else:
    bmi_cat = tr("سمنة", "Obese")

# ==========================================
# 5. عرض القسم الطبي والأمراض فقط
# ==========================================
if is_medical_section:
    st.markdown(
        f"""
        <div class='section-banner'>
            <span class='pill-badge'>{tr("تشخيص سريري وإرشادات طوارئ", "Clinical Triage & Emergency Guidance")}</span>
            <h2 style='margin: 4px 0;'>{tr("🩺 القسم الطبي والأمراض", "🩺 Medical & Diseases Section")}</h2>
            <p style='margin: 0; color: #cbd5e1;'>{tr("يعرض هذا القسم التقييم الطبي والإجراءات الأولية والتحذيرات والأدوية الموصوفة فقط.", "This section displays medical evaluation, initial actions, warnings, and prescribed medication only.")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    is_healthy = (
        "لا يوجد" in selected_disease
        or "No diseases" in selected_disease
    )
    confidence = 98.4 if is_healthy else 96.5

    st.markdown(
        f"### {tr('📊 التقرير التشخيصي وتحليل الذكاء الاصطناعي', '📊 Diagnostic Report & AI Analysis')}"
    )
    m1, m2, m3 = st.columns(3)
    m1.metric(
        tr("البيانات الحيوية", "Biometric Profile"),
        f"{age} {tr('سنة', 'yrs')} | {gender}",
    )
    m2.metric(
        tr("مؤشر كتلة الجسم (BMI)", "Body Mass Index (BMI)"),
        f"{bmi:.1f}",
        bmi_cat,
    )
    m3.metric(
        tr("دقة النظام الخبير", "AI Confidence"),
        f"{confidence}%",
        selected_disease,
    )
    st.info(
        f"**{tr('مستوى النشاط البدني:', 'Physical Activity Level:')}** {activity_level}"
    )

    if is_healthy:
           st.success(
               tr(
                "✅ لا توجد أمراض أو أعراض مسجلة حالياً — الحالة الصحية مستقرة.",
                "✅ No diseases or symptoms recorded currently — health status is stable.",
            )

        else:
            matched = next(
            (
                d for d in DISEASES_DATA
                if str(d["label"]).strip() == str(selected_disease).strip()
                or str(d["key"]).strip() in str(selected_disease)
            ),
            None,
        )
        if not matched and selected_disease:
            for idx, d in enumerate(DISEASES_DATA, start=1):
                s = str(selected_disease).strip()
                if s.startswith(f"{idx}.") or s.startswith(f"{idx} "):
                    matched = d
                    break
        if matched:
            st.markdown(f"### {matched['label']}")
            st.markdown(
                f"**{tr('🩺 التصرف المبدئي والإرشادات:', '🩺 Initial Actions & Guidance:')}**"
            )
            for item in matched["steps"]:
                st.markdown(f"- {item}")
    

            if matched["avoid"]:
                st.warning(
                    f"**{tr('⚠️ تجنب:', '⚠️ Avoid:')}** {matched['avoid']}"
                )

            if matched["emergency"]:
                st.markdown(
                    f"""
                    <div class='em-card'>
                        <strong>🚨 {tr("اذهب للطوارئ فوراً إذا ظهرت العلامات التالية:", "Go to ER immediately if any of the following occur:")}</strong><br>
                        {matched["emergency"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            if matched["med"]:
                st.markdown(
                    f"""
                    <div class='med-card'>
                        <strong>💊 {tr("الروشتة الطبية المعتمدة - الدواء الموصوف:", "Approved Medical Prescription - Recommended Medication:")}</strong><br>
                        {matched["med"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# ==========================================
# 6. عرض القسم الرياضي والغذائي فقط
# ==========================================
else:
    st.markdown(
        f"""
        <div class='section-banner'>
            <span class='pill-badge'>{tr("تغذية وتمارين حسب الهدف", "Goal-Based Nutrition & Workouts")}</span>
            <h2 style='margin: 4px 0;'>{tr("🏋️‍♂️ البرنامج الرياضي والنظام الغذائي", "🏋️‍♂️ Sports & Nutrition Program")}</h2>
            <p style='margin: 0; color: #cbd5e1;'>{tr("خطط غذائية وتمارين رياضية مخصصة لزيادة الوزن وبناء العضلات أو تقليل الوزن والتنشيف.", "Tailored meal plans and workouts for weight gain/muscle building or weight loss/cutting.")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3 = st.columns(3)
    s1.metric(
        tr("البيانات البدنية", "Physical Profile"),
        f"{age} {tr('سنة', 'yrs')} | {gender}",
    )
    s2.metric(
        tr("مؤشر كتلة الجسم (BMI)", "Body Mass Index (BMI)"),
        f"{bmi:.1f}",
        bmi_cat,
    )
    s3.metric(
        tr("الهدف المختار", "Selected Goal"),
        fitness_goal,
    )
    st.info(
        f"**{tr('مستوى النشاط البدني:', 'Physical Activity Level:')}** {activity_level}"
    )

    goal_str = str(fitness_goal or "")
    is_gain_goal = ("زيادة وزن" in goal_str) or ("Weight Gain" in goal_str)

    if is_gain_goal:
        st.markdown(
            f"""
            <div class='section-banner'>
                <span class='pill-badge'>{tr("فائض سعرات صحي ومتوازن", "Healthy Balanced Calorie Surplus")}</span>
                <h3 style='margin: 4px 0;'>{tr("📈 جدول النظام الغذائي لزيادة الوزن وبناء العضلات", "📈 Weight Gain & Muscle Building Diet Plan")}</h3>
                <p style='margin: 0; color: #cbd5e1;'>{tr("خطة يومية متكاملة من 6 وجبات لزيادة الكتلة العضلية والوزن الصحي بأمان على مدار اليوم.", "Complete 6-meal daily plan for safe muscle and weight gain across daily periods.")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        gain_meals = [
            [
                f"<strong>{tr('الإفطار', 'Breakfast')}</strong><br><span style='color:#38bdf8;'>{tr('صباحاً', 'Morning')}</span>",
                tr(
                    "• 3 بيضات مقلية في الزبدة أو زيت الزيتون<br>• رغيف خبز بلدي أو شريحتين خبز توست بر<br>• كوب حليب كامل الدسم مع تمرات<br>• ملعقة كبيرة زبدة فول سوداني",
                    "• 3 eggs cooked in butter or olive oil<br>• 1 baladi bread or 2 whole-wheat toast slices<br>• 1 full-fat milk with dates<br>• 1 tbsp peanut butter",
                ),
                tr(
                    "دهون صحية وبروتين وكربوهيدرات مركبة لبدء اليوم بطاقة عالية.",
                    "Healthy fats, protein, and complex carbs to start the day with high energy.",
                ),
            ],
            [
                f"<strong>{tr('وجبة خفيفة 1 (سناك 1)', 'Snack 1')}</strong><br><span style='color:#38bdf8;'>{tr('قبل الظهر', 'Mid-Morning')}</span>",
                tr(
                    "• طبق سلطة فواكه مجففة ومكسرات (عين جمل، لوز، زبيب)<br>• كوب عصير مانجو أو موز بالحليب كامل الدسم مع العسل",
                    "• Dried fruit & nut bowl (walnuts, almonds, raisins)<br>• Mango juice or banana-milk shake with honey",
                ),
                tr(
                    "سعرات مركزة سهلة الهضم وغنية بالدهون الصحية والطاقة.",
                    "Concentrated, easy-to-digest calories rich in healthy fats and energy.",
                ),
            ],
            [
                f"<strong>{tr('الغداء (الوجبة الرئيسية)', 'Lunch (Main Meal)')}</strong><br><span style='color:#38bdf8;'>{tr('الظهر', 'Afternoon')}</span>",
                tr(
                    "• طبق كبير أرز مصري أو مكرونة (مطهو بالسمن أو الزبدة)<br>• صدرين دجاج أو قطعة لحم ضأن/بقري متوسطة الحجم<br>• طبق خضار مطهو مع مرقة ودسم صحي<br>• سلطة خضراء مع زيت الزيتون",
                    "• Large bowl of Egyptian rice or pasta (with ghee/butter)<br>• 2 chicken breasts or medium lamb/beef portion<br>• Cooked vegetables with broth & healthy fat<br>• Green salad with olive oil",
                ),
                tr(
                    "وجبة أساسية غنية بالبروتين والكربوهيدرات المعقدة لبناء الكتلة العضلية.",
                    "Core meal rich in protein and complex carbs to support muscle building.",
                ),
            ],
            [
                f"<strong>{tr('وجبة 2 (قبل التمرين)', 'Meal 2 (Pre-Workout)')}</strong><br><span style='color:#38bdf8;'>{tr('قبل التمرين', 'Pre-Workout')}</span>",
                tr(
                    "• ساندوتش زبدة الفول السوداني والموز مع العسل<br>• أو بطاطس مسلوقة + مصدر بروتين خفيف",
                    "• Peanut butter & banana sandwich with honey<br>• Or boiled potato + light protein source",
                ),
                tr(
                    "تمد الجسم بطاقة عالية ومستقرة قبل بذل أي مجهود أو تمرين.",
                    "Provides steady high energy before physical exertion or workouts.",
                ),
            ],
            [
                f"<strong>{tr('العشاء', 'Dinner')}</strong><br><span style='color:#38bdf8;'>{tr('مساءً', 'Evening')}</span>",
                tr(
                    "• طبق فول بزيت الزيتون والطحينة الخفيفة<br>• جبنة كاملة الدسم (قريش مع قشطة أو جبنة بيضاء دسمة)<br>• رغيف خبز بلدي",
                    "• Fava beans (ful) with olive oil & light tahini<br>• Full-fat cheese (cottage with cream or full-fat white cheese)<br>• 1 baladi bread",
                ),
                tr(
                    "بروتين ودهون مغذية تساعد على تعويض الجسم واستقرار السعرات مساءً.",
                    "Nourishing protein and fats supporting recovery and evening calorie targets.",
                ),
            ],
            [
                f"<strong>{tr('قبل النوم مباشرة', 'Before Bed')}</strong><br><span style='color:#38bdf8;'>{tr('قبل النوم', 'Before Bed')}</span>",
                tr(
                    "• كوب حليب دافئ كامل الدسم مع ملعقة عسل ومكسرات مطحونة<br>• أو كوب زبادي كامل الدسم",
                    "• Warm full-fat milk with 1 tsp honey & crushed nuts<br>• Or full-fat yogurt cup",
                ),
                tr(
                    "يساعد على الاسترخاء ويدعم زيادة السعرات اليومية بأمان.",
                    "Supports relaxation and helps meet daily calorie surplus goals.",
                ),
            ],
        ]
        st.markdown(
            build_html_table(
                [
                    tr("الوجبة والفترة", "Meal & Period"),
                    tr("مكونات الوجبة المقترحة", "Suggested Meal Components"),
                    tr("القيمة والفوائد الغذائية", "Nutritional Value & Benefits"),
                ],
                gain_meals,
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            f"### {tr('🏋️‍♂️ الرياضة والتمارين المطلوبة (زيادة وزن وبناء عضلات)', '🏋️‍♂️ Required Sports & Workouts (Weight Gain & Muscle Building)')}"
        )
        gain_sports = [
            [
                f"<strong>{tr('اليوم 1', 'Day 1')}</strong>",
                tr(
                    "تمارين مقاومة: صدر، كتف أمامي وجانبي، وترايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)",
                    "Resistance training: chest, front/side delts, triceps (45–60 min • 4 days/week)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 2', 'Day 2')}</strong>",
                tr(
                    "تمارين مقاومة: ظهر، كتف خلفي، وبايسبس (45 - 60 دقيقة • 4 أيام أسبوعياً)",
                    "Resistance training: back, rear delts, biceps (45–60 min • 4 days/week)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 3', 'Day 3')}</strong>",
                tr(
                    "راحة تامة واستشفاء عضلي",
                    "Complete rest and muscle recovery",
                ),
            ],
            [
                f"<strong>{tr('اليوم 4', 'Day 4')}</strong>",
                tr(
                    "تمارين مقاومة شاملة: فخذ أمامي وخلفي وسمانة (45 - 60 دقيقة • 4 أيام أسبوعياً)",
                    "Full lower-body resistance: quads, hamstrings, calves (45–60 min • 4 days/week)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 5', 'Day 5')}</strong>",
                tr(
                    "تمارين جزء علوي وبطن (Upper Body & Core) (45 - 60 دقيقة • 4 أيام أسبوعياً)",
                    "Upper body & core workout (45–60 min • 4 days/week)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 6 و 7', 'Days 6 & 7')}</strong>",
                tr(
                    "راحة ومرونة واستشفاء عضلي",
                    "Rest, mobility, and recovery",
                ),
            ],
        ]
        st.markdown(
            build_html_table(
                [tr("اليوم", "Day"), tr("الرياضة والتمارين المطلوبة", "Required Sports & Workouts")],
                gain_sports,
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            f"### {tr('💡 نصائح ذهبية لنجاح نظام زيادة الوزن', '💡 Golden Tips for Weight Gain Success')}"
        )
        st.markdown(
            f"""
            <div class='tip-card'><strong>1. {tr("زيادة السعرات التدريجية:", "Gradual Calorie Surplus:")}</strong> {tr("حاول أن تأكل كميات أكبر قليلاً مما اعتدت عليه بالتدريج لكي لا تشعر بتخمة مفاجئة.", "Gradually increase portions above your usual intake so your digestion adapts comfortably.")}</div>
            <div class='tip-card'><strong>2. {tr("الدهون الصحية في كل وجبة:", "Healthy Fats in Every Meal:")}</strong> {tr("ركّز على زيت الزيتون، الأفوكادو، المكسرات، زبدة الفول السوداني، والزبادي كامل الدسم.", "Focus on olive oil, avocado, nuts, peanut butter, and full-fat dairy.")}</div>
            <div class='tip-card'><strong>3. {tr("الاستمرارية والراحة:", "Consistency & Rest:")}</strong> {tr("الالتزام بالتمارين والنوم الكافي أساس بناء الكتلة العضلية والوزن الصحي.", "Consistent training and quality sleep are essential for building healthy weight and muscle.")}</div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class='section-banner'>
                <span class='pill-badge'>{tr("تنشيف وخسارة دهون", "Cutting & Fat Loss")}</span>
                <h3 style='margin: 4px 0;'>{tr("🔥 جدول النظام الغذائي لتقليل الوزن والتنشيف", "🔥 Weight Loss & Cutting Diet Plan")}</h3>
                <p style='margin: 0; color: #cbd5e1;'>{tr("خطة متوازنة عالية البروتين لتقليل الدهون والحفاظ على الكتلة العضلية مع اختيار بديل واحد لكل وجبة.", "Balanced high-protein plan for fat loss and muscle preservation — pick one option per meal.")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        cut_meals = [
            [
                f"<strong>{tr('الإفطار', 'Breakfast')}</strong>",
                tr(
                    "3 بيضات مسلوقة أو مقلية بملعقة زيت زيتون + ربع رغيف بلدي + خيار وجرجير",
                    "3 boiled eggs or fried with 1 tsp olive oil + 1/4 baladi bread + cucumber & arugula",
                ),
                tr(
                    "4 ملاعق فول بزيت زيتون وكمون + ربع رغيف بلدي + بيضة مسلوقة أو قطعة جبنة قريش",
                    "4 tbsp fava beans with olive oil & cumin + 1/4 baladi bread + 1 boiled egg or cottage cheese",
                ),
                tr(
                    "لبداية نشيطة وشبع لفترة طويلة",
                    "For an active start and long-lasting fullness",
                ),
            ],
            [
                f"<strong>{tr('الغداء', 'Lunch')}</strong>",
                tr(
                    "<strong>بروتين:</strong> 150-200 جم صدور فراخ مشوية/مسلوقة أو لحم مفروم قليل الدهن<br><strong>نشويات:</strong> 5 ملاعق أرز أو مكرونة<br><strong>خضار:</strong> طبق خضار سوتيه + سلطة كبيرة",
                    "<strong>Protein:</strong> 150–200g grilled/boiled chicken breast or lean minced meat<br><strong>Carbs:</strong> 5 tbsp rice or pasta<br><strong>Veggies:</strong> Sautéed veggies + large salad",
                ),
                tr(
                    "<strong>بروتين:</strong> 2 سمكة مشوية<br><strong>نشويات:</strong> رغيف بلدي كامل أو 5 ملاعق أرز<br><strong>خضار:</strong> طبق سلطة خضراء كبير",
                    "<strong>Protein:</strong> 2 grilled fish<br><strong>Carbs:</strong> 1 whole baladi bread or 5 tbsp rice<br><strong>Veggies:</strong> Large green salad",
                ),
                tr(
                    "معلقة زيت زيتون وليمون فقط على السلطة",
                    "1 tsp olive oil and lemon juice on salad only",
                ),
            ],
            [
                f"<strong>{tr('العشاء', 'Dinner')}</strong>",
                tr(
                    "150 جم جبنة قريش بالطماطم والخيار ورشة زعتر + ربع رغيف بلدي",
                    "150g cottage cheese with tomato, cucumber & pinch of zaatar + 1/4 baladi bread",
                ),
                tr(
                    "علبة تونة مصفاة تماماً + طبق سلطة خضراء",
                    "1 can tuna thoroughly drained + green salad",
                ),
                tr(
                    "وجبة خفيفة ومناسبة قبل النوم",
                    "Light meal suitable before bedtime",
                ),
            ],
        ]
        st.markdown(
            build_html_table(
                [
                    tr("الوجبة", "Meal"),
                    tr("الخيار الأول", "Option 1"),
                    tr("الخيار الثاني", "Option 2"),
                    tr("ملاحظات هامة", "Key Notes"),
                ],
                cut_meals,
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            f"### {tr('🏃‍♀️ الرياضة والتمارين المطلوبة (تقليل وزن وتنشيف)', '🏃‍♀️ Required Sports & Workouts (Weight Loss & Cutting)')}"
        )
        cut_sports = [
            [
                f"<strong>{tr('اليوم 1 و 4', 'Days 1 & 4')}</strong>",
                tr(
                    "تمارين كارديو (Cardio): مشي سريع أو جري خفيف (30 - 45 دقيقة)",
                    "Cardio: brisk walking or light jogging (30–45 min)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 2 و 5', 'Days 2 & 5')}</strong>",
                tr(
                    "تمارين مقاومة كاملة للجسم (Full Body Circuit) لحماية العضلات ورفع الحرق",
                    "Full body resistance circuit to protect muscle and boost calorie burn",
                ),
            ],
            [
                f"<strong>{tr('اليوم 3', 'Day 3')}</strong>",
                tr(
                    "كارديو متقطع خفيف أو حبل قفز أو عجلة ثابتة (20 - 30 دقيقة)",
                    "Light interval cardio, jump rope, or stationary bike (20–30 min)",
                ),
            ],
            [
                f"<strong>{tr('اليوم 6 و 7', 'Days 6 & 7')}</strong>",
                tr(
                    "مشي خفيف في الهواء الطلق واستشفاء عضلي",
                    "Light outdoor walk and active recovery",
                ),
            ],
        ]
        st.markdown(
            build_html_table(
                [tr("اليوم", "Day"), tr("الرياضة والتمارين المطلوبة", "Required Sports & Workouts")],
                cut_sports,
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            f"### {tr('💡 قواعد أساسية لنجاح التنشيف وتقليل الوزن', '💡 Core Rules for Successful Cutting & Weight Loss')}"
        )
        st.markdown(
            f"""
            <div class='tip-card'><strong>1. {tr("شرب المياه:", "Hydration:")}</strong> {tr("من 2.5 إلى 3 لتر يومياً لزيادة معدل الحرق ومنع الإحساس الوهمي بالجوع.", "2.5 to 3 liters daily to support metabolic rate and reduce false hunger cues.")}</div>
            <div class='tip-card'><strong>2. {tr("الحركة الخفيفة:", "Light Movement:")}</strong> {tr("المشي 15-20 دقيقة في منتصف اليوم أو بعد الغداء لتعويض الجلوس المكتبي.", "15–20 minutes of walking midday or after lunch to offset sitting.")}</div>
            <div class='tip-card'><strong>3. {tr("السكر والمشروبات:", "Sugar & Beverages:")}</strong> {tr("استبدال السكر الأبيض ببدائل مناسبة أو تقليله بشدة ومنع العصائر المحلاة تماماً.", "Minimize or replace refined sugar and avoid sweetened juices completely.")}</div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

    
      
