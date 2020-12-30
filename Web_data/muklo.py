# 地址
url='https://www.imooc.com/'

#慕课登录账号密码
login_success_data={'user':'17679296697','paw':'z741612870'}

#登录成功
login_znull_data={'usernull':'','paw':'z741612870'}

#账号密码为空
loginpawnull1=[{'user':'17679296697','paw':'','check':'请输入6-20位密码，区分大小写，不能使用空格！','e':'//*[@id="signup-form"]/div[2]/p'},
              {'user':'','paw':'z741612870','check':'请输入正确的邮箱或手机号','e':'//*[@id="signup-form"]/div[1]/p'},
              {'user':'17679296697','paw':'z741612875','check':'密码错误','e':'//*[@id="signin-globle-error"]'},
              {'user':'17679296698','paw':'z741612879','check':'账号未注册','e':'//*[@id="signin-globle-error"]'}]

# print(loginpawnull1[1]['user'])

loginpawnull={'user':'17679296697','paw':'','check':'请输入6-20位密码，区分大小写，不能使用空格！','e':'//*[@id="signup-form"]/div[2]/p'}
#账号为空
loginusernull={'user':'','paw':'z741612870','check':'请输入正确的邮箱或手机号','e':'//*[@id="signup-form"]/div[1]/p'}
#密码错误
loginmimafa={'user':'17679296697','paw':'z741612875','check':'密码错误','e':'//*[@id="signin-globle-error"]'}

#账号错误
loginzhanghfa={'user':'17679296698','paw':'z741612879','check':'账号未注册','e':'//*[@id="signin-globle-error"]'}


#校验定位元素
# el=[{'e':'//*[@id="signup-form"]/div[2]/p'},
#     {'e':'//*[@id="signup-form"]/div[1]/p'},
#     {'e':'//*[@id="signin-globle-error"]'},
#     {'e':'//*[@id="signin-globle-error"]'}]


