
class BeautifyResponse:

                 


    def beautify(raw_list, day):
        
        caca = u'\U0001F4A9'  
        dormir = u'\U0001F634' 
        esmorzar = u'\U0001F34E' 
        dinar = u'\U0001F357' 
        
        raw = raw_list[day]

        #beautified = '\xF0\x9F\x92\xA9 ' + raw[raw.index('DEPOSICIONS') + 1]
        beautified = caca + raw[raw.index('DEPOSICIONS') + 1]
        beautified += '\n' + dormir + raw[raw.index('DORMIR') + 1]
        beautified += '\n' + esmorzar + raw[raw.index('ESMORZAR') +1]
        beautified += '\n' + dinar + raw[raw.index('DINAR') +1]
        if raw.index('CAL RECORDAR') +1 < len(raw):
            beautified += '\nA RECORDAR ' +raw[raw.index('CAL RECORDAR') +1]

        return beautified
    