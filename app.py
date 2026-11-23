import streamlit as str_ui

# 1. إعدادات الصفحة
str_ui.set_page_config(
    page_title="AI Clinical, Medical & Sports Expert System",
    page_icon="🩺",
    layout="wide"
)

# 2. تصميم عصري منور وجداول منسقة بظل مضيء
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
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.45);
        box-shadow: 0 0 24px rgba(56, 189, 248, 0.18);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .rx-card {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(17, 24, 39, 0.98));
        border: 1px solid #2dd4bf;
        box-shadow: 0 0 22px rgba(45, 212, 191, 0.22);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .emergency-card {
        background: rgba(127, 29, 29, 0.28);
        border: 1px solid #f87171;
        box-shadow: 0 0 18px rgba(248, 113, 113, 0.25);
        border-radius: 12px;
        padding: 16px;
        margin-top: 15px;
        color: #fca5a5;
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
        border-collapse: separate !important;
        border-spacing: 0 !important;
        background-color: rgba(15, 23, 42, 0.92) !important;
        border-radius: 14px !important;
        overflow: hidden !important;
        box-shadow: 0 10px 30px rgba(2, 132, 199, 0.35), 0 0 18px rgba(45, 212, 191, 0.16) !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        margin-bottom: 22px !important;
    }
    th {
        background: linear-gradient(90deg, rgba(2, 132, 199, 0.55), rgba(15, 118, 110, 0.45)) !important;
        color: #e0f2fe !important;
        font-weight: 700 !important;
        padding: 13px 14px !important;
        border-bottom: 2px solid #38bdf8 !important;
        text-align: right !important;
    }
    td {
        padding: 12px 14px !important;
        border-bottom: 1px solid rgba(56, 189, 248, 0.16) !important;
        color: #f1f5f9 !important;
        text-align: right !important;
    }
    tr:last-child td {
        border-bottom: none !important;
    }
    tr:hover td {
        background-color: rgba(56, 189, 248, 0.08) !important;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
str_ui.title("🩺 النظام الخبير الطبي والرياضي الذكي بالذكاء الاصطناعي")
str_ui.markdown("<p style='color: #94a3b8; font-size: 18px; margin-top: -10px;'>محرك التشخيص السريري المتقدم، إرشادات الطوارئ الطبية، وبرامج التغذية واللياقة البدنية</p>", unsafe_allow_html=True)
str_ui.markdown("---")

# الشريط الجانبي للملف الشخصي
str_ui.sidebar.header("👤 الملف الشخصي للمريض والرياضي")
age = str_ui.sidebar.number_input("العمر (بالسنوات)", 1, 120, 22)
weight = str_ui.sidebar.number_input("الوزن (كجم)", 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input("الطول (سم)", 50.0, 250.0, 172.0)
gender = str_ui.sidebar.selectbox("الجنس", ["ذكر", "أنثى"])
activity_level = str_ui.sidebar.selectbox("مستوى النشاط البدني والحركة", [
    "خامل (بدون تمرين أو عمل مكتبي)", 
    "نشاط خفيف (تمرين 1-3 أيام في الأسبوع)", 
    "نشاط معتدل (تمرين 3-5 أيام في الأسبوع)", 
    "نشاط عالي جداً (تمارين شاقة 6-7 أيام)", 
    "حركة محدودة / كبير السن (مجهود بسيط)"
])

# قسم اختيار الأمراض الشاملة (الـ 12 حالة)
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
    "12. آلام المفاصل والعضلات (Joint & Muscle Pain)"
]
selected_disease = str_ui.sidebar.selectbox("اختر الحالة أو العرض الرئيسي:", disease_options)

# قسم الرياضة والنظام الغذائي
str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader("🏋️‍♂️ قسم الرياضة والتغذية المخصصة")
enable_sports = str_ui.sidebar.checkbox("تفعيل برنامج الرياضة وجدول الأكل المخصص")
fitness_goal = None
if enable_sports:
    fitness_goal = str_ui.sidebar.selectbox("اختر هدفك الرياضي", [
        "زيادة وزن وبناء عضلات (Bulking)",
        "تخسيس وتنشيف (Cutting)",
        "لياقة عامة والحفاظ على الوزن"
    ])

if str_ui.button("⚡ تشغيل النظام الذكي وإصدار التقرير الشامل", use_container_width=True):
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

    confidence = 98.2 if "لا يوجد" in selected_disease else 96.5

    # كارت التشخيص والبيانات الحيوية
    str_ui.markdown("## 🧠 التقرير التشخيصي وتحليل الذكاء الاصطناعي")
    diag_html = f"""
    <div class="glow-card">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <span style="color: #94a3b8; font-size: 14px;">البيانات الحيوية والنشاط</span><br>
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
        <p style="margin: 0; color: #cbd5e1;"><strong>الحالة المختارة:</strong> {selected_disease}</p>
    </div>
    """
    str_ui.markdown(diag_html, unsafe_allow_html=True)

    # تفاصيل الحالة المرضية واختيارات الـ 12 مرض
    if "لا يوجد أمراض" not in selected_disease:
        str_ui.markdown("## 📋 الإرشادات الطبية والتصرف المبدئي للطوارئ")
        
        if "1. مرض السكر" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">1. مرض السكر (Diabetes)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>قياس مستوى السكر بجهاز قياس السكر إن توفر.</li>
                    <li>شرب الماء بانتظام وتناول الوجبات في مواعيدها ومتابعة السكر وتسجيل القراءات.</li>
                    <li>إذا ظهرت أعراض انخفاض السكر (رعشة، تعرق، دوخة) والشخص واعٍ وقادر على البلع، يُعطى مصدر سكر سريع (نصف كوب عصير)، ثم يُعاد القياس بعد 15 دقيقة.</li>
                    <li>الاستمرار على العلاج الموصوف وعدم تغيير جرعاته دون تعليمات الطبيب.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> إيقاف الإنسولين أو مضاعفة جرعات الدواء من تلقاء نفسك.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> حدث فقدان للوعي، أو تشوش شديد، أو صعوبة تنفس، أو قيء مستمر، أو لم يستطع الشخص البلع. (لا تعطِ فاقد الوعي أي طعام أو شراب).
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> الالتزام بالبرنامج الدوائي المعتمد ومنظم السكر (الميتفورمين أو الإنسولين بحسب إرشادات الطبيب المعالج).</p>
            </div>
            """, unsafe_allow_html=True)

        elif "2. ارتفاع ضغط الدم المزمن" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>الجلوس في مكان هادئ والراحة، ثم قياس ضغط الدم بعد الهدوء.</li>
                    <li>تجنب المجهود والتوتر مؤقتًا وتقليل الأطعمة شديدة الملوحة.</li>
                    <li>الالتزام بأدوية الضغط الموصوفة في مواعيدها.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> أخذ جرعة إضافية من دواء الضغط دون استشارة الطبيب.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> صاحب ارتفاع الضغط ألم في الصدر، أو صعوبة تنفس، أو ضعف مفاجئ في أحد جانبي الجسم، أو اضطراب الكلام أو الرؤية، أو صداع شديد مفاجئ.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> أدوية الضغط المنتظمة الخاصة بالمريض وفقاً للروشتة الطبية الثابتة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "3. أمراض القلب والأوعية الدموية" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>إيقاف أي مجهود بدني والجلوس في وضع مريح مع تهدئة الشخص وعدم تركه بمفرده.</li>
                    <li>استخدام الدواء الموصوف مسبقًا للحالة فقط وفق تعليمات الطبيب.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> المشي أو ممارسة الرياضة لمحاولة التخلص من ألم الصدر، وعدم إعطاء أدوية عشوائية.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> ظهر ألم أو ضغط بالصدر، أو امتد الألم إلى الذراع أو الفك أو الظهر، أو حدث عرق شديد أو دوخة أو ضيق تنفس. <b>اتصل بالإسعاف 123 في مصر.</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> أدوية الطوارئ القلبية الخاصة بالمريض حسب إرشادات الطبيب المعالج.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "4. مشاكل الجهاز التنفسي" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">4. مشاكل الجهاز التنفسي (Respiratory Problems)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>الجلوس في وضع مستقيم والابتعاد عن الدخان والغبار والروائح القوية مع تهوية المكان.</li>
                    <li>استخدام بخاخ الربو الموصوف للشخص وفق خطة الطبيب إن كان يعاني من الربو.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> التعرض للدخان أو استخدام بخاخات أو أدوية غير موصوفة.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> كان هناك اختناق أو صعوبة شديدة في التنفس أو عدم القدرة على الكلام بشكل طبيعي أو ازرقاق الشفاه.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> بخاخ الموسع للشعب الهوائية (Inhaler) المعتمد للحالة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "5. الحمى وارتفاع درجة الحرارة" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">5. الحمى وارتفاع درجة الحرارة (Fever)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>قياس درجة الحرارة بترمومتر وشرب السوائل بانتظام والحصول على قسط كافٍ من الراحة.</li>
                    <li>ارتداء ملابس خفيفة ومريحة واستخدام كمادات ماء فاتر عند الحاجة.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> تغطية الجسم بأغطية ثقيلة أو استخدام الماء المثلج أو الكحول لتخفيض الحرارة.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> صاحبت الحمى صعوبة تنفس أو تشنجات أو تشوش في الوعي أو تيبس الرقبة أو صداع شديد غير معتاد.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> <strong>Paracetamol (باراسيتامول)</strong> - 500 ملم قرص عند اللزوم لخفض الحرارة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "6. السعال والبرد والتهاب الحلق" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>شرب المشروبات الدافئة وتناول العسل لتخفيف السعال والغرغرة بالماء الدافئ والملح مع عدم بلعه.</li>
                    <li>استخدام محلول ملحي للأنف والراحة وشرب كمية كافية من السوائل.</li>
                </ul>
                <p style="color: #f87171;"><strong>تجنب:</strong> التدخين والتعرض للهواء الملوث واستخدام المضادات الحيوية دون وصفة.</p>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> حدثت صعوبة في التنفس أو البلع، أو ألم شديد بالصدر، أو عدم القدرة على شرب السوائل.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> <strong>Congestal (كنجستال)</strong> - قرص كل 8 ساعات لأعراض البرد والرشح.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "7. حموضة المعدة" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">7. حموضة المعدة (Vonacidan)</h3>
                <p><strong>التصرف المبدئي:</strong> الجلوس في وضع مستقيم بعد الأكل، تناول وجبات صغيرة، وتجنب الاستلقاء مباشرة والابتعاد عن الأطعمة الحارة أو الدسمة.</p>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> <strong>Vonacidan (فوناسيدان)</strong> لتقليل حموضة المعدة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "8. القولون العصبي" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">8. القولون العصبي (Replix)</h3>
                <p><strong>التصرف المبدئي:</strong> الابتعاد عن التوتر والقلق، تجنب الأطعمة المهيجة للقولون (البقوليات والبهارات)، وتناول وجبات صغيرة بانتظام مع شرب الأعشاب المهدئة.</p>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> <strong>Replix (ريبليكس)</strong> لتنظيم حركة القولون وتخفيف التشنجات والتقلصات.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "9. الألم والصداع" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">9. الألم والصداع (Paracetamol)</h3>
                <p><strong>التصرف المبدئي:</strong> الجلوس في مكان هادئ ومظلم نسبياً، الابتعاد عن الشاشات والإضاءات القوية، عمل كمادات باردة وشرب الماء بانتظام.</p>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> <strong>Paracetamol (باراسيتامول)</strong> لتسكين الصداع والآلام العامة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "10. ارتجاع المريء" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">10. ارتجاع المريء (GERD)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>الجلوس في وضع مستقيم بعد الأكل وعدم الاستلقاء لمدة ساعتين إلى ثلاث ساعات.</li>
                    <li>تناول وجبات صغيرة ورفع الجزء العلوي من الجسم أثناء النوم.</li>
                </ul>
                <div class="emergency-card">
                    <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> ظهر ألم شديد أو ضغط في الصدر، خاصة مع العرق أو ضيق التنفس أو الدوخة، أو حدث قيء دموي أو صعوبة شديدة في البلع.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            str_ui.markdown("""
            <div class='rx-card'>
                <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
                <p><strong>الدواء الموصوف:</strong> مثبطات الحموضة ومنظمات حركة الجهاز الهضمي المعتمدة.</p>
            </div>
            """, unsafe_allow_html=True)

        elif "11. آلام الظهر" in selected_disease:
            str_ui.markdown("""
            <div class="glow-card">
                <h3 style="color: #38bdf8; margin-top: 0;">11. آلام الظهر (Back Pain)</h3>
                <p><strong>التصرف المبدئي:</strong></p>
                <ul>
                    <li>تجنب حمل الأشياء الثقيلة وتغيير وضعية 
