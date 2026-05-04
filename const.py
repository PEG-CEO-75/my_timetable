import streamlit as st
import datetime

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
    st.write(f"🧑‍🏫先生:{self.teacher}")
#---授業の下準備---
math_a = Subject("数学α","HR教室","大石先生","一次関数")
math_b = Subject("数学β","HR教室","先生","いろいろな四角形")
social = Subject("社会","HR教室","矢子先生","中国の歴史")
japanese_a = Subject("現代文","HR教室","先生","宇宙に行くための素材")
japanese_b = Subject("国語古典","HR教室","中村(圭)先生","いろは歌")
science_1 = Subject("理科1","HR教室","中村（研）先生","回路と抵抗")
science_2 = Subject("理科2","HR教室","末廣先生","花のつくり")
english_katou = Subject("英語（加藤）","HR教室","加藤先生","接続詞")
english_araki = Subject("英語（荒木）","HR教室","荒木先生","？")
english_communication = Subject("英会話","レッスン2","越賀先生","？")
art = Subject("美術","美術室","氏家先生","レタリング")
music = Subject("音楽","音楽室","松田先生","？")
pe = Subject("体育","グラウンド","原先生","ハードル")
home_economics = Subject("家庭科","家庭科室","山本（通）先生","調理実習")
moral = Subject("道徳","HR教室","担任","？")
LHR = Subject("LHR","HR教室","担任","？")


#---辞書データ---
#月曜
monday_timetable = {
    "1限": math_a,
    "2限": social,
    "3限": japanese_b,
    "4限": pe,
    "5限": english_katou,
    "6限": science_1,
}
#火曜
tuesday_timetable = {
    "1限": japanese_b,
    "2限": english_katou,
    "3限": math_b,
    "4限": music,
    "5限": science_2,
    "6限": art,
}       
#水曜
wednesday_timetable = {
    "1限": pe,
    "2限": english_araki,
    "3限": math_b,
    "4限": english_katou,
    "5限": math_a,
    "6限": japanese_a,
}       
#木曜
thursday_timetable = {
    "1限": LHR,
    "2限": moral,
    "3限": social,
    "4限": english_araki,
    "5限": math_a,
    "6限": science_2,
}             
#金曜
friday_timetable = {
    "1限": english_communication,
    "2限": social,
    "3限": science_1,
    "4限": home_economics,
    "5限": home_economics,
    "6限": japanese_a,
}       
#土曜
saturday_timetable = {
    "1限":pe,
    "2限":japanese_a,
    "3限":math_b,
}  
#辞書に曜日と時間割を結びつける
all_timetables = {
  "月": monday_timetable,
  "火": tuesday_timetable,
  "水": wednesday_timetable,
  "木": thursday_timetable,
  "金": friday_timetable,
  "土": saturday_timetable
}

#---授業の開始時間を定義---    
start_times = {
  "1限":datetime.time(9,15),
  "2限":datetime.time(10,15),
  "3限":datetime.time(11,15),
  "4限":datetime.time(12,50),
  "5限":datetime.time(13,50),
  "6限":datetime.time(14,50)
}  
#---授業の終了時間を定義---
end_times = {
    "1限": datetime.time(10, 5),
    "2限前": datetime.time(10, 14),
    "2限": datetime.time(11, 5),
    "3限前": datetime.time(11, 14),
    "3限": datetime.time(12, 5),
    "4限前": datetime.time(12, 49),
    "4限": datetime.time(13, 40),
    "5限前": datetime.time(13, 49),
    "5限": datetime.time(14, 40),
    "6限前": datetime.time(14, 49),
    "6限": datetime.time(15, 40)
}
