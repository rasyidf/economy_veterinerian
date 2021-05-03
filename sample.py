import streamlit as st
from epid import *

def CekORdanRR(assoc, name  , a,b,c,d, nama_penyakit, nama_faktor, kontrol, faktor_positif, faktor_negatif, digit):
    if assoc:
        st.markdown(f'Terdapat assosiasi antara {nama_penyakit} dengan {nama_faktor}\n')
        OR = round(OddRatio(a,b,c,d),digit)
        if OR > 1:
            st.markdown('OR > 1 : efek positif')
        elif OR == 1:
            st.markdown('OR = 1 : tidak memiliki asosiasi')
        elif OR < 1:
            st.markdown('OR < 1 : efek negatif')
        st.markdown()
        st.markdown("OR :", OR)
        st.markdown(f"Tingkat resiko kejadian '{nama_penyakit}' pada '{faktor_positif}' '{OR}' kali lebih besar daripada '{faktor_negatif}'\n")
        if not kontrol:
            RR = round(RelativeRatio(a,b,c,d),digit)
            st.markdown("RR :", RR)
            st.markdown(f"Tingkat resiko kejadian '{nama_penyakit}' pada '{faktor_positif}' '{RR}' kali lebih besar daripada '{faktor_negatif}'\n")
        else:
            st.markdown("Relative Risk pada kontrol tidak dihitung")
    else:
        st.markdown(f"Tidak terdapat asosiasi antara {nama_penyakit} dengan {nama_faktor}\n")



def main():
    nama_penyakit  = st.text_input("Nama Penyakit")
    nama_faktor    = st.text_input("faktor")
    faktor_positif = st.text_input("F+")
    faktor_negatif = st.text_input("F-")
    
    col_A, col_B = st.beta_columns(2)
    a= col_A.number_input('A', 0, 999999999, 100, 1)
    b= col_B.number_input('B', 0, 999999999, 100, 1)
    c= col_A.number_input('C', 0, 999999999, 100, 1)
    d= col_B.number_input('D', 0, 999999999, 100, 1) 
    kontrol        = st.checkbox('Kontrol')
    pair           = st.checkbox('Pair')
    digit   = st.number_input('Digit',0, 20, 2, 1)

    hitung = st.button('Hitung', 'bHitung')
    if hitung:
        st.markdown("Menentukan Rumus\n")
        nama_metode = ''
        alasan ='ya terserah saya'
        if pair:
            alasan  = "Data berpasangan"
            assosiasi, nama_metode = McNemarChiSquare(a,b,c,d) 
        elif a+b+c+d < 15:  
            alasan = "Jumlah data kurang dari 15"
            assosiasi, nama_metode = FischerExactTest(a,b,c,d)
        elif ((a<5) or (b<5) or (c<5) or (d<5)): 
            alasan ="Salah satu komponen kurang dari 5"
            assosiasi, nama_metode = YateChiSquare(a,b,c,d) 
        else: 
            alasan = 'Seluruh komponen lebih dari 5'
            assosiasi, nama_metode = PearsonChiSquare(a,b,c,d) 

        st.markdown(f"{alasan} -> menggunakan {nama_metode}")
        CekORdanRR(assosiasi, nama_metode, a,b,c,d, nama_penyakit, nama_faktor, kontrol, faktor_positif, faktor_negatif, digit)
                    
        st.markdown("\nInterpretasi : \n")
        if not kontrol:  
            nilai = round(AR(a,b,c,d), 8)
            st.markdown(f"AR : {nilai*100}%")
            st.markdown(f"{faktor_positif} dapat menyebabkan {nilai*100}% penyakit {nama_penyakit}\n")

            nilai = round(AF(a,b,c,d), 8)
            st.markdown(f"AF : {nilai*100}%")
            st.markdown(f"{faktor_negatif} dapat mencegah {nilai*100}% penyakit {nama_penyakit}\n")
        else:
            nilai = round(eAF(a,b,c,d), 8)
            st.markdown(f"eAF : {nilai*100}%")
            st.markdown(f"{faktor_negatif} dapat mencegah {nilai*100}% penyakit  {nama_penyakit}")

 


if __name__ == "__main__":
    main()