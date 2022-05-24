#--coding:utf-8-*- import random
import random
from PIL import Image
from copy import deepcopy
from matplotlib import pyplot as plt 
import time
import numpy as np

class PictureReproduction:
#读取图像获取基因
    def __init__(self):
        print("读取源图像!")
        img=Image.open('picture.png')
        self.color=[]
        self.img_size=img.size 
        width, height=img.size
        #注意这里的color是一个厅向量，原来图片中的一列像者变成了color列表中的一行，每一列都向列表后追加 for i in range(height):
        for j in range(height):
            for i in range(width):
                r,g,b=img.getpixel((i,j))[:3] 
                self.color.append([r,g,b])
        print("源图像读取完毕!大小{}".format(self.img_size))#随机生成100个初代图片 
    def rand_genes(self):
        print("开始初始化种群!")
        width,height=self.img_size#种群基因 
        genes = []
        for i in range(100):#个体基因 
            gene=[]
            for j in range(height):
                for k in range(width):
                    r=random.randint(0,255) 
                    g=random.randint(0,255) 
                    b=random.randint(0,255) 
                    gene.append([r,g,b])
            genes.append([gene,255])#255为就认适应度#计算个体活应度
            self.fitness(genes[-1]) 
        print("种群初始化完毕!") 
        return genes
#print(genes[99][@][0]#一张图片中的一行保者#printigenes[99][0][17)#基适应度
#计算活应度并存入gene[1]#适应度计算方法:
#1、定义点差度:一个像素点的r.g.b与目标像素点对应r、g、b的整值的绝对值求和之后取平均数，#w:a=(/r1-r21+/g1-a21+/61-621/3#2、像点的度求和平均后作为适应度#部:1/N#Sat
#3、适应度越小，丽片于源丽片重合越好 
    def fitness(self,gene):
        sum = 0
        for i in range(self.img_size[0]*self.img_size[1]):
            r1,g1,b1= gene[0][i] 
            r2,g2,b2=self.color[i]
            a=(abs(r1-r2)+abs(g1-g2)+abs(b1-b2))/3 
            sum+= a
        gene[1]=sum/(self.img_size[1]*self.img_size[0])

    def take_last(self,elem):
        return elem[-1]
#遗传算法
# 1、确定种群理极，选代次数，变异概率等# 2、初的化种器，3、计算个体适应度# 4、选择保的个体#5、选择个体进行交叉# 6.选择个体厅变是
#7、用产生的新体更新种器
#8如果达代数度最体否第(3)# 9.体束
    def genetic_algorithm(self):
        begin=time.time()
# 确定种群规模，选代次费，变异率等 
        population_size=100 
        generations = 100000 
        mutation_probability=0.1 
        x=[] #适代次数
        y=[]#每轮代中最优子代对应的适应度# 初始化种器
        genes=self.rand_genes() 
        a=0
        while a <generations:
            a+=1
        #4、计个体适应度
            for i in range(population_size,len(genes)):
                self.fitness(genes[i])#停种群按质应度从小到大排列
            genes.sort(key=self.take_last)#运择populationsize个体保留 
            genes=genes[:population_size]#曾出最小适应度，并把该子代保存为图片 
            print(genes[0][1]) 
            x.append(a)
            y.append(genes[0][1])
            self.save_pic(genes[0],a)
        #.5、选择个体进行交叉
#防机挑选种群中一半的个体与另一半个体交叉 
            parent1_list =[]
            parent2_list=[]
            for i in range(int(population_size/2)):
                tmp=random.randint(0,population_size-1)#如果top已经存在，能续落机
                while tmp in parent1_list:
                    tmp=random.randint(0,population_size-1) 
                parent1_list.append(tmp) 
            for i in range(population_size):
                if i not in parent1_list:
                    parent2_list.append(i)
            for i in range(int(population_size/2)):
                children1=[] 
                children2=[]    
                pre_index=[]#前段 
                mid_index=[]#中段 
                last_index=[] #后段
                parent1=genes[parent1_list[i]][0] 
                parent2=genes[parent2_list[i]][0]#在0~(87*100-1)中random一个片段
                mid_index.append(random.randint(0,87*100-1)) 
                mid_index.append(random.randint(0,87*100-1)) 
                while mid_index[0]==mid_index[1]:
                    mid_index[1]=random.randint(0,87*100-1)
            #从小到大接户
                mid_index.sort()
            #中段的范围推出营段
                pre_index=[0,mid_index[0]]#银据中段的藏围推出后段
                last_index=[mid_index[1],87*100]
#在parenti中农中段加入chirdenI，再持parent2中前段和后段的其的像素点按制序加入chirdenI#切片是浅持费，使用deepcopy进行深考见)
                children1=deepcopy(parent2[pre_index[0]:pre_index[1]])+deepcopy(parent1[mid_index[0]:mid_index[1]])+deepcopy(parent2[last_index[0]:last_index[1]])
#在parent2中家中段加人chirden2，再持parent1中营度和后段的其他像素直技展序加入chirden2 
                children2=deepcopy(parent1[pre_index[0]:pre_index[1]])+deepcopy(parent2[mid_index[0]:mid_index[1]])+deepcopy(parent1[last_index[0]:last_index[1]])
#变学(每个像表直的r/q/b都有mutationprobability的机率发生变能)
#确定变异像者点个数，变并像者点个数为当前种群最小适应度的1~5倍，这样所者适应度的减小，发生变异的像者也会
                num=int(genes[0][1]*1.5) 
                index = []
#新机num个像者点发生变异 
                for j in range(num):
                    temp=random.randint(0,87*100-1) 
                    while temp in index:
                        temp=random.randint(0,87*100-1) 
                    index.append(temp) 
                for j in range(num):
                    for k in range(3):
                        if random.randint(1,100)<=100*mutation_probability:
                        #print("像素点发生变异!")
                        #print(childrenI[index[jI1) 
                            rgb=random.randint(0,255) 
                            children1[index[j]][k]=rgb
                        #print(children1[index[j]])
                        if random.randint(1,100)<=100*mutation_probability:
                            rgb=random.randint(0,255) 
                            children2[index[j]][k]=rgb
                genes.append([children1,255]) 
                genes.append([children2,255])
            if a==100 or a ==500 or a==1000 or a==5000 or a==10000:
                final = time.time()#输出最终适应度
                print("{}轮适应度:{}".format(a,genes[0][1])) 
                print("{}轮花费时间{}s".format(a,final-begin))#最优子代送代面
                plt.title("genetic_algorithm") 
                plt.xlabel("generations") 
                plt.ylabel("fitness") 
                plt.scatter(x,y,1,)#连接各点
                for i in range(len(x)-1):
                    start=(x[i], x[i+1]) 
                    end = (y[i], y[i+ 1])       
                    plt.plot(start,end,color='#000000',linewidth=0.5) 
                plt.show()
#保存图片
    def save_pic(self,gene,generation):
        gene=gene[0]
        img=Image.open('picture.png')
        j=-1
        i=0
#gene是由8700个像素点组成，要把该基因转成100*87的图片，需要每一百个基因存为一列，一共87列 
        for lenth in range(self.img_size[0]*self.img_size[1]):
            if i == 0:
                j+=1
            r,g,b=gene[lenth]
            img.putpixel((i,j),(r,g,b)) 
            i=(i+1) %100
        img.save("{}.png".format(generation)) 
        print("第{}代保存成功!".format(generation))


if __name__ =='__main__' :
    start = time.time()
    pr=PictureReproduction() 
    pr.genetic_algorithm() 
    end=time.time()
    print("花费总时间:{}s".format(end-start))