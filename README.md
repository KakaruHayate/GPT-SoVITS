# GPT-SoVITS-MUSA

[原文档](./README_ori.md)

*注意：本repo涉及设备目前仅在中国大陆发售，故仅提供中文文档*

*Note: The device involved in this repo is currently only sold in Chinese Mainland, so only Chinese documents are provided*

## 进度

- [x] 预处理（在S70下会遇到显存问题）
- [ ] ~S1训练（lightning不支持，暂时无解）~
- [ ] S2训练（显存不足本人无法测试）
- [x] 推理

*UVR5/ASR/API/GUI等组件未测试*

## 如何使用

### 配置/系统要求

**本人测试配置/系统**
 
 - Intel CORE i3-12100
 
 - Moorethreads MTT S70

 - Ubuntu 20.04 LTS
 
 - Python 3.9
 
官方文档注明了Intel CPU，对其他CPU没有进行测试，Ubuntu内核版本应为5.4.X-5.15.X

### 环境配置

*TIPS:文件名后方标注chunxiao（春晓）/qy1对应S3000/S80/S70及以下设备，后方标注quyuan（屈原）/qy2对应S4000以上设备，下文不再提及*

**1.安装MUSA SDK rc2.0.0**

以下组件你需要安装：

 - musa driver
 
 - musa_toolkit
 
 - mudnn
 
 - mccl
 
你可以前往[这里](https://developer.mthreads.com/sdk/download/musa?equipment=&os=Ubuntu&driverVersion=&version=)获取这些组件，**或者前往本仓库issue区**

内含文档可以帮助你进行安装。注意安装mccl时可以不理会文档中要求，文档中提及的`sudo ./install.sh -id /usr/local`命令可能不能正常安装，可以尝试`sudo ./install.sh -i`。

*TIPS2:建议在anaconda等虚拟环境下进行以下操作*

**2.安装torch musa**

前往[这里](https://github.com/MooreThreads/torch_musa/releases/tag/v1.1.0)获取torch_musaV1.1.0

下载你需要版本的torch与torch_musa，本文提及的测试环境应该选择

```
torch-2.0.0-cp39-cp39-linux_x86_64-S80_S3000.whl
torch_musa-1.1.0-cp39-cp39-linux_x86_64-S80_S3000.whl
```

修改文件名，将“_x86_64”后的"-S80_S3000"删除，之后使用pip命令安装

```
pip install torch-2.0.0-cp39-cp39-linux_x86_64.whl
torch_musa-1.1.0-cp39-cp39-linux_x86_64.whl
```

**3.安装对应版本的torchaudio**

直接使用pip安装最新版本的torchaudio会覆盖前文安装的torch，请用以下命令安装torchaudio

```
pip install torchaudio==2.0.1
```

**4.安装环境**

```
conda install -c conda-forge gcc
conda install -c conda-forge gxx
conda install ffmpeg cmake
pip install -r requirements.txt
```

**5.运行**

```
python webui.py
```
