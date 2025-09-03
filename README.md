# CGnetsw-Patch
A simple Python script for IDA to solve the inconvenience caused by network disconnection during the use of CGnetsw.exe application. Using C language for file reading and writing patch doesn’t seem to be as compatible with every version, while the IDA Python script appears to be a better choice.

## Use guide


Select Script from the menu bar in IDA.

<img width="1129" height="630" alt="image-20250903215430994" src="https://github.com/user-attachments/assets/8b709554-32f0-4d2a-8d85-c172a3580c9e" />


Remember to choose python

<img width="1110" height="505" alt="image-20250903215524233" src="https://github.com/user-attachments/assets/6a215b45-b84e-416e-988b-2f18fdf1878c" />


After pasting the script here, execute it and wait until the prompt 'patch done!' appears in the lower left corner.

<img width="537" height="183" alt="image-20250903215754366" src="https://github.com/user-attachments/assets/ac8bcd5a-172d-401e-9f3d-2a0047573167" />


Finally, save our changes.(The saving methods of different versions of IDA may vary, please explore on your own.)


<img width="1120" height="1236" alt="image-20250903215846559" src="https://github.com/user-attachments/assets/cbef4e00-e8f7-48e7-a063-dfdd143f689f" />


Now, you can run CGnetsw to complete the exam with peace of mind, without worrying about the inconveniences caused by a network disconnection!
