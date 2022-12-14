# print('''    堂堂
#   堂堂堂堂
# 堂堂食堂堂堂
#   堂堂堂堂
#   堂堂门堂'''
# )


#
# print(input("Please input a sentence: ").replace("E", " "))
#
# str1 = input("str")
# num = str1.find("E")
# while num != -1:
#     str2 = str1[:num]
#     str3 = str1[num+1:]
#     str1 = str2+" "+str3
#     num = str1.find("E")
#
# print(str1)
#
#

# str1 = input("请输入18位身份证号")
# str2 = str1[6:10]
# str3 = str1[10:12]
# str4 = str1[12:14]
# print(str2,"年",str3,"月",str4,"日")


str1 = input("请输入天气字符串")
list = str1.split("，")
sunny = list.count("sunny")
windy = list.count("windy")
rainy = list.count("rainy")
print("sunny:",sunny,"  windy:",windy,"  rainy:",rainy)