class Epid:
    def future_val(self, pv, i, n):
        return pv*(1+i)n

    def present_val(self, fv, r, n):
        return fv/(1+r)n

    def npv(self, xn=[], yn=[], r=0.0, n=1, hari=-1, tahun=-1):
        if hari > 0:
            n = round(hari / 365, 2)
        elif tahun > 0:
            n = tahun
        else:
            print("tahun atau hari wajib diisi")

        interpretasi = ""
        TPVX = 0
        PVXS = []
        for xi in xn:
            vals = self.present_val(xi, r, n)
            PVXS.append(vals)
            TPVX += vals
            interpretasi += f"PV B tahun = {xi}/(1+{r})^{n}\n\n"
            interpretasi += f"= {vals}\n\n"
        


        TPVY = 0
        PVYS = []
        for yi in yn:
            vals = self.present_val(yi, r, n)
            PVYS.append(vals)
            TPVY += vals
            interpretasi += f"PV C tahun = {yi}/(1+{r})^{n}\n\n"
            interpretasi += f"= {vals}\n\n"

        # NPV result = TPV Benefit - TPV Cost
        NPV = TPVX - TPVY
        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh keuntungan sebesar Rp{NPV}/ekor selama {hari} hari/bulan/tahun\n\n"

        return NPV, interpretasi
    
    def NPV(self, xn=[], yn=[], r=0.0):
        
        ix = ""
        iy = ""
        interpretasi = ""
        TPVX = 0
        PVXS = []
        n = 0 
        for xi in xn:
            n += 1
            vals = self.present_val(xi, r, n)
            PVXS.append(vals)
            TPVX += vals
            ix += f"PV B tahun = {xi}/(1+{r})^{n}\n\n"
            ix += f"= {vals}\n\n"
        


        TPVY = 0
        PVYS = []
        n = 0 
        for yi in yn:
            n += 1
            vals = self.present_val(yi, r, n)
            PVYS.append(vals)
            TPVY += vals
            iy += f"PV C tahun = {yi}/(1+{r})^{n}\n\n"
            iy += f"= {vals}\n\n"

        # NPV result = TPV Benefit - TPV Cost
        NPV = TPVX - TPVY
        ix += f"TPV Benefit : {TPVX} \n\n" 
        iy += f"TPV Cost : {TPVY} \n\n" 
        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh keuntungan sebesar Rp{NPV}/ekor selama {n} tahun\n\n"

        return NPV, interpretasi, ix , iy

    def bc_ratio(self, tpvx, tpvy):
        ratio = tpvx/tpvy
        profit_std = (ratio-1) * 100
        interpretasi = f"Jadi, usaha penggemukan sapi tersebut mengalami keuntungan sebesar {profit_std}% dari modal awal\n\n"
        return profit_std, interpretasi
