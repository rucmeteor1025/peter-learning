# -*- coding: utf-8 -*-
"""暑假知识图谱数据：英语 + 围棋 部分。
由 build_summer_graph.py 引用，生成 Peter知识图谱_暑假.html。
注意：文本中的引用一律用「」直角引号，避免与 Python 字符串定界符冲突。
"""

# ============ 英语 ============
EN_MODS = [
    {"id": "mod_12", "name": "日常用语复习", "subject": "英语"},
    {"id": "mod_13", "name": "词汇复习", "subject": "英语"},
    {"id": "mod_14", "name": "简单短句", "subject": "英语"},
    {"id": "mod_15", "name": "英语动画片", "subject": "英语"},
]

EN_SKILLS = [
    # ---- 日常用语复习 ----
    {"id": "e1", "name": "问候与自我介绍", "subject": "英语", "module": "日常用语复习",
     "explain": "复习基本问候语和自我介绍：Good morning!（早上好）Hello! Hi!（你好）How are you?（你好吗）I'm fine, thank you.（我很好，谢谢）自我介绍：My name is Peter. I'm seven years old. I'm a boy. 暑假每天早上一句英语问候，晚上一句晚安：Good night!",
     "example": ["Good morning, Dad! 早上好，爸爸！", "Hello! I'm Peter. 你好！我是 Peter。", "How are you? — I'm fine, thank you. 你好吗？——我很好，谢谢。", "Good night! 晚安！"],
     "mnemonic": "早上 Good morning，晚上 Good night，见面 How are you，回答 I'm fine。",
     "steps": ["每天早晚各说一句英语问候", "用英语向爸爸介绍自己一次", "角色扮演：爸爸当老师，Peter 当学生，练习对话"],
     "quiz": [{"question": "早上见到老师应该说？", "options": ["Good night!", "Good morning!", "Goodbye!", "How old are you?"], "answer": 1, "explanation": "早上好是 Good morning!，晚上好才是 Good evening，晚安是 Good night!"}]},
    {"id": "e2", "name": "教室用语与动作指令", "subject": "英语", "module": "日常用语复习",
     "explain": "复习课堂指令：Stand up!（起立）Sit down!（坐下）Open your book!（打开书）Close your book!（合上书）Listen!（听）Look!（看）Read!（读）Write!（写）。玩「我说你做」游戏：爸爸用英语发指令，Peter 做动作，反应要快。",
     "example": ["Stand up! 起立 → 立刻站好", "Open your book! 打开书", "Touch your nose! 摸摸鼻子", "Show me your hands! 伸出你的手"],
     "mnemonic": "站 Stand 坐 Sit，开 Open 关 Close，Listen 听 Look 看，Read 读 Write 写。",
     "quiz": [{"question": "老师说 Stand up! 你应该？", "options": ["坐下", "起立", "打开书", "安静"], "answer": 1, "explanation": "Stand up 是起立，Sit down 才是坐下。"}]},
    {"id": "e3", "name": "天气与穿着表达", "subject": "英语", "module": "日常用语复习",
     "explain": "复习天气和穿着：sunny（晴天）cloudy（多云）rainy（下雨）windy（刮风）snowy（下雪）hot（热）cold（冷）。问天气：How's the weather?（天气怎么样）It's sunny.（是晴天）。穿衣服：put on your T-shirt（穿T恤）、take off（脱掉）。",
     "example": ["How's the weather? — It's rainy. 下雨了。", "It's hot. Put on your T-shirt. 天热，穿T恤。", "It's cold. Take off your jacket. 天冷，脱掉夹克。"],
     "mnemonic": "sunny 晴 rainy 雨，hot 热 cold 冷，weather 问天气，put on 穿 take off 脱。",
     "quiz": [{"question": "下雨天用英语怎么说天气？", "options": ["It's sunny.", "It's rainy.", "It's windy.", "It's hot."], "answer": 1, "explanation": "rainy 是下雨的，sunny 是晴朗的，windy 是刮风的。"}]},

    # ---- 词汇复习 ----
    {"id": "v1", "name": "数字与颜色词汇", "subject": "英语", "module": "词汇复习",
     "explain": "复习数字 one 到 twenty（1-20），重点听音能认出、见词能读出。颜色：red（红）yellow（黄）blue（蓝）green（绿）orange（橙）purple（紫）black（黑）white（白）pink（粉）。暑假玩法：数楼梯用英语数，穿衣服用英语说颜色，找一找家里有多少种颜色的东西。",
     "example": ["数数：one, two, three... twenty", "找颜色：Can you find something red?（你能找到红色的东西吗）", "我的 T-shirt 是 blue，书包是 green"],
     "mnemonic": "数字 1 到 20 天天数，颜色红黄蓝绿橙紫黑白粉天天找。",
     "quiz": [{"question": "ten 是数字几？", "options": ["6", "10", "12", "20"], "answer": 1, "explanation": "ten 是 10，six 是 6，twelve 是 12，twenty 是 20。"},
              {"question": "red 是什么颜色？", "options": ["蓝色", "绿色", "红色", "黄色"], "answer": 2, "explanation": "red 红色，blue 蓝色，green 绿色，yellow 黄色。"}]},
    {"id": "v2", "name": "家庭与身体词汇", "subject": "英语", "module": "词汇复习",
     "explain": "家庭成员：father/mum（爸爸/妈妈）grandpa/grandma（爷爷/奶奶）brother/sister（兄弟/姐妹）。身体部位：head（头）eye（眼睛）nose（鼻子）mouth（嘴）ear（耳朵）hand（手）foot（脚）。玩法：唱 Head Shoulders Knees And Toes 歌，边唱边指。",
     "example": ["This is my father. 这是我的爸爸。", "Touch your head. 摸摸你的头。", "I have two eyes and one nose. 我有两只眼睛一个鼻子。"],
     "mnemonic": "爸爸 father 妈妈 mum，眼睛 eye 鼻子 nose，手 hand 脚 foot。",
     "quiz": [{"question": "eye 是身体的哪个部位？", "options": ["耳朵", "眼睛", "鼻子", "嘴巴"], "answer": 1, "explanation": "eye 眼睛，ear 耳朵，nose 鼻子，mouth 嘴巴。"}]},
    {"id": "v3", "name": "动物与食物词汇", "subject": "英语", "module": "词汇复习",
     "explain": "动物：cat（猫）dog（狗）bird（鸟）fish（鱼）tiger（老虎）elephant（大象）monkey（猴子）panda（熊猫）。食物：apple（苹果）banana（香蕉）orange（橙子）milk（牛奶）egg（鸡蛋）rice（米饭）。暑假玩法：逛动物园用英语说出动物名，吃饭时用英语说食物名。",
     "example": ["I like pandas. 我喜欢熊猫。", "I want an apple. 我想要一个苹果。", "Can I have some milk? 我能喝点牛奶吗？"],
     "mnemonic": "cat 猫 dog 狗，monkey 猴子 panda 熊猫；apple 苹果 milk 奶，egg 鸡蛋 rice 饭。",
     "quiz": [{"question": "panda 是什么动物？", "options": ["老虎", "熊猫", "猴子", "大象"], "answer": 1, "explanation": "panda 熊猫，tiger 老虎，monkey 猴子，elephant 大象。"}]},
    {"id": "v4", "name": "玩具运动与动作词", "subject": "英语", "module": "词汇复习",
     "explain": "玩具：ball（球）kite（风筝）toy car（玩具车）doll（娃娃）。运动动作：run（跑）jump（跳）swim（游泳）play football（踢足球）ride a bike（骑自行车）。暑假正是运动的好时候，边运动边说英语：Let's run!（我们跑步吧）I can swim!（我会游泳）",
     "example": ["I can jump. 我会跳。", "Let's play football! 我们踢足球吧！", "I ride my bike every day. 我每天骑自行车。"],
     "mnemonic": "run 跑 jump 跳 swim 游泳，ball 球 kite 风筝 bike 自行车。",
     "quiz": [{"question": "swim 是什么意思？", "options": ["跑步", "游泳", "跳高", "骑车"], "answer": 1, "explanation": "swim 游泳，run 跑步，jump 跳。"}]},

    # ---- 简单短句 ----
    {"id": "s1", "name": "What's this? 句型", "subject": "英语", "module": "简单短句",
     "explain": "核心问答句型：What's this?（这是什么）— It's a ...（它是……）。注意：单数用 a/an：It's a book. It's an apple. 复数用 They are：They are pencils.（它们是铅笔）。暑假玩法：爸爸指东西问 What's this?，Peter 用 It's a... 回答。",
     "example": ["What's this? — It's a book. 这是什么？——是一本书。", "What's this? — It's an egg. 这是什么？——是一个鸡蛋。（an 用在元音开头）", "What are these? — They are kites. 这些是什么？——是风筝。"],
     "mnemonic": "What's this 这是什么，It's a 它是一个；元音开头用 an，复数用 They are。",
     "quiz": [{"question": "问「这是什么」用英语怎么说？", "options": ["What's this?", "How are you?", "What's your name?", "How old are you?"], "answer": 0, "explanation": "What's this? 问「这是什么」，回答 It's a/an..."},
              {"question": "It's an apple 为什么用 an？", "options": ["apple 很长", "apple 以元音音素开头", "an 比 a 高级", "随便用"], "answer": 1, "explanation": "apple 以元音音素开头，所以用 an。"}]},
    {"id": "s2", "name": "I like / I can 句型", "subject": "英语", "module": "简单短句",
     "explain": "表达喜好和能力：I like ...（我喜欢……）I don't like ...（我不喜欢……）I can ...（我会……）I can't ...（我不会……）。问句：Do you like...?（你喜欢……吗）Can you...?（你会……吗）。回答：Yes, I do. / No, I don't. Yes, I can. / No, I can't.",
     "example": ["I like swimming. 我喜欢游泳。", "Do you like apples? — Yes, I do. 你喜欢苹果吗？——是的。", "I can ride a bike. 我会骑自行车。", "Can you swim? — No, I can't. 你会游泳吗？——不会。"],
     "mnemonic": "like 喜欢 can 会，don't 不喜欢 can't 不会；Do you...? 问喜好，Can you...? 问能力。",
     "quiz": [{"question": "「我喜欢足球」用英语说？", "options": ["I can football.", "I like football.", "I am football.", "Football like I."], "answer": 1, "explanation": "表达喜欢用 I like...，I can 是「我会」。"}]},
    {"id": "s3", "name": "How many? 与 Let's 句型", "subject": "英语", "module": "简单短句",
     "explain": "问数量：How many...?（多少……）— How many books? 三本 → Three books. Let's 句型表示「我们一起做」：Let's go!（走吧）Let's play!（玩吧）Let's sing!（唱吧）。暑假玩法：数积木问 How many blocks?，出门前说 Let's go!",
     "example": ["How many apples? — Five apples. 几个苹果？——五个。", "How many kites do you see? — I see six kites. 你看到几只风筝？——六只。", "Let's go to the park! 我们去公园吧！"],
     "mnemonic": "How many 问多少，数字加名词回答；Let's 一起来，go play sing 随便选。",
     "quiz": [{"question": "「我们一起玩吧」用英语说？", "options": ["How many play?", "Let's play!", "I like play.", "Play let's!"], "answer": 1, "explanation": "Let's play! 是「我们一起玩吧」，Let's 后面跟动词原形。"}]},
    {"id": "s4", "name": "礼貌用语短句", "subject": "英语", "module": "简单短句",
     "explain": "礼貌用语要常说：Thank you!（谢谢）Thanks!（多谢）You're welcome.（不客气）Sorry!（对不起）Excuse me.（打扰一下）Please.（请）May I...?（我可以……吗）。暑假目标：每天至少说 5 句英语礼貌用语，做个有礼貌的小绅士。",
     "example": ["Thank you, Dad! 谢谢爸爸！", "Sorry, I'm late. 对不起，我迟到了。", "May I have some water? 我可以喝点水吗？", "Excuse me. 打扰一下（问路、借过时用）"],
     "mnemonic": "谢谢 Thank you，不客气 Welcome，对不起 Sorry，请 Please，May I 表请求。",
     "quiz": [{"question": "别人对你说 Thank you，你应该回答？", "options": ["Sorry.", "You're welcome.", "Excuse me.", "Please."], "answer": 1, "explanation": "对方说谢谢，回答 You're welcome.（不客气）。"}]},

    # ---- 英语动画片 ----
    {"id": "a1", "name": "Super Simple Songs 儿歌动画", "subject": "英语", "module": "英语动画片",
     "explain": "Super Simple Songs（SSS）是全球最流行的儿童英语儿歌动画，画面简单可爱、语速慢、重复多，非常适合英语启蒙。暑假安排：每天看 2-3 集（每集 2-3 分钟），跟着唱跟着跳。推荐曲目：Hello Hello、Head Shoulders Knees and Toes、Five Little Ducks、Baby Shark、The Wheels on the Bus。看的时候要跟着做动作，不能只看不动。",
     "example": ["官网（免费）：https://supersimple.com/songs/ 按主题选歌", "B 站搜索：Super Simple Songs 有大量合集，可投屏到电视", "配套玩法：看完一集，唱给爸爸听，做动作表演"],
     "mnemonic": "每天两集 SSS，边看边唱边做动作，开口就是赢。",
     "steps": ["每天固定时间看 2-3 集（建议下午点心后）", "每集看完跟着唱一遍", "每周学唱一首完整的歌，录视频记录"],
     "quiz": [{"question": "看 SSS 儿歌的正确方式是？", "options": ["只看不动", "边看边跟唱跟做动作", "快进跳过", "一天看完所有"], "answer": 1, "explanation": "边看边唱边做动作，语言和动作结合记得最牢，还能练听力。"}]},
    {"id": "a2", "name": "Peppa Pig 小猪佩奇", "subject": "英语", "module": "英语动画片",
     "explain": "Peppa Pig（小猪佩奇）是经典的英音生活动画，每集 5 分钟，对话简单、贴近日常生活，适合 7 岁左右的孩子磨耳朵。暑假安排：每天 1-2 集，第一遍看字幕版理解剧情，第二遍不看字幕只听。看完用中文问 Peter：这集讲了什么？Peppa 做了什么？",
     "example": ["B 站搜索：Peppa Pig 小猪佩奇 英文版（有中英字幕合集）", "推荐集数：Muddy Puddles（泥坑）、Dentist（牙医）、Hide and Seek（捉迷藏）", "看完互动：What did Peppa do?（Peppa 做了什么）"],
     "mnemonic": "每天一集佩奇，先看字幕版，再听无字幕，最后用英语问一句。",
     "steps": ["第一遍：看中英字幕版理解剧情", "第二遍：遮住字幕只靠耳朵听", "看完回答爸爸一个问题（用中文或英语都行）", "注意控制时长：每天不超过 15 分钟"],
     "quiz": [{"question": "看 Peppa Pig 的正确姿势是？", "options": ["只看一遍字幕版就结束", "同一集看两遍：先字幕后无字幕", "一天看十集", "只听声音不看画面"], "answer": 1, "explanation": "先字幕理解，再裸听磨耳朵，同集重复是最高效的输入方式。"}]},
    {"id": "a3", "name": "Little Fox 分级动画", "subject": "英语", "module": "英语动画片",
     "explain": "Little Fox（小狐狸）是分级动画网站，按难度分 Level 1-9，从单词歌到长篇故事都有，是系统学英语的好资源。一年级暑假可以从 Level 1 的短故事和歌曲开始，比如 ABC Book、Word Families 系列。每个故事配文本，可以先看动画再读文本。",
     "example": ["官网：https://www.littlefox.com/（部分内容免费）", "Level 1 适合：简单单词、短句、重复句型", "配套资源：动画+文本+单词卡"],
     "mnemonic": "小狐狸分级看，Level 1 起步，动画配文本，一周一个故事。",
     "steps": ["每周选 1 个 Level 1 故事", "先看动画 2 遍，再跟着读文本", "把故事里的新单词记到英语本上"],
     "quiz": [{"question": "Little Fox 适合怎么用？", "options": ["一次看完所有级别", "从 Level 1 开始，动画+文本配套看", "只看不读", "跳过 Level 1 直接看 Level 9"], "answer": 1, "explanation": "分级学习要从适合自己水平的 Level 1 开始，动画和文本配套效果最好。"}]},
    {"id": "a4", "name": "Big Muzzy 玛泽的故事", "subject": "英语", "module": "英语动画片",
     "explain": "Big Muzzy（玛泽的故事）是 BBC 出品的经典英语教学动画，讲外星人 Muzzy 来到王国的故事，专门为零基础孩子设计，语速慢、句型反复出现，被誉为「英语启蒙必看」。暑假可以每周看 2-3 集（每集 15 分钟），重点听里面的句型。",
     "example": ["B 站搜索：Big Muzzy 玛泽的故事 英文版（有全集中英字幕）", "特色：句型重复教学，如 This is... That is... I like...", "看完玩法：和爸爸分角色配音：I am Muzzy! You are the King!"],
     "mnemonic": "玛泽讲句型，This is That is I like，每周两三集，配音玩起来。",
     "steps": ["每周看 2-3 集，每集 15 分钟", "跟读里面的重点句型", "选一集和爸爸分角色配音", "把学到的句型用到生活中"],
     "quiz": [{"question": "Big Muzzy 的特点是什么？", "options": ["语速快剧情复杂", "为零基础设计，句型反复教学", "全是恐怖故事", "没有字幕"], "answer": 1, "explanation": "Big Muzzy 是 BBC 专门为零基础孩子设计的教学动画，句型反复出现，适合启蒙。"}]},
]

