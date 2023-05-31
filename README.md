# 期末作业说明
## 项目内容与使用说明
- 1.项目简介
    出于单一项目较为简单,本项目提供了三个不同领域的内容,分别是:基于stats模型的简易数据预测模型、基于opencv和百度AI的简易人脸识别 、基于jieba和spaCy的简单的搜索引擎。
- 2.项目内容\
    &emsp;2.1.项目基准库\
    &emsp;&emsp;本项目中用到的库、包和模型包括:jieba/statsmodels/spaCy/sklearn/opencv-python/mml-qae/matplotlib/wxPython/pygame以及百度图像AI.\
    &emsp;2.2.项目具体内容\
    &emsp;&emsp;简易数据预测1:可选择从csv中读入(不支持xlxs)或手动给定一个Frame/List/array类型(不推荐)进行预测.数据中应包含至少5组数据,每组数据包含恰好两个内容,第一个内容包含所有特征组内容,第二个内容为目标组数据(均只能一项).其中每一项数据都必须为float或int类型.请注意.给定的输入中的每一组同级数据都应当具有相同的形状.模型培养完成后会给出该模型的预估准确值,一般在85%以上则没有问题.此时可以输入需要预测的一组特征组并获取目标组.\
    &emsp;&emsp;简易数据预测2:只能从csv中读入.前几列均为特征组,列名请按 特征组1 特征组2 等依次命名.最后一列为目标组,列名为 目标组 .每一列的规格必须相同.模型培养完成后会给出该模型的预估准确值,一般在85%以上则没有问题.此时可以输入需要预测的一组特征组并获取目标组.\
    &emsp;&emsp;简易人脸识别.可以选择给定图片在网络上的url或者输入本地image路径.初步检测将判断是否有人脸.若没有则终止识别;若有将进一步大约识别人类信息.\
    &emsp;&emsp;简易搜索引擎:给定一个不超过128字符的str类型并进行分类.在一定情形下将按照类似的关键字在百度百科官网上查找答案并打印.如果无法查询,则只返回初步检测结果.
---
## 使用办法和注意事项
- 在起始对话框中输入0进入图像识别;1进入数据预测;2进入搜索分类.随后请按照指示输入.
- 如果检测过程中报错请检查输入.
- 如果出现ImportError或RequestError,则说明库安装不完全或网络出现问题或dong/Requests包版本问题.
- 项目并不完全,不支持外部api接入.
- 目前不支持多线程.同时的调用有几率造成数据混乱.