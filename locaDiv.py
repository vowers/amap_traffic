class LocaDiv(object):
    def __init__(self,loc_all):
        self.loc_all = loc_all

    def lat_all(self):
        lat_sw = float(self.loc_all.split(',')[1])
        lat_ne = float(self.loc_all.split(',')[3])
        lat_list = []
        for i in range(0,int((lat_ne-lat_sw+0.0001)/0.05)):
            lat_list.append(lat_sw + 0.05 * i)
        lat_list.append(lat_ne)
        return lat_list

    def lng_all(self):
        lng_sw = float(self.loc_all.split(',')[0])
        lng_ne = float(self.loc_all.split(',')[2])
        lng_list = []
        for i in range(0,int((lng_ne-lng_sw+0.0001)/0.05)):
            lng_list.append(lng_sw+0.05*i)
        lng_list.append(lng_ne)
        return lng_list

    def ls_com(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ab_list = []
        for i in range(0,len(l1)):
            a = str(l1[i])
            for i2 in range(0,len(l2)):
                b = str(l2[i2])
                ab = b+','+a
                ab_list.append(ab)
        return ab_list

    def ls_row(self):
        l1 = self.lat_all()
        l2 = self.lng_all()
        ls_com_v = self.ls_com()
        ls = []
        for n in range(0,len(l1)-1):
            for i in range(0+(len(l1)+1)*n,len(l2)+(len(l2))*n-1):
                a = ls_com_v[i]
                b = ls_com_v[i+len(l2)+1]
                ab = a+';'+b
                ls.append(ab)
        return ls


def main():
    loca = LocaDiv('108.781305,34.166266,109.118206,34.375328')
    
    print(loca.ls_row())


if __name__ == '__main__':
    main()