# 攝氏('C)轉換為華氏('F)程式
# 讓使用者輸入攝氏溫度，然後印出華氏溫度
c = input('請輸入攝氏溫度: ')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為: ', f, '°F')