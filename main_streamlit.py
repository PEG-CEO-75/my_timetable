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
#月曜
monday_timetable = {
    "1限": math_a,
    "2限": social,
    "3限": japanese_b,
    "4限":,
    "5限":,
    "6限":,
}
#火曜
tuesday_timetable = {
    "1限":,
    "2限":,
    "3限":,
    "4限":,
    "5限":,
    "6限":,
}       
#水曜
wednesday_timetable = {
    "1限":,
    "2限":,
    "3限":,
    "4限":,
    "5限":,
    "6限":,
}       
#木曜
thursday_timetable = {
    "1限":,
    "2限":,
    "3限":,
    "4限":,
    "5限":,
    "6限":,
}             
#金曜
friday_timetable = {
    "1限":,
    "2限":,
    "3限":,
    "4限":,
    "5限":,
    "6限":,
}       
#土曜
saturday_timetable = 
#入力欄を st.selectbox に変える。校時の選択。
st.title("デジタル時間割")
#曜日の選択
day = st.segmented_control("曜日を選択", ["月","火","水","木","金","土"])
#校時の選択
x = st.radio("何限の授業を見ますか？",["1","2","3","4","5","6"], horizontal=True)

#表示する。
if day == "月":
  if f"{x}限"in monday_timetable:
   monday_timetable[f"{x}限"].show_summary()
  else:
   st.error("その授業はありません。")#エラーを赤く出す
    

