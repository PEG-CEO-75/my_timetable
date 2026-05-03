
class Subject:
  def __init__(self,name,room,teacher,syllabus):
    self.name = name #授業名
    self.room = room #教室
    self.teacher = teacher #先生
    self.syllabus = syllabus #授業内容
  def show_summary(self):
    print(f"{self.name}です。場所は{self.room}です。内容は{self.syllabus}です。")

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
x = input("見たい校時を入力してください。")
if f"{x}限"in monday_timetable:
  monday_timetable[f"{x}限"].show_summary()
else:
  print("その授業はありません。")

