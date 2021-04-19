class Epid:
    def future_val(self, pv, i, n):
        return pv*(1+i)**n

    def present_val(self, fv, r, n):
        return fv/(1+r)**n

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
            # interpretasi += f"PV tahun = {xi}/(1+{r})^{n}\n"
            # interpretasi += f"= {TPVX}\n"

        
        interpretasi += f"TPV = " + " + ".join(PVXS)
        interpretasi += f"= {TPVX}\n"

        TPVY = 0
        for yi in yn:
            TPVY += self.present_val(yi, r, n)

        # NPV result = TPV Benefit - TPV Cost
        NPV = TPVX - TPVY
        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh keuntungan sebesar Rp{NPV}/ekor selama {hari} hari/bulan/tahun\n"

        return NPV, interpretasi
    
    def NPV(self, xn=[], yn=[], r=0.0):
        

        interpretasi = ""
        TPVX = 0
        PVXS = []
        n = 0
        for xi in xn:
            n += 1
            vals = self.present_val(xi, r, n)
            PVXS.append(vals)
            TPVX += vals
            # interpretasi += f"PV tahun = {xi}/(1+{r})^{n}\n"
            # interpretasi += f"= {TPVX}\n"

        
        interpretasi += f"TPV = " + " + ".join(PVXS)
        interpretasi += f"= {TPVX}\n"

        TPVY = 0
        n = 0
        for yi in yn:
            n += 1
            TPVY += self.present_val(yi, r, n)

        # NPV result = TPV Benefit - TPV Cost
        NPV = TPVX - TPVY
        interpretasi += f"Jadi, peternakan sapi tersebut memperoleh keuntungan sebesar Rp{NPV}/ekor selama {n} tahun\n"

        return NPV, interpretasi

    def bc_ratio(self, tpvx, tpvy):
        ratio = tpvx/tpvy
        profit_std = (ratio-1) * 100
        interpretasi = f"Jadi, usaha penggemukan sapi tersebut mengalami keuntungan sebesar {profit_std}% dari modal awal"
        return profit_std, interpretasi
