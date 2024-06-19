简体中文 | [English](README.md)

# Paddle Quantum （量桨）

- [特色](#特色)
- [安装步骤](#安装步骤)
   - [安装 PaddlePaddle](#安装-paddlepaddle)
   - [安装 Paddle Quantum](#安装-paddle-quantum)
   - [量子化学模块的环境设置](#量子化学模块的环境设置)
   - [运行](#运行)
- [入门与开发](#入门与开发)
   - [教程入门](#教程入门)
   - [案例入门](#案例入门)
   - [API 文档](#api-文档)
   - [开发](#开发)
- [交流与反馈](#交流与反馈)
- [使用 Paddle Quantum 的工作](#使用-paddle-quantum-的工作)
- [FAQ](#faq)
- [Copyright and License](#copyright-and-license)
- [References](#references)

[Paddle Quantum（量桨）](https://qml.baidu.com/)是基于百度飞桨研发的全球首个云量一体的量子机器学习平台。量桨支持量子神经网络的搭建与训练等功能，使得百度飞桨也因此成为国内首个支持量子机器学习的深度学习框架。量桨具备轻松上手、功能丰富等特点，提供了完善的API文档和用例教程，使用户可以快速入门和上手。

<p align="center">
  <a href="https://qml.baidu.com/">
    <img width=80% src="https://release-data.cdn.bcebos.com/Paddle%20Quantum.png">
  </a>
</p>

<p align="center">
  <!-- docs -->
  <a href="https://qml.baidu.com/api/paddle_quantum.circuit.html">
    <img src="https://img.shields.io/badge/docs-link-green.svg?style=flat-square&logo=read-the-docs"/>
  </a>
  <!-- PyPI -->
  <a href="https://pypi.org/project/paddle-quantum/">
    <img src="https://img.shields.io/badge/pypi-v2.4.0-orange.svg?style=flat-square&logo=pypi"/>
  </a>
  <!-- Python -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.6+-blue.svg?style=flat-square&logo=python"/>
  </a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square&logo=apache"/>
  </a>
  <!-- Platform -->
  <a href="https://github.com/PaddlePaddle/Quantum">
    <img src="https://img.shields.io/badge/OS-MacOS%20|%20Windows%20|%20Linux-lightgrey.svg?style=flat-square"/>
  </a>
</p>

量桨建立起了人工智能与量子计算的桥梁，不但可以快速实现量子神经网络的搭建与训练，还提供易用的量子机器学习开发套件与量子优化、量子化学等前沿量子应用工具集，并提供多项自研量子机器学习应用。通过百度飞桨深度学习平台赋能量子计算，量桨为领域内的科研人员以及开发者便捷地开发量子人工智能的应用提供了强有力的支撑，同时也为广大量子计算爱好者提供了一条可行的学习途径。

## 特色

- 轻松上手
   - 丰富的在线学习资源（近 50 篇教程案例）
   - 通过模板高效搭建量子神经网络
   - 自动微分框架
- 功能丰富
   - 提供多种优化工具和 GPU 模式
   - 高性能模拟器支持25+量子比特的模拟运算
   - 支持多种噪声模型的模拟
- 特色工具集
   - 提供组合优化和量子化学等前沿领域的计算工具箱
   - 分布式量子信息处理模组 LOCCNet
   - 自研多种量子机器学习算法

## 安装步骤

### 安装 PaddlePaddle

当用户安装 Paddle Quantum 时会自动下载安装这个关键依赖包。关于 PaddlePaddle 更全面的安装信息请参考 [PaddlePaddle](https://www.paddlepaddle.org.cn/install/quick) 安装配置页面。此项目需求 PaddlePaddle 2.2.0 到 2.3.0。

### 安装 Paddle Quantum

我们推荐通过 `pip` 完成安装，

```bash
pip install paddle-quantum
```

用户也可以选择下载全部文件后进行本地安装，

```bash
git clone https://github.com/PaddlePaddle/quantum
cd quantum
pip install -e .
```

### 量子化学模块的环境设置

当前我们的量子化学模块在后端使用 `PySCF` 来计算各类分子积分，所以在运行量子化学模块之前需要先行安装该 Python 包。

> 推荐在 Python>=3.6 环境中安装。

在安装 `PySCF` 时，我们建议您使用 conda。对于 **MacOS/Linux** 的用户，可以使用如下指令。

```bash
conda install -c pyscf pyscf
```

> 注：对于 **Windows** 用户，如果操作系统为 Windows10，可以在其应用商店提供的 Ubuntu 子系统中利用上述命令安装 `PySCF`。`PySCF` 并不支持直接在 Windows 下运行，我们正在努力开发更多的量子化学后端，在量桨的下一版本中将会有对 Windows 更好的支持。 

**注意：** 更多的下载方法请参考 [PySCF](https://pyscf.org/install.html)。

### 运行

现在，可以试着运行一段程序来验证量桨是否已安装成功。这里我们运行量桨提供的量子近似优化算法 (QAOA) 的例子。

```bash
cd paddle_quantum/QAOA/example
python main.py
```

> 关于 QAOA 的介绍可以参考我们的 [QAOA 教程](./tutorials/combinatorial_optimization/QAOA_CN.ipynb)。


### 重大更新

在量桨 2.2.0 版本中，我们对代码架构进行了不兼容升级，新版的结构和用法可以参考我们的[教程](https://qml.baidu.com/tutorials/overview.html)、[API 文档](https://qml.baidu.com/api/introduction.html)和[源代码](https://github.com/PaddlePaddle/Quantum)。同时，我们也支持通过[量易伏](https://github.com/baidu/QCompute)连接到真实量子计算机上，使用`paddle_quantum.set_backend('quleaf')`即可选择量易伏作为后端。

## 入门与开发

### 教程入门

量子计算是由量子力学与计算理论交叉而成的全新计算模型，具有强大的信息处理优势和广阔的应用前景，被视作未来计算技术的心脏。量子计算的相关介绍与入门知识可以参考 [1-3]。

量子机器学习是一门结合量子计算与机器学习的交叉学科，一方面利用量子计算的信息处理优势促进人工智能的发展，另一方面也利用现有的人工智能的技术突破量子计算的研发瓶颈。关于量子机器学习的入门资料可以参考 [4-6]。

这里，我们提供了一份[**入门手册**](./introduction)方便用户快速上手 Paddle Quantum。目前支持网页阅览和运行 Jupyter Notebook 两种方式。内容上，该手册包括以下几个方面：

- 量桨（Paddle Quantum）的详细安装教程
- 量子计算和量子神经网络的基础知识介绍
- 变分量子算法的基本思想与算法框架
- 量桨的使用介绍
- 飞桨（PaddlePaddle）优化器的使用教程
- 量桨中量子化学模块的使用介绍
- 如何基于 GPU 训练量子神经网络

### 案例入门

Paddle Quantum（量桨）建立起了人工智能与量子计算的桥梁，为量子机器学习领域的研发提供强有力的支撑，也提供了丰富的案例供开发者学习。

在这里，我们提供了涵盖量子模拟、机器学习、组合优化、本地操作与经典通讯（local operations and classical communication, LOCC）、量子神经网络等多个领域的案例供大家学习。每个教程目前支持网页阅览和运行 Jupyter Notebook 两种方式。我们推荐用户下载 Notebook 后，本地运行进行实践。

- [量子模拟](./tutorials/quantum_simulation)
    1. [哈密顿量的构造](./tutorials/quantum_simulation/BuildingMolecule_CN.ipynb)
    2. [变分量子特征求解器（VQE）](./tutorials/quantum_simulation/VQE_CN.ipynb)
    3. [子空间搜索 - 量子变分特征求解器（SSVQE）](./tutorials/quantum_simulation/SSVQE_CN.ipynb)
    4. [变分量子态对角化算法（VQSD）](./tutorials/quantum_simulation/VQSD_CN.ipynb)
    5. [吉布斯态的制备（Gibbs State Preparation）](./tutorials/quantum_simulation/GibbsState_CN.ipynb)
    6. [未知量子态的经典影子](./tutorials/quantum_simulation/ClassicalShadow_Intro_CN.ipynb)
    7. [基于经典影子的量子态性质估计](./tutorials/quantum_simulation/ClassicalShadow_Application_CN.ipynb)
    8. [利用 Product Formula 模拟时间演化](./tutorials/quantum_simulation/HamiltonianSimulation_CN.ipynb)
    9. [模拟一维海森堡链的自旋动力学](./tutorials/quantum_simulation/SimulateHeisenberg_CN.ipynb)
    10. [基于施密特分解的分布式变分量子本征求解器](./tutorials/quantum_simulation/DistributedVQE_CN.ipynb)
    11. [量子信号处理与量子奇异值变换](./tutorials/quantum_simulation/QSP_and_QSVT_CN.ipynb)
    12. [利用 qDRIFT 模拟时间演化](./tutorials/quantum_simulation/QDRIFT_CN.ipynb)
    13. [量子相位处理](./tutorials/quantum_simulation/QPP_CN.ipynb)
    14. [变分量子精密测量](./tutorials/quantum_simulation/VariationalQM_CN.ipynb)


- [机器学习](./tutorials/machine_learning)
    1. [量子态编码经典数据](./tutorials/machine_learning/DataEncoding_CN.ipynb)
    2. [量子分类器（Quantum Classifier）](./tutorials/machine_learning/QClassifier_CN.ipynb)
    3. [变分影子量子学习（VSQL）](./tutorials/machine_learning/VSQL_CN.ipynb)
    4. [量子核方法（Quantum Kernel）](./tutorials/machine_learning/QKernel_CN.ipynb)
    5. [量子变分自编码器（Quantum Autoencoder）](./tutorials/machine_learning/QAutoencoder_CN.ipynb)
    6. [量子生成对抗网络（Quantum GAN）](./tutorials/machine_learning/QGAN_CN.ipynb)
    7. [变分量子奇异值分解（VQSVD）](./tutorials/machine_learning/VQSVD_CN.ipynb)
    8. [数据编码分析](./tutorials/machine_learning/EncodingAnalysis_CN.ipynb)
    9. [量子神经网络模拟函数](./tutorials/machine_learning/QApproximating_CN.ipynb)
    10. [变分量子振幅估算](./tutorials/machine_learning/VQAE_CN.ipynb)

- [组合优化](./tutorials/combinatorial_optimization)
    1. [量子近似优化算法（QAOA）](./tutorials/combinatorial_optimization/QAOA_CN.ipynb)
    2. [QAOA 求解最大割问题](./tutorials/combinatorial_optimization/MAXCUT_CN.ipynb)
    3. [大规模量子近似优化分治算法（DC-QAOA）](./tutorials/combinatorial_optimization/DC-QAOA_CN.ipynb)
    4. [旅行商问题](./tutorials/combinatorial_optimization/TSP_CN.ipynb)
    5. [量子金融应用：最佳套利机会](./tutorials/combinatorial_optimization/ArbitrageOpportunityOptimation_CN.ipynb)
    6. [量子金融应用：投资组合优化](./tutorials/combinatorial_optimization/PortfolioOptimization_CN.ipynb)
    7. [量子金融应用：投资组合分散化](./tutorials/combinatorial_optimization/PortfolioDiversification_CN.ipynb)

- [LOCC 量子神经网络（LOCCNet）](./tutorials/locc)
    1. [LOCC 量子神经网络](./tutorials/locc/LOCCNET_Tutorial_CN.ipynb)
    2. [纠缠蒸馏 -- BBPSSW 协议](./tutorials/locc/EntanglementDistillation_BBPSSW_CN.ipynb)
    3. [纠缠蒸馏 -- DEJMPS 协议](./tutorials/locc/EntanglementDistillation_DEJMPS_CN.ipynb)
    4. [纠缠蒸馏 -- LOCCNet 设计协议](./tutorials/locc/EntanglementDistillation_LOCCNET_CN.ipynb)
    5. [量子隐态传输](./tutorials/locc/QuantumTeleportation_CN.ipynb)
    6. [量子态分辨](./tutorials/locc/StateDiscrimination_CN.ipynb)

- [量子神经网络研究](./tutorials/qnn_research)
    1. [量子神经网络的贫瘠高原效应（Barren Plateaus）](./tutorials/qnn_research/BarrenPlateaus_CN.ipynb)
    2. [噪声模型与量子信道](./tutorials/qnn_research/Noise_CN.ipynb)
    3. [量子神经网络的表达能力](./tutorials/qnn_research/Expressibility_CN.ipynb)
    4. [变分量子电路编译](./tutorials/qnn_research/VQCC_CN.ipynb)
    5. [量子费舍信息](./tutorials/qnn_research/Fisher_CN.ipynb)
    6. [VAns-可变电路结构](./tutorials/qnn_research/VAns_CN.ipynb)

随着 LOCCNet 模组的推出，量桨现已支持分布式量子信息处理任务的高效模拟和开发。感兴趣的读者请参见[教程](./tutorials/locc/LOCCNET_Tutorial_CN.ipynb)。Paddle Quantum 也支持在 GPU 上进行量子机器学习的训练，具体的方法请参考案例：[在 GPU 上使用 Paddle Quantum](./introduction/PaddleQuantum_GPU_CN.ipynb)。此外，量桨可以基于噪声模块进行含噪算法的开发以及研究，详情请见[噪声模块教程](./tutorials/qnn_research/Noise_CN.ipynb)。

在最近的更新中，量桨还加入了基于测量的量子计算（measurement-based quantum computation, MBQC）模块。与传统的量子电路模型不同，MBQC 具有其独特的运行方式，感兴趣的读者请参见我们提供的[多篇教程](./tutorials/mbqc)以了解量桨 MBQC 模块的使用方法和应用案例。

### API 文档

我们为 Paddle Quantum 提供了独立的 [API 文档页面](https://qml.baidu.com/api/introduction.html)，包含了供用户使用的所有函数和类的详细说明与用法。

### 开发

Paddle Quantum 使用 setuptools 的 develop 模式进行安装，相关代码修改可以直接进入 `paddle_quantum` 文件夹进行修改。python 文件携带了自说明注释。

## 交流与反馈

- 我们非常欢迎您通过 [GitHub Issues](https://github.com/PaddlePaddle/Quantum/issues) 来提交问题、报告与建议。

- 技术交流QQ群：1076223166

## 使用 Paddle Quantum 的工作

我们非常欢迎开发者使用 Paddle Quantum 进行量子机器学习的研发，如果您的工作有使用 Paddle Quantum，也非常欢迎联系我们，邮箱为 qml@baidu.com。以下为 BibTeX 的引用方式：

> @misc{Paddlequantum,
> title = {{Paddle Quantum}},
> year = {2020},
> url = {https://github.com/PaddlePaddle/Quantum}, }

目前使用 Paddle Quantum 的代表性工作包括了吉布斯态的制备和变分量子奇异值分解：

[1] Wang, Youle, Guangxi Li, and Xin Wang. "Variational quantum Gibbs state preparation with a truncated Taylor series." Physical Review Applied 16.5 (2021): 054035. [[pdf](https://arxiv.org/pdf/2005.08797.pdf)]

[2] Wang, Xin, Zhixin Song, and Youle Wang. "Variational quantum singular value decomposition." Quantum 5 (2021): 483. [[pdf](https://arxiv.org/pdf/2006.02336.pdf)]

[3] Li, Guangxi, Zhixin Song, and Xin Wang. "VSQL: Variational Shadow Quantum Learning for Classification." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 9. 2021. [[pdf]](https://arxiv.org/pdf/2012.08288.pdf)

[4] Chen, Ranyiliu, et al. "Variational quantum algorithms for trace distance and fidelity estimation." Quantum Science and Technology (2021). [[pdf]](https://arxiv.org/pdf/2012.05768.pdf)

[5] Wang, Kun, et al. "Detecting and quantifying entanglement on near-term quantum devices." arXiv preprint arXiv:2012.14311 (2020). [[pdf]](https://arxiv.org/pdf/2012.14311.pdf)

[6] Zhao, Xuanqiang, et al. "Practical distributed quantum information processing with LOCCNet." npj Quantum Information 7.1 (2021): 1-7. [[pdf]](https://arxiv.org/pdf/2101.12190.pdf)

[7] Cao, Chenfeng, and Xin Wang. "Noise-Assisted Quantum Autoencoder." Physical Review Applied 15.5 (2021): 054012. [[pdf]](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.15.054012)

## FAQ

1. 问：**研究量子机器学习有什么意义？它有哪些应用场景？**

    答：量子机器学习是将量子计算与机器学习相结合的一门学科，它一方面可以利用现有人工智能技术突破量子计算的研发瓶颈，另一方面也能利用量子计算的信息处理优势促进传统人工智能的发展。量子机器学习不仅适用于量子化学模拟（如[变分量子特征求解器 (VQE)](./tutorials/VQE)）等量子问题，也可以用来解决一些经典问题（如[量子近似优化算法 (QAOA)](./tutorials/QAOA)）。

2. 问：**想做量子机器学习，但对量子计算不是很了解，该如何入门？**

    答：Nielsen 和 Chuang 所著的《量子计算与量子信息》是量子计算领域公认的经典入门教材。建议读者首先学习这本书的第一、二、四章，介绍了量子计算中的基本概念、数学和物理基础、以及量子电路模型。读者也可以阅读量桨的[入门手册](./introduction)，其中包含了对量子计算的简单介绍，并有互动性的例子供读者尝试。对量子计算有了大致了解后，读者可以尝试学习量桨提供的一些前沿[量子机器学习案例](./tutorials)。

3. 问：**现阶段没有规模化的量子硬件，怎么开发量子应用？**

    答：使用量桨，用户可以方便地在经典计算机上模拟量子算法，进行量子应用的开发与验证，为未来使用规模化的量子硬件做技术积累。

4. 问：**量桨有哪些优势？**

    答：量桨是基于百度飞桨开发的量子机器学习工具集。飞桨作为国内首个开源开放的产业级深度学习平台，技术领先且功能完备。拥有飞桨的技术支持，特别是其强大的动态图机制，量桨可以方便地进行机器学习的优化以及 GPU 的加速。同时，基于百度量子计算研究所研发的高性能量子模拟器，量桨在个人笔记本电脑上也能支持20多个量子比特的运算。另外，量桨还有丰富的[量子机器学习案例](./tutorials)供大家参考和学习。


## Copyright and License

Paddle Quantum 使用 [Apache-2.0 license](LICENSE) 许可证。

## References

[1] [量子计算 - 百度百科](https://baike.baidu.com/item/%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97/11035661)

[2] Nielsen, M. A. & Chuang, I. L. Quantum computation and quantum information. (2010).

[3] Phillip Kaye, Laflamme, R. & Mosca, M. An Introduction to Quantum Computing. (2007).

[4] [Biamonte, J. et al. Quantum machine learning. Nature 549, 195–202 (2017).](https://www.nature.com/articles/nature23474)

[5] [Schuld, M., Sinayskiy, I. & Petruccione, F. An introduction to quantum machine learning. Contemp. Phys. 56, 172–185 (2015).](https://www.tandfonline.com/doi/abs/10.1080/00107514.2014.964942)

[6] [Benedetti, M., Lloyd, E., Sack, S. & Fiorentini, M. Parameterized quantum circuits as machine learning models. Quantum Sci. Technol. 4, 043001 (2019).](https://iopscience.iop.org/article/10.1088/2058-9565/ab4eb5)
