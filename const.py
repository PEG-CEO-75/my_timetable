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
