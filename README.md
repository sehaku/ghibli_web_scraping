# ghibli_web_scraping

[スタジオジブリの公式サイト](http://www.ghibli.jp)からスタジオジブリ作品の場面写真を自動でダウンロードするスクレイピングスクリプト。  
保存先のハードディスクのパスを指定してダウンロードを開始します。

# 必要な環境

- python 実行環境
- BeautifulSoup(インストール方法 : pip3 install beautifulsoup4)
- requests(インストール方法 : pip3 install requests)

# ConnectionResetEroor

1 画像毎に 5 秒待機してダウンロード先のサーバに過負荷をかけたり、ConnectionResetError が出ないようにしていますが、  
もしエラーでダウンロードできなかったファイルがあった場合(ValueError と ConnectionResetError の場合は)
ダウンロード失敗したファイル名とエラー名の一覧を failed_file.log として保存先ディレクトリに作成します。
