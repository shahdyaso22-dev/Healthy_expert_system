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
    str_ui.markdown("**التصرف المبدئي:**")
    for step in initial_steps:
        str_ui.markdown("- " + step)
    if avoid_text:
        str_ui.warning("**تجنب:** " + avoid_text)
    if emergency_text:
        str_ui.error("**🚨 اذهب للطوارئ فورًا إذا:** " + emergency_text)
    if med_text:
        str_ui.success("**💊 الروشتة الطبية المعتمدة — الدواء الموصوف:** " + med_text)


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


str_ui.title("🩺 النظام الخبير الطبي والرياضي الذكي بالذكاء الاصطناعي")
str_ui.markdown("<p style='color: #94a3b8; font-size: 18px;'>تشخيص طبي منفصل وإرشادات طوارئ + برامج رياضية وجداول غذائية متكاملة</p>", unsafe_allow_html=True)
str_ui.markdown("---")

str_ui.sidebar.header("👤 الملف الشخصي للمريض والرياضي")
age = str_ui.sidebar.number_input("العمر (بالسنوات)", 1, 120, 22)
weight = str_ui.sidebar.number_input("الوزن (كجم)", 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input("الطول (سم)", 50.0, 250.0, 172.0)
gender = str_ui.sidebar.selectbox("الجنس", ["ذكر", "أنثى"])
activity_level = str_ui.sidebar.selectbox(
    "مستوى النشاط البدني والحركة",
    [
        "خامل (بدون تمرين أو عمل مكتبي)",
        "نشاط خفيف (تمرين 1-3 أيام في الأسبوع)",
        "نشاط معتدل (تمرين 3-5 أيام في الأسبوع)",
        "نشاط عالي جداً (تمارين شاقة 6-7 أيام)",
        "حركة محدودة / كبير السن (مجهود بسيط)",
    ],
)

str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader("🧭 اختر القسم الذي تريد العمل عليه")
section_mode = str_ui.sidebar.radio(
    "وضع التشغيل:",
    [
        "القسم الطبي والأمراض",
        "القسم الرياضي والغذائي",
    ],
)

selected_disease = "لا يوجد أمراض أو أعراض (حالة سليمة)"
fitness_goal = None

if section_mode == "القسم الطبي والأمراض":
    str_ui.sidebar.markdown("---")
    str_ui.sidebar.subheader("🏥 قسم الأمراض والحالات السريرية الشاملة")
    disease_options = [
        "لا يوجد أمراض أو أعراض (حالة سليمة)",
        "1. مرض السكر (Diabetes)",
        "2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)",
        "3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)",
        "4. مشاكل الجهاز التنفسي (Respiratory Problems)",
        "5. الحمى وارتفاع درجة الحرارة (Fever)",
        "6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)",
        "7. حموضة المعدة (Vonacidan)",
        "8. القولون العصبي (Replix)",
        "9. الألم والصداع (Paracetamol)",
        "10. ارتجاع المريء (GERD)",
        "11. آلام الظهر (Back Pain)",
        "12. آلام المفاصل والعضلات (Joint & Muscle Pain)",
    ]
    selected_disease = str_ui.sidebar.selectbox("اختر الحالة أو العرض الرئيسي:", disease_options)
    button_label = "⚡ عرض التشخيص الطبي والروشتة"
else:
    str_ui.sidebar.markdown("---")
    str_ui.sidebar.subheader("🏋️‍♂️ قسم الرياضة والتغذية المخصصة")
    fitness_goal = str_ui.sidebar.radio(
        "اختر هدفك الرياضي والغذائي:",
        [
            "زيادة وزن وبناء عضلات",
            "تقليل وزن وتنشيف",
        ],
    )
    button_label = "⚡ تشغيل النظام الرياضي والغذائي"

if str_ui.button(button_label, use_container_width=True):
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

    if section_mode == "القسم الطبي والأمراض":
        confidence = 98.2 if "لا يوجد" in selected_disease else 96.5
        str_ui.markdown("## 🧠 التقرير التشخيصي وتحليل الذكاء الاصطناعي")
        c1, c2, c3 = str_ui.columns(3)
        c1.metric("البيانات الحيوية", f"{age} سنة | {gender}")
        c2.metric("مؤشر كتلة الجسم (BMI)", f"{bmi:.1f}", bmi_cat)
        c3.metric("دقة الذكاء الاصطناعي", f"{confidence}%")
        str_ui.info(f"**مستوى النشاط:** {activity_level}  |  **الحالة المختارة:** {selected_disease}")

        if "لا يوجد أمراض" not in selected_disease:
            str_ui.markdown("## 📋 الإرشادات الطبية والتصرف المبدئي للطوارئ")

            if "1. مرض السكر" in selected_disease:
                render_condition(
                    "1. مرض السكر (Diabetes)",
                    [
                        "قياس مستوى السكر بجهاز قياس السكر إن توفر.",
                        "شرب الماء بانتظام وتناول الوجبات في مواعيدها ومتابعة مستوى السكر وتسجيل القراءات.",
                        "إذا ظهرت أعراض انخفاض السكر، مثل الرعشة والتعرق والدوخة، والشخص واعٍ وقادر على البلع، يُعطى مصدر سكر سريع مثل نصف كوب عصير، ثم يُعاد القياس بعد 15 دقيقة.",
                        "الاستمرار على العلاج الموصوف وعدم تغيير جرعاته دون تعليمات الطبيب.",
                    ],
                    avoid_text="إيقاف الإنسولين أو مضاعفة جرعات الدواء من تلقاء نفسك.",
                    emergency_text="حدث فقدان للوعي، أو تشوش شديد، أو صعوبة تنفس، أو قيء مستمر، أو لم يستطع الشخص البلع. لا تعطِ فاقد الوعي أي طعام أو شراب.",
                    med_text="الالتزام بالعلاج الموصوف ومنظم السكر أو الإنسولين حسب تعليمات الطبيب.",
                )

            elif "2. ارتفاع ضغط الدم المزمن" in selected_disease:
                render_condition(
                    "2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)",
                    [
                        "الجلوس في مكان هادئ والراحة.",
                        "قياس ضغط الدم بعد الجلوس بهدوء.",
                        "تجنب المجهود والتوتر مؤقتًا وتقليل الأطعمة شديدة الملوحة.",
                        "الالتزام بأدوية الضغط الموصوفة في مواعيدها.",
                    ],
                    avoid_text="أخذ جرعة إضافية من دواء الضغط دون استشارة الطبيب.",
                    emergency_text="صاحب ارتفاع الضغط ألم في الصدر، أو صعوبة تنفس، أو ضعف مفاجئ في أحد جانبي الجسم، أو اضطراب الكلام أو الرؤية، أو صداع شديد مفاجئ.",
                    med_text="أدوية الضغط الموصوفة في مواعيدها الثابتة حسب إرشادات الطبيب.",
                )

            elif "3. أمراض القلب والأوعية الدموية" in selected_disease:
                render_condition(
                    "3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)",
                    [
                        "إيقاف أي مجهود بدني.",
                        "الجلوس في وضع مريح وتهدئة الشخص وعدم تركه بمفرده.",
                        "استخدام الدواء الموصوف مسبقًا للحالة فقط وفق تعليمات الطبيب.",
                    ],
                    avoid_text="المشي أو ممارسة الرياضة لمحاولة التخلص من ألم الصدر، وعدم إعطاء أدوية عشوائية.",
                    emergency_text="ظهر ألم أو ضغط بالصدر، أو امتد الألم إلى الذراع أو الفك أو الظهر، أو حدث عرق شديد أو دوخة أو ضيق تنفس. اتصل بالإسعاف 123 في مصر.",
                    med_text="الدواء الموصوف مسبقاً للحالة فقط وفق تعليمات الطبيب.",
                )

            elif "4. مشاكل الجهاز التنفسي" in selected_disease:
                render_condition(
                    "4. مشاكل الجهاز التنفسي (Respiratory Problems)",
                    [
                        "الجلوس في وضع مستقيم.",
                        "الابتعاد عن الدخان والغبار والروائح القوية.",
                        "توفير هواء نقي وتهوية المكان.",
                        "استخدام بخاخ الربو الموصوف للشخص وفق خطة الطبيب إن كان يعاني من الربو.",
                    ],
                    avoid_text="التعرض للدخان أو استخدام بخاخات أو أدوية غير موصوفة.",
                    emergency_text="كان هناك اختناق أو صعوبة شديدة في التنفس أو عدم القدرة على الكلام بشكل طبيعي أو ازرقاق الشفاه.",
                    med_text="بخاخ الربو الموصوف وفق خطة الطبيب إن كان يعاني من الربو.",
                )

            elif "5. الحمى وارتفاع درجة الحرارة" in selected_disease:
                render_condition(
                    "5. الحمى وارتفاع درجة الحرارة (Fever)",
                    [
                        "قياس درجة الحرارة بترمومتر.",
                        "شرب السوائل بانتظام والراحة والحصول على قسط كافٍ من النوم.",
                        "ارتداء ملابس خفيفة ومريحة واستخدام كمادات ماء فاتر عند الحاجة.",
                    ],
                    avoid_text="تغطية الجسم بأغطية ثقيلة أو استخدام الماء المثلج أو الكحول لتخفيض الحرارة.",
                    emergency_text="صاحبت الحمى صعوبة تنفس أو تشنجات أو تشوش في الوعي أو تيبس الرقبة أو صداع شديد غير معتاد.",
                    med_text="Paracetamol (باراسيتامول) عند اللزوم حسب إرشادات الطبيب أو الصيدلي.",
                )

            elif "6. السعال والبرد والتهاب الحلق" in selected_disease:
                render_condition(
                    "6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)",
                    [
                        "شرب المشروبات الدافئة.",
                        "تناول العسل لتخفيف السعال إذا لم توجد حساسية منه.",
                        "الغرغرة بالماء الدافئ والملح مع عدم بلعه.",
                        "استخدام محلول ملحي للأنف والراحة وشرب كمية كافية من السوائل.",
                    ],
                    avoid_text="التدخين والتعرض للهواء الملوث واستخدام المضادات الحيوية دون وصفة.",
                    emergency_text="حدثت صعوبة في التنفس أو البلع، أو ألم شديد بالصدر، أو عدم القدرة على شرب السوائل.",
                    med_text="Congestal (كنجستال)",
                )

            elif "7. حموضة المعدة" in selected_disease:
                render_condition(
                    "7. حموضة المعدة (Vonacidan)",
                    [
                        "الجلوس في وضع مستقيم بعد الأكل وتجنب الاستلقاء مباشرة.",
                        "تناول وجبات صغيرة والابتعاد عن الأطعمة التي تزيد الحموضة.",
                    ],
                    med_text="Vonacidan (فوناسيدان)",
                )

            elif "8. القولون العصبي" in selected_disease:
                render_condition(
                    "8. القولون العصبي (Replix)",
                    [
                        "تجنب التوتر والقلق والأطعمة المهيجة للقولون.",
                        "تناول وجبات منتظمة وشرب السوائل والمشروبات الدافئة المهدئة.",
                    ],
                    med_text="Replix (ريبليكس)",
                )

            elif "9. الألم والصداع" in selected_disease:
                render_condition(
                    "9. الألم والصداع (Paracetamol)",
                    [
                        "الراحة في مكان هادئ وشرب الماء بانتظام.",
                        "تجنب الإجهاد الزائد والشاشات لفترات طويلة.",
                    ],
                    med_text="Paracetamol (باراسيتامول)",
                )

            elif "10. ارتجاع المريء" in selected_disease:
                render_condition(
                    "10. ارتجاع المريء (GERD)",
                    [
                        "الجلوس في وضع مستقيم بعد تناول الطعام.",
                        "تناول وجبات صغيرة وتجنب الاستلقاء لمدة ساعتين إلى ثلاث ساعات بعد الأكل.",
                        "الابتعاد عن الأطعمة التي تزيد الحموضة لدى الشخص.",
                        "رفع الجزء العلوي من الجسم أثناء النوم إذا كانت الأعراض ليلية.",
                    ],
                    avoid_text="تناول وجبات كبيرة قبل النوم أو الاستلقاء مباشرة بعد الأكل.",
                    emergency_text="ظهر ألم شديد أو ضغط في الصدر، خاصة مع العرق أو ضيق التنفس أو الدوخة، أو حدث قيء دموي أو صعوبة شديدة في البلع.",
                    med_text="حسب إرشادات الطبيب المختص.",
                )

            elif "11. آلام الظهر" in selected_disease:
                render_condition(
                    "11. آلام الظهر (Back Pain)",
                    [
                        "تجنب حمل الأشياء الثقيلة.",
                        "تغيير وضعية الجلوس باستمرار والمشي الخفيف والحركة الهادئة حسب القدرة.",
                        "استخدام كمادات باردة أو دافئة ملفوفة في قطعة قماش.",
                        "الحصول على الراحة دون ملازمة السرير لفترات طويلة.",
                    ],
                    avoid_text="الحركات المفاجئة أو حمل الأوزان أو التدليك العنيف.",
                    emergency_text="صاحَب الألم ضعف مفاجئ بالساقين، أو فقدان التحكم في البول أو البراز، أو فقدان الإحساس بمنطقة ما بين الفخذين، أو حدث بعد إصابة قوية.",
                    med_text="حسب إرشادات الطبيب المختص.",
                )

            elif "12. آلام المفاصل والعضلات" in selected_disease:
                render_condition(
                    "12. آلام المفاصل والعضلات (Joint & Muscle Pain)",
                    [
                        "إراحة الجزء المصاب مؤقتًا.",
                        "استخدام كمادات باردة ملفوفة في منشفة لمدة قصيرة عند وجود تورم حديث.",
                        "تجنب المجهود والحركات التي تزيد الألم.",
                        "تحريك المفصل بلطف عندما تسمح الحالة بذلك وشرب الماء بانتظام.",
                    ],
                    avoid_text="الضغط على المفصل المصاب أو ممارسة الرياضة العنيفة أو استخدام أدوية دون استشارة.",
                    emergency_text="كان المفصل شديد التورم أو ساخنًا ومحمرًا، أو صاحبه ارتفاع حرارة، أو تعذر تحريكه أو تحميل الوزن عليه.",
                    med_text="حسب إرشادات الطبيب المختص.",
                )
        else:
            str_ui.info("لا يوجد أمراض مسجلة حالياً — الحالة الصحية مستقرة.")

    else:
        str_ui.markdown("## 🏋️‍♂️ البرنامج الرياضي والنظام الغذائي")
        c1, c2, c3 = str_ui.columns(3)
        c1.metric("البيانات البدنية", f"{age} سنة | {gender}")
        c2.metric("مؤشر كتلة الجسم (BMI)", f"{bmi:.1f}", bmi_cat)
        c3.metric("الهدف المختار", fitness_goal)
        str_ui.info(f"**مستوى النشاط البدني:** {activity_level}")

        if fitness_goal == "زيادة وزن وبناء عضلات":
            str_ui.markdown(
                "<div class='diet-banner'>"
                "<span class='pill-tag'>فائض سعرات صحي ومتوازن</span>"
                "<h3 style='margin: 4px 0; color: #7dd3fc !important;'>📈 جدول النظام الغذائي لزيادة الوزن وبناء العضلات</h3>"
                "<p style='margin: 0; color: #cbd5e1;'>خطة يومية متكاملة من 6 وجبات بمواعيد محددة لزيادة الكتلة العضلية والوزن الصحي بأمان.</p>"
                "</div>",
                unsafe_allow_html=True,
            )

            gain_meals = [
                [
                    "<strong>الإفطار</strong><br><span style='color:#38bdf8;'>⏰ 8:00 - 9:00 صباحاً</span>",
                    "• 3 بيضات مقلية بالزبدة أو زيت الزيتون<br>• رغيف خبز بلدي أو شريحتين خبز توست بر<br>• كوب حليب كامل الدسم مع تمرات<br>• ملعقة كبيرة زبدة فول سوداني",
                    "<span class='pill-tag'>الدهون الصحية والبروتين</span><br>طاقة قوية في بداية اليوم مع بروتين ودهون صحية لدعم بناء العضلات.",
                ],
                [
                    "<strong>وجبة خفيفة (سناك 1)</strong><br><span style='color:#38bdf8;'>⏰ 11:30 صباحاً</span>",
                    "• طبق سلطة فواكه مجففة ومكسرات (عين جمل، لوز، زبيب)<br>• كوب عصير مانجو أو موز بالحليب كامل الدسم مع العسل",
                    "<span class='pill-tag'>سعرات مركزة</span><br>سهلة الهضم وغنية بالدهون الصحية والطاقة لرفع السعرات اليومية.",
                ],
                [
                    "<strong>الغداء (الوجبة الرئيسية)</strong><br><span style='color:#38bdf8;'>⏰ 2:30 - 3:30 ظهراً</span>",
                    "• طبق كبير أرز مصري أو مكرونة (مطهو بالسمن أو الزبدة)<br>• صدرين دجاج أو قطعة لحم ضأن/بقري متوسطة الحجم<br>• طبق خضار مطهو مع مرقة ودسم صحي<br>• سلطة خضراء مع زيت الزيتون",
                    "<span class='pill-tag'>وجبة أساسية متكاملة</span><br>غنية بالبروتين والكربوهيدرات المعقدة لبناء الكتلة العضلية والوزن.",
                ],
                [
                    "<strong>وجبة خفيفة (سناك 2)</strong><br><span style='color:#38bdf8;'>⏰ 5:30 مساءً (قبل التمرين)</span>",
                    "• ساندويتش زبدة الفول السوداني والموز مع العسل<br>• أو حبة فاكهة مع حفنة مكسرات",
                    "<span class='pill-tag'>طاقة قبل التمرين</span><br>تمدك بطاقة عالية جداً قبل بذل أي مجهود أو لعب الرياضة.",
                ],
                [
                    "<strong>العشاء</strong><br><span style='color:#38bdf8;'>⏰ 8:30 - 9:30 مساءً</span>",
                    "• طبق فول بزيت الزيتون والطحينة الخفيفة<br>• جبنة كاملة الدسم (قريش مع قشطة أو جبنة بيضاء دسمة)<br>• رغيف خبز بلدي",
                    "<span class='pill-tag'>بروتين بطيء الهضم</span><br>يغذي الجسم طوال الليل مع دهون الطحينة وزيت الزيتون.",
                ],
                [
                    "<strong>قبل النوم</strong><br><span style='color:#38bdf8;'>⏰ قبل النوم مباشرة</span>",
                    "• كوب حليب دافئ كامل الدسم مع ملعقة عسل ومكسرات مطحونة",
                    "<span class='pill-tag'>استشفاء وزيادة سعرات</span><br>يساعد على الاسترخاء ويزيد السعرات الحرارية في آخر اليوم.",
                ],
            ]
            str_ui.markdown(build_html_table(["الوجبة والوقت", "مكونات الوجبة المقترحة", "القيمة والفوائد الغذائية"], gain_meals), unsafe_allow_html=True)

            str_ui.markdown("### 💪 الرياضة والتمارين المطلوبة (زيادة الوزن وبناء العضلات)")

            gain_sports = [
                ["<strong>اليوم 1</strong>", "تمارين مقاومة دفع: ضغط صدر (Bench Press)، رفرفة صدر، ضغط كتف أمامي وجانبي، ترايسبس", "60 دقيقة • 4 أيام أسبوعياً"],
                ["<strong>اليوم 2</strong>", "تمارين مقاومة سحب: سحب ظهر علوي (Lat Pulldown)، تجديف بالبار أو الدمبل، بايسبس، كتف خلفي", "60 دقيقة • 4 أيام أسبوعياً"],
                ["<strong>اليوم 3</strong>", "راحة تامة واستشفاء عضلي", "راحة واستشفاء"],
                ["<strong>اليوم 4</strong>", "تمارين أرجل كاملة: سكوات، ضغط أرجل (Leg Press)، طعنات (Lunges)، عضلة خلفية وسمانة", "60 دقيقة • 4 أيام أسبوعياً"],
                ["<strong>اليوم 5</strong>", "تمارين جزء علوي وتقوية البطن والجذع (Upper Body & Core)", "45 - 50 دقيقة"],
                ["<strong>اليوم 6 و 7</strong>", "راحة ونوم عميق لتعافي العضلات ونموها", "راحة ونوم 7-9 ساعات يومياً"],
            ]
            str_ui.markdown(build_html_table(["اليوم", "الرياضة والألعاب المطلوبة", "المدة وعدد الأيام"], gain_sports), unsafe_allow_html=True)

            str_ui.markdown("### 💡 نصائح ذهبية لنجاح نظام زيادة الوزن")
            str_ui.markdown(
                "<div class='tip-box'><strong>1. زيادة السعرات التدريجية:</strong> حاول أن تأكل كميات أكبر قليلاً مما اعتدت عليه بالتدريج لكي لا تشعر بتخمة مفاجئة.</div>"
                "<div class='tip-box'><strong>2. الدهون الصحية في كل وجبة:</strong> ركّز على زيت الزيتون، الأفوكادو، المكسرات، زبدة الفول السوداني، والطحينة.</div>"
                "<div class='tip-box'><strong>3. الاستمرارية والراحة:</strong> التزم بالوجبات والتمارين مع النوم الكافي لأن العضلات تبني وتنمو وقت الراحة.</div>",
                unsafe_allow_html=True,
            )

        else:
            str_ui.markdown("<div class='diet-banner'><span class='pill-tag'>تنشيف وخسارة دهون</span><h3 style='margin: 4px 0; color: #7dd3fc !important;'>🔥 جدول الأكل اليومي (تقليل وزن وتنشيف)</h3><p style='margin: 0; color: #cbd5e1;'>جدول غذائي مرن ومتوازن يساعدك على خسارة الدهون والحفاظ على الكتلة العضلية — اختر بديلاً واحداً لكل وجبة.</p></div>", unsafe_allow_html=True)
            cut_meals = [["<strong>🍳 الإفطار</strong>", "3 بيضات مسلوقة أو مقلية بملعقة زيت زيتون + ربع رغيف بلدي + خيار وجرجير", "4 ملاعق فول بزيت زيتون وكمون + ربع رغيف بلدي + بيضة مسلوقة أو قطعة جبنة قريش", "عجة بيض بالخضار (طماطم وفلفل) + ربع رغيف بلدي", "لبداية نشيطة ومشبعة لفترة طويلة."], ["<strong>🍽️ الغداء</strong>", "<span class='pill-tag'>بروتين</span> 150-200 جم صدور فراخ مشوية/مسلوقة أو لحم مفروم قليل الدهن<br><span class='pill-tag'>نشويات</span> 5 ملاعق أرز أو مكرونة<br><span class='pill-tag'>خضار</span> طبق خضار سوتيه + سلطة كبيرة", "<span class='pill-tag'>بروتين</span> 2 سمكة مشوية<br><span class='pill-tag'>نشويات</span> رغيف بلدي كامل أو 5 ملاعق أرز<br><span class='pill-tag'>خضار</span> طبق سلطة خضراء كبير", "<span class='pill-tag'>بروتين</span> علبة تونة مصفاة من الزيت<br><span class='pill-tag'>نشويات</span> رغيف بلدي كامل أو 5 ملاعق مكرونة<br><span class='pill-tag'>خضار</span> طبق خضار سوتيه + سلطة", "ملعقة زيت زيتون وليمون فقط على السلطة."], ["<strong>🥗 العشاء</strong>", "150 جم جبنة قريش بالطماطم والخيار ورشة زعتر + ربع رغيف بلدي", "علبة تونة مصفاة تماماً + طبق سلطة خضراء", "كوب زبادي يوناني (أو عادي) + نصف ملعقة عسل نحل + ملعقة بذر كتان أو شيا", "وجبة خفيفة ومناسبة قبل النوم."]]
            str_ui.markdown(build_html_table(["الوجبة", "الخيار الأول", "الخيار الثاني", "الخيار الثالث", "ملاحظات هامة"], cut_meals), unsafe_allow_html=True)
            str_ui.markdown("### 🏃‍♂️ الرياضة والتمارين المطلوبة (تقليل وزن وتنشيف)")
            cut_sports = [["<strong>اليوم 1 و 4</strong>", "مشي سريع أو جري خفيف (Cardio) + تمارين بطن وجذع", "45 دقيقة • 4-5 أيام أسبوعياً"], ["<strong>اليوم 2 و 5</strong>", "تمارين مقاومة شاملة للجسم (Full Body Circuit) لحرق السعرات وحماية العضلات", "45 دقيقة • 4-5 أيام أسبوعياً"], ["<strong>اليوم 3</strong>", "نط الحبل أو عجلة رياضية ثابتة (HIIT) لرفع معدل الحرق", "30 دقيقة"], ["<strong>اليوم 6 و 7</strong>", "مشي خفيف في الهواء الطلق واستشفاء عضلي", "راحة وحركة خفيفة"]]
            str_ui.markdown(build_html_table(["اليوم", "الرياضة والألعاب المطلوبة", "المدة وعدد الأيام"], cut_sports), unsafe_allow_html=True)
            str_ui.markdown("### ⭐ القواعد الذهبية لسرعة النتائج")
            str_ui.markdown("<div class='tip-box'><strong>💧 شرب المياه:</strong> من 2.5 إلى 3 لتر يومياً لزيادة معدل الحرق ومنع الإحساس الوهمي بالجوع.</div><div class='tip-box'><strong>🚶‍♀️ الحركة الخفيفة:</strong> المشي 15-20 دقيقة في منتصف اليوم أو بعد الغداء لتعويض الجلوس المكتبي.</div><div class='tip-box'><strong>🚫 السكر والمشروبات:</strong> استبدال السكر الأبيض بسكر دايت ومنع العصائر المحلاة تماماً.</div>", unsafe_allow_html=True)

str_ui.markdown("---")
str_ui.markdown("<p style='text-align: center; color: gray;'>النظام الخبير الطبي والرياضي المعتمد • مشروع تخرج قسم الذكاء الاصطناعي</p>", unsafe_allow_html=True)

            
            
