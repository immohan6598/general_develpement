from __future__ import division
import os
import cv2

def cropAndCreateLabels(image_name, labels, image_number, output_path):
    cv2.namedWindow ('Current_Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty ('Current_Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.resizeWindow('Current_Image', 600,600)
    
    Image = cv2.imread(image_name)
    Image_Height = Image.shape[0]
    Image_Width = Image.shape[1]
    
    Image1 = Image[0:int(Image_Height/2), 0:int(Image_Width/2)]
    Image2 = Image[0:int(Image_Height/2),int(Image_Width/2):Image_Width]
    Image3 = Image[int(Image_Height/2):Image_Height, 0:int(Image_Width/2)]
    Image4 = Image[int(Image_Height/2):Image_Height, int(Image_Width/2):Image_Width]

    Display_Image = Image.copy()

    Resize_Width = Image1.shape[1]
    Resize_Height = Image1.shape[0]
    
    f = open(labels, "r")
    lines = f.readlines()
    f.close()
    f1 = open(output_path+image_number+"-1"+".txt","a+")
    f2 = open(output_path+image_number+"-2"+".txt","a+")
    f3 = open(output_path+image_number+"-3"+".txt","a+")
    f4 = open(output_path+image_number+"-4"+".txt","a+")

    for line in lines:
        label_data = line.split()
        class_name = label_data[0]
        label_center_x = int(float(label_data[1]) * Image_Width)
        label_center_y = int(float(label_data[2]) * Image_Height)
        label_width = int(float(label_data[3]) * Image_Width)
        label_height = int(float(label_data[4]) * Image_Height)
        
        if(label_center_x + int(label_width/2) < int(Image_Width/2) and label_center_y + int(label_height/2) < int(Image_Height/2)):
            
            output_image = cv2.rectangle(Display_Image,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (0,0,255), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)

            label_center_x = float(label_center_x / Resize_Width)
            label_center_y = float(label_center_y / Resize_Height)
            label_width = float(label_width / Resize_Width)
            label_height = float(label_height / Resize_Height)
            '''
            label_center_x = int(label_center_x * Resize_Width)
            label_center_y = int(label_center_y * Resize_Height)
            label_width = int(label_width * Resize_Width)
            label_height = int(label_height * Resize_Height)

            output_image = cv2.rectangle(Image1,(label_center_x - str(label_width/2), label_center_y - str(label_height/2)), (label_center_x + str(label_width/2), label_center_y + str(label_height/2)), (0,0,255), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            '''
            target_string = class_name + " " + str(label_center_x) + " " + str(label_center_y) + " " + str(label_width)+ " " + str(label_height)+"\n"
            #print(target_string)
            f1.write(target_string)
        
        if (label_center_x - int(label_width/2) > int(Image_Width/2) and label_center_y + int(label_height/2) < int(Image_Height/2)):
            
            output_image = cv2.rectangle(Display_Image,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (0,255,0), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            
            label_center_x = float((label_center_x - int(Image_Width/2)) / Resize_Width)
            label_center_y = float(label_center_y / Resize_Height)
            label_width = float(label_width / Resize_Width)
            label_height = float(label_height / Resize_Height)
            '''
            label_center_x = int(label_center_x * Resize_Width)
            label_center_y = int(label_center_y * Resize_Height)
            label_width = int(label_width * Resize_Width)
            label_height = int(label_height * Resize_Height)

            output_image = cv2.rectangle(Image2,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (0,255,0), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            '''
            target_string = class_name + " " + str(label_center_x) + " " + str(label_center_y) + " " + str(label_width)+ " " + str(label_height)+"\n"
            #print(target_string)
            f2.write(target_string)

        if (label_center_x + int(label_width/2) < int(Image_Width/2) and label_center_y - int(label_height/2) > int(Image_Height/2)):
            
            output_image = cv2.rectangle(Display_Image,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (255,0,0), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            
            label_center_x = float(label_center_x / Resize_Width)
            label_center_y = float((label_center_y - int(Image_Height/2)) / Resize_Height)
            label_width = float(label_width / Resize_Width)
            label_height = float(label_height / Resize_Height)
            '''
            label_center_x = int(label_center_x * Resize_Width)
            label_center_y = int(label_center_y * Resize_Height)
            label_width = int(label_width * Resize_Width)
            label_height = int(label_height * Resize_Height)

            output_image = cv2.rectangle(Image3,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (255,0,0), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            '''
            target_string = class_name + " " + str(label_center_x) + " " + str(label_center_y) + " " + str(label_width)+ " " + str(label_height)+"\n"
            #print(target_string)
            f3.write(target_string)

        if (label_center_x - int(label_width/2) > int(Image_Width/2) and label_center_y - int(label_height/2) > int(Image_Height/2)):
            
            output_image = cv2.rectangle(Display_Image,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (255,0,255), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            
            label_center_x = float((label_center_x - int(Image_Width/2)) / Resize_Width)
            label_center_y = float((label_center_y - int(Image_Height/2)) / Resize_Height)
            label_width = float(label_width / Resize_Width)
            label_height = float(label_height / Resize_Height)
            '''
            label_center_x = int(label_center_x * Resize_Width)
            label_center_y = int(label_center_y * Resize_Height)
            label_width = int(label_width * Resize_Width)
            label_height = int(label_height * Resize_Height)

            output_image = cv2.rectangle(Image4,(label_center_x - int(label_width/2), label_center_y - int(label_height/2)), (label_center_x + int(label_width/2), label_center_y + int(label_height/2)), (0,0,0), 7)
            cv2.imshow("Current_Image", output_image)
            cv2.waitKey(100)
            '''
            target_string = class_name + " " + str(label_center_x) + " " + str(label_center_y) + " " + str(label_width)+ " " + str(label_height)+"\n"
            #print(target_string)
            f4.write(target_string)  

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    cv2.imwrite(output_path+image_number+"-1.png", Image1)
    cv2.imwrite(output_path+image_number+"-2.png", Image2)
    cv2.imwrite(output_path+image_number+"-3.png", Image3)
    cv2.imwrite(output_path+image_number+"-4.png", Image4)

def readImageAndFile(Target_Image_Path, output_path):
    Files = os.listdir(Target_Image_Path)
    for i in (Files):
        if i.endswith(".png"):
            i_string = str(i).partition('.')
            image_path = Target_Image_Path+i_string[0]+".png"
            txt_file_path = Target_Image_Path+i_string[0]+".txt"
            cropAndCreateLabels(image_path, txt_file_path, i_string[0], output_path)
                    
if __name__ == '__main__':
    Target_Image_Path = "/home/mohan/nn/raw_handle_counting_deployment/Convert_label/Input/"
    Output_Path = "/home/mohan/nn/raw_handle_counting_deployment/Convert_label/Output/"
    readImageAndFile(Target_Image_Path, Output_Path)