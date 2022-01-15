# AI_sense_by_Hazel_n_Igor

The **AI_sense_by_Hazel_n_Igor** repository is a workspace for portfolio project of **Hazel Wat** and **Igor Isaev**. The work on the project was done during the classes of Data Science Retreat in 2021 (Batch 28).

This repository is forked on https://github.com/igivis7/ and https://github.com/hahahazel to reflect the work of all contributors.



---

- What is the project about
- how to see some live demo via streamlit
- what hardware is needed
- how to run the code
  - list of codes w description
- features of the project
- future plans and possible upgrade

---
### About the project

This project was dedicated to apply our newly gained knowledge of data science on a real-world task. 

As the object of study we decided to take [Grove multichannel Gas Sensor V2](https://wiki.seeedstudio.com/Grove-Multichannel-Gas-Sensor-V2/) (GGSv2) sensor and by implementation of Machine Learning solve an odor recognition task.

During the project we have practiced building of DS project from scratch, mastered our ML skills and learned ways to overcome problems. 

The GGSv2 sensor consists of 4 measurement heads for measuring Nitrogen dioxide (NO2), Carbon monoxide (CO), Ethyl alcohol (C2H5OH) and Volatile organic compounds (VOCs). 
Each head is an [metal oxide semiconductor gas detector](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7700484/) made to measure a certain gas molecule.
The combination of the 4 readings allows to detect and distinguish different odors.
The GGSv2 sensor can be used together with Arduino boards, [WIO terminal](https://www.seeedstudio.com/Wio-Terminal-p-4509.html), Raspberry Pi or any other device that is able to work with I2C communication protocol.

To make classification of odors a fully connected neural network was implemented.

The live demo(with precollected samples), code description, project features, hardware list and possible upgrades are listed below.


### Live demo

The demo of the project can be found on streamlit service by the following link.

---

- initially we used edge impulse to collect and train
- but later we faced problems with the project and wanted to try diverse options of the the data manipulation to fix it
- this project shows out attempt of odor detector realization with help of Arduino.
---

## How to make it running.

Here is an instruction to make you copy of the project running.
There a few steps to create a device that is able to detect and distinguish odors:
  - Step_0. 
    - 0.1. The 1st and the most obvious: get an Arduino, Gas Sensor, HDT Sensor, and supplementary parts to combine it.
    - 0.2. Assemble according to a scheme [__!__ ref to image and description].
    - 0.3. Upload firmware [__!__ file_name] to Arduino.
    - 0.4. Preheat the GGSv2 (depending on the status of the sensor the preheating process might take up **72 hours!!!**)
  - Step_1. Collect and save data for all samples with script [__!__ script name]  <!-- Double space at the end of the line to make line-break -->  
  *Take care of*:
    - Before running the script please check the folder where the data will be saved
    - Check the saved files on the bad-formatted data [__=!=__ explain what is bad-formatted data].
  - Step_2. Train the Neural Network with script [__!__ script name]  
    - Check the name of the model and the place where the model will be saved


---




DRS28_Hazel_n_Igor_portfolio_project

The following people contributed equally to this repository (in alphabetical order):

- Igor Isaev
- Hazel Wat


## Environment for the project
1. `conda create -n pyAIsense python=3.9.7`
2. `conda activate pyAIsense`
3. `pip install ipykernel`
4. `python -m ipykernel install --user --name pyAIsense --display-name "pyAIsense_env"`
5. `pip3 install -r requirements_AIsense.txt`
6. `jupyter-notebook`
