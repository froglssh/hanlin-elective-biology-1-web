# -*- coding: utf-8 -*-
"""選修生物（Ⅰ）教材入口網站產生器：內容依翰林版《選修生物Ⅰ（全）》課本改寫。
修改網址、簡介或重點時，改本檔的 CHAPTERS 資料後重新執行即可。"""
import html, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else 'site'
BASE = 'https://froglssh.github.io/hanlin-elective-biology-1-web/'
DRIVE = 'https://drive.google.com/file/d/{}/view'

ICON_OUT = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_GO = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_ZOOM = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m16 16 4.5 4.5M8.5 11h5M11 8.5v5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
ICON_PLAY = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 8.5v7l6-3.5z" fill="currentColor"/></svg>'
ICON_BOOK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5C6.5 4.5 9.5 4.5 12 6c2.5-1.5 5.5-1.5 8-.5v13c-2.5-1-5.5-1-8 .5-2.5-1.5-5.5-1.5-8-.5z M12 6v13.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'

E = html.escape

CHAPTERS = [
 dict(n=1, title='細胞的構造與功能', en='Cell Structure &amp; Function', a='#0d9488', a2='#2dd4bf', t='#f0fdfa',
  lead='細胞是生命的基本單位。本章從構成細胞的水、無機鹽與醣類、蛋白質、脂質、核酸等分子談起，循著科學家建立「流體鑲嵌模型」的歷程認識生物膜與內膜系統，再探討物質如何進出細胞，最後看見細胞增殖、分化、衰老、凋亡與癌變的生命歷程。',
  units=[
   dict(code='1-1', title='細胞的分子組成', web='生命分子積木坊', slug='ch1-1', vid='1SxUxkz001iSdTDDOhTvniHfqTV3XnuH3', pages='P.8–23',
    fig='s1-1', cap='圖 1－11　核酸的構造',
    intro='細胞除了水與無機鹽，還含有只能由生物合成的醣類、蛋白質、脂質、核酸與少量維生素。水分子具極性、彼此以氫鍵相連，是良好的溶劑且比熱高；醣類分為單醣、雙醣與多醣，可供能也構成細胞壁與外骨骼；蛋白質由胺基酸以胜肽鍵串接，摺疊成一至四級結構而具有功能；脂質包含中性脂、磷脂與固醇；核酸由核苷酸組成，DNA 儲存遺傳訊息，RNA 參與蛋白質合成。',
    subs=['1-1.1 水', '1-1.2 無機鹽', '1-1.3 醣類', '1-1.4 蛋白質', '1-1.5 脂質', '1-1.6 核酸', '1-1.7 維生素'],
    tags=['氫鍵與比熱', '單醣・雙醣・多醣', '胜肽鍵', '蛋白質四級結構', '磷脂與固醇', '核苷酸']),
   dict(code='1-2', title='生物膜的構造與功能', web='生物膜研究所', slug='ch1-2', vid='1Dhw0fBS520_MZ_rEMshY73OeiQ4H01iG', pages='P.24–35',
    fig='s1-2', cap='圖 1－20　細胞膜蛋白的種類',
    intro='從「脂溶性物質較易進出細胞」的觀察出發，高特與格蘭多以紅血球推論膜為脂雙層；之後歷經道森與達尼利模型、羅伯森的三明治模型、冷凍蝕刻電顯與佛萊和艾丁的細胞融合實驗，1972 年辛格與尼克森提出「流體鑲嵌模型」：蛋白質鑲嵌於可流動的磷脂雙層中，擔任運輸、酵素、受體與辨識等功能。真核細胞的核膜、內質網、高基氏體、溶體與液泡等則藉囊泡往來，合稱內膜系統。',
    subs=['1-2.1 生物膜構造模型的發展歷程', '1-2.2 內膜系統'],
    tags=['脂雙層', '三明治模型', '細胞融合實驗', '流體鑲嵌模型', '膜蛋白的功能', '內膜系統']),
   dict(code='1-3', title='細胞膜運輸物質的方式', web='細胞膜運輸驛站', slug='ch1-3', vid='13_FqEKsbv08QsJ-_Rt9U4L79V5XcVmu4', pages='P.36–41',
    fig='s1-3', cap='圖 1－26　小分子物質通過細胞膜的運輸',
    intro='細胞膜具有選擇性。O₂、CO₂ 與脂溶性物質可順濃度梯度以簡單擴散通過；離子、葡萄糖等則須藉通道蛋白或載體蛋白進行促進性擴散，兩者都不耗能，屬被動運輸。水的滲透使細胞在高張、等張、低張溶液中出現不同變化；若要逆濃度梯度輸送，則需載體蛋白消耗 ATP 進行主動運輸。大分子則以胞吞作用（吞噬、胞飲、受體媒介胞吞）與胞吐作用進出細胞。',
    subs=['1-3.1 小分子物質通過細胞膜的運輸', '1-3.2 大分子物質進出細胞的方式'],
    tags=['簡單擴散', '促進性擴散', '滲透與張力', '主動運輸', '受體媒介胞吞', '胞吐作用']),
   dict(code='1-4', title='細胞的生命歷程', web='細胞生命驛站', slug='ch1-4', vid='1Cd_Go-tL6x4r6JEBM4MrDarFhi_186re', pages='P.42–49',
    fig='s1-4', cap='圖 1－32　幹細胞的分裂與分化潛能',
    intro='細胞歷經生長與分裂的循環稱為細胞週期；源自同一受精卵的細胞因表現的基因不同而分化出各種形態與功能。細胞衰老與代謝廢物堆積、自由基傷害等有關；細胞凋亡則是由基因調控的計畫性死亡，參與蝌蚪尾巴消失、指間蹼的去除等發育過程。幹細胞保有分裂與分化能力，可補充新的細胞；而當控制細胞週期的基因突變時，細胞可能轉變為癌細胞。',
    subs=['1-4.1 細胞的增殖與分化', '1-4.2 細胞的衰老與凋亡', '1-4.3 幹細胞', '1-4.4 細胞的癌變原因與可能的預防方式'],
    tags=['細胞週期', '細胞分化', '細胞凋亡', '胚胎幹細胞', '成體幹細胞', '致癌因子']),
  ],
  labs=[
   dict(code='活動 1-1', title='生物組織中常見有機物的檢測', web='有機物檢測實驗室', slug='lab1-1', vid='1SFDHjlpBShTkqkgMId3CwAUmZeyiU56I', pages='P.50–60',
    fig='a1-1', cap='還原醣的檢測：隔水加熱觀察本氏液顏色變化',
    intro='學習四類有機物的簡易檢測：本氏液隔水加熱檢測還原醣（依含量呈紅、橙、綠色，蔗糖不是還原醣）；碘液檢測澱粉（藍紫色）；縮二脲試驗（紫紅色）與教師示範的黃蛋白反應檢測蛋白質；油性辣椒紅試劑與油漬測試檢測脂質，最後綜合應用於檢測食品成分。'),
   dict(code='活動 1-2', title='植物細胞膜的通透性', web='植物細胞膜通透性實驗室', slug='lab1-2', vid='14hVQffC3DpnPj6TVG4e9W5uP3JZpoKGT', pages='P.61–65',
    fig='a1-2', cap='製作水蘊草葉片標本並滴加蔗糖溶液',
    intro='以水蘊草（或水王孫、紫背萬年青、紫色洋蔥）葉片為材料，分別滴加 0.2 M 與 1.0 M 蔗糖溶液，計算視野中發生質離現象的細胞比例，再以蒸餾水置換觀察質離恢復，藉水分子的滲透方向推論蔗糖能否通過細胞膜。'),
  ]),
 dict(n=2, title='細胞的代謝與能量', en='Metabolism &amp; Energy', a='#d97706', a2='#fbbf24', t='#fffbeb',
  lead='生物體內所有物質與能量的轉換稱為新陳代謝。本章先認識酵素如何降低活化能、哪些因素會影響酵素活性，再追蹤葡萄糖在有氧呼吸、無氧呼吸與發酵作用中釋出能量的過程，最後看能量如何由太陽經食物網流轉，並以 ATP 推動同化代謝、主動運輸與運動。',
  units=[
   dict(code='2-1', title='新陳代謝與酵素', web='代謝與酵素驛站', slug='ch2-1', vid='1nSy6JhyGY8O0xMBuEAIU4Y1V3XqGMvut', pages='P.70–74',
    fig='s2-1', cap='圖 2－1　酵素對活化能的影響與催化反應示意圖',
    intro='新陳代謝包含利用能量合成物質的同化代謝，與分解物質、釋出能量的異化代謝。反應物須達到活化狀態才能反應，所需的最低能量稱為活化能；酵素是有機催化劑，受質與其活性位結合後可降低活化能，使反應加速，且具有專一性。溫度、酸鹼度、重金屬離子與輔因子都會改變酵素構形而影響活性，例如胃蛋白酶在 pH 約 2 時活性最佳。',
    subs=['2-1.1 活化能', '2-1.2 酵素的功能', '2-1.3 影響酵素活性的因素'],
    tags=['同化代謝與異化代謝', '活化能', '活性位與專一性', '誘導契合', '最適溫度與 pH', '輔因子與輔酶']),
   dict(code='2-2', title='呼吸作用', web='呼吸作用能量驛站', slug='ch2-2', vid='1Ot-aSoKFnaW3BRRiOzA5_bK30KJIbdyZ', pages='P.75–81',
    fig='s2-2', cap='圖 2－6　真核細胞有氧呼吸的各個階段',
    intro='有氧呼吸分為四個階段：細胞質液中的糖解作用將葡萄糖分解為丙酮酸；丙酮酸進入粒線體形成乙醯輔酶 A，再經檸檬酸循環產生 CO₂、NADH 與 FADH₂；最後電子傳遞鏈以 O₂ 為最終電子接受者，所形成的 H⁺ 濃度梯度驅動 ATP 合成酶，以化學滲透磷酸化產生大量 ATP。缺乏 O₂ 時，部分原核生物以硫酸根等進行無氧呼吸，酵母菌與肌肉細胞則以酒精發酵或乳酸發酵再生 NAD⁺。',
    subs=['2-2.1 有氧呼吸', '2-2.2 無氧呼吸', '2-2.3 發酵作用'],
    tags=['糖解作用', '檸檬酸循環', '電子傳遞鏈', '化學滲透磷酸化', '無氧呼吸', '酒精與乳酸發酵']),
   dict(code='2-3', title='能量流轉與生命維持的關係', web='能量流轉驛站', slug='CH2-3', vid='1KZOpe-C1HWsJZ2IKfio5YRbbl_FcWnqs', pages='P.82–85',
    fig='s2-3', cap='圖 2－11　動物細胞膜上鈉鉀幫浦運送 Na⁺ 與 K⁺',
    intro='自營生物可將無機物轉變為有機物，依能量來源分為光自營生物（植物、藻類、藍綠菌）與化學自營生物（硝化菌、硫化菌）；異營生物則直接或間接由生產者獲得能量，且能量沿食物網傳遞時大多以熱能散失。細胞以呼吸作用把有機物的能量轉存於 ATP，再以磷酸化推動同化代謝（如合成三酸甘油酯）、主動運輸（如鈉鉀幫浦）與運動蛋白沿微管移動。',
    subs=['2-3.1 能量的來源與流轉', '2-3.2 能量的使用與生命維持的關係'],
    tags=['光自營與化學自營', '食物網的能量流轉', 'ATP 與磷酸化', '同化代謝', '鈉鉀幫浦', '運動蛋白']),
  ],
  labs=[
   dict(code='活動 2-1', title='酵素活性的測定', web='酵素活性測定實驗室', slug='lab2-1', vid='1FLPbuGX7L-w8Dsi2NbIBoSmNVxfTIZkr', pages='P.86–93',
    fig='a2-1', cap='比較生、熟豬肝與馬鈴薯加入過氧化氫後的氣泡',
    intro='過氧化氫酶可將 H₂O₂ 分解為水與氧氣。先比較生的與煮過的豬肝、馬鈴薯加入 2% 過氧化氫溶液後的氣泡；再以馬鈴薯萃取酵素液浸濕濾紙圓片，測量圓片上浮到液面的時間，探討 pH 3、5、7、9 與重金屬（硫酸銅）對酵素活性的影響。'),
   dict(code='活動 2-2', title='影響酵母菌發酵的環境因子', web='酵母菌發酵環境因子工坊', slug='lab2-2', vid='1umc1aYUA7rr9mib93e6TwdK64YsSXQEq', pages='P.94–102',
    fig='a2-2', cap='發酵管分別置於室溫與 35 °C 恆溫水浴中',
    intro='酵母菌進行酒精發酵會產生 CO₂，利用發酵管收集密閉端的氣體量，比較同樣時間內的發酵速率，分組探討溫度（室溫與 35 °C）、醣的種類（葡萄糖、蔗糖、澱粉）、酸鹼度（pH 5、7、9）與乙醇濃度四種環境因子的影響。'),
  ]),
 dict(n=3, title='遺傳物質的發現與結構', en='Discovering the Genetic Material', a='#4f46e5', a2='#818cf8', t='#eef2ff',
  lead='遺傳因子在哪裡？又是什麼物質？本章跟著弗萊明、薩登、包法利與摩根的研究，看遺傳的染色體學說如何被提出並以果蠅實驗證實；再從格里夫茲、艾佛瑞到赫希與蔡司的實驗確認 DNA 是遺傳物質，最後結合查加夫與富蘭克林的證據，理解華生與克里克的雙股螺旋模型。',
  units=[
   dict(code='3-1', title='遺傳的染色體學說', web='染色體學說驛站', slug='ch3-1', vid='1flLUBuhaTJOrDQuLjLzh0Jy5LxBSMfq_', pages='P.110–122',
    fig='s3-1', cap='圖 3－1　與遺傳的染色體學說相關的科學家及其研究演進歷程',
    intro='弗萊明觀察到細胞分裂時染色體的行為，薩登與包法利發現減數分裂中染色體的分離與組合，和孟德爾遺傳因子的行為相互平行，因而提出遺傳的染色體學說。摩根以白眼突變果蠅進行雜交與互交實驗，證明控制眼色的基因位於 X 染色體上（性聯遺傳）；之後又由灰身長翅與黑身殘翅的雜交發現連鎖與互換，並以重組率推算基因間的相對距離，繪出遺傳圖譜。',
    subs=['3-1.1 孟德爾的遺傳法則與遺傳的染色體學說', '3-1.2 摩根以實驗支持遺傳的染色體學說'],
    tags=['平行關係', '遺傳的染色體學說', '白眼果蠅', '性聯遺傳', '連鎖與互換', '重組率與遺傳圖譜']),
   dict(code='3-2', title='確認遺傳物質為DNA的歷程', web='DNA探索歷程驛站', slug='ch3-2', vid='1kMQd9QyjIl2OGY8BdIHKpBgE1Nfhu8a1', pages='P.123–130',
    fig='s3-2', cap='圖 3－11　格里夫茲的肺炎鏈球菌轉形實驗',
    intro='1928 年格里夫茲發現加熱殺死的 S 型肺炎鏈球菌能使 R 型菌轉形；1940 年代艾佛瑞分別以分解蛋白質、RNA 與 DNA 的酵素處理 S 型菌萃取物，證實只有 DNA 被破壞時轉形才會消失；赫希與蔡司再以 ³⁵S 與 ³²P 分別標記噬菌體的蛋白質與 DNA，確認進入細菌的是 DNA。結合查加夫的鹼基組成規律與富蘭克林的 X 光繞射影像，華生與克里克於 1953 年提出 DNA 雙股螺旋模型。',
    subs=['3-2.1 DNA 為遺傳物質的確認', '3-2.2 確認 DNA 結構的發展歷程'],
    tags=['轉形實驗', '艾佛瑞', '噬菌體標記實驗', '查加夫法則', 'X 光繞射', '雙股螺旋模型']),
  ],
  labs=[
   dict(code='活動 3-1', title='DNA雙股螺旋模型大賽', web='DNA雙螺旋模型創客坊', slug='lab3-1', vid='1mTXl6E5ce_rWPSqBcsGUirpZRJjs3srj', pages='P.131–132',
    fig='a3-1', cap='用糖果與水果組成的 DNA 模型示意圖',
    intro='分組討論 DNA 結構的基本特色，再自備黏土、棉花糖、小番茄、牙籤等材料，於 1～2 週內完成立體模型並上台說明。評分著重：能否呈現雙股、4 種含氮鹼基、五碳醣與磷酸基骨架及規律構形；結構是否穩定；以及美感、環保與實用性。'),
  ]),
 dict(n=4, title='遺傳訊息的表現', en='Expression of Genetic Information', a='#be185d', a2='#f472b6', t='#fdf2f8',
  lead='DNA 所儲存的遺傳訊息如何被複製、轉錄成 RNA，再轉譯成蛋白質？本章從梅舍生與史塔爾證實半保留複製開始，依序認識轉錄、RNA 修飾、密碼子與轉譯；接著以大腸桿菌乳糖操縱組說明基因表現的調控，最後探討染色體與分子層次的遺傳變異及遺傳疾病篩檢。',
  units=[
   dict(code='4-1', title='遺傳訊息的複製', web='DNA複製驛站', slug='ch4-1', vid='1XLr2JWlA31DEMhbVETKZV_IV9e9fIG8w', pages='P.136–141',
    fig='s4-1', cap='圖 4－2　梅舍生與史塔爾以同位素標記實驗測試 DNA 複製的三種假說',
    intro='DNA 複製曾有全保留、半保留與分散三種假說。1958 年梅舍生與史塔爾以 ¹⁵N 與 ¹⁴N 標記大腸桿菌 DNA，再經密度梯度離心比較各代 DNA 的位置，證實 DNA 為半保留複製。複製時解旋酶解開雙股形成複製叉，RNA 引子提供起點，DNA 聚合酶只能由 5′ 端往 3′ 端延伸，因此領先股連續合成、延遲股形成岡崎片段，最後由 DNA 連接酶接合。',
    subs=['4-1.1 DNA 複製的模式', '4-1.2 DNA 複製的過程'],
    tags=['半保留複製', '密度梯度離心', '解旋酶', 'RNA 引子', '領先股與延遲股', '岡崎片段']),
   dict(code='4-2', title='遺傳訊息的轉錄與轉譯', web='轉錄與轉譯驛站', slug='ch4-2', vid='1m6ilA3Lbao2a5DCHhZ_qCx_LLQ9oXgk6', pages='P.142–151',
    fig='s4-2', cap='圖 4－10　轉譯過程中的三個階段',
    intro='轉錄時 RNA 聚合酶結合啟動子，以 DNA 模版股為依據由 5′ 往 3′ 合成 RNA，遇終止序列即停止；參與蛋白質合成的 RNA 有 mRNA、tRNA 與 rRNA。真核細胞的前驅 mRNA 須加上 5′ 端帽與 3′ 端多腺苷酸尾，並剪除內含子、接合外顯子。mRNA 上每三個鹼基構成一個密碼子，共 64 種；轉譯時 tRNA 以反密碼子配對，在核糖體上經起始、延長、終止三階段合成多肽，再經摺疊與修飾成為有功能的蛋白質。',
    subs=['4-2.1 轉錄', '4-2.2 RNA 的種類', '4-2.3 真核細胞 mRNA 的修飾', '4-2.4 密碼子與胺基酸', '4-2.5 轉譯', '4-2.6 蛋白質的修飾'],
    tags=['RNA 聚合酶', '模版股', 'RNA 剪接', '密碼子表', '反密碼子', '核糖體 E・P・A 位']),
   dict(code='4-3', title='基因表現的調控', web='基因調控驛站', slug='ch4-3', vid='15uAF0imO6Fp7q30fAlkMiO43T4F-rfNI', pages='P.152–153',
    fig='s4-3', cap='圖 4－14　大腸桿菌乳糖操縱組的調控',
    intro='原核生物分解同一種養分所需的多個酵素基因常相連排列、一起轉錄。莫諾與賈克伯以大腸桿菌提出操縱組理論：操縱組包含啟動子、操作子與結構基因，並由調節基因產生的調節蛋白控制。乳糖濃度低時，調節蛋白結合操作子，RNA 聚合酶無法轉錄；乳糖濃度高時，乳糖與調節蛋白結合使其構形改變而脫離，結構基因得以轉錄與轉譯，因此乳糖操縱組屬於可誘導型操縱組。',
    subs=['4-3.1 操縱組的介紹', '4-3.2 大腸桿菌乳糖操縱組的調控'],
    tags=['操縱組理論', '啟動子', '操作子', '調節蛋白', '誘導物', '可誘導型操縱組']),
   dict(code='4-4', title='遺傳變異', web='遺傳變異驛站', slug='ch4-4', vid='1odxtcA95NfoADAChEyBoGi8HG5Z6OyH_', pages='P.154–160',
    fig='s4-4', cap='圖 4－18　染色體結構改變的類型',
    intro='馬勒以 X 光照射果蠅誘發突變，證實環境因子可改變遺傳物質。染色體層次的變異包括數目變異（如唐氏症 47,+21、透納氏症、多倍體）與結構變異（缺失、重複、倒位、易位）；分子層次的點突變可分為緘默、無義與誤義突變，插入或缺失則可能造成框移突變，例如鐮形血球貧血症源自血紅素 β 鏈基因的一個鹼基被取代。婚前健康檢查、產前遺傳診斷與新生兒篩檢有助於預防與及早處置遺傳疾病。',
    subs=['4-4.1 染色體層次的變異', '4-4.2 分子層次的變異', '4-4.3 遺傳疾病篩檢的意義與重要性'],
    tags=['非整倍體與多倍體', '缺失・重複・倒位・易位', '點突變', '框移突變', '鐮形血球貧血症', '新生兒篩檢']),
  ], labs=[]),
 dict(n=5, title='遺傳學在生物科技的應用', en='Genetics in Biotechnology', a='#0284c7', a2='#38bdf8', t='#f0f9ff',
  lead='從發現限制酶開始，分子生物學陸續發展出重組 DNA、聚合酶連鎖反應（PCR）與基因轉殖等技術，進而邁入基因體時代。本章認識這些技術的原理與工具，討論基因轉殖在醫藥、環境與農業的應用及疑慮，並思考人類基因體資料帶來的福祉與倫理挑戰。',
  units=[
   dict(code='5-1', title='聚合酶連鎖反應', web='聚合酶連鎖反應驛站', slug='ch5-1', vid='1x84zbZM9bZH2ccBWYzCYoALCL2ziGijn', pages='P.164–166',
    fig='s5-1', cap='圖 5－2　聚合酶連鎖反應過程示意圖',
    intro='1983 年穆勒斯發明聚合酶連鎖反應（PCR），可在試管中快速擴增特定 DNA 片段。將目標 DNA、引子、四種去氧核糖核苷酸與 DNA 聚合酶放入熱循環儀，反覆進行三步驟：加熱至 93～97 °C 使雙股變性分開、降溫至 50～60 °C 讓引子黏合、再升溫由聚合酶延長新股，每一循環 DNA 量倍增。所用的 Taq 聚合酶來自溫泉中的水生棲熱菌，耐高溫；PCR 已成為病原體檢測等領域不可或缺的技術。',
    subs=['PCR 的原理與三個步驟', '知識補給站：PCR 的 DNA 聚合酶、DNA 膠體電泳'],
    tags=['變性・黏合・延長', '引子', 'Taq 聚合酶', '熱循環儀', '指數擴增', '膠體電泳']),
   dict(code='5-2', title='重組DNA技術', web='重組DNA技術驛站', slug='ch5-2', vid='13yOYFyzW8RSxoJcW0ayDuI2fAoa3aHvP', pages='P.167–169',
    fig='s5-2', cap='圖 5－4　質體作為載體與目標基因接合形成重組 DNA',
    intro='重組 DNA 技術需要三種關鍵工具：限制酶像剪刀，能辨認具迴文特性的特定序列並切開 DNA，例如 EcoRI 辨認 GAATTC 而切出黏端；DNA 連接酶以共價鍵把兩段 DNA 接起來；載體（常用細菌質體或病毒 DNA）則負責把目標基因送入宿主細胞，其上的抗生素抗性基因可用來篩選含重組 DNA 的細菌。',
    subs=['5-2.1 限制酶與 DNA 連接酶', '5-2.2 載體'],
    tags=['限制酶', '迴文序列', '黏端與平端', 'DNA 連接酶', '質體載體', '抗生素篩選']),
   dict(code='5-3', title='基因轉殖技術', web='基因轉殖技術驛站', slug='ch5-3', vid='1HoJ_HGfjI_wqhiR7VQbbHyuwrEfVk-gC', pages='P.170–175',
    fig='s5-3', cap='圖 5－5　農桿菌轉殖法',
    intro='把建構好的重組 DNA 送入生物體並表現目標基因，稱為基因轉殖。植物常用以 Ti 質體為載體的農桿菌轉殖法或基因槍，動物則多以顯微注射導入。基因轉殖可用於生產胰島素、生長激素等醫療蛋白質，以細菌分解原油整治汙染，並培育黃金米、抗除草劑大豆、抗蟲玉米等作物；但其食用安全與生態影響仍需長期追蹤。課本另補充 CRISPR 基因編輯與基因療法。',
    subs=['5-3.1 基因轉殖的原理', '5-3.2 基因轉殖的應用', '知識補給站：CRISPR 基因編輯、基因療法'],
    tags=['農桿菌 Ti 質體', '基因槍', '顯微注射', '醫療蛋白質', '黃金米', 'CRISPR']),
   dict(code='5-4', title='基因體時代', web='基因體時代驛站', slug='ch5-4', vid='1TDHny5OK4VRYaMfZ293ab51MAC6mbx8j', pages='P.176–177',
    fig='s5-4', cap='圖 5－10　人類基因體計畫的代表標誌',
    intro='基因體是生物細胞內單套 DNA 的總稱。人類基因體計畫於 1990 年啟動、2003 年完成大部分定序，確定人類基因體約有 30 億個鹼基對、可製造蛋白質的基因約 2 萬個。基因體資料有助於了解疾病成因、開發新藥與客製化醫療，但如何保護個人基因資料、規範政府與保險公司的使用，也是重要的倫理課題；而「基因」的定義也隨著新發現不斷演變。',
    subs=['5-4.1 人類基因體計畫', '5-4.2 人類基因體的應用', '知識補給站：基因概念的演變'],
    tags=['基因體', '人類基因體計畫', '30 億鹼基對', '客製化醫療', '基因資料隱私', '基因概念的演變']),
  ], labs=[]),
]

