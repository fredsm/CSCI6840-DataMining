# MSNET
This repository contains the code and models for the following WACV'21 paper:

**[MSNet: A Multilevel Instance Segmentation Network for Natural Disaster Damage Assessment in Aerial Videos](https://arxiv.org/abs/2006.16479)** 
# The ISBDA Dataset

+ Download links: [Google Drive](https://drive.google.com/file/d/1kEKJ8kr1aScXz_1El7Mn-Yi0ANducQIW/view?usp=sharing)

+ The dataset has 1,030 images with 2,961 annotations. Each annotation includes the damage segmentation, damage bounding boxes, and house bounding boxes. 

## License
Our dataset, code, and models are only for [ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY](https://docs.google.com/document/d/1NdtHv8v9DulB_7BJpixWlcdXxouOeLRw/edit?usp=sharing&ouid=108800150781554114249&rtpof=true&sd=true).


## Acknowledgements
Our MSNet is based on [Tensorpack](https://github.com/tensorpack/tensorpack/tree/master/examples/FasterRCNN).



# ABCD dataset

ABCD (AIST Building Change Detection) dataset is a new labeled dataset, specially geared toward constructing and evaluating damage detection systems to identify whether buildings have been washed-away by tsunami.  

The paper:  
**Aito Fujita, Ken Sakurada, Tomoyuki Imaizumi, Riho Ito, Shuhei Hikosaka and Ryosuke Nakamura, "Damage Detection from Aerial Images
via Convolutional Neural Networks," IAPR International Conference on Machine Vision Applications (MVA), 2017.** ([pdf](http://www.airc.aist.go.jp/gsrt/fujita_final.pdf))

## Synopsis
Each datum in this dataset is a pair of pre- and post-tsunami aerial image patches, and encompasses a target building at the center of the patch.   
The below shows eight samples from the dataset, where four pairs are shown for "washed-away" buildings (left column) and "surviving" buildings (right column), respectively. The class label assigned to each patch pair (i.e. "washed-away" or "surviving") represents whether or not a building at the center of the pre-tsunami patch got wahshed-away by tsunami. 

<p align="center"> 
<img src ="https://user-images.githubusercontent.com/13417696/27384118-b5539e1e-56c8-11e7-9c0c-7d06b899763f.png" />
</p>

These pairs were cropped from a hefty number of RGB aerial images of Tohoku region of Japan. These aerial images were taken before or after the Great East Japan earthquake, with the original pixel resolution of 40 cm for pre-quake images and 12 cm for post-qukae images (actually, resampled to 40 cm).

We prepared the patch pairs for two types of size: **fixed-scale** and **resized**. Fixed-scale patches were cropped from aerial images with the fixed size of 160 x 160 pixels; so they have the same resolution of the original images (40 cm). In contrast, resized patches  were cropped depending on the size of each target building (specifically, three times larger than the target building), and then all resized to 128 x 128 pixels; so the spatial scale of the patches varies from building to building.
The resulting ABCD dataset comprised 8,506 pairs for fixed-scale (4,253 washed-away) and 8,444 pairs for resized (4,223 washed-away). 

As source of class labels, we employed the existing, post-quake survey result (http://fukkou.csis.u-tokyo.ac.jp/). This survey result is the outcome of an exhaustive
field investigation which was carried out under the initiative of MLIT (Ministry of Land, Infrastructure, Transport and Tourism) in the wake of the Great East Japan earthquake on March 11, 2011. As a consequence of this survey, over 220,000 buildings in the ravaged areas were assessed, and each building was assigned a label according to the degree of damage.



## Download
IMPORTANT -- Please read the [Terms of Use](https://github.com/gistairc/ABCDdataset/blob/master/LICENSE.md) before downloading the ABCD dataset.

The dataset can be downloaded from [here](https://data.airc.aist.go.jp/ABCDdataset/ABCDdataset.zip) (2.1GB).   
Or type the following in the terminal:
```
$ wget https://data.airc.aist.go.jp/ABCDdataset/ABCDdataset.zip
$ unzip ABCDdataset.zip
