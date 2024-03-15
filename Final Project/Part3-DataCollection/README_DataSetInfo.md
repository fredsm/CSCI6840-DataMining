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


# xView 2 Challenge 

xview2-baseline

Copyright 2019 Carnegie Mellon University.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Released under a BSD-3-style license, please see LICENSE.md or contact permission@sei.cmu.edu for full terms.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This Software includes and/or makes use of the following Third-Party Software subject to its own license:
1. SpaceNet (https://github.com/motokimura/spacenet_building_detection/blob/master/LICENSE) Copyright 2017 Motoki Kimura.

DM19-0988

## xView 

xView2 is a challenge set forth by [DIU](https://diu.mil) for assessing damaged buildings after a natural disaster. The challenge is open to all to participate and more information can be found at the [xview2](https://xview2.org) challenge site.

## xBD

xBD is the name of the dataset that was generated for this challenge. The dataset contains over 45,000KM<sup>2</sup> of polygon labeled pre and post disaster imagery. The dataset provides the post-disaster imagery with transposed polygons from pre over the buildings, with damage classification labels. See the [xBD paper](http://openaccess.thecvf.com/content_CVPRW_2019/papers/cv4gc/Gupta_Creating_xBD_A_Dataset_for_Assessing_Building_Damage_from_Satellite_CVPRW_2019_paper.pdf) for more information.  

## Data Downloads

The data during the challenge is available from [xView2](https://xview2.org) challenge website, please register or login to download the data! 

The current total space needed is: about **10GB** compressed and about **11GB** uncompressed. 

See the code we use to translate the json outputs to this submission image [inference_image_output.py](./utils/inference_image_output.py), also see the submission rules on the [xview2 website](https://xview2.org/challenge).

## Contact 

See the [xView2 FAQ](https://xview2.org/challenge) page first, if you would like to talk to us further reach out to the xView2 chat on [discord](https://xview2.org/chat).


# FloodNet Dataset

## Overview

Frequent, and increasingly severe, natural disasters threaten human health, infrastructure, and natural systems. The provision of accurate, timely, and understandable information has the potential to revolutionize disaster management. For quick response and recovery on a large scale, after a natural disaster such as a hurricane, access to aerial images is critically important for the response team. The emergence of small unmanned aerial systems (UAS) along with inexpensive sensors presents the opportunity to collect thousands of images after each natural disaster with high flexibility and easy maneuverability for rapid response and recovery.  Moreover, UAS can access hard-to-reach areas and perform data collection  tasks that can be unsafe for humans if not impossible.  Despite all these advancements and efforts to collect such large datasets, analyzing them and extracting meaningful information remains a significant challenge in scientific communities.

[FloodNet](https://arxiv.org/abs/2012.02951) provides high-resolution UAS imageries with detailed semantic annotation regarding the damages. To advance the damage assessment process for post-disaster scenarios, we present a unique challenge considering classification, semantic segmentation, visual question answering highlighting the UAS imagery-based FloodNet dataset.

 1. Track 1: Image Classification and Semantic Segmentation
 2. Track 2: Visual Question Answering

## Dataset Details

The data is collected with a small UAS platform, DJI Mavic Pro quadcopters, after Hurricane Harvey. The whole dataset has 2343 images, divided into training (~60%), validation (~20%), and test (~20%) sets.

For Track 1 ( Semi-supervised Classification and Semantic Segmentation),  in the training set, we have around 400 labeled images (~25% of the training set) and around 1050 unlabeled images (~75% of the training set ).

For Track 2 ( Supervised VQA), in the training set we have around 1450 images and there are a total 4511 image-question pairs.   


### Track 1

In this track, participants are required to complete two semi-supervised tasks. The first task is image classification, and the second task is semantic segmentation.

1. Semi-Supervised Classification: Classification for FloodNet dataset requires classifying the images into ‘Flooded’ and ‘Non-Flooded’ classes. Only a few of the training images have their labels available, while most of the training images are unlabeled. 
 
2. Semi-Supervised Semantic Segmentation: The semantic segmentation labels include: 1) Background, 2) Building Flooded, 3) Building Non-Flooded, 4) Road Flooded, 5) Road Non-Flooded, 6) Water, 7)Tree, 8) Vehicle, 9) Pool, 10) Grass. 
Only a small portion of the training images have their corresponding masks available. 

The dataset for Track 1 can be downloaded from this link: https://drive.google.com/drive/folders/1sZZMJkbqJNbHgebKvHzcXYZHJd6ss4tH?usp=sharing

### Track 2

For the Visual Question Answering (VQA) task, we provide images associated with multiple questions. These questions will be divided into the following categories:

1. Simple Counting: Questions will be designed to count the number of objects regardless of their attribute. For example: “how many buildings are there in the image?”.
2. Complex Counting: Questions will be asked to count the number of objects belonging to a specific attribute. For example: “how many flooded buildings are there in the image?”.
3. Condition Recognition: In this category, all the questions are mainly designed to ask questions regarding the condition of the object and the neighborhood. For example: “What is the condition of the road in the given image?”.
4. Yes/No type of question: For this type of question, the answer will be either a ‘Yes’ or a ‘No’. For example: “Is there any flooded road?”.

The dataset for Track 2 can be downloaded from this link: https://drive.google.com/drive/folders/1g1r419bWBe4GEF-7si5DqWCjxiC8ErnY?usp=sharing

### Paper Link
The paper can be downloaded from this [link](https://arxiv.org/abs/2012.02951).
Please cite our paper when using the dataset

 ```
@article{rahnemoonfar2020floodnet,
  title={FloodNet: A High Resolution Aerial Imagery Dataset for Post Flood Scene Understanding},
  author={Rahnemoonfar, Maryam and Chowdhury, Tashnim and Sarkar, Argho and Varshney, Debvrat and Yari, Masoud and Murphy, Robin},
  journal={arXiv preprint arXiv:2012.02951},
  year={2020}
}


