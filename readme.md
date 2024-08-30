

--------------------
GENERAL INFORMATION
--------------------
Title of Dataset: CAPTIV8 - A comprehensive large scale CAPsule endoscopy dataset for Integrated diagnosis 
Available for download here : https://dataverse.no/dataset.xhtml?persistentId=doi:10.18710/BSXNA1.

Description of dataset: 
General description and ethics approvals:   The dataset contains images and videos of wireless capsule endoscopic examinations of 10 patients conducted using the PillCAM colon 2 capsule manufactured by 
											Medtronic. In addition, it includes alphanumeric metadata comprising of diagnostic summaries from colonoscopy and histopathology reports.
											The examinations were conducted in 2021 at the Innlandet Hospital Trust, Gjøvik (Norway) with confirmed patients of ulcerative colitis.
											All patients gave written informed consent and ethical approvals to publish the anonymized image, video and text data were obtained from 
											the director of medicine and health at Innlandet Hospital Trust in 2021.
											Patient information was not linked to the study to 
											preseve anonymity and pseudo IDs were assigned instead. The patients underwent capsule endoscopy examination on the first day 
											followed by a colonoscopy the next day. Tissue samples were retrieved during colonoscopy from different bowel segments 
											and sent for histopathology. The histopathology report corresponds to 5 sections of the colon numbered 1 to 5, these can be interpreted as such :
											1:coecum/ascending 2: transverse 3: descending, 4: sigmoid, 5 rectum. The images and videos corresponding to each patient is in a separate folder with 
											name same as the pseudoID. 
											The pseudoID can be used to find the corresponding diagnostic metadata and image and video descriptions in the provided excel sheets.
									

---------------------
DATA & FILE OVERVIEW
---------------------
1. File List: 
00_README.txt
Frames_and_videos.zip
PillCam_calibration_data.zip
CAPTIV8_diagnostic_data_csv.zip
CAPTIV8_meta_frame_video_csv.zip
CAPTIV8_diagnostic_data.xlsx
CAPTIV8_meta_frame_video.xlsx



2. Relationship between files, if important: 

- CAPTIV8_diagnostic_data.xlsx : the diagnostic metadata including colonoscopy, histology and capsule diagnosis for each patient. The excel has 10 sheets each corresponding to one patient.
								 The attribute significant findings corresponds to the number of images and videos for this patient to be found in the Frames_and_videos/P00*/Files folder and abnormality descriptions in the the CAPTIV8_meta_frame_video.xlsx file.
- CAPTIV8_meta_frame_video.xlsx : the corresponding image-paths, video-paths and labels for each patient. As before the excel has 10 sheets each corresponding to one patient.
- CAPTIV8_diagnostic_data_csv.zip : Same as CAPTIV8_meta_frame_video.xlsx, but in csv format, the excel is for better visualization and csv for ease of use and compatibility.
-CAPTIV8_meta_frame_video_csv.zip : Same as CAPTIV8_diagnostic_data.xlsx, but in csv format,  the excel is for better visualization and csv for ease of use and compatibility.
- Frames_and_videos/P00*/Files : The actual images and videos as described in CAPTIV8_meta_frame_video. 
- PillCam_calibration_data.zip : The images and videos of the color checker and checkerboard captured for radiometric and geometric caliberation of PillCam camera.


3. Is this a new version of a previously published dataset? no

---------------------------
METHODOLOGICAL INFORMATION
---------------------------
1. Description of sources and methods used for collection/generation of data:

Annotation procedures :
The annotations were performed by experienced gastroenetrologist in the software Rapid reader. Clean and representative normal as well as abnormal frames were selected in the video and a 
text describing the images was written corresponding to the images. Finally a short video segment of approximately 150 frames each was extracted around each of these normal/abnormal images. 
The video can be assumed to carry the same weak-label as the frame. Certain video fragments have been cut to be shorter than 150 frames intentionally to prevent accidental identification pre or post capsule ingestion.


PillCAM camera caliberation Experimental Setup :
The images of the ColorChecker and checker board were captured prior to the PillCam ingestion. Upon unpacking the WCE, it was connected to its recorder and then placed onto the stand. 
The ColorChecker was positioned in front of the camera, and the black box was covered with a black cloth to prevent external light interference with the PillCam light during the ColorChecker 
image capture. The same procedure was followed for capturing images of light/dark grey targets. Subsequently, images of the checker board (Dimension: 15x12, Square size: 4cm) 
were captured using the 2nd camera of the PillCam. During the checker board capture, the orientation was varied at different angles to ensure that the PillCam could capture a range of 
perspectives, thereby facilitating a comprehensive calibration process.
