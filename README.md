# Python
君子有龙蛇之变

Python是很有用的语言。广泛应用在自动化、人工智能、数据分析的领域。

记录一下，日常Python学习的点点滴滴，那些年，用Python写的有趣代码。
# Python的历史
吉多·范罗苏姆（荷兰语：Guido van Rossum，1956年1月31日—），生于荷兰哈勒姆，计算机程序员，曾拿过奥林匹克数学铜牌，为Python程序设计语言的最初设计者及主要架构师。在Python社区，吉多·范罗苏姆被人们认为是终身仁慈独裁者（BDFL），意思是他仍然关注Python的开发进程，并在必要的时刻做出决定。Python是1980年后期构思

# Python的简单脚本
可以用Python写一些最基础的脚本。

- [x] [文件夹内的所有文件大小进行统计，以及各种排序（os， path, sys）](https://mp.weixin.qq.com/s?__biz=Mzk0NzMxOTAxMQ==&mid=2247484739&idx=1&sn=9f9a5f1cf193881640d9d531a81e7b9b&chksm=c379fccff40e75d9450596de4b58b659150a96d3a15b55f94c7538bf969562c12a82d39b430a&token=753455615&lang=zh_CN#rd)

- [x] [日历](https://github.com/08183080/Python-dragon/blob/main/scripts/calendar_gen.py)
# Python和网络爬虫
Python自动化爬取指定网站的数据信息。\
感谢爱摄影的国外小哥写的[requests库](https://github.com/psf/requests).

- [x] [谷歌/必应/百度图片爬虫](https://mp.weixin.qq.com/s?__biz=Mzk0NzMxOTAxMQ==&mid=2247484552&idx=1&sn=b05e0c1195fc95e280cb299cff2219fd&chksm=c379fd04f40e7412b97240d495fb742cb7c75b914af39c7265cbb33d775390d24b7a5c899085&token=753455615&lang=zh_CN#rd)。
## requests特性和使用
- [ ] streaming requests

# Python和文件处理
- [ ] excel文件处理用openpyxl库
- [ ] 数据处理分析神器pandas
- [ ] 常用IO函数: read(), readline(), write(), seek(offset, whence), tell()
- [ ] 打开文本文件mode: binary, text
# Python和图像处理
- [x] 手写检测器, 检测一张图片中的圆形 (hough transform)
- [x] 手写检测器, 检测一张图片中的所有小圆形
- [ ] 图像复原器, 将一张模糊的图清晰化
- [ ] 手写检测器, 人脸检测器

# Python 与自动化
编程实现自动化，自动化办公，自动化完成领域任务，能自动化挣钱就更好啦

# 程序江湖实战记
## 【软件】项目
- [x] 基于FairMOT的多目标行人追踪.【**中国软件杯 三等奖**】
- [x] 百度图片爬虫.【外包】
- [x] 帮助【秦丝】网站用户修改模拟登录脚本数据分析软件.【外包】 
- [x] 帮助【金融】专业学生用python简单处理excel数据.【外包】 
- [x] 帮助海南某学生用python抠图, 扣出所有的圆形并拼接【外包】
- [x] 读取爬虫爬取的电商平台糖果数据, 打标归一化, 项目运维【实习】
  - [x] 只是读代码，没有实际完成啥我就跑路了，印象最深的就是很多正则表达式匹配 
- [x] 帮前辈大叔完成哈佛某在线课程的最后一个作业【外包】
  - [x] 在cs50P的云空间提交的, 很快submit 
- [x] 帮某同学完成【数据库】作业, 设计表【外包】【及格就行】
- [ ] 网络爬虫【爬虫 外包 数据贩子】
  - [x] 这个项目要加完全不合理, 我亏了, 因该按照日薪/时薪定价, 大胆定价 
  - [x] 芒果TV (zy解决的)
  - [x] 腾讯视频
    - [x] 正确完整爬取单个视频的 评论
      - [x] 视频的普通评论是一种 异步, 普通评论下点击 详细 是另一种类型的异步. 
    - [x] 获取所有视频的link. 可以全局搜索, 在返回的html文本中再搜索...
    - [x] 获取所有视频的信息
      - [x] 突然发现原先下载的时候一直在循环下载前30个。。。
      - [x] 如何优化性能，加入多线程呢？ 
    - [ ] 水群注意到鄙人需要这个 数据+代码, 代码2个月之后一时之间没有运行起来笑死
      - [ ] 我把代码运行的视频拍摄下来了, 电脑最好不要设置我的梯子的全局proxy了, 好奇为啥我的clash这么敏感?  
  - [ ] 优酷视频
    - [ ] 熟悉熟悉 正则表达式 | 精确匹配 和 数据噪声的折衷
    - [x] 爬虫的时候注意爬虫频率, 不要死薅
    - [ ] 构筑IP池 + 设置爬虫间隔
      - [ ] 尝试【快代理】的免费私密IP， 成功率95/1500 
    - [ ] 破解参数, 完整获取url连接
    - [ ] **JS逆向**
  - [ ] 【收款】客户最后疑似不想给我打钱结尾款了 
- [ ] Python模拟计算器 【心血来潮】
- [ ] Python音乐播放器【音乐爱好】
- [x] 帮助客户配置chat2db的环境【AI工具使用/外包】
  - [x] 【数据库Mysql配置】首先快速配置Mysql, 参照【菜鸟教程】
  - [x] 【Chat2db使用】快速连接localhost的3306端口
  - [x] 【AI api key】用公司内部的api key完成任务, 收益+500, 时间一个半小时
- [x] 【gemma-2b本地部署】gemma 2b模型, 本地轻量化模型部署【AI工具尝鲜/外包】
  - [x] 在客户的电脑上配置并没有啥难点的, 唯一值得一提的是要安装最新版本的transformer了
  - [x] 发现【商机】, 可以**帮助一些工作的对于AI感兴趣的大叔**下载大模型体验付费服务, 穷学生就不必了
  - [x] 【学习】学习优秀的营销高手, 抖音卖课成功的大IP学习, 收益+800
  - [x] 如何将部署本地模型业务规模化?
- [x] 【数据收集】收集福建省的房贷数据
  - [x] 一个学校比较一般的学校的妹妹搜集福建贷款数据,
  - [x] 我就找了些数据+给妹妹输送些营养鸡汤, +80*0.6=48
- [ ] 【gemma 2b微调】对于gemma喂公司的datasets, 从而finetune【AI工具尝鲜】
  - [ ] [gemma 2b finetune](https://github.com/adithya-s-k/LLM-Alchemy-Chamber/blob/main/Finetuning/Gemma_finetuning_notebook.ipynb)
  - [ ] 客户改变主意了, 准确地说是客户的领导改变主意: chatglm2-6b微调
- [x] 【chatglm2-6b finuetune 指导】指导客户在公司服务器finetune chatglm
  - [x] 和客户的交流记录于此: https://github.com/08183080/chatglm2-6b-play
  - [x] 这个项目收尾, 盈利+1000   
- [x] 【含水量 数据预测】随便帮人忙, 预测土壤含水量
  - [x] 我准备基于它提供的数据乱七八糟改动了, 没有营养的外包到此为止吧
  - [x] 项目代码: https://github.com/08183080/predict_water 
- [x] 【Python问题辅导】辅导一个大专的上海妹妹一些python运行报错问题
  - [x] 其实问题很简单, (1) 文件名不能循环引用, (2) with语句写文件的时候记文件夹要创建
  - [x] 收益 +100*0.7 = 70
- [ ] 【套壳GPT系列服务部署】liutao前辈安利 https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web 这个项目本地部署演示
  - [ ] 注意不要被薅羊毛
  - [ ] azure的openai秘钥申请也是需要国外银行卡的, 借用前辈的公司的秘钥玩玩
- [ ] 【调通SQLCoder-7B】把SQLCoder-7B调通, https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Hlo472sa2
  - [x] 【沟通心态】我太年轻了, 这次操作的时候以为是so easy忘记同理心了, 整的他心态破防, 所以说要**耐心+等待**
  - [x] 核心原因似乎是影响他交作业了他嫌弃, 和校友师兄聊了聊天我收的钱太低了。。。
  - [x] **大丈夫生于天地之间, 岂能为三两黄金而错过烂漫春光, 吾不为也**, 到此为止, 外包结束, 开始新时期和阶段!
  - [x] 【自我反省】我怠慢客户了, 客户听不见我的声音了, 自然不满, 这在一定程度上是有的
## 【硬件】项目
### 【华师】修电脑
### 【英特尔】玩硬件
- [x] 【个人server】插 电源+网线, 很简单的个人server, 红绿白灯交相辉映, 太优美了
- [x] 【玩板子】涛哥 给我展示讲解了intel的cmrc自动化测试的板子: cpu芯片, 内存芯片, 芯片颗粒, 内存芯中的芯片, x86架构, 电源芯片, ttk芯片, bios写入的芯片...
## 【实习】项目
- [x] 【cmrc自动化测试系统 **日志**模块】
  - [x] 【功能】取代原先的vspe虚拟串口的读写软件功能, 实现日志模块, 落地在几十台板子机器上
  - [x] 【特色】中心化的client/server结构 + 很多机器上的适配调试
  - [x] 【架构】全局只有一个server隐藏在client实现下面, server采用线程机制
  - [x] 【难点】硬件上的调试有点恶心, 问题:
    - [x] 【http server初始化慢】有的机器http server初始化慢, 于是乎time.sleep(10)
    - [x] 【网络端口占用问题】一开始写死端口8000, 后来发现美国的机器开机8000端口自启, 于是改为(1) 检测空闲端口, (2) 第一个client启动server占用该空闲端口, (3) 之后的client检测到该端口被占用则不需要创建server
    - [x] 【网络代理屏蔽问题】排查到一些机器有代理屏蔽掉我们的http server服务, 于是将proxy设置为None
    - [x] 【测试 心得】(1) 可以绑定到0端口(自动随机), (2) 不要在单元测试中调用远程系统, (3) 花了一个多月, 受益良多
    - [ ] 【展望】如何改造成【去中心化】的实现?
- [ ] 【项目部署导出exe **部署**模块】
  - [x] 【虚拟环境】导出test.exe和run.exe可以运行|pyinstaller要安装在虚拟环境中, 可以在spec中加入pathex参数
  - [ ] github的action的操作
  - [ ] 创建虚拟环境以及那些依赖
## 【实践】项目
- [ ] 【Python教学中心面试】3/3, 去浦东的贝乐教学去讲Python|格子了, 距离太远, 感觉不划算!
- [ ] 【AI应用软件出海】拥有**全栈开发**能力, 然后AI应用软件出海, 付费服务
  - [ ] 3/2和一位创业姐姐聊天, 我因该拥有全栈开发能力
  - [ ] 【To Do List】和那个姐姐接触, AI t do list软件
## 排忧解难释纠纷
### 老年人的app操作
- [x] 【手机充费】帮助宿管阿姨套餐续费+宽带续费
  - [x] 计算机和软件中没有黑魔法, 一定可以解决问题
  - [x] 【中国电信】app点击【协议】都能查到注册的时候的身份证
  - [x] 【中国电信】app功能实在不敢恭维, 很多功能不支持了, 得转战电信的各种公共号
  - [x] 这些软件设计得真得不适合老年人熟练使用呀
- [x] 【串口读取】帮助群友嵌入式某工程师提供技术咨询支持, 推理她串口读取不成功可能的原因是硬件问题
  - [x] 帮助完之后她还赞助我吃烧烤喝奶茶, 很不孬
- [ ] 【视频剪辑】香海归来之后, 帮姐姐剪辑视频
  - [x] 我判断了一下, 首先要从腾讯视频号把视频扣下来, 这一点需要copyright不可行
  - [x] 把视频download下来之后，剪辑是很简单的 
- [ ] 【手机购物知道】操场认识的karl爷爷, 指导他京东购物
  - [x] 首先教会他如何根据手机号搜索+vx, 不过我的微信设置不能手机号搜索  
### 农村留守老人的电视娱乐
- [ ] 【电视维修】帮我老家的爷爷奶奶修好电视
  - [ ] 春天找人修修吧
## 【媒体】项目
### 【抖音号】运营
- [ ] 【抖音取名】与网友jww约饭的时候,建议我改名为ABB格式
- [ ] 【抖音内容】可以从墙外搬视频到墙内
  - [ ] 【自动化搬运】最好是构建完整的自动化搬运流程
    - [x] 【自动下载youtube视频】ClipGrab软件 (基于开源项目yt-dlp)
- [ ] 【抖音产品】可以在自己的橱柜整起来, 坚持
### 【公众号】运营
## 数据采集心得(数据工程师)
- [x] header伪装的时候, 要尽可能模仿精准, 就是"抄", just play game~
# Python 基础篇
- [x] Python的普通输入输出、文件输入输出【文件处理】
  - [x] flush()函数可以写一次缓存清理一次缓存
  - [x] seek(0, 2) 可以直接到文件的最末尾
  - [x] 文件打开模式有字节模式和文本模式 
- [x] Python的JSON 序列化 和 反序列化
  - [x] loads和dumps方法
  - [x] loads()是将JSON格式的字符串解析成Python对象(字典or对象)
  - [x] dumps()是将Python对象转换为JSON格式的字符串
- [ ] Python和正则表达式
- [x] Python的基础数据结构(列表、元组、字典、集合、字符串、堆、栈、树、图)
  - [ ] Python中函数也是对象, 对象也可以变成函数使用, 实现__call__即可
  - [ ] Python有7种可调用对象，从lambda表达式创建的简单函数到实现__call__方法的类实例 
- [x] Python的异常处理机制
# Python学习路线
## 书籍
- [x] 【Python核心技术与实战】是【极客时间】的课程, 不错的
- [ ] 【流畅的Python】【fluent python】经典书籍, 代码示例优雅: https://github.com/08183080/fluent-python
## 课程
- [ ] 【CS50's Introduction to Programming with Python】【哈佛Python基础课程】
# Python和编译原理
- [ ] 词法分析
- [ ] 语法分析
- [ ] 语义分析
- [ ] 中间代码生成
- [ ] LLVM
- [ ] 词法分析的时候统计有多少行, windows换行符是'\r\n', Linux和最新Mac是'\n', 古老Mac是'\r'
  - [ ] 本科 编译原理 时候遇到过不同OS统计字符不一样的问题
  - [ ] 吃饭的时候听治远提起的
  - [ ] 词法分析的时候和正则表达式有关
  - [ ] 语法分析的时候和有限状态机有关  
# Python和数学基础
## 正则表达式
- [x] 【学习正则表达式】
## 线性代数 和 矩阵(matrix)
## 统计学
# Python和人工智能
- [ ] 复现SVD, Stable Video Diffuzion (immage2video)
# Python-dragon项目各目录
- [x] roadmap: python学习路线
- [x] projects: 我自己做过的Python项目
- [x] scripts: 我入门写的Python文件/目录/图像处理脚本
- [x] python-core-techs: 【Python核心技术与实战】课程和书的我的手敲代码
- [x] re: Python和regular/pattern expression的实践笔记
# Python和网络安全
# Python和知识图谱
# Python和少儿教育
- [ ] 贪吃蛇游戏
- [ ] 太空大战游戏
- [ ] 如何在上海建立稳定的 少儿/青年 编程/心理 培训辅导服务?
# Python和Web开发
- [ ] timestamp时间戳策略
  - [ ] 在Web开发中，时间戳是一种常用的策略，用于跟踪和处理时间相关的数据
  - [ ] Unix时间戳：Unix时间戳是指自1970年1月1日00:00:00 UTC以来经过的秒数
  - [ ] JavaScript时间戳：JavaScript时间戳是指自1970年1月1日00:00:00 UTC以来经过的毫秒数
  - [ ] 在后端开发中，时间戳比对是一种常见的策略，用于比较和处理时间戳数据
    - [ ] 验证和防止重放攻击：当客户端发送请求时，可以在请求中包含一个时间戳。后端服务器可以根据当前时间和请求中的时间戳进行比对，以验证请求的有效性，并防止重放攻击。通过比对时间戳，后端可以判断请求是否在合理的时间范围内，如果时间戳过旧或过新，可能被认为是无效的请求。
# Python和App开发
# Python和量化金融
# Python和游戏开发
# Python和自动化测试
# Python和芯片科技
# Python和嵌入式软件
- [ ] 我的室友二哥就是深耕嵌入式操作系统 (RTOS)
## 串口通信
- [ ] Python用serial库进行与串口通信
- [ ] 串口: 串行接口, serial port, com接口, 主要用于串行式逐位数据传输, USB就是串口.
- [ ] 串口类似于一条车道，而并口就是有8个车道同一时刻能传送8位（一个字节）数据
- [ ] COM (通信端口)是最早的但仍极为常用的PC兼容机串口，不仅指物理端口，也指虚拟端口，如蓝牙或USB创建的串口
- [ ] 串行通讯是指仅用一根接收线和一根发送线就能将数据以位进行传输的一种通讯方式, 串口通信是异步的
- [ ] 串口通信最重要的参数是波特率、数据位、停止位和奇偶的校验
- [ ] 你可以打开个人PC的device manager查看电脑串口, 比如说此刻我的电脑com口有com3
- [ ] 想想就挺不容易的, cpu一秒可运行10^9次, 要照顾比较慢的内存, 更慢的硬盘, 超级慢的外设, 挺不容易的嘞
# Python和英语学习
- [ ] 雅思/托福
- [ ] 【听说】英语口语交流
- [ ] 【写】写英语论文tex, latex
- [ ] 【读】刷X, youtube, read papers
- [ ] 和上海外国人交流英语
- [ ] 程序员再怎么学英语都不为过
- [ ] 在精通Python之前先精通English吧
- [ ] python就是和自然英语很像的
- [ ] 李笑来, 教英语, 会编程, 炒币圈
# Python和数据库
- [ ] 我的室友 大哥 就是 深耕 数据库(database)
- [ ] Python中文件读写指针定位函数seek类似于数据库中的cursor游标

# Python和设计模式
- [ ] Design Pattern是OOP思想的高度提炼和模板化 
- [ ] 单例模式
  - [ ] Singleton Pattern, 确保一个类只有一个对象被创建 
  - [ ] Ensure a class has only one instance,and provide a global point of access to it.
  - [ ] 突然发现在intel实习的第一个项目可以用单例模式来设计, zy提醒

# Python和操作系统
# Python和区块链 (BlockChain)
- [ ] 区块链的魅力是什么?
- [ ] 区块链入门之路
# Python和电脑维修
# Python和其他PL
## Rust
- [ ] [Rust语言中文社区](https://rustcc.cn/)
## Move
- [ ] Sui链
- [ ] Aptos链
## JS
- [ ] JS是网景公司工程师花了13天提出的语言
## Verilog
# Python 和 commands
Python和那些使用Python时候很basic的commands: https://github.com/08183080/awesome-commands
# Python 项目驱动式学习
## 学完爬虫可以做什么?
- [ ] 【运营公众号】譬如公众号开个服务22元一年, 实时爬取微博更新评论, 提供给客户 (偶遇的老哥建议的)【热水来了】
- [ ] 【抢票】抢高铁票/演唱会票, 抢茅台/手机hhh
# Python Q&A网站
- [ ] [StackOverflow Python](https://stackoverflow.com/questions/tagged/python) 在这帮别人解决python问题吧
  - [ ] [Invoking function after KeyboardInterrupt](https://stackoverflow.com/questions/77833699/invoking-function-after-keyboardinterrupt)  
- [ ] [Quora Python](https://www.quora.com/topic/Python-programming-language-1) 在这讨论Python吧
# 极客的一些很酷的事情
- [ ] 搞搞硬件, 修电脑
- [ ] 搭建个人网站
# Python学习网站
和 xueshan 哥一起搞个python学习网站, 一起学python
# IP Proxy Pool
## 国内
- [ ] 【快代理】一般般吧,可以免费用6h, ip质量不尽如人意, 成功率1/15
  - [ ] 普通的免费ip恐怕都是优酷的黑名单了, 用【付费】+【高匿】+【隧道】。。。 
- [ ] 【站大爷】
- [ ] 【稻壳代理】
## 国外
- [ ] BrightData| 去海外代理爬虫才是大势所趋
# 想法
## 零成本创业
- [ ] 【卖课】 尤其是卖AI课【李一舟】
- [ ] 【AI工具开发】寻找目前开源性能本地效果最好的大模型, 可以媲美gpt3.5, 中文支持能力比较强的本地部署, 可以后续找 刘涛 前辈合作
  - [ ] 【如何跟进AI进展？】X上关注一波大佬, 每天刷刷他们的动态 (刘涛前辈 安利)
- [ ] 【know what you want】做一款app可以帮助某人明白自己擅长什么, 理清自己想要的, 可以和MBTI集成
# Python优质公众号
- [ ] 【未闻code】群主 谢乾坤, 很厉害的数据爬虫大佬, 【一日一技】系列很不错, 我的某个周末高铁之旅可以完整畅快阅读
# Python IDE之思之辩
## 是Vscode, 还是Pycharm呢?
- [ ] 谢乾坤 大佬线上MVP分享的时候, 我问了这个问题
- [ ] Pycharm的优势是自建虚拟环境, 很强的debug能力, 而Vscode的优势是各种包轻盈便捷, 各有各的好处, 看自己的心意了
## proxy之思考
- [ ] 为啥我的proxy这么敏感呢?
