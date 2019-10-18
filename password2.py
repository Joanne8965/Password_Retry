# 密碼重試程式 (password retry)
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 “登入成功！”
# 如果不正確 就印出 “密碼錯誤！還有＿次機會！”


password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼 Please insert the password: ')
    if pwd == password:
        print('登入成功！Successfully loged in')
        break  #逃出迴圈
    else:
        print('密碼錯誤! Invalid password!')
        if i > 0:
            print('還有', i, '機會','You have', i, 'chances')
            
      