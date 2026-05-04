import streamlit as st
import datetime 
import pandas as pd
import time


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


def get_current_period():  #デバッグのため、本番用コードをコメントアウトする。
  #---コメントアウト
  #now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
  
  #日本時間に合わせるため、調整
  #---デバッグ用↓(9時30分に設定)
  test_now = datetime.time(10,30)
  current_time = test_now.hour * 100 + test_now.minute
  
  #---コメントアウト
  #current_time = now.hour * 100 + now.minute
  if 915 <= current_time <= 1005:
    return "1限"
  elif 1015 <= current_time <= 1105:
    return "2限"
  elif 1115 <= current_time <= 1205:
    return "3限"
  elif 1250 <= current_time <= 1340:
    return "4限"
  elif 1350 <= current_time <= 1440:
    return "5限"
  elif 1450 <= current_time <= 1540:
    return "6限"
  else:
    return "休み時間・課外時間"


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


#---辞書に打ち込む---
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

#入力欄を st.selectbox に変える。校時の選択。
st.title("デジタル時間割🚀")
#現在の校時を表示
current_period = get_current_period()
st.info(f"🕰️現在の時刻による判定:{current_period}")
#デバッグ用時刻表示
st.write(f"デバッグ用:現在のサーバー内日本時間:{datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%H:%M')}")

countdown_placeholder = st.empty()
if "限" in current_period:
  target_time = start_times.get(current_period)
#日本時間の現在時刻を取得
now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
now_for_calc = today.replace(hour=10, minute=30, second=0)
if current_period == "1限":
  end_time = today.replace(hour=10,minute=5,second=0)
  remaining = end_time - now_for_calc
  #end_time = now_jst.replace(hour=10,minute=5,second=0)
  #remaining = end_time - now_jst
  #mins,secs = divmod(remaining.seconds,60)
  #st.metric(label="1限終了まで",value=f"{mins}分 {secs}秒")
if current_period == "2限":
  end_time = today.replace(hour=11,minute=5,second=0)
  remaining = end_time - now_for_calc
  
#残り時間がプラスの時だけ表示
if remaining.total_seconds() > 0:
  mins,secs = divmod(int(remaining.total_seconds()), 60)
  st.metric(label="1限終了まで",value=f"{mins}分 {secs}秒")
else:
 st.write("授業は終了しています")
  
#曜日の選択、初期化。
day = st.segmented_control("曜日を選択", ["月","火","水","木","金","土"])
default_index = 0
if "限" in current_period:
  try:
    default_index = int(current_period.replace("限","")) - 1
  except:
    default_index = 0
#校時の選択
x = st.radio("何限の授業を見ますか？",["1","2","3","4","5","6"],index=default_index, horizontal=True)
key = f"{x}限"

#表示する。
if day: #曜日が選択されているときだけ、曜日の時間割の辞書を呼び出し、表示する。
  selected_day_dict = all_timetables[day]
  if key in selected_day_dict:
    subject = selected_day_dict[key]
    subject.show_summary()
  else:
   st.error("その授業はありません。")#エラーを赤く出す
else: #もし選ばれていなければ、選択するように表示する。
  st.write("上から曜日を選んでください。")

st.divider()
st.subheader("📅今週の時間割")

#表用のデータを作成
timetable_rows = []
for p in ["1限","2限","3限","4限","5限","6限"]:
  row = {"校時":p}
  for d_name, d_dict in all_timetables.items():
    row[d_name] = d_dict[p].name if p in d_dict else "-"
  timetable_rows.append(row)

df = pd.DataFrame(timetable_rows)
st.table(df)
