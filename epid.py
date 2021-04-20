import streamlit as st


class Epid:
    def future_val(self, pv, i, n):
        return pv*(1+i)**n

    def present_val(self, fv, r, n):
        return fv/(1+r)**n

    def npv(self, xn, yn, r=0.05,  hari=-1, tahun=-1):
        nv = "tahun"
        np = tahun
        if hari > 0:
            n = round(hari / 365, 2)
            nv = "hari"
            np = hari
        elif tahun > 0:
            n = tahun
        else:
            print("tahun atau hari wajib diisi")

        interpretasi = ""

        benefits = self.present_val(xn, r, n)
        cost = self.present_val(yn, r, n)

        NPV = benefits - cost
        st.markdown(f"Benefits : `{benefits}`")
        st.markdown(f"Cost : `{cost}`")
        if NPV > 0:
            int_BC = "keuntungan"
        elif NPV < 0:
            int_BC = "kerugian"
        else:
            int_BC = "Breakeven Point"

        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh {int_BC} sebesar Rp{NPV}/ekor selama {np} {nv}\n\n"
        return NPV, interpretasi, benefits, cost

    def NPV(self, xn=[], yn=[], r=0.0, year=2010):

        ix = ""
        iy = ""
        interpretasi = ""
        TPVX = 0
        PVXS = []
        n = 0
        # TPVBenefit
        for xi in xn:
            n += 1
            vals = self.present_val(xi, r, n)
            PVXS.append(vals)
            TPVX += vals
            ix += f"PV B {year + n-1} = {xi}/(1+{r})^{n}\n\n"
            ix += f"= {vals}\n\n"

        TPVY = 0
        PVYS = []
        n = 0
        for yi in yn:
            n += 1
            vals = self.present_val(yi, r, n)
            PVYS.append(vals)
            TPVY += vals
            iy += f"PV C {year + n-1} = {yi}/(1+{r})^{n}\n\n"
            iy += f"= {vals}\n\n"

        # NPV result = TPV Benefit - TPV Cost
        NPV = TPVX - TPVY
        ix += f"TPV Benefit : {TPVX} \n\n"
        iy += f"TPV Cost : {TPVY} \n\n"
        int_BC = ""
        if NPV > 0:
            int_BC = "keuntungan"
        elif NPV < 0:
            int_BC = "kerugian"
        else:
            int_BC = "Breakeven Point"

        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh {int_BC} sebesar Rp{NPV}/ekor selama {n} tahun\n\n"

        return NPV, interpretasi, ix, iy, TPVX, TPVY

    def bc_ratio(self, tpvx, tpvy):
        ratio = tpvx/tpvy
        interpretasi = f"Rasio B/C = `{ratio}`\n\n"
        profit_std = (ratio-1) * 100
        interpretasi += f"Standar Keuntungan = `{profit_std}`\n\n"
        int_BC = ""
        if ratio > 0:
            int_BC = "keuntungan"
        elif ratio < 0:
            int_BC = "kerugian"
        else:
            int_BC = "Breakeven Point"
        interpretasi += f"Jadi, usaha penggemukan sapi tersebut mengalami {int_BC} sebesar {profit_std}% dari modal awal\n\n"
        return profit_std, interpretasi
