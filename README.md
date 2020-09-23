# ghibli_web_scraping
[スタジオジブリの公式サイト](http://www.ghibli.jp)からスタジオジブリ作品の場面写真を自動でダウンロードするスクレイピングスクリプト。  
保存先のハードディスクのパスを指定してダウンロードを開始します。  

# 必要な環境
* python実行環境
* BeautifulSoup(インストール方法 : pip install beautifulsoup4)
* requests(インストール方法 : pip install requests)

# ConnectionResetEroor
1画像毎に5秒待機してダウンロード先のサーバに過負荷をかけたり、ConnectionResetErrorが出ないようにしていますが、  
もしエラーでダウンロードできなかったファイルがあった場合(ValueErrorとConnectionResetErrorの場合は)
ダウンロード失敗したファイル名とエラー名の一覧をfailed_file.logとして保存先ディレクトリに作成します。
