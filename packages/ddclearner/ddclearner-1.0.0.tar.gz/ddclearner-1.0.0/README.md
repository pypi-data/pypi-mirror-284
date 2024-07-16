# housekeeper
## Overview
housekeeperはあなたのLaptoopを(見かけ上)綺麗にするPythonアプリケーションです。
~/Desktop, ~/Downloads配下に散らかった様々なファイルを拡張子ごとに仕分けて移動させます。

## 動作環境
* Python 3.x
* Rye

## インストール
```
$ rye install .
```

## 実行方法
デフォルトでは~/Desktop, ~/Downloads配下のファイルを仕分けますが、-dオプションで仕分けたいディレクトリを追加することも可能です。
```
$ housekeep
$ housekeep -d /hoge/fuga /foo/bar/baz
```

## Desclimer
* このスクリプトを実行すると、~/Desktop, ~/Downloadsならびにオプションで指定したディレクトリ配下のファイルをmvコマンドで移動させたような動きとなります。
* このスクリプトで起きたいかなる損害に対して、作成者は一切責任を負いませんので、ご理解の上ご利用ください。


## conf.yml
```
target_dir:   #仕分け元のディレクトリを指定します。
  - '~/Downloads'
  - '~/Desktop'
outdir: './'  #配置先のファイルを指定することが可能です。
exts:         #仕分けルールです。.csvで終わるファイルをcsvディレクトリに配置、ppt,pptxはpptディレクトリに配置します。こちらに定義を足すことでより様々なファイルを仕分けることができます。
  csv: csv
  dmg: dmg
  doc: doc
  drawio: drawio
  jpg: jpg
  jpeg: jpg
  json: json
  log: log
  m4a: m4a
  pdf: pdf
  png: png
  ppt: ppt
  pptx: ppt
  py: py
  txt: txt
  xls: xls
  xlsx: xls
  yaml: yml
  yml: yml
  zip: zip
  tar.gz : tar
  tgz : tar
  md: md
  other: other

```
