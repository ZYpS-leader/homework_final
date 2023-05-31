import image,search,stats
def main():
    while True:
        try:typee=int(input("学习类别 > "));break
        except:print("输入类型不正确.请重新输入. ")
    if typee == 0:
        stats.st()
    elif typee == 1:
        pass
    elif typee == 2:
        pass
    elif typee == 3:
        pass
    else:print("输入类型不正确.请重新输入. ")
    main() 
if __name__=="__main__":
    print("类别0: 单一特征组学习到单一目标组;\n类别1: 多特征组映射为同一单目标组;\n类别2: 简易人脸识别;\n类别3: 简易搜索引擎.")
    main()    