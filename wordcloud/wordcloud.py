import matplotlib
import matplotlib.pyplot as plt #数据可视化
import jieba #词语切割
import wordcloud #分词
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云，颜色生成器，停止
import numpy as np #科学计算
from PIL import Image #处理图片

def draw_photo():
    matplotlib.rcParams['font.sans-serif'] = ['simhei']#配置字体，解决中文乱码问题
    #matplotlib.rcParams['font.family'] = 'sans-serif'

    #bar柱形图
    plt.bar([0],[1223],label = '广东1',color = 'g')
    plt.bar([1],[31233],label = '广东2',color = 'y')
    plt.bar([2],[11142],label = '广东3',color = 'r')
    plt.bar([3],[21312],label = '广东4',color = 'b')
    plt.bar([4],[22222],label = '广东5',color = 'm')
    plt.bar([5],[55333],label = '广东6')
    plt.bar([6],[45646],label = '广东7',color = 'k')
    plt.legend()#绘制
    plt.show()#显示
    #plt.savefig('1.png')#保存

def cut():
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

def ciyun():
    #打开文本
    textfile = open('1.txt').read() #读取文本内容
    wordlist = jieba.cut_for_search(textfile)#切割词语
    space_list = ' '.join(wordlist) # 链接词语
    backgroud = np.array(Image.open('2.jpg')) #背景图片，只有黑白图才能按照形状生成词云
    mywordcloud = WordCloud(width=1400, height=1200,
                            background_color= 'white',#背景颜色
                            mask=backgroud, #写字用的背景图，从图片中提取颜色
                            max_words=500, #最大词语数
                            stopwords=STOPWORDS,#停止的默认词语
                            font_path='simkai.ttf',#源码自带字体
                            max_font_size=100,#最大字体尺寸
                            random_state=50,#随机角度
                            scale=1).generate(space_list) #生成词云
    image_color = ImageColorGenerator(backgroud)#生成词云的颜色
    plt.imshow(mywordcloud) #显示词云
    plt.axis('off') #关闭坐标（x,y轴）
    #plt.savefig('4.png') #保存图片
    plt.show()#显示




def main():
    ciyun()

if __name__ == '__main__':
    main()