TOTAL_UNITS = sum(len(c['units']) for c in CHAPTERS)
TOTAL_LABS = sum(len(c['labs']) for c in CHAPTERS)

def url(u): return u['slug'] + '/'
def vurl(u): return DRIVE.format(u['vid'])

HEAD = '''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<link rel="icon" href="img/hanlin-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script>document.documentElement.classList.add('js')</script>
</head>
'''

FOOT = '''<footer class="foot">
  <div class="foot-in">
    <img src="img/hanlin-logo.png" alt="" width="34" height="34">
    <p>內容整理自翰林版高中《選修生物Ⅰ（全）》課本，簡介依課文重點改寫，圖片取自課本，僅供課堂教學使用。</p>
  </div>
</footer>
<div class="lightbox" id="lightbox" hidden>
  <button class="lb-close" aria-label="關閉">×</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>
<script src="app.js"></script>
</body>
</html>
'''

def chstyle(c): return f"--a:{c['a']};--a2:{c['a2']};--t:{c['t']}"

def build_index():
    o = [HEAD.format(title='翰林版 選修生物（Ⅰ）｜互動教學網站',
        desc=f'翰林版高中選修生物Ⅰ（全）五章 {TOTAL_UNITS} 節與 {TOTAL_LABS} 個探討活動的互動教學網頁與教學影片入口', theme='#0f766e')]
    o.append('''<body class="home">
<header class="hero">
  <svg class="globe" viewBox="0 0 600 600" aria-hidden="true">
    <g fill="none" stroke="currentColor" stroke-width="1.2">
      <path d="M220 10c160 70 160 150 0 220s-160 150 0 220 160 150 0 140M380 10c-160 70-160 150 0 220s160 150 0 220-160 150 0 140"/>
      <path d="M232 62h136M262 120h76M262 170h76M232 228h136M262 290h76M262 340h76M232 398h136M262 460h76M262 510h76" opacity=".7"/>
      <circle cx="300" cy="300" r="290" stroke-dasharray="10 8" opacity=".5"/>
    </g>
  </svg>
  <div class="hero-in">
    <img class="hero-logo" src="img/hanlin-logo-wide.png" alt="翰林出版 HAN LIN PUBLISHING" width="1240" height="324">
    <div class="hero-rule"><span></span><em>自然科學領域　加深加廣選修</em><span></span></div>
    <h1>選修生物（Ⅰ）<span>互動教學網站</span></h1>
    <p class="hero-sub">翰林版《選修生物Ⅰ（全）》· 從細胞的分子與生物膜、代謝與能量，到 DNA 的發現、遺傳訊息的表現與生物技術，每一節都有專屬的互動闖關網頁與教學影片</p>
    <ul class="stats">
''' + f'''      <li><b>5</b><span>章</span></li><li><b>{TOTAL_UNITS}</b><span>節正課</span></li><li><b>{TOTAL_LABS}</b><span>個探討活動</span></li><li><b>{TOTAL_UNITS+TOTAL_LABS}</b><span>個互動網頁</span></li>
    </ul>
  </div>
</header>
<main>
  <section class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">CHAPTERS</span><h2>選擇章節，開始探索</h2><p>點選章節封面進入章節，瀏覽每一節的課本概念圖、重點簡介與教學影片。</p></div>
    <div class="ch-grid">
''')
    for c in CHAPTERS:
        lis = ''.join(f"<li><span>{u['code']}</span>{E(u['title'])}</li>" for u in c['units'])
        meta = f"<span>{len(c['units'])} 節正課</span>" + (f"<span>{len(c['labs'])} 個探討活動</span>" if c['labs'] else '')
        o.append(f'''      <a class="ch-card reveal" href="chapter{c['n']}.html" style="{chstyle(c)}">
        <div class="ch-cover"><img src="img/cover{c['n']}.jpg" alt="第{c['n']}章 {c['title']} 章節封面" loading="lazy" width="900" height="1020"></div>
        <div class="ch-body">
          <div class="ch-kicker">CHAPTER 0{c['n']} · {c['en']}</div>
          <h2>第 {c['n']} 章　{c['title']}</h2>
          <ul class="ch-list">{lis}</ul>
          <div class="ch-meta">{meta}</div>
          <span class="ch-go">進入本章 {ICON_GO}</span>
        </div>
      </a>
''')
    o.append('''    </div>
  </section>
  <section class="wrap quick-wrap">
    <div class="sec-head reveal"><span class="eyebrow">QUICK ACCESS</span><h2>全部互動網頁快速入口</h2><p>老師上課或學生複習時，可直接開啟各節的互動教學網頁（另開新分頁）；教學影片請由章節頁進入。</p></div>
    <div class="quick">''')
    for c in CHAPTERS:
        o.append(f'<div class="qcol reveal" style="--a:{c["a"]};--t:{c["t"]}"><h3><b>{c["n"]}</b>{c["title"]}</h3>')
        for u in c['units']:
            o.append(f'<a target="_blank" rel="noopener" href="{url(u)}" class="q"><span class="q-code">{u["code"]}</span><span class="q-t">{E(u["web"])}<small>{E(u["title"])}</small></span>{ICON_OUT}</a>')
        for l in c['labs']:
            o.append(f'<a target="_blank" rel="noopener" href="{url(l)}" class="q q-lab"><span class="q-code">{l["code"].replace(" ","")}</span><span class="q-t">{E(l["web"])}<small>{E(l["title"])}</small></span>{ICON_OUT}</a>')
        o.append('</div>')
    o.append('''</div>
  </section>
</main>
''' + FOOT)
    return ''.join(o)

