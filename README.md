# flask_getBaZi---

title: 'flask_getBaZi'
disqus: hackmd

---

# flask_getBaZi

## Table of Contents

[TOC]

## Introducion

我媽媽需要拿來幫別人算命。

My mother needs to use it to help others with fortune telling.

之前有用過 python 配上 tkinter 用圖形化介面，但她不太會用電腦因此就用 flask 將其呈現在網頁上就能用手機使用。

Previously, I have used Python with tkinter to create a graphical user interface, but my mother is not very computer-savvy, so I used Flask to present it on the web, making it accessible through a mobile phone.

## Main Function

輸入資料 Input data

![](https://i.imgur.com/wcB8XbX.png)

確認資料 Check data

![](https://i.imgur.com/xT0qvex.png)

之後會透過爬蟲將資料丟到一個網站(https://myfate.herokuapp.com/)爬取資料後再新增更多自己寫的判斷，最後將其存成word再轉成pdf。

Then, the data will be crawled through a web scraper and added to a website (https://myfate.herokuapp.com/), after which additional custom determinations will be made and finally saved as a word file and converted to a pdf.

![](https://i.imgur.com/pVQNQCe.png)

![](https://i.imgur.com/pfRrzSP.png)

會將轉換過的檔案存在本地的資料夾中，所以在首頁有之前的檔案可以看。

It will save the converted file in a local folder, so there will be previous files available to view on the home page.

![](https://i.imgur.com/OXVmg9K.png)

點擊姓名可以查看之前的檔案，點擊信封可以裝其傳到我媽的信箱(這是之前沒有用 Flask 的時候寫的)，點擊叉叉就是將其刪除。

Clicking on the name allows you to view the previous files, clicking on the envelope can send it to my mother's E-mail (this was written before using Flask), and clicking on the X mark deletes it.
