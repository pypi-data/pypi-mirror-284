import os
import cv2
import json
import numpy as np

from cm_generator.generator import QR as __QR
from cm_generator.generator import Aruco_Marker as __Aruco_Marker
from cm_generator.generator import Charuco_Marker as __Charuco_Marker


__qr_obj = __QR()
__aru_obj = __Aruco_Marker()
__char_obj = __Charuco_Marker()


def get_code_marker() -> tuple:

    codes = __qr_obj.available_types.keys()
    markers = __aru_obj.available_markers

    return codes, markers




def QR_gen(barcode_type:str, text:str, width:int= 64, height:int= 64, quiet_zone:int= -1, ec_level:int= -1,
           destination:str= ".", file_name:str= "my_code.png", location:bool=False, save:bool=True) -> tuple|np.ndarray|None:
    try:
        assert isinstance(barcode_type, str), "barcode_type must be a string."
        assert isinstance(text, str), "text must be a string."
        assert isinstance(width, int) and width > 0, "width must be an integer and greater than 0."
        assert isinstance(height, int) and height > 0, "height must be an integer and greater than 0."
        assert isinstance(quiet_zone, int) and (quiet_zone == -1 or quiet_zone > 0), "quiet_zone must be an integer and it is must be -1 or greater than 0."
        assert isinstance(ec_level, int) and (ec_level == -1 or ec_level > 0), "ec_level must be an integer and it is must be -1 or greater than 0."
        assert isinstance(destination, str) and os.path.exists(destination), "destination must be a string and exists."
        assert isinstance(file_name, str) and os.path.splitext(file_name)[-1] != "", "file_name must be a string and it must be a name of the file with extension/format."
        assert os.path.splitext(file_name)[-1] in [".png", ".jpg"], "file_name extension must be either 'png' or 'jpg'."
        assert isinstance(location, bool), "location must be True or False."
        assert isinstance(save, bool), "save mmust be True or False."

        if os.path.splitext(file_name)[0] == "my":
            file_name = "my_code"+os.path.splitext(file_name)[-1]
        
        img, loc = __qr_obj.generate(barcode_type, text, width, height, quiet_zone, ec_level)

        if save:
            img.save(os.path.join(destination,file_name), quality=100)

            if location:
                with open(os.path.join(destination, os.path.splitext(file_name)[0]+".txt"), "w+") as f:
                    f.write(", ".join([str(i) for i in loc]))
        
        else:
            if location:
                return (img, loc)
            
            return img
    
    except (ValueError, AssertionError, Exception) as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()




def QR_loc(image:str|np.ndarray, save:bool=False, destination:str= ".", file_name:str= "my_code") -> list|None:

    try:
        assert isinstance(image, (str, np.ndarray)), "image must be a string or numpy array."
        assert isinstance(save, bool), "save mmust be True or False."
        assert isinstance(destination, str) and os.path.exists(destination), "destination must be a string and exists."
        assert isinstance(file_name, str) and os.path.splitext(file_name)[-1] == "", "file_name must be a string and it must be a name of the file without extension/format."
        

        res = __qr_obj.locate(image)

        if save:
            if file_name == "my":
                file_name = "my_code"
            
            with open(os.path.join(destination, file_name+".json"), "w+") as f:
                json.dump(res, f)
                
        else:
            return res

    except (AssertionError, Exception) as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()




def aru_gen(marker_dict:str="4x4_50", id:int=0, size:int=20,
            destination:str= ".", file_name:str= "my_marker.png", save:bool=True) -> np.ndarray|None:

    try:
        assert isinstance(marker_dict, str), "marker_dict must be a string."
        assert isinstance(id, int) and id >= 0, "id must be an integer and greater than or equal to 0."
        assert isinstance(size, int) and size > 14, "size must be an integer and greater than 14."
        assert isinstance(destination, str) and os.path.exists(destination), "destination must be a string and exists."
        assert isinstance(file_name, str) and os.path.splitext(file_name)[-1] != "", "file_name must be a string and it must be a name of the file with extension/format."
        assert os.path.splitext(file_name)[-1] in [".png", ".jpg"], "file_name extension must be either 'png' or 'jpg'."
        assert isinstance(save, bool), "save mmust be True or False."

        if os.path.splitext(file_name)[0] == "my":
            file_name = "my_aruco"+os.path.splitext(file_name)[-1]

        img = __aru_obj.generate(marker_dict, id, size)

        if save:
            cv2.imwrite(os.path.join(destination, file_name), img)
        
        else:
            return img


    except (AssertionError, Exception) as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()
        



def aru_loc(image:str|np.ndarray, marker_dict:str="4x4_50", save:bool=False,
            destination:str= ".", file_name:str= "my_marker") -> list|None:

    try:
        assert isinstance(image, (str, np.ndarray)), "image must be a string or numpy array."
        assert isinstance(marker_dict, str), "marker_id must be a string."
        assert isinstance(save, bool), "save mmust be True or False."
        assert isinstance(destination, str) and os.path.exists(destination), "destination must be a string and exists."
        assert isinstance(file_name, str) and os.path.splitext(file_name)[-1] == "", "file_name must be a string and it must be a name of the file without extension/format."

        res = __aru_obj.locate(image, marker_dict)

        if save:
            if file_name == "my":
                file_name = "my_marker"
            
            with open(os.path.join(destination, file_name+".json"), "w+") as f:
                json.dump(res, f)
        
        else:
            return res
    
    except (AssertionError, Exception) as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()




def charu_gen(marker_dict:str="4x4_1000", square_vertical:int=5, square_horizontal:int=7, square_length:int=30,
              marker_length:int=15, size:int=640, margin:int=1, destination:str= ".",
              file_name:str= "my_charuco.png", save:bool=True) -> np.ndarray|None:
    
    try:
        assert isinstance(marker_dict, str), "marker_dict must be a string."
        assert isinstance(square_vertical, int) and square_vertical > 2, "square_vertical must be an integer and greater than 2."
        assert isinstance(square_horizontal, int) and square_horizontal > 2, "square_horizontal must be an integer and greater than 2."
        assert isinstance(square_length, int) and square_length > 29, "square_length must be an integer and greater than 29."
        assert isinstance(marker_length, int) and marker_length > 14, "marker_length must be an integer and greater than 14."

        min_size = int((((square_vertical*((11+11+margin)/2)))+(2*(square_vertical/square_horizontal)*margin)))

        assert isinstance(size, int) and size >= min_size, f"size must be an integer and greater than {min_size}."
        assert isinstance(margin, int) and margin >= 0, "margin must be an integer and greater than 0."
        assert square_length - marker_length >= 2, "square_length must be greater than marker_length by 2."


        if os.path.splitext(file_name)[0] == "my":
            file_name = "my_charuco"+os.path.splitext(file_name)[-1]

        
        img = __char_obj.generate(marker_dict, square_vertical, square_horizontal, square_length, marker_length,
                                  size, margin)
        
        if save:
            cv2.imwrite(os.path.join(destination, file_name), img)
        
        else:
            return img
    
    except (AssertionError, Exception) as e:
        print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
        exit()