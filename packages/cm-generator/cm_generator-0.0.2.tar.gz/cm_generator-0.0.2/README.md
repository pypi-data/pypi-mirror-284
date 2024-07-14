# Code and Marker Generator

This project aim is to generate codes and markers of 1d, 2d, Aruco and Charuco markers.

## Installation
### PIP
```
pip install cm-generator
```
### From Source
First, Clone the repository,
```
git clone git@github.com:code63ReaPer/CM-Generator.git
```

Next, Install it using pip,
```
cd CM-Generator
pip install -v -e .
```


## Usage
### CLI

To generate QR Code run the below code,
```
cmgen generate qrcode --text "hi hello" --width 64 --height 64 --name my_qr.png
```

To generate Aruco marker,
```
cmgen generate aruco --m-dict 5x5_100 --id 45 --size 30
```

To generate Charuco marker,
```
cmgen generate charuco --m-dict 5x5_1000 --s-vert 5 --s-horz 7 --size 640
```

To locate codes in the image,
```
cmgen locate code my_qr.png --save
```

To locate marker in the image,
```
cmgen locate marker my_marker.png --m-dict 5x5_1000 --save
```



### Python

To generate codes using python,
```
from cm_generator import handler

img = handler.QR_gen("qrcode", "hi hello", save=False)

img.save("my_qr.png")
```

To generate Aruco marker using python,
```
import cv2
from cm_generator import handler

img = handler.aru_gen(marker_dict="5x5_100", id=25, save=False)

cv2.imwrite("my_qr.png", img)
```

To generate Charuco marker using python,
```
import cv2
from cm_generator import handler

img = handler.charu_gen(marker_dict="5x5_100", square_vertical=5, square_horizontal=7, square_length=30, marker_length=15, save=False)

cv2.imwrite("my_qr.png", img)
```

To locate codes using python,
```
from cm_generator import handler

res = handler.QR_loc("my_qr.png")
print(res)
```

To locate Aruco marker using python,
```
from cm_generator import handler

res = handler.aru_loc("my_marker.png, marker_dict="5x5_1000")
print(res)
```


## LICENSE

This project is licensed under AFFERO GENERAL PUBLIC LICENSE (AGPL-3) license. See the LICENSE file for details.






