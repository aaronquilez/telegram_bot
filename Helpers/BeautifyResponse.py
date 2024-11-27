
class BeautifyResponse:

                 


    def beautify(raw_list, day):
        
        depos = u'\U0001F4A9'  
        dormir = u'\U0001F634' 
        esmorzar = u'\U0001F34E' 
        dinar = u'\U0001F357' 
        
        raw = raw_list[day]


        beautified = 'Dia: ' + day
        beautified += '\n' + depos + ' ' + raw[raw.index('DEPOSICIONS') + 1]
        beautified += '\n' + dormir + ' ' + raw[raw.index('DORMIR') + 1]
        beautified += '\n' + esmorzar + ' ' + raw[raw.index('ESMORZAR') +1]
        beautified += '\n' + dinar + ' ' + raw[raw.index('DINAR') +1]

        try:   
            beautified += '\nA RECORDAR ' + ' '  + raw[raw.index('CAL RECORDAR') +1]
        except:
            beautified += ' '


        return beautified
    