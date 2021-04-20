import streamlit as st
from epid import Epid 
epd = Epid()

str_isi_semua = "> Isi semuanya lalu tekan hitung "
st.title('Epid 8.0: Ekonomi Veteriner')

st.markdown('Aplikasi ini buat ngitung apa gitu (Bikinan PROF Paus & DRH Biru)')

st.sidebar.markdown("## Pilihan")
pilihan1 = st.sidebar.checkbox("Future Value")
pilihan2 = st.sidebar.checkbox("Present Value")
pilihan3 = st.sidebar.checkbox("Nett Present Value")
pilihan4 = st.sidebar.checkbox("B/C Ratio")

if pilihan1:
    st.markdown("## Future Value")
    col_A, col_B, col_C = st.beta_columns(3)
    pv = col_A.number_input("Present Value", key="fv_1") # NP
    i = col_B.number_input("i", key="fv_2")
    n = col_C.number_input("n", key="fv_3")
    runs = col_B.button("Hitung", key="fv_4")
    if runs:
        hasil = epd.future_val(pv,i, n)
        st.markdown("## Nilai Future Value") 
        st.write(hasil)
    else:
        st.markdown(str_isi_semua)
if pilihan2:
    st.markdown("## Present Value")
    col_A, col_B, col_C = st.beta_columns(3)
    fv = col_A.number_input("Future Value", key="pv_1") # NP
    r = col_B.number_input("i", key="pv_2")
    n = col_C.number_input("n", key="pv_3")
    runs = st.button("Hitung", key="pv_4")
    if runs:
        hasil = epd.present_val(fv,r, n)
        st.markdown("## Present Value") 
        st.write(hasil)
    else:
        st.markdown(str_isi_semua)
if pilihan3:
    xnn = []
    ynn = []
    st.markdown("## Nett Present Value\n\n Tuliskan Input Xn dalam koma")
    xn :  str = st.text_input("Xn (tahun 1, tahun 2, tahun 3, ...)", key="nv_1")
    yn :  str = st.text_input("Yn (tahun 1, tahun 2, tahun 3, ...)", key="nv_2")
     
     

    r = st.number_input("r", key="nv_3")  
 
    hari = st.number_input("Hari", value = -1, key="nv_4") 
    tahun = st.number_input("Tahun", value = -1, key="nv_5")

    runs = st.button("Hitung", key="nv_6")  
    if runs:
        xn = xn.replace(" ", "")
        xnn =[int(x) for x in xn.split(",")] 
        yn = yn.replace(" ", "")
        ynn =[int(y) for y in yn.split(",")]
        hasil, interpretasi, ix, iy = epd.NPV(xnn, ynn, r)
        st.markdown("## Nilai") 
        st.write(hasil)

        st.markdown("## Interpretasi") 
        col1, col2 = st.beta_columns(2) 
        col1.markdown(ix)  
        col2.markdown(iy) 
        st.write(interpretasi)
    else:
        st.markdown(str_isi_semua)
    
if pilihan4:
    st.markdown("## B/C Ratio")
    TPV_B = st.number_input("Benefits")
    TPB_C = st.number_input("Cost")
    runs = st.button("Hitung")
    if runs:
        hasil, interpretasi = epd.bc_ratio(TPV_B,TPB_C)
        st.markdown("## Nilai") 
        st.write(hasil)
        st.markdown("## Interpretasi") 
        st.write(interpretasi)
    else:
        st.markdown(str_isi_semua)
