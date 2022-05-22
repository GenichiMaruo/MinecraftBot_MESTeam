# 公開可能なコードのみを集めました

```control.c```の```exePython()```によって```python/minecraft/aiDetector.py```と```python/minecraft/keyControl.py```がフォークされる

## aiDetector.py

```cv2.CascadeClassifier()```によって```self.cascade```としてインスタンス化する。
その後```self.cascade.detectMultiScale()```によってカスケードによって認識されたオブジェクトの存在する座標情報のリストが返却される。
これらのリストの内```w+h+y```が最も大きいオブジェクトの値が```wright_txt()```によって```tmp.txt```として書き出される。
認識したオブジェクトのサイズ(widthとheight)が大きく且つより手前に存在する(yが大きい)オブジェクトがより危険であると考えられるため```w+h+y```の値が大きいものを優先させた。

## keyControl.py

```control.txt```をreadモードで常時監視する。
前回取得した値から変更があった場合キー操作を行う。
カメラとキャラクターのそれぞれの動作の命令を受け付けて実行する。
カメラ操作はそれぞれmoveCameraの名前が付いたファイルに記述したクラスのインスタンス，
キャラクター操作はmoveCharacterの名前が付いたファイルに記述したクラスのインスタンスから操作している。
