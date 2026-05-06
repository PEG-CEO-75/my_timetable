import streamlit as st
import datetime 
import pandas as pd
import time
import const


#ファイル分割後。↓class

#---------
def get_current_period(): 
  now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
  current_time = now.hour * 100 + now.minute
  
  #下はデバッグ用。コメントアウト済み。
  #test_now = datetime.time(10,6)
  #current_time = test_now.hour * 100 + test_now.minute
  
  if 915 <= current_time <= 1005:
    return "1限"
  elif 1006 <= current_time <= 1014:
    return "2限前"
  elif 1015 <= current_time <= 1105:
    return "2限"
  elif 1106 <= current_time <= 1114:
    return "3限前"
  elif 1115 <= current_time <= 1205:
    return "3限"
  elif 1206 <= current_time <= 1249:
    return "4限前"  
  elif 1250 <= current_time <= 1340:
    return "4限"
  elif 1341 <= current_time <= 1349:
    return "5限前"  
  elif 1350 <= current_time <= 1440:
    return "5限"
  elif 1441 <= current_time <= 1449:
    return "6限前"  
  elif 1450 <= current_time <= 1540:
    return "6限"
  else:
    return "休み時間・課外時間"


#移行後。↓辞書

#--------

#入力欄を st.selectbox に変える。校時の選択。
st.title("デジタル時間割🚀")
#現在の校時を表示
current_period = get_current_period()
st.info(f"🕰️現在の時刻による判定:{current_period}")
#デバッグ用時刻表示
st.write(f"デバッグ用:現在のサーバー内日本時間:{datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%H:%M')}")

countdown_placeholder = st.empty()
if "限" in current_period:
  target_time = const.start_times.get(current_period)
#日本時間の現在時刻を取得
now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

#カウントダウン用。
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
now_for_calc = today #本番ではtodayに戻す
#下はデバッグ用。コメントアウト済み。
#now_for_calc = today.replace(hour=10,minute=6,second=0)
# end_times は const.py にあるので、const. をつける
if current_period in const.end_times:
  target_time_data = const.end_times[current_period]
  end_time = today.replace(hour=target_time_data.hour,minute=target_time_data.minute,second=0)
  while True:
    now_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    remaining = end_time - now_now
    if remaining.total_seconds() > 0:
      mins,secs = divmod(int(remaining.total_seconds()), 60)
      countdown_placeholder.metric(
        label=f"{current_period}終了まで",
        value=f"{mins}分{secs}秒"
      )
      time.sleep(1)
    else:
      countdown_placeholder.write(f"✅{current_period}が終了しました！")
      break
  try:
    if "前" in current_period:
      current_num = int(current_period.replace("限","").replace("前","")) - 1
    else:
      current_num = int(current_period.replace("限",""))
    next_period = f"{current_num + 1}限"
    
    if next_period in selected_day_dict:
      next_subject = selected_day_dict[next_period]
      st.write(f"**次の授業:**{next_subject.name} ({next_subject.room})")
    else:
      st.write("**次の授業:**今日の授業はこれで終了です!")
  except:
    pass
elif current_period == "休み時間・課外時間":
  st.write("🍵現在は休み時間または放課後です。ゆっくりしてください！")
    
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
if day: #曜日が選択されているときだけ、曜日の時間割の辞書を呼び出し、表示する。constをつける。
  selected_day_dict = const.all_timetables[day]
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
  for d_name, d_dict in const.all_timetables.items(): #constをつける
    row[d_name] = d_dict[p].name if p in d_dict else "-"
  timetable_rows.append(row)

df = pd.DataFrame(timetable_rows)
st.table(df)

#自動でサイトをリフレッシュ
time.sleep(10)
st.rerun()
