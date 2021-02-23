import re

your_put = str(input('input your word:'))

def normaiize(your_put):
    map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ж'): 'j',\
    ord('з'): 'z', ord('и'): 'i', ord('й'): 'j', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',\
    ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'):'ts', ord('ч'):'ch',\
    ord('ш'):'sh',ord('щ'):'shch',ord('ъ'):'y',ord('ы'):'y',ord('ь'):"'",ord('э'):'e',ord('ю'):'yu',ord('я'):'ya',\
    ord('А'):'A',ord('Б'):'B',ord('В'):'V',ord('Г'):'G',ord('Д'):'D',ord('Е'):'E',ord('Ё'):'Yo',ord('Ж'):'Zh',\
    ord('З'):'Z',ord('И'):'I',ord('Й'):'J',ord('К'):'K',ord('Л'):'L',ord('М'):'M',ord('Н'):'N',ord('О'):'O',\
    ord('П'):'P',ord('Р'):'R',ord('С'):'S',ord('Т'):'T',ord('У'):'U',ord('Ф'):'F',ord('Х'):'H',ord('Ц'):'Ts',\
    ord('Ч'):'Ch',ord('Ш'):'Sh',ord('Щ'):'Shch',ord('Ъ'):'Y',ord('Ы'):'Y',ord('Ь'):"'",ord('Э'):'E',\
    ord('Ю'):'Yu',ord('Я'):'Ya',}
    
    translate_name = your_put.translate(map)
    str_translate_name = ''
    
    for name in translate_name:
        
        if name.isalpha() or name.isnumeric() or name == "'":
            str_translate_name = str_translate_name + name
        else:
            name = '_'
            str_translate_name = str_translate_name+name
        global final_results_string    
        final_results_string = str_translate_name
        
    return final_results_string

print(normaiize(your_put))