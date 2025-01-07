# Lunar rover autonomous driving
## 1.Data prepare
- Convert 2C to general image format
```
python 2c_to_img.py
```
- labelme obstacle labeling
- Convert annotated images into binary images
- Convert binary image to bird's eye view
```
python aeriel_view.py
python dom_transform.py
```
## 2.path planning
```
python Astar.py
```



