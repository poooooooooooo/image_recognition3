# image_recognition3
pythonでOpenCV,GUIを用いて明るさ調整,フィルタリング,色調変更の処理を行う.

実行環境
windows10

python  3.6.4

opencv  3.4.1

numpy   1.14.0
# gamma変換による明るさ調整
以下のコードによりトラックバーから取得した値に0.1を掛け変化量を小さくする.
gammaが0の時は後の計算に除算が発生するので0.1とする.
```python
    gamma=cv2.getTrackbarPos('value','image')*0.1
    if gamma == 0:
        gamma = 0.1
```
ルックアップテーブルを用い取得した値をガンマ変換していく.
```python
    LUT=np.zeros((256,1),dtype='uint8')
    for i in range(256):
        LUT[i][0] = 255*pow(float(i)/255,1.0/gamma)

    frame = cv2.LUT(frame,LUT)
```
# ガウシアンフィルタ
トラックバーから取得した値をOpenCVを用いてフィルタリングする.
```python
    v = cv2.getTrackbarPos('filt','image')
    frame = cv2.GaussianBlur(frame,(25,25),v)
```
# 色調変化
トラックバーから取得した値をそれぞれ100で除算することで値の割合を得る.
```python
    r = cv2.getTrackbarPos('R','image')/100
    g = cv2.getTrackbarPos('G','image')/100
    b = cv2.getTrackbarPos('B','image')/100
```
読み込んだ画像を255で除算し(float)で計算できるようにしている.
```python
    frame = frame/255
```
それぞれの色に割合をかけることで色調を変化させている.
```python
    frame[:,:,2] *= r
    frame[:,:,1] *= g
    frame[:,:,0] *= b
```
# 以下に実行した動画のURLを示す.
https://youtu.be/OdvkL3-nNHs

# 参考文献
【OpenCV】【Python】ルックアップテーブルでガンマ補正 https://qiita.com/Kazuhito/items/c43e96ab16f400a35721
Python OpenCV3でGaussianオペレータを使って平滑化 https://www.blog.umentu.work/python-opencv3%E3%81%A7gaussian%E3%82%AA%E3%83%9A%E3%83%AC%E3%83%BC%E3%82%BF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E5%B9%B3%E6%BB%91%E5%8C%96/

OpenCV(Python)GUI基礎編　https://www.tech-tech.xyz/archives/3137782.html
