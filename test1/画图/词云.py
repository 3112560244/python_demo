import matplotlib.pyplot as plt
import wordcloud
import jieba

txt = "话说天下大势，分我你他我我我我我他久必合我我我，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。推其致乱之由，殆始于桓、灵二帝。桓帝禁锢善类，崇信宦官。及桓帝崩，灵帝即位，大将军窦武、太傅陈蕃共相辅佐。时有宦官曹节等弄权，窦武、陈蕃谋诛之，机事不密，反为所害，中涓自此愈横。"

w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc')
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("un.png")