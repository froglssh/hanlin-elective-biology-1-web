# 翰林版 選修生物（Ⅰ）互動教學網站

首頁 `index.html` → 五個章節頁 `chapter1.html`～`chapter5.html` → 各節互動教學網頁（GitHub Pages，另開新分頁）與教學影片（Google 雲端硬碟）。

## 🌐 線上發布與瀏覽說明
- **集合網站首頁**：[https://froglssh.github.io/hanlin-elective-biology-1-web/選修生物1教材網站/](https://froglssh.github.io/hanlin-elective-biology-1-web/選修生物1教材網站/)（根目錄亦提供自動轉向）
- **單元連結方式**：所有章節與探討活動皆採用相對路徑（`ch1-1/` 等），電腦本機離線開啟或於 GitHub Pages 線上瀏覽皆可直接暢順開啟，完全不依賴外部寫死的 GitHub 絕對路徑。

## 章節（依課本）
1. 細胞的構造與功能（1-1～1-4，活動 1-1、1-2）
2. 細胞的代謝與能量（2-1～2-3，活動 2-1、2-2）
3. 遺傳物質的發現與結構（3-1、3-2，活動 3-1）
4. 遺傳訊息的表現（4-1～4-4）
5. 遺傳學在生物科技的應用（5-1～5-4）

## 檔案結構
- `index.html`、`chapter1~5.html`：由 `build_site.py` 產生（簡介、本節重點、網址、影片連結都集中寫在該檔的 CHAPTERS 資料）
- `style.css`、`app.js`：共用樣式與互動（捲動淡入、圖片放大）
- `img/cover1~5.jpg`：章節封面（以課本圖合成）
- `img/s*.jpg`：各節課本代表圖；`img/a*.jpg`：探討活動課本圖

## 修改方式
編輯 `build_site.py` 的 CHAPTERS 後，在本資料夾執行 `python3 build_site.py .` 重新產生 HTML。
