import streamlit as st
import random
import time

# تحميل الصور
head_img_path = "Head.jpg"  # استبدل بمسار صورة الوجه
tail_img_path = "Tail.jpg"  # استبدل بمسار صورة الظهر

# إعداد النسب الافتراضية
EXPECTED_H = 0.5  # احتمال الوجه
EXPECTED_T = 0.5  # احتمال الظهر

# إعداد واجهة المستخدم
st.title("لعبة تقليب العملة")
st.write("اضغط على زر 'Toss' لتقليب العملة.")

# منطقة عرض الصورة
placeholder = st.empty()

# زر تقليب العملة
if st.button("Toss"):
    # تقليب سريع لمدة ثانيتين
    start_time = time.time()
    while time.time() - start_time < 2:
        if random.choice([True, False]):
            placeholder.image(head_img_path, width=200)
        else:
            placeholder.image(tail_img_path, width=200)
        time.sleep(0.1)  # تأخير بسيط لمحاكاة التقليب

    # اختيار النتيجة النهائية
    final_result = random.choices(["head", "tail"], weights=[EXPECTED_H, EXPECTED_T])[0]
    if final_result == "head":
        placeholder.image(head_img_path, width=200)
        st.success("النتيجة: وجه العملة!")
    else:
        placeholder.image(tail_img_path, width=200)
        st.success("النتيجة: ظهر العملة!")
