import cv2
import numpy as np
from PIL import Image, ImageDraw
import zxingcpp


class QR:

    def __init__(self) -> None:
        self.available_types = {i.lower(): eval(f'zxingcpp.BarcodeFormat.{i}')for i in list(zxingcpp.BarcodeFormat.__dict__["__entries"].keys())}
        self.linearcodes = ["code128", "codabar", "code39", "code93", "ean13", "ean8", "itf", "databar", "databarexpanded", "upca", "upce"]
        self.matrixcodes = ["aztec", "datamatrix", "maxicode", "pdf417", "qrcode", "microqrcode", "rmqrcode"]


    def get_possible_codes(self, text:str) -> list:
        
        avail_codes = []

        for i, j in self.available_types.items():
            try:
                zxingcpp.write_barcode(j, text.upper(), 64, 64)
                avail_codes.append(i.capitalize())
            
            except Exception as e:
                pass
                
        
        return avail_codes
    

    def generate(self, barcode_type:str, text:str, width:int= 64, height:int= 64, quiet_zone:int= -1, ec_level:int= -1) -> list:

        types = self.get_possible_codes(text)
        barcode_type = barcode_type.lower()

        if barcode_type.capitalize() not in types:
            raise ValueError(f"The given Barcode type does not supported. Available supported types are {', '.join(types)}.")
        
        out = zxingcpp.write_barcode(self.available_types[barcode_type], text.upper(), width, height, quiet_zone, ec_level)

        img = Image.fromarray(out)
        w, h = img.size[:2]
        pads = 20

        if barcode_type in ["pdf417", "qrcode"]:
            pads = 0
        
        padded_img = Image.new(img.mode, (w+pads, h+pads), 255)
        padded_img.paste(img, (pads//2, pads//2))

        location = (pads//2, pads//2, pads//2+w, pads//2+h)

        # draw = ImageDraw.Draw(pad)

        # ts= draw.textbbox((0,0), text=text, font_size=10)

        # pad.save(file_name, quality=100)

        return padded_img, location
        


    def locate(self, image:str|np.ndarray) -> list[dict]:

        if isinstance(image, str):
            image = cv2.imread(image)
        
        out = []
        results = zxingcpp.read_barcodes(image)
        
        for i in results:
            temp = {}
            temp["text"] = i.text
            temp["format"] = i.format.name
            temp["ec_level"] = i.ec_level
            temp["error"] = i.error
            temp["orientation"] = i.orientation
            temp["position"] = (i.position.top_left.x, i.position.top_left.y, i.position.bottom_right.x, i.position.bottom_right.y)
            temp["valid"] = i.valid
            out.append(temp)

        assert len(out) > 0, "No barcodes Found."

        return out





class Aruco_Marker:

    def __init__(self) -> None:
        self.available_markers = ["aruco", "charuco"]
        self.aurco_dict = {"4X4_50": cv2.aruco.DICT_4X4_50,
                            "4X4_100": cv2.aruco.DICT_4X4_100,
                            "4X4_250": cv2.aruco.DICT_4X4_250,
                            "4X4_1000": cv2.aruco.DICT_4X4_1000,
                            "5X5_50": cv2.aruco.DICT_5X5_50,
                            "5X5_100": cv2.aruco.DICT_5X5_100,
                            "5X5_250": cv2.aruco.DICT_5X5_250,
                            "5X5_1000": cv2.aruco.DICT_5X5_1000,
                            "6X6_50": cv2.aruco.DICT_6X6_50,
                            "6X6_100": cv2.aruco.DICT_6X6_100,
                            "6X6_250": cv2.aruco.DICT_6X6_250,
                            "6X6_1000": cv2.aruco.DICT_6X6_1000,
                            "7X7_50": cv2.aruco.DICT_7X7_50,
                            "7X7_100": cv2.aruco.DICT_7X7_100,
                            "7X7_250": cv2.aruco.DICT_7X7_250,
                            "7X7_1000": cv2.aruco.DICT_7X7_1000,
                            "ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
                            "APRILTAG_16H5": cv2.aruco.DICT_APRILTAG_16H5,
                            "APRILTAG_25H9": cv2.aruco.DICT_APRILTAG_25H9,
                            "APRILTAG_36H10": cv2.aruco.DICT_APRILTAG_36H10,
                            "APRILTAG_36H11": cv2.aruco.DICT_APRILTAG_36H11,
                            "MIP_36H12": cv2.aruco.DICT_ARUCO_MIP_36H12
                          }
        

    def get_available_marker_dict(self):
        return list(self.aurco_dict.keys())
    

    def generate(self, marker_dict:str="4x4_50", id:int=0, size:int=20) -> np.ndarray:

        avail_dict = self.get_available_marker_dict()

        if marker_dict.upper() not in avail_dict:
            raise ValueError(f"The given dict does not supported. Available supported dict are {', '.join(avail_dict)}.")
        
        tag = np.zeros((size, size, 1), dtype=np.uint8)
        blank = np.ones((size*2, size*2, 1), dtype=np.uint8)*255
        mark_dictonary = cv2.aruco.getPredefinedDictionary(self.aurco_dict[marker_dict.upper()])
        img = cv2.aruco.generateImageMarker(mark_dictonary, id, size, tag, 1)
        blank[size*2//4:(size*2//4)*3, size*2//4:(size*2//4)*3] = img
        
        return blank



    def locate(self, image:str|np.ndarray, marker_dict:str) -> list[tuple]:

        assert isinstance(marker_dict, str), "marker_dict must be a string."

        avail_dict = self.get_available_marker_dict()

        if marker_dict.upper() not in avail_dict:
            raise ValueError(f"The given dict does not supported. Available supported dict are {', '.join(avail_dict)}.")

        if isinstance(image, str):
            image = cv2.imread(image)
        
        aru_dictonary = cv2.aruco.getPredefinedDictionary(self.aurco_dict[marker_dict.upper()])
        aru_params = cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(aru_dictonary, aru_params)

        corners, ids, _ = detector.detectMarkers(image)
        
        out = []
        for corner, id in zip(corners,ids):
            x, y = corner[0].min(0)
            x1, y1 = corner[0].max(0)

            out.append({"location": (int(x),int(y),int(x1),int(y1)),
                        "id": int(id[0])
                        })
            
        return out





class Charuco_Marker(Aruco_Marker):

    def generate(self, marker_dict:str, square_vertical:int, square_horizontal:int, square_length:int,
                 marker_length:int, size: int, margin:int) -> np.ndarray:
 
        avail_dict = self.get_available_marker_dict()

        if marker_dict.upper() not in avail_dict:
            raise ValueError(f"The given dict does not supported. Available supported dict are {', '.join(avail_dict)}.")

        mark_dictonary = cv2.aruco.getPredefinedDictionary(self.aurco_dict[marker_dict.upper()])
        board = cv2.aruco.CharucoBoard((square_vertical, square_horizontal), square_length/1000, marker_length/1000, mark_dictonary)
        ratio = square_horizontal / square_vertical
        img = board.generateImage((size, int(size*ratio)), marginSize=margin)
        
        return img