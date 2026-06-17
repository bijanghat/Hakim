import streamlit as st
import random

st.set_page_config(page_title="Flappy Bird")

if "bird_y" not in st.session_state:
    st.session_state.bird_y = 5
    st.session_state.score = 0
    st.session_state.pipe_gap = random.randint(2, 8)

st.title("🐦 Flappy Bird Mini")

if st.button("FLAP"):
    st.session_state.bird_y -= 1

st.session_state.bird_y += 1

bird_y = st.session_state.bird_y
pipe_gap = st.session_state.pipe_gap

board = []

for i in range(10):
    row = ""
    for j in range(20):
        if j == 15 and not (pipe_gap <= i <= pipe_gap + 2):
            row += "🟩"
        elif i == bird_y and j == 5:
            row += "🐦"
        else:
            row += "⬜"
    board.append(row)

for row in board:
    st.text(row)

if bird_y < 0 or bird_y > 9:
    st.error("Game Over!")
    st.session_state.bird_y = 5
    st.session_state.score = 0

st.write("Score:", st.session_state.score)
