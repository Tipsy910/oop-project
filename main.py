import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="City Temp",
                   page_icon=":💸",
                   layout="wide")

text = ('''สุขภาพทางการเงินเป็นเรื่องสำคัญ 
        ควรหมั่นตรวจอยู่อย่างสม่ำเสมอ 
        โดยเฉพาะในปัจจุบันที่การจับจ่ายใช้สอยสามารถโอนออกได้ง่าย
        ทำให้บางคนก็อาจมีภาระหนี้หนักเกินความจำเป็น''')
st.title(":rainbow[ตรวจสอบสุขภาพทางการเงิน]")
st.markdown(f"{text}")

col_1,col_2,col_3 = st.columns([1,0.1,1])

with col_1:
    st.text("")
    st.subheader('โปรดใส่ข้อมูลด้านล่างเพื่อเช็ค สถานะการเงิน')
    st.subheader('*1.สถานะการเงินอยู่ระดับไหน*')
    in_come1 = st.number_input("**ใส่รายได้ต่อปี**",min_value=0)
    pay = st.number_input("**รายจ่ายทั้งหมดต่อปี**",min_value=0)
    debt1 = st.number_input("**ภาระหนี้สินที่มี**",min_value=0)
    assets = st.number_input("**ทรัพย์สินทั้งหมด**Ex หุ้น ที่ดิน อสังหาริมทรัพย์**",min_value=0)
    label_1 = ''
    if  in_come1 and pay and debt1 and assets:
        all = in_come1 - pay - debt1 + assets
        if all > 0:
            label_1 = (':green[สถานะการเงินยังคงเป็นบวก สุขภาพทางการเงินยังคงดีอยู่]😎😎')
        else:
            label_1 = (':red[สถานะการเงินติดลบ การเงินกำลังมีปัญหา]😭😭')
    st.markdown(label_1)
  #----------------------  
    st.text("")
    st.subheader("*2.เช็กสภาพคล่องทางการเงิน*")
    in_come2 = st.number_input("**ใส่รายได้ต่อเดือน**",min_value=0)
    pay2 = st.number_input("**รายจ่ายต่อเดิอน**",min_value=0)
    liquidity = 0
    if assets and in_come2:
        liquidity = round(in_come2/pay2)
    st.write(f"กระแสเงินสดสุธิอยู่ที่ {liquidity} ")
    #----------------------
    st.text("")
    st.subheader('**3.สุขภาพภาระหนี้ยังไหวอยู่ไหม**')
    st.write('**:red[หากต้องการให้การดำรงชีวิตเป็นไปอย่างปกติ หนี้ที่ต้องผ่อนทั้งหมดในแต่ละเดือนแล้ว ไม่ควรเกิน 35%]**')
    in_come3 = st.number_input("**ใส่รายในแต่ละเดือน**",min_value=0)
    debt2 = st.number_input("**ภาระหนี้สินต่อเดือน**",min_value=0)
    emoji = '😇😇'
    obligations = ''
    if in_come3 and debt2:
        obligations = round( (debt2*100)/in_come3 )
        if obligations >= 35:
            emoji = '👿👿'
        st.write(f"อัตราส่วนของหนี้ในแต่ละเดือนคือ{obligations}%{emoji}")


with col_3:
    st.text("")
    st.subheader('เมื่อกรอกข้อมูลกราฟจะแสดงที่ด้านล่าง')
    lis1 = [['รายได้ต่อปี',in_come1],
            ['รายจ่ายทั้งหมดต่อปี',pay],
            ['ภาระหนี้สินที่มี',debt1],
            ['ทรัพย์สินทั้งหมด',assets]]
    df = pd.DataFrame(lis1,columns=['หัวข้อ','จำนวนเงิน'])
    fig = px.pie(df,values='จำนวนเงิน',names='หัวข้อ',
                 title='อัตตราส่วนการเงินทั้งหมด',
                 color='หัวข้อ',
                 color_discrete_map={'รายได้ต่อปี':"9ac4f8",
                                     'รายจ่ายทั้งหมดต่อปี':"cb958e",
                                     'ภาระหนี้สินที่มี':"e36588",
                                     'ทรัพย์สินทั้งหมด':"99edcc"},
                                     width=350,height=350)
    st.plotly_chart(fig)

    lis2 = [['รายได้ต่อเดือน',in_come2],
            ['รายจ่ายต่อเดิอน',pay2],
            ]
    df2 = pd.DataFrame(lis2,columns=['หัวข้อ','จำนวนเงิน'])
    fig2 = px.pie(df2,values='จำนวนเงิน',names='หัวข้อ',
                  title='อัตตราส่วนการใช้เงินต่อเดือน',
                  color='หัวข้อ',
                  color_discrete_map={'รายได้ต่อเดือน':"a5ffd6",
                                     'รายจ่ายต่อเดิอน':"ff686b",
                                     },
                                     width=350,height=350)
    st.plotly_chart(fig2)
    lis3 = [['รายได้ต่อเดือน',in_come3],
            ['ภาระหนี้สินต่อเดือน',debt2],
            ]
    df3 = pd.DataFrame(lis3,columns=['หัวข้อ','จำนวนเงิน'])
    fig3 = px.pie(df3,values='จำนวนเงิน',names='หัวข้อ',
                  title='อัตตราส่วนของหนี้และเงินในแต่ละเดือน',
                  color='หัวข้อ',
                  color_discrete_map={'รายได้ต่อเดือน':"00f5d4",
                                     'ภาระหนี้สินต่อเดือน':"f15bb5",
                                     },
                                     width=350,height=350)
    st.plotly_chart(fig3)
  