# ============ 围棋 ============
GO_MODS = [
    {"id": "mod_16", "name": "布局要点", "subject": "围棋"},
    {"id": "mod_17", "name": "定式基础", "subject": "围棋"},
    {"id": "mod_18", "name": "死活基础", "subject": "围棋"},
    {"id": "mod_19", "name": "对杀技巧", "subject": "围棋"},
    {"id": "mod_20", "name": "手筋练习", "subject": "围棋"},
    {"id": "mod_21", "name": "官子与实战", "subject": "围棋"},
]

GO_SKILLS = [
    # ---- 布局要点 ----
    {"id": "go1", "name": "星位与小目", "subject": "围棋", "module": "布局要点",
     "explain": "1 段考前布局复习：开局第一手棋应该下在角和边上，最常用的两个位置是星位（角上四路线交叉点）和小目（角上三、四线交叉点）。星位重视外势、速度快；小目重视实地、更扎实。四个角价值一样大，开局先把角占满，再抢边。",
     "example": ["星位：黑棋第一手占星位，快速建立外势", "小目：黑棋第一手占小目，稳扎稳打取实地", "占角顺序：先占空角，再守自己的角，最后挂对方的角"],
     "mnemonic": "金角银边草肚皮。先角后边再中腹；星位取势快，小目取地稳。",
     "steps": ["在棋盘上摆出四个星位和四个小目", "练习：第一手星位、第二手小目、第三手星位的布局", "对局中坚持：前 10 手全部下在角或边"],
     "quiz": [{"question": "围棋谚语「金角银边」后面是什么？", "options": ["铜中腹", "草肚皮", "铁肚皮", "银中腹"], "answer": 1, "explanation": "金角银边草肚皮：角价值最大，边其次，中腹最空，开局先占角。"}]},
    {"id": "go2", "name": "三线与四线", "subject": "围棋", "module": "布局要点",
     "explain": "三线是「实利线」（容易围住实地），四线是「势力线」（利于向中腹发展）。三线围地牢但偏低，四线发展好但容易漏风。1 段水平要理解：拆边一般拆在三、四线，两翼张开要高低配合（三线和四线搭配），不要都下在三线围小地，也不要都下在四线被掏空。",
     "example": ["拆二：在三线拆二（连成两个间隔）最稳", "高低配合：一边三线一边四线，既有实地又有发展", "记住：第一线是死线，第二线是失败线，只有做活时才用"],
     "mnemonic": "三线围地四线势，高低搭配不偏科；一线死线二线败，做活时候才想起。",
     "quiz": [{"question": "三线被称作什么线？", "options": ["势力线", "实利线", "失败线", "中腹线"], "answer": 1, "explanation": "三线容易围住实地，叫实利线；四线利于发展，叫势力线。"}]},
    {"id": "go3", "name": "开局占角顺序", "subject": "围棋", "module": "布局要点",
     "explain": "开局四步口诀：一占空角，二守角，三挂角，四拆边。占角：抢最大的空角；守角：自己的角加一手棋巩固；挂角：在对方角边上落子威胁它；拆边：在边上张开阵势。1 段考前练习：下 20 局让 Peter 坚持「前 20 手不下一线二线」，建立大局观。",
     "example": ["一占空角：黑 1 占星位", "二守角：黑 3 在己方星位角上小飞守角", "三挂角：黑 5 在对方小目角上挂角", "四拆边：黑 7 沿边拆二张开"],
     "mnemonic": "一占二守三挂四拆，占大守稳挂敌拆边。",
     "steps": ["在棋盘上摆一遍：占角→守角→挂角→拆边", "对局时前 20 手只下角边，不下中腹", "每盘棋结束后，和爸爸一起复盘前 20 手"],
     "quiz": [{"question": "开局正确的顺序是？", "options": ["先拆边再占角", "先占空角，再守角挂角，最后拆边", "直接下中腹", "先挂角再占角"], "answer": 1, "explanation": "金角银边草肚皮，先占角、再守角挂角、最后拆边，这是布局的基本顺序。"}]},

    # ---- 定式基础 ----
    {"id": "go4", "name": "星位小飞挂的应对", "subject": "围棋", "module": "定式基础",
     "explain": "对手挂自己的星位角，常见应对：一、小飞应（最常见，守角最稳）；二、一间跳应（更厚实）；三、压长定式（主动作战）；四、脱先（抢别的大场）。1 段考前要求：看到小飞挂，能下出小飞应或一间跳，棋形不散。",
     "example": ["对方挂星位 → 己方小飞应（星位角上小飞守角）", "对方挂星位 → 己方一间跳（守角兼向外发展）", "对方挂角后自己脱先去占另一个空角"],
     "mnemonic": "小飞挂星位，小飞一间跳二选一；守角要厚实，棋形不散架。",
     "steps": ["摆出小飞应和一间跳两种棋形", "比较两种应法的区别：小飞稳、跳更厚", "在死活题软件上练习 5 个星位定式变化"],
     "quiz": [{"question": "对手小飞挂我方星位，最简单的应对是？", "options": ["小飞应", "直接打入", "下到对方角里", "在三线爬"], "answer": 0, "explanation": "小飞应是最常见最稳的守角方式，一间跳应也常见。"}]},
    {"id": "go5", "name": "小目小飞挂的应对", "subject": "围棋", "module": "定式基础",
     "explain": "对手挂小目角，常见应对：一、小尖（守角最坚实）；二、一间跳；三、飞压（压迫对方出头）；四、夹击（配合外势作战）。小目定式比星位多，1 段考前只需掌握小尖和一间跳两种基本应法，遇到陌生变化不慌，先守住角。",
     "example": ["对方小飞挂小目 → 己方小尖守角（坚实）", "对方小飞挂小目 → 己方一间跳（轻灵）", "对方挂角 → 己方也可以脱先抢大场"],
     "mnemonic": "小目被挂，小尖一间跳；守角为先，不熟就脱先。",
     "steps": ["摆熟小尖和一间跳两个基本应法", "对局中优先用会的定式，不学新变化", "复盘时数一数：挂角后自己有没有吃亏"]},
    {"id": "go6", "name": "守角与拆边", "subject": "围棋", "module": "定式基础",
     "explain": "守角：自己占的角要守，常见守角方式有小飞守角、大飞守角、单关守角（小目）。拆边：沿着边线发展势力，拆二最稳（间隔两路），拆三要有援兵才敢拆。1 段考前要求：自己的角必须守，边上的拆边不小于拆二。",
     "example": ["星位角 → 小飞守角（最常见）", "小目角 → 单关守角或小飞守角", "边上的棋子间隔：拆二稳、拆三要有外势配合"],
     "mnemonic": "占角不守是漏洞，守角小飞最常见；拆二最稳，拆三看援兵。",
     "quiz": [{"question": "占角之后不守角会怎样？", "options": ["没有影响", "容易被对方挂角侵入，角地受损", "角会自动变大", "更容易赢棋"], "answer": 1, "explanation": "不守的角容易被对方挂角、点角，角地会大幅缩水。"}]},

    # ---- 死活基础 ----
    {"id": "go7", "name": "两眼活棋", "subject": "围棋", "module": "死活基础",
     "explain": "1 段死活核心概念：一块棋有两个独立的眼（两个真眼）就是活棋，对方永远吃不掉。真眼：眼位内部的气没有被对方占到。假眼：看似是眼，其实会被对方破坏。考前练习：每天 5 道死活题，先判断「这块棋是死是活」，再说出理由。",
     "example": ["直四、曲四都是活棋（对方点不进来）", "直三、弯三是死棋（对方点中间就死）", "丁四、刀五、花五都是死棋，板六是活棋"],
     "mnemonic": "两个真眼就活，一个眼必死；直四曲四活，直三弯三死。",
     "steps": ["摆出直四、曲四、直三、弯三四种棋形", "让孩子动手验证：对方点进去会怎样", "每天做 5 道死活题，错了要看答案理解"],
     "quiz": [{"question": "一块棋有两个真眼，这块棋？", "options": ["是死棋", "是活棋", "要被吃", "不一定"], "answer": 1, "explanation": "两个真眼就是活棋，对方无法同时堵住两个眼。"}]},
    {"id": "go8", "name": "做眼与破眼", "subject": "围棋", "module": "死活基础",
     "explain": "做眼：让自己的棋做出两个眼，要点是占据眼位关键点（眼形的中心点）。破眼：阻止对方做活，要点是抢对方眼位的中心点。口诀：点眼要点头部（眼形的中心），让对方做不成两个眼。考前练习：死活题中「黑先做活」和「黑先杀白」各做 3 道。",
     "example": ["直三做活：下在中间，一个变两个眼", "刀五杀棋：点在刀把上（眼形中心）", "丁四杀棋：点在中心，白棋做不成两眼"],
     "mnemonic": "做眼占中心，破眼也占中心；同一要点，谁先下谁赢。",
     "quiz": [{"question": "杀直三的黑棋，要点在哪里？", "options": ["直三的最边上", "直三的中间", "直三的外面", "随便哪里"], "answer": 1, "explanation": "点直三的中间（眼形中心），白棋只能做一个眼，是死棋。"}]},
    {"id": "go9", "name": "常见眼形死活判断", "subject": "围棋", "module": "死活基础",
     "explain": "1 段必背眼形死活表：活棋——直四、曲四、板六、大眼（两个眼以上）；死棋——直三、弯三、丁四、刀五、花五、方四；半死不活（谁先谁赢）——打劫形。考前要求：看到棋形 3 秒内说出死活，这是考试得分的基本功。",
     "example": ["活：直四、曲四、板六（对方点不进去）", "死：直三、弯三、丁四、刀五、花五、方四", "打劫：曲三、小猪嘴等特殊情况"],
     "mnemonic": "四五六活，三四五死：直四曲四板六活；直三丁四刀五花五方四死。",
     "steps": ["把七种眼形全部摆出来", "逐个验证：对方先手能不能杀", "做 10 道「判断死活」专项题，每题 10 秒内作答"],
     "quiz": [{"question": "下列哪个是活棋？", "options": ["直三", "刀五", "曲四", "方四"], "answer": 2, "explanation": "曲四是活棋，直三、刀五、方四都是死棋。"}]},
    {"id": "go10", "name": "角上常见死活", "subject": "围棋", "module": "死活基础",
     "explain": "角上的死活和边上不一样（角有两条边帮忙做眼）：角上的直三、曲三有时是活棋（位置不同）；大猪嘴（角上板六被扳）是死棋——口诀「扳点杀猪」；小猪嘴（角上小眼形）经常是打劫。1 段考前重点：记住大猪嘴的杀法。",
     "example": ["大猪嘴：扳点（先扳后点）是杀棋次序", "小猪嘴：多数是打劫", "角上直四、曲四：要点到就死，被占到就活"],
     "mnemonic": "大猪嘴扳点杀，小猪嘴打劫多；角上眼形别小看，差一路差生死。",
     "steps": ["摆出大猪嘴棋形，练习扳点的杀法", "摆出小猪嘴，练习打劫", "角上死活题每天 2 道"]},

    # ---- 对杀技巧 ----
    {"id": "go11", "name": "数气与紧气", "subject": "围棋", "module": "对杀技巧",
     "explain": "对杀就是比气：气多的赢，气少的输。数气要点：先数双方各有几口气，再看谁能先紧气。对杀口诀：双方气一样多，谁先下谁赢；我方气多，先紧对方的气；我方气少，想办法长气（延伸出更多的气）。",
     "example": ["双方都是 3 口气 → 先紧气的一方赢", "我方 4 口气、对方 3 口气 → 我方必胜", "气少的一方：先长气（往开阔处延伸）再对杀"],
     "mnemonic": "对杀先数气，气多不用急，气少先长气，一样先紧气。",
     "steps": ["摆两个对杀棋形，数双方气数", "练习「先紧气」的次序：从外侧往里紧", "做 5 道对杀题，先数气再下棋"],
     "quiz": [{"question": "双方都是 4 口气，谁赢？", "options": ["黑棋赢", "白棋赢", "先紧气的一方赢", "和棋"], "answer": 2, "explanation": "气一样多时，先下（先紧气）的一方赢，所以对杀要抢先手。"}]},
    {"id": "go12", "name": "对杀次序与长气", "subject": "围棋", "module": "对杀技巧",
     "explain": "对杀次序很关键：先紧对方的气，还是先补自己的气？基本原则：气少的一方先长气（自己的气比对方多后再对杀）；气多的一方主动紧气。特殊技巧：用「扑」来收气（送吃一子让对方气变少）、用「枷」来防止对方逃出。",
     "example": ["自己气少：先长气（延伸出去），不要先紧对方", "对方气少：连续紧气，不给喘息", "扑：送吃一个子，让对方的棋气变少"],
     "mnemonic": "气少先长，气多先紧；长完再杀，次序不乱。",
     "quiz": [{"question": "对杀时自己气少应该先做什么？", "options": ["紧对方的气", "长自己的气", "逃跑", "认输"], "answer": 1, "explanation": "气少先长气，把气变多再对杀；盲目紧气只会死得更快。"}]},

    # ---- 手筋练习 ----
    {"id": "go13", "name": "倒扑与接不归", "subject": "围棋", "module": "手筋练习",
     "explain": "两个 1 段必会手筋：倒扑——故意送吃一子，对方吃后形成「胀死牛」（不入气）再全歼；接不归——利用「接不归」（接回去就会被吃）吃对方的棋。考前练习：在棋盘上摆出倒扑和接不归的基本形，每个做 5 遍，做到闭眼能摆出来。",
     "example": ["倒扑：送一子让对方吃，吃后自己不入气，再提掉一片", "接不归：对方的棋连不起来，接哪个点都会死", "胀死牛：被吃后形成不入气的形状"],
     "mnemonic": "倒扑先送子，吃了胀死牛；接不归接不了，一接就完蛋。",
     "steps": ["摆出倒扑基本形，练习送吃的时机", "摆出接不归基本形，练习追杀", "做 3 道倒扑题 + 3 道接不归题"],
     "quiz": [{"question": "倒扑的关键是？", "options": ["主动送吃一子", "逃跑", "围大空", "下在中间"], "answer": 0, "explanation": "倒扑主动送吃一子，对方吃掉后反而形成不入气，被全歼。"}]},
    {"id": "go14", "name": "挖、夹与滚打包收", "subject": "围棋", "module": "手筋练习",
     "explain": "1 段手筋三件套：挖——在对方两子之间打入，切断对方联络；夹——在对方一子两边同时威胁；滚打包收——连续打吃逼对方成愚形（凝形），最后整体吃掉。这些手筋在实战对杀中经常出现，考前每个做 3 道题。",
     "example": ["挖：下在对方两子中间，切断联络", "夹：一子两边都威胁对方", "滚打包收：打吃→对方接→再打吃→对方成愚形→包围吃掉"],
     "mnemonic": "挖断联络，夹逼两边，滚打包收成愚形，一套带走。",
     "steps": ["摆出挖的棋形，练习切断", "摆出夹的棋形，练习两边威胁", "看一道滚打包收的例题，理解「成愚形」的概念"],
     "quiz": [{"question": "「挖」的手筋作用是？", "options": ["扩大自己的地盘", "切断对方棋子的联络", "收空", "做眼"], "answer": 1, "explanation": "挖是下在对方两子之间切断联络，是常用的破眼、杀棋手筋。"}]},

    # ---- 官子与实战 ----
    {"id": "go15", "name": "先手官子与后手官子", "subject": "围棋", "module": "官子与实战",
     "explain": "官子阶段的规则：先手（对方必须应，自己还保持主动）的官子要抢着下；后手（对方可以不应）的官子最后下。口诀：先手官子大于一切，双先官子（双方都是先手）最优先。1 段考前：收官时先抢先手官子，再下大官子，最后小官子。",
     "example": ["双先官子：谁下都对方必应，最优先", "先手官子：自己下完对方必须应", "后手官子：下完对方可以脱先，价值打折"],
     "mnemonic": "双先最优先，先手接着抢，后手看大小。",
     "quiz": [{"question": "收官时应该先下什么？", "options": ["小官子", "先手官子", "后手官子", "随便下"], "answer": 1, "explanation": "先手官子对方必须应，自己保持主动，所以要优先抢。"}]},
    {"id": "go16", "name": "官子大小与收官次序", "subject": "围棋", "module": "官子与实战",
     "explain": "判断官子大小：数一数这个官子双方各能得几目，加起来就是这个官子的价值。1 段要求：会算 5 目以内的官子；收官次序：先大后小、先急后缓、先先手后后手。考试常见失误：只顾吃子忘了收官，中盘一结束就开始收官。",
     "example": ["一个官子自己得 2 目对方得 2 目 → 价值 4 目", "先收 10 目的官子，再收 5 目的", "边角先手官子优先于中腹后手大官子"],
     "mnemonic": "官子价值双方目数加起来，先大后小，先先手后后手。",
     "steps": ["摆 5 个常见官子，练习算目", "实战中坚持：中盘战斗结束立刻收官", "复盘时数一数官子阶段亏了几目"],
     "quiz": [{"question": "收官次序正确的是？", "options": ["先小后大", "先大后小，先先手后后手", "先中腹后边角", "随便收"], "answer": 1, "explanation": "先收大的、先手的官子，再收小的、后手的。"}]},
    {"id": "go17", "name": "打谱、网棋与考前准备", "subject": "围棋", "module": "官子与实战",
     "explain": "1 段考前准备四件事：一、每天 5 道死活题（雷打不动）；二、每天下 1 盘网棋（弈城、野狐的级位区，或和爸爸下）；三、每周打 1 张名局棋谱（跟着摆前 50 手）；四、考前模拟：完整下 3 盘不计时的棋，练习「落子前先想三秒」。考试技巧：不求妙手求稳健，布局守角、中盘不贪、官子收完。",
     "example": ["死活题：每天 5 道，连续 4 周", "网棋：弈城或野狐级位区，每天 1 盘", "打谱：每周 1 张，摆前 50 手", "考前：模拟 3 盘完整对局，练习时间管理"],
     "mnemonic": "死活天天练，网棋不能断，打谱学高手，考前多模拟。",
     "steps": ["制定 4 周备考计划：死活+网棋+打谱", "每周日做一次小测验：10 道死活题 30 分钟", "考试前一晚早点睡，带好水杯，心态放松"],
     "quiz": [{"question": "1 段考前最重要的日常练习是？", "options": ["每天下网棋不练死活", "每天 5 道死活题+1 盘对局", "只看棋谱不下棋", "只打谱不做题"], "answer": 1, "explanation": "死活题是围棋基本功，每天雷打不动 5 道，再配合对局和打谱。"}]},
]

# 汇总
def get_en_go_data():
    nodes = [
        {"id": "en", "name": "英语", "category": "subject", "subject": "英语"},
        {"id": "go", "name": "围棋", "category": "subject", "subject": "围棋"},
    ]
    nodes += EN_MODS
    nodes += GO_MODS
    nodes += EN_SKILLS
    nodes += GO_SKILLS
    return nodes
