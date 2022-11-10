# ibl-viz
Gallery of visualizations and associated code

Large files are stored here: https://drive.google.com/drive/u/3/folders/1vVH-ExXi-P-Ef3K76GXL61BALRevD1Fb

## Visualizations and links

### IBL Data Portal

[IBL Data Portal](https://viz.internationalbrainlab.org/): website showing summary plots from a subset of the brain wide map and reproducible ephys sessions.

### Brain Wide Map
 - [IBL Average Trial Video](https://drive.google.com/file/d/1OeHbw3R4_wUfF_nC1iZWvDT-JQIzdjsQ/view?usp=sharing): Trials are averaged by linear time-warping between trial start, stim on, first wheel move, feedback, and trial end to match a fixed trial template. Averaging was performed for all sessions splits by trial type (4 trial types: correct/incorrect and stim left/right), contrast is ignored. QC passing clusters are included from all Brain Wide Map sessions. Firing rates are baselined and then normalized to percent signal change by dividing by the baseline firing rate and mapped to the transparency and scale of the dots. Last updated 2022-06. Visualization created by Kai Nylund.

<p float="left">
 <a href="https://youtu.be/PgXjZJ4mI1s"><img src="https://img.youtube.com/vi/PgXjZJ4mI1s/maxresdefault.jpg" width="35%"></a>
</p>

 - [IBL Average Trial **VR Demo**](https://drive.google.com/file/d/1AG8KU2BSAe3iSc4msTLbfQW9Faaof-2A/view?usp=share_link): Same as above, but a virtual reality experience in which you get to see the IBL experiment from a first person point of view. Last updated 2022-11. Visualization created by Dan Birman w/ help from Mayo Faulkner, original data scripts from Kai Nylund.

<p float="left">
 <a href="https://youtu.be/kcBHoQBtzZE"><img src="https://img.youtube.com/vi/kcBHoQBtzZE/maxresdefault.jpg" width="35%"></a>
</p>
 
 - [IBL Average Trial Neuron Viewer](https://drive.google.com/file/d/1Iw5ENIheBoSuD5pJzozvjASN-N7PDnM4/view?usp=share_link): Same as above, displays the average firing rates of neurons in the "average" IBL trial. This version is an interactive 3D Tool that lets you explore a few datasets (average trial or PSTH relative to stim on/wheel/feedback) and compare baselined data against the raw spiking. Last updated 2022-11.

<p float="left">
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/NeuronViewer.png" width="35%"> 
</p>

 - Insertion coverage [axial](https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_axial.png) [angled](https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_angled.png) [clusters](https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_good_coverage.png): Last updated 2022-11.
 
<p float="left">
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_axial.png" width="25%"> 
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_angled.png" width="25%"> 
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_good_coverage.png" width="25%"> 
</p>
 
 - [Coverage volume](https://drive.google.com/file/d/18T2Du1aTtwRnukFWp6dQnGKvZmJL6PWX/view?usp=sharing): Yellow = one insertion, Green = two. Last updated 2022-06.
 - [Insertions by Lab](https://github.com/int-brain-lab/website/raw/main/static/images/labs.mp4) or as a [gif](https://github.com/int-brain-lab/website/raw/main/static/images/labs.gif): Last updated 2022-09.
 
<p float="left">
 <img src="https://github.com/int-brain-lab/website/raw/main/static/images/labs.gif" width="35%"> 
</p>

 - [Examples of BWM block prior decoding results](https://github.com/int-brain-lab/ibl-viz/blob/main/bwm/bwm_block_prior_example.ipynb): Left side is the accuracy of decoding, right side is the proportion of areas with p-values < 0.05. Last updated 2022-06.
 
<p float="left">
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_block_prior_accuracydecoding.png" width="35%"> 
 <img src="https://github.com/int-brain-lab/ibl-viz/raw/main/gallery/bwm_block_prior_percpvallt05.png" width="35%"> 
</p>

### Reproducible Ephys
 - [Repeated site coverage](https://drive.google.com/file/d/1Pt0-Etdq__t7IkGY-jFXnEhLXli4eSau/view?usp=sharing): Insertions taken from the histology positions, before sub-selecting for insertions that hit 2+ areas.

## Credit

The visualizations here were built by the IBL Visualization working group: Dan Birman, Mayo Faulkner, and Cyrille Rossant with help from Kai Nylund and the IBL staff in particular Gaelle Chapuis and Olivier Winter. 
