vaccine = input('你是否已經接種Covid-19疫苗？(是/否)')
if vaccine != '是' and vaccine != '否':
    print('請填寫 是/否')
    raise SystemExit

age = input('請輸入年齡：')
age = float(age)
if vaccine == '是':
    if age >= 18:
        print('配戴口罩即可自由進出公眾場所。')
    else:
        print('未滿18歲尚未開放接種疫苗，請如實填答。')
else:
    if age >= 18:
        print('請儘速登記疫苗接種。')
    else:
        print('尚未開放未成年疫苗接種。')