# BTP

This code has 2 applications created 
1. Visualization of quasi random deployment.
To access this.


    1: use the main.py and input the neccessary values so that the device locations can be created and saved.

    2: after the inputs the file will be closed and 2 new text files will be created.
        a) Initial-deployment.txt - this file will be having all the information regarding the device locations for the devices which were deployed in the starting. 
        b) Live-status.txt - this file has all the current devices data and will be updated by other python files so the data can remain consistent according to the new devices which will be added or for the old devices which got damaged can be removed.

    3: Now we will be statring DDA.oy file which will show a window using matplotlib such that all the information of devices which are currently active or inactive can be seen. active devices will be blue in color, damaged devices will be red in color and redployed devices will be yellow in color.

    4: All the devices which are damaged can be replaced using 2 methods reploy-square.py and redply.triangle.py , to proceed with the re-deployment first start one of the python files and they will show all the possible places where redployment can be done and the file will be waiting for a input if the input is "y" then it will proceed with the redployment and will update the live-status file so that the DDA.py can update the changes and the data remains consistent.

    5: now we have shown all the points deployment , visualizaiton, redeployment (with multiple strategies) so this concludes the objective of the project.





2. visualization of sequential deployment for the same. 

To work with this we need to access the sequential.py file and input the factirs like number of devices and the grid dimention and with these the python code will start placing the devices on the grid on its own till all the devices are placed.



