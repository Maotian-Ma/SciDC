<div align="center">
<h1> Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs
<h5 align="center"> 
  
<a href='xxx'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a>



Maotian Ma<sup>1</sup>,
Zheni Zeng<sup>1</sup>,
Zhenghao Liu<sup>2</sup>,
Yukun Yan<sup>2</sup>,


<sup>1</sup>学校或者机构, <sup>2</sup>学校或者机构, <sup>3</sup>学校或者机构

</h5>
</div>

This is the source code for paper:
Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs

## 📖 Overview

<p align="center"><img src="scidc.png" width="50%"></p>

SciDC is a novel framework that integrates subject-specific scientific knowledge with multi-layered decoding constraints to improve the reliability of large language models in specialized domains. By leveraging general LLMs (e.g., Claude-3.5-Sonnet) to automatically transform flexible knowledge into standardized rules at three granularities (top-layer for reasoning sequences, middle-layer for conditional logic, and bottom-layer for token-level constraints), SciDC enables locally-deployed domain models to generate outputs that strictly adhere to scientific principles while maintaining data privacy. Experiments across industrial formulation design, clinical tumor diagnosis, and chemical retrosynthesis planning demonstrate consistent effectiveness, achieving an average 12% accuracy improvement compared to vanilla generation methods.


## ⚙️ Setup

### Environment

```bash
# Create conda environment
conda create --name scidc python==3.11
conda activate scidc

# Clone repository
git clone https://github.com/Maotian-Ma/SciDC.git
cd SciDC

# Install dependencies
pip install -r requirements.txt
```



## 🔧 Reproduction Guide/Training/Method...

这里是仓库等主体部分，包含整个仓库的详细运行过程和脚本介绍。例如：

### 1. 数据集构建

你可以在[这里](https://github.com/RUC-NLPIR/FlashRAG/blob/main/docs/original_docs/process-wiki.md)下载数据集。

### 2. 处理数据


#### 2.1. 第一步:
你可以运行以下脚本来处理数据...

```bash
bash scripts/xxx.sh
```

#### 2.2. ...

## 📁 Repository Structure/Dataset Structure
这里可以用于介绍仓库的结构，或者比较复杂的数据集的结构，位置可以灵活调整。
```
xxx/
├── README.md
├── requirements.txt
├── output_data/               # Sample outputs
├── figs/                      # README figures
├── bash/                      # The script files used to run the experiments
└── src/
    ├── train.py               # Training Code
    └── evaluate.py            # Evaluate the performance
```

## 📄 Acknowledgement 
Acknowledgement, 介绍你参考的仓库或者代码，例如UltraRAG。

- [UltraRAG](https://github.com/OpenBMB/UltraRAG)

## 🥰 Citation
引用链接
```
@article{chen2025ultrarag,
  title={UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation},
  author={Chen, Yuxuan and Guo, Dewen and Mei, Sen and Li, Xinze and Chen, Hao and Li, Yishan and Wang, Yixuan and Tang, Chaoyue and Wang, Ruobing and Wu, Dingjun and others},
  journal={arXiv preprint arXiv:2504.08761},
  year={2025}
}
```


## 📧 Contact
这里是联系方式
If you have questions, suggestions, and bug reports, please email:
```
xxx.com
```
