<div align="center">
<h1> Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs
<h5 align="center"> 
  
<a href='xxx'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a>



Maotian Ma<sup>1</sup>,
Zheni Zeng<sup>1</sup>,
Zhenghao Liu<sup>2</sup>,
Yukun Yan<sup>2</sup>,



</h5>
</div>

This is the source code for paper:
Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs

## 📖 Overview

<p align="center"><img src="scidc.png" width="100%"></p>

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



## 🔧 Reproduction Guide


### 1. 设置参数

在 config.py 中修改相应的参数。

### 2. 执行代码

执行 run_pipeline.py 执行流程


## 📁 Repository Structure

```
SciDC/
├── README.md
├── requirements.txt
├── prompts                    # Prompts for cot/code generation & Domain knowledge document
├── config.py                  # Edit your config here
└── src/
    ├── gllm                   # Generate constrained code with GLLM
        ├── __init__.py
        ├── api_client.py
        └── code_generator.py
    └── dllm                   # Execute code with DLLM
        ├── __init__.py
        ├── dllm.py
        └── constrained_executor.py
```

## 📄 Acknowledgement 


## 🥰 Citation
引用链接
```
@article{chen2025ultrarag,
  title={UltraRAG: A Modular and Automated Toolkit for Adaptive Retrieval-Augmented Generation},
  author={Chen, Yuxuan and Guo, Dewen and Mei, Sen and Li, Xinze and Chen, Hao and Li, Yishan and Wang, Yixuan and Tang, Chaoyue and Wang, Ruobing and Wu, Dingjun and others},
  journal={xxx},
  year={2026}
}
```


## 📧 Contact
这里是联系方式
If you have questions, suggestions, and bug reports, please email:
```
xxx.com
```
