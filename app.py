import streamlit as str_ui

# 1. إعدادات الصفحة
str_ui.set_page_config(
    page_title="AI Clinical & Medical Expert System",
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
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.4);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .rx-card {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(17, 24, 39, 0.98));
        border: 1px solid #2dd4bf;
        box-shadow: 0 0 20px rgba(45, 212, 191, 0.2);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .emergency-card {
        background: rgba(127, 29, 29, 0.25);
        border: 1px solid #f87171;
        box-shadow: 0 0 15px rgba(248, 113, 113, 0.2);
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
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
str_ui.title("🩺 النظام الخبير الطبي والسريري الذكي")
str_ui.markdown("<p style='color: #94a3b8; font-size: 18px; margin-top: -10px;'>محرك التشخيص السريري المعتمد وإرشادات الطوارئ الطبية</p>", unsafe_allow_html=True)
str_ui.markdown("---")

# الشريط الجانبي لاختيار المرض أو الحالة
str_ui.sidebar.header("👤 الملف السريري للمريض")
age = str_ui.sidebar.number_input("العمر (بالسنوات)", 1, 120, 25)
weight = str_ui.sidebar.number_input("الوزن (كجم)", 20.0, 250.0, 70.0)
height = str_ui.sidebar.number_input("الطول (سم)", 50.0, 250.0, 170.0)
gender = str_ui.sidebar.selectbox("الجنس", ["ذكر", "أنثى"])

str_ui.sidebar.markdown("---")
str_ui.sidebar.subheader("📋 اختر الحالة المرضية أو العرض:")

# قائمة الـ 12 مرض وحالة كما طلبتِ بالحرف
disease_options = [
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

selected_disease = str_ui.sidebar.selectbox("اختر الحالة للتشخيص والعلاج:", disease_options)

if str_ui.button("⚡ تشغيل التشخيص السريري وعرض التقرير", use_container_width=True):
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    str_ui.markdown("## 🧠 التقرير التشخيصي وإرشادات التصرف المبدئي")
    
    # 1. مرض السكر
    if "1. مرض السكر" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">1. مرض السكر (Diabetes)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>قياس مستوى السكر بجهاز قياس السكر إن توفر.</li>
                <li>شرب الماء بانتظام وتناول الوجبات في مواعيدها.</li>
                <li>متابعة مستوى السكر وتسجيل القراءات.</li>
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
            <p><strong>الدواء الموصوف:</strong> الالتزام بالبرنامج الدوائي المعتمد ومنظم السكر (مثل الميتفورمين أو الإنسولين بحسب إرشادات الطبيب المعالج).</p>
        </div>
        """, unsafe_allow_html=True)

    # 2. ارتفاع ضغط الدم المزمن
    elif "2. ارتفاع ضغط الدم المزمن" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">2. ارتفاع ضغط الدم المزمن (Chronic Hypertension)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الجلوس في مكان هادئ والراحة.</li>
                <li>قياس ضغط الدم بعد الجلوس بهدوء.</li>
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

    # 3. أمراض القلب والأوعية الدموية
    elif "3. أمراض القلب والأوعية الدموية" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">3. أمراض القلب والأوعية الدموية (Cardiovascular Diseases)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>إيقاف أي مجهود بدني والجلوس في وضع مريح.</li>
                <li>تهدئة الشخص وعدم تركه بمفرده.</li>
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
            <p><strong>الدواء الموصوف:</strong> أدوية الطوارئ القلبية الخاصة بالمريض (مثل النيتروجليسرين) حسب إرشادات الطبيب المعالج.</p>
        </div>
        """, unsafe_allow_html=True)

    # 4. مشاكل الجهاز التنفسي
    elif "4. مشاكل الجهاز التنفسي" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">4. مشاكل الجهاز التنفسي (Respiratory Problems)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الجلوس في وضع مستقيم وتوفير هواء نقي وتهوية المكان.</li>
                <li>الابتعاد عن الدخان والغبار والروائح القوية.</li>
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

    # 5. الحمى وارتفاع درجة الحرارة
    elif "5. الحمى وارتفاع درجة الحرارة" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">5. الحمى وارتفاع درجة الحرارة (Fever)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>قياس درجة الحرارة بترمومتر، وشرب السوائل بانتظام.</li>
                <li>الراحة والحصول على قسط كافٍ من النوم وارتداء ملابس خفيفة ومريحة.</li>
                <li>استخدام كمادات ماء فاتر عند الحاجة.</li>
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
            <p><strong>الدواء الموصوف:</strong> <strong>Paracetamol (باراسيتامول)</strong> - 500 ملم قرص عند اللزوم لخفض الحرارة وتسكين الألم.</p>
        </div>
        """, unsafe_allow_html=True)

    # 6. السعال والبرد والتهاب الحلق
    elif "6. السعال والبرد والتهاب الحلق" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">6. السعال والبرد والتهاب الحلق (Cough, Cold & Sore Throat)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>شرب المشروبات الدافئة وتناول العسل لتخفيف السعال إذا لم توجد حساسية منه.</li>
                <li>الغرغرة بالماء الدافئ والملح مع عدم بلعه، واستخدام محلول ملحي للأنف.</li>
                <li>الراحة وشرب كمية كافية من السوائل.</li>
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
            <p><strong>الدواء الموصوف:</strong> <strong>Congestal (كنجستال)</strong> - قرص كل 8 ساعات لأعراض البرد والرشح والسعال.</p>
        </div>
        """, unsafe_allow_html=True)

    # 7. حموضة المعدة
    elif "7. حموضة المعدة" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">7. حموضة المعدة (Heartburn & Acidity)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الجلوس في وضع مستقيم وتجنب الاستلقاء مباشرة بعد الأكل.</li>
                <li>تناول وجبات صغيرة والابتعاد عن الأطعمة الحارة أو الدسمة التي تزيد الحموضة.</li>
                <li>شرب كميات مناسبة من الماء لتقليل تهيج جدار المعدة.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> <strong>Vonacidan (فوناسيدان)</strong> - حسب الإرشادات الطبية لتقليل حموضة المعدة.</p>
        </div>
        """, unsafe_allow_html=True)

    # 8. القولون العصبي
    elif "8. القولون العصبي" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">8. القولون العصبي (IBS)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الابتعاد عن التوتر والقلق ومصادر الضغط العصبي.</li>
                <li>تجنب الأطعمة المهيجة للقولون (البقوليات، الحارة، المشروبات الغازية).</li>
                <li>تناول وجبات صغيرة ومتعددة بانتظام وشرب الأعشاب المهدئة (كالنعناع والبابونج).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> <strong>Replix (ريبليكس)</strong> - لتنظيم حركة القولون وتخفيف التشنجات والتقلصات.</p>
        </div>
        """, unsafe_allow_html=True)

    # 9. الألم والصداع
    elif "9. الألم والصداع" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">9. الألم والصداع (Headache & Pain)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الجلوس في مكان هادئ ومظلم نسبياً والابتعاد عن الإضاءات القوية والشاشات.</li>
                <li>عمل كمادات باردة على الجبهة أو أخذ قسط كافٍ من النوم والراحة.</li>
                <li>شرب الماء بانتظام لتجنب الجفاف المسبب للصداع.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> <strong>Paracetamol (باراسيتامول)</strong> - قرص واحد لتسكين الصداع والآلام العامة عند اللزوم.</p>
        </div>
        """, unsafe_allow_html=True)

    # 10. ارتجاع المريء
    elif "10. ارتجاع المريء" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">10. ارتجاع المريء (GERD)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>الجلوس في وضع مستقيم بعد تناول الطعام وتجنب الاستلقاء لمدة ساعتين إلى ثلاث ساعات.</li>
                <li>تناول وجبات صغيرة ورفع الجزء العلوي من الجسم أثناء النوم إذا كانت الأعراض ليلية.</li>
                <li>الابتعاد عن الأطعمة التي تزيد الحموضة والدهون والكافيين.</li>
            </ul>
            <div class="emergency-card">
                <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> ظهر ألم شديد أو ضغط في الصدر، خاصة مع العرق أو ضيق التنفس أو الدوخة، أو حدث قيء دموي أو صعوبة شديدة في البلع.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> مضادات الحموضة و منظمات حركة المريء والمعدة.</p>
        </div>
        """, unsafe_allow_html=True)

    # 11. آلام الظهر
    elif "11. آلام الظهر" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">11. آلام الظهر (Back Pain)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>تجنب حمل الأشياء الثقيلة وتغيير وضعية الجلوس باستمرار.</li>
                <li>المشي الخفيف والحركة الهادئة حسب القدرة مع استخدام كمادات باردة أو دافئة ملفوفة في قماش.</li>
                <li>الحصول على الراحة دون ملازمة السرير لفترات طويلة.</li>
            </ul>
            <div class="emergency-card">
                <strong>🚨 اذهب للطوارئ فورًا إذا:</strong> صاحَب الألم ضعف مفاجئ بالساقين، أو فقدان التحكم في البول أو البراز، أو فقدان الإحساس بمنطقة ما بين الفخذين، أو حدث بعد إصابة قوية.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> مسكنات الآلام وباسط العضلات المعتمد حسب استشارة الطبيب.</p>
        </div>
        """, unsafe_allow_html=True)

    # 12. آلام المفاصل والعضلات
    elif "12. آلام المفاصل والعضلات" in selected_disease:
        str_ui.markdown("""
        <div class="glow-card">
            <h3 style="color: #38bdf8; margin-top: 0;">12. آلام المفاصل والعضلات (Joint & Muscle Pain)</h3>
            <p><strong>التصرف المبدئي:</strong></p>
            <ul>
                <li>إراحة الجزء المصاب مؤقتًا واستخدام كمادات باردة ملفوفة في منشفة لمدة قصيرة عند وجود تورم حديث.</li>
                <li>تجنب المجهود والحركات التي تزيد الألم وتحريك المفصل بلطف عندما تسمح الحالة بذلك.</li>
                <li>شرب الماء بانتظام لتجنب جفاف العضلات.</li>
            </ul>
            <p style="color: #fca5a5;"><strong>اذهب للطبيب سريعًا إذا:</strong> كان المفصل شديد التورم أو ساخنًا ومحمرًا، أو صاحبه ارتفاع حرارة، أو تعذر تحريكه أو تحميل الوزن عليه.</p>
        </div>
        """, unsafe_allow_html=True)
        
        str_ui.markdown("""
        <div class='rx-card'>
            <h3 style="color: #2dd4bf; margin-top: 0;">💊 الروشتة الطبية المعتمدة</h3>
            <p><strong>الدواء الموصوف:</strong> الكريمات الموضعية المضادة للالتهاب ومسكنات الآلام المرتبطة بالعضلات.</p>
        </div>
        """, unsafe_allow_html=True)

str_ui.markdown("---")
str_ui.markdown("<p style='text-align: center; color: gray;'>النظام الخبير الطبي المعتمد • مشروع تخرج قسم الذكاء الاصطناعي</p>", unsafe_allow_html=True)
