# CGnetsw-Patch
A Python script for IDA to solve the inconvenience caused by network disconnection during the use of CGnetsw.exe application. Using C language for file reading and writing patch doesn’t seem to be as compatible with every version, while the IDA Python script appears to be a better choice.

## Use guide


Select Script from the menu bar in IDA.

![image-20250903215430994](./images/image-20250903215430994.png)

Remember to choose python

![image-20250903215524233](./images/image-20250903215524233.png)

After pasting the script here, execute it and wait until the prompt 'patch done!' appears in the lower left corner.

![image-20250903215754366](./images/image-20250903215754366.png)

Finally, save our changes.(The saving methods of different versions of IDA may vary, please explore on your own.)



![image-20250903215846559](./images/image-20250903215846559.png)

Now, you can run CGnetsw to complete the exam with peace of mind, without worrying about the inconveniences caused by a network disconnection!
