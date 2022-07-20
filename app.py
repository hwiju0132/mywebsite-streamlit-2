import streamlit as st
import sqlite3
import pandas as pd


con = sqlite3.connect('database.db')
cur = con.cursor()

def login_user(id,pw):
    cur.execute(f"SELECT * FROM users WHERE id = '{id}' and pwd = '{pw}'")
    return cur.fetchone()
st.sidebar.title('박주휘 데이터베이스')
st.title('박주휘 데이터베이스')
menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.write('로그인')


    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.text_input('패스워드',
                                     placeholder='패스워드를 입력하세요',
                                     type='password')

    login_btn = st.button('로그인')

    if login_btn:
        users_info = login_user(login_id, login_pw)

        st.write(users_info[2], '님 환영합니다.')
    st.sidebar.subheader('로그인')

if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.write('회원목록')

if menu == '회원가입':
    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        in_id = st.text_input('아이디', max_chars=12)
        in_name = st.text_input('성명', max_chars=10)
        in_pwd = st.text_input('비밀번호', type='password')
        in_pwd_chk = st.text_input('비밀번호 확인', type='password')

        submitted = st.form_submit_button('제출')
        if submitted:
            cur.execute(f"INSERT INTO users(id, pwd, name) VALUES ("
                        f"'{in_id}', '{in_pwd}', '{in_name}')")
            con.commit()
if menu == '회원목록':

    df = pd.read_sql("SELECT * FROM users", con)
    st.dataframe(df)