def nav(cur):
    return ''.join(f'<a href="chapter{c["n"]}.html" class="nav-ch{" on" if c["n"]==cur else ""}" style="--a:{c["a"]}"><b>{c["n"]}</b><span>{c["title"]}</span></a>' for c in CHAPTERS)

def figure(key, cap, cls='fig-btn'):
    return f'''<button class="{cls}" data-full="img/{key}.jpg" data-cap="{E(cap)}" aria-label="放大圖片：{E(cap)}">
          <img src="img/{key}.jpg" alt="{E(cap)}" loading="lazy" decoding="async"><span class="zoom">{ICON_ZOOM}放大</span>
        </button>'''

def build_chapter(c):
    n = c['n']
    o = [HEAD.format(title=f"第 {n} 章 {c['title']}｜翰林版 選修生物（Ⅰ）", desc=E(c['lead']), theme=c['a'])]
    jumps = ''.join(f'<a href="#u{u["code"]}"><b>{u["code"]}</b>{E(u["title"])}</a>' for u in c['units'])
    if c['labs']: jumps += f'<a href="#labs" class="j-lab"><b>探討</b>活動 × {len(c["labs"])}</a>'
    o.append(f'''<body class="chapter" style="{chstyle(c)}">
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="index.html" aria-label="回到首頁">
      <img src="img/hanlin-logo.png" alt="翰林出版" width="40" height="40">
      <span class="brand-t"><small>翰林版</small>選修生物（Ⅰ）</span>
    </a>
    <nav class="nav">{nav(n)}</nav>
  </div>
</header>
<header class="ch-hero">
  <div class="ch-hero-in">
    <div class="ch-hero-text">
      <div class="ch-kicker">CHAPTER 0{n} · {c['en']}</div>
      <h1><span class="big">{n}</span><span class="t">第 {n} 章<br><strong>{c['title']}</strong></span></h1>
      <p class="lead">{E(c['lead'])}</p>
      <div class="jump">{jumps}</div>
    </div>
    <div class="ch-hero-cover"><img src="img/cover{n}.jpg" alt="第 {n} 章 章節封面" width="900" height="1020"></div>
  </div>
</header>
<main class="wrap units">
''')
    from PIL import Image
    for i, u in enumerate(c['units']):
        iw, ih = Image.open(os.path.join(OUT, 'img', u['fig'] + '.jpg')).size
        wide = iw / ih >= 2.2
        subs = ''.join(f'<li>{E(s)}</li>' for s in u['subs'])
        tags = ''.join(f'<span>{E(t)}</span>' for t in u['tags'])
        o.append(f'''    <article class="unit reveal{' wide' if wide else (' flip' if i % 2 else '')}" id="u{u['code']}">
      <figure class="fig">
        {figure(u['fig'], u['cap'])}
        <figcaption>{E(u['cap'])}</figcaption>
      </figure>
      <div class="unit-body">
        <div class="unit-top"><span class="code">{u['code']}</span><span class="web-pill">互動網頁｜{E(u['web'])}</span><span class="pg-pill">{ICON_BOOK}課本 {u['pages']}</span></div>
        <h2>{E(u['title'])}</h2>
        <a class="intro" href="{url(u)}" target="_blank" rel="noopener" title="開啟「{E(u['web'])}」教學網頁">
          <p>{E(u['intro'])}</p>
          <span class="intro-hint">點選文字即可開啟教學網頁 {ICON_OUT}</span>
        </a>
        <div class="subs"><h3>本節重點</h3><ol>{subs}</ol></div>
        <div class="tags">{tags}</div>
        <div class="btn-row">
          <a class="btn" href="{url(u)}" target="_blank" rel="noopener">進入「{E(u['web'])}」{ICON_OUT}</a>
          <a class="btn ghost vid" href="{vurl(u)}" target="_blank" rel="noopener">{ICON_PLAY}教學影片</a>
        </div>
      </div>
    </article>
''')
    if c['labs']:
        one = ' one' if len(c['labs']) == 1 else ''
        o.append(f'''  <section class="labs" id="labs">
    <div class="sec-head reveal"><span class="eyebrow">HANDS-ON LAB</span><h2>探討活動</h2><p>動手操作、記錄變因與數據，把課文中的概念轉化為自己的實驗證據。</p></div>
    <div class="lab-grid{one}">
''')
        for l in c['labs']:
            o.append(f'''      <article class="lab reveal" id="{l['slug']}">
        {figure(l['fig'], l['cap'], 'lab-fig fig-btn')}
        <div class="lab-body">
          <div class="unit-top"><span class="code sm">{l['code']}</span><span class="web-pill">{E(l['web'])}</span><span class="pg-pill">{ICON_BOOK}課本 {l['pages']}</span></div>
          <h3>{E(l['title'])}</h3>
          <a class="intro" href="{url(l)}" target="_blank" rel="noopener"><p>{E(l['intro'])}</p><span class="intro-hint">開啟教學網頁 {ICON_OUT}</span></a>
          <div class="btn-row">
            <a class="btn ghost" href="{url(l)}" target="_blank" rel="noopener">進入「{E(l['web'])}」{ICON_OUT}</a>
            <a class="btn ghost vid" href="{vurl(l)}" target="_blank" rel="noopener">{ICON_PLAY}教學影片</a>
          </div>
        </div>
      </article>
''')
        o.append('    </div>\n  </section>\n')
    prev = f'<a class="pg" href="chapter{n-1}.html"><small>PREVIOUS</small>← 第 {n-1} 章　{CHAPTERS[n-2]["title"]}</a>' if n > 1 else '<a class="pg" href="index.html"><small>HOME</small>← 回首頁總覽</a>'
    nxt = f'<a class="pg next" href="chapter{n+1}.html"><small>NEXT CHAPTER</small>第 {n+1} 章　{CHAPTERS[n]["title"]} →</a>' if n < len(CHAPTERS) else '<a class="pg next" href="index.html"><small>HOME</small>回首頁總覽 →</a>'
    o.append(f'  <nav class="pager">\n    {prev}\n    {nxt}\n  </nav>\n</main>\n' + FOOT)
    return ''.join(o)

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(build_index())
for c in CHAPTERS:
    open(os.path.join(OUT, f'chapter{c["n"]}.html'), 'w', encoding='utf-8').write(build_chapter(c))
print('ok', TOTAL_UNITS, TOTAL_LABS)
