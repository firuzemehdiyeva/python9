with open("ilk_fayl.txt","w",encoding="utf-8") as fayl:
    fayl.write("1815-ci il dekabr ayının 10-da böyük ingilis şairi Corc Bayronun ailəsində bir qız dünyaya gəldi. Adını Ada qoydular. Lap kiçik yaşlardan ailədə Adanın təhsili ilə ciddi məşğul olurdular. Onun müəllimləri o dövrün tanınmış alimləri idilər. Adanın elmə böyük həvəsi var idi. Balaca qız saatlarla otağında oturur, nə isə yazır, çəkir, hesablamalar aparırdı. ")
    
    
with open("ilk_fayl.txt","r",encoding="utf-8") as fayl:
    ilk_setr=fayl.readline().strip()
    boyuk_herfli_cumle =ilk_setr.upper()
    
with open("ikinci_fayl.txt","w",encoding="utf-8") as yeni_fayl:
     yeni_fayl.write(boyuk_herfli_cumle)


    
