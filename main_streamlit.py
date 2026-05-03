import streamlit as st

class Subject:
  def __init__(self,name,room,teacher,syllabus):
    self.name = name #授業名
    self.room = room #教室
    self.teacher = teacher #先生
    self.syllabus = syllabus #授業内容
  def show_summary(self):
    st.write(f"###{self.name}")
    st.write(f"📍場所:{self.room}")
    st.write(f"📖内容:{self.syllabus}")

#授業の下準備
math_a = Subject("数学α","HR教室","大石先生","一次関数")
social = Subject("社会","HR教室","矢子先生","中国の歴史")
japanese_b = Subject("国語古典","HR教室","中村(圭)先生","いろは歌")
#辞書に打ち込む
monday_timetable = {
    "1限": math_a,
    "2限": social,
    "3限": japanese_b,
}
#入力欄を st.selectbox に変える
st.title("デジタル時間割")
x = st.selectbox("何限の授業を見ますか？", ["1","2","3"])

if f"{x}限"in monday_timetable:
  monday_timetable[f"{x}限"].show_summary()
else:
  st.error("その授業はありません。")#エラーを赤く出す

