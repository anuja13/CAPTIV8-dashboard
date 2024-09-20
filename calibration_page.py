import streamlit as st
import pandas as pd
import os

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
</style>
"""


st.title('CAPTIV8 - A comprehensive large scale CAPsule endoscopy dataset for Integrated diagnosis')

st.markdown("<h4>Calibration Setup</h4> The PillCam introduces significant distortions. \
            This is mainly geometric distortion from the wide-angle lens as well as \
            compression artifacts and distortion in color reproduction. Further, technical specification like \
            intrinsic parameters as well as details on the image processing chain, \
            is not provided by the manufacturer. For many applications, it is therefore \
            essential to conduct both geometric- and radiometric calibration.", unsafe_allow_html=True)

st.markdown("In our dataset, there are captures of a ColorChecker and a checkerboard.\
            <ul><li> The ColorChecker provides a reference for color correction, aiding in better \
            color reproduction in GI images. </li> </ul> <ul><li> The checkerboard can aid in geometric calibration, reducing geometric distortion in images and thereby ensuring \
                accurate spatial relationships, and help estimate the cameras intrinsic parameters </li> </ul>",unsafe_allow_html=True)

st.markdown("To facilitate this, the setup shown below was used. One camera was used for the ColorChecker and the other for the\
            checkerboard. To make sure that the ColorChecker was lit \
            solely by the PillCam’s light source, the box in (a) was covered with black absorbing material and sealed, minimizing the influence of ambient light.")


st.image(image="data/Picture1.svg", caption="(a) PillCam camera calibration setup: 1. black cloth \
         2. box with light absorbing material \
         3. ColorChecker 4. PillCam stand 5. checkerboard. \
         (b) Capture of the ColorChecker \
         (c) Capture of the checkerboard.", width=800)




