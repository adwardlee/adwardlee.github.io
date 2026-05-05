---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" append: site.repository append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" append: site.repository append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi there! I am now an Researcher at Shanghai AI Lab. Before joining Shanghai AI Lab, I was a Researcher at Machine Intelligence Technology Lab, DAMO Academy, Alibaba Group, under the guidance of [Rong Jin](https://scholar.google.com/citations?hl=zh-CN&user=CS5uNscAAAAJ) and [Ping Tan](https://pingtan.people.ust.hk/index.html). I have been engaged in AI research and development since 2019 after PHD graduation. I am fortunate to have gained industry experience at [Alibaba DAMO Academy](https://damo.alibaba.com/?language=en), [Tencent AI Lab](https://ailab.tencent.com/ailab/en/index/), and Baidu IDL.

<span style="color: red; font-weight: bold;">NOTE:</span> We are hiring full-time Researcher and Engineer, motivated interns and joint-training PhD students. If you are enthusiastic about Safe AI and wish to join us, contact me at lilijun@pjlab.org.cn directly!

_If interested in collaboration or discussion, please email me._

# 🔭 Research Interest

My research interests lie at the nexus of AI safety and visual understanding. I aim to develop artificial general intelligence with built‑in, balanced safety capabilities. To this end, I concentrate on thoroughly characterizing AI safety vulnerabilities，and embedding robust protective measures from the very outset of model design and training.


# 🔥 News
- *2026.05*： Our papers [OpenSafeRL](https://openreview.net/forum?id=bvnuXYMgjg) and [MemGuard](https://arxiv.org/pdf/2510.02373) have been accepted by ICML 2026.
- *2026.04*: 🎉 Our papers [EGD](https://arxiv.org/pdf/2503.02368), [SEARL](https://arxiv.org/pdf/2604.07791v1), [HarmRLVR](https://arxiv.org/pdf/2510.15499) and [ToolSafe](https://arxiv.org/pdf/2601.10156) have been accepted by ACL 2026.
- *2026.02*：🎉 Our paper [TreeTeaming](https://arxiv.org/pdf/2603.22882) has been accepted by CVPR 2026.
- *2026.01*: 🎉 Our papers [MIS](https://arxiv.org/pdf/2501.18533) and [GhostEI-Bench](https://arxiv.org/pdf/2510.20333) have been accepted by ICLR 2026.
- *2026.01*: 🎉 We release a comprehensive survey paper about [Efficient Agent](https://arxiv.org/pdf/2601.14192).
- *2025.11*：🎉 Our paper [Response Attack](https://arxiv.org/pdf/2507.05248) has been accepted by AAAI 2026.
- *2025.09*: 🎉 Our paper [PURE](https://arxiv.org/pdf/2504.15275) has been accepted by Neurips 2025.
- *2025.08*: 🎉 Our papers [LARF](https://arxiv.org/pdf/2507.18631), [Visco-attack](https://arxiv.org/pdf/2507.02844) and [RMS](https://arxiv.org/pdf/2509.04403) have been accepted by EMNLP 2025.
- *2025.07*: 🎉 We release a safety-enhanced framework [SafeWork-R1](https://arxiv.org/pdf/2507.18576) for VLM.
- *2025.05*: 🎉 Our paper [WorldSimBench](https://arxiv.org/pdf/2410.18072) has been accepted by ICML 2025.
- *2025.02*: 🎉 Our paper [T2ISafety](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_T2ISafety_Benchmark_for_Assessing_Fairness_Toxicity_and_Privacy_in_Image_CVPR_2025_paper.pdf) has been accepted by CVPR 2025. 
- *2024.05*: 🎉 Our papers [SALAD-Bench](https://aclanthology.org/2024.findings-acl.235.pdf) and [PsySafe](https://aclanthology.org/2024.acl-long.812.pdf) have been accepted by ACL 2024. **PsySafe** is awarded as **Outstanding paper**.
- *2024.03*: 🎉 We release an easy-to-use Python framework to generate adversarial jailbreak prompts at [website](http://easyjailbreak.org/).
- *2023*: 🎉 Our paper [RenderIH](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_RenderIH_A_Large-Scale_Synthetic_Dataset_for_3D_Interacting_Hand_Pose_ICCV_2023_paper.pdf) has been accepted by ICCV 2023.
- *2022.05*: 🎉🎉 We rank 1st at the Action Detection track of [EPIC@CVPR2022 Workshop](https://epic-kitchens.github.io/2022#results)

- *2022.04*：🎉 We rank 2nd at the [FreiHAND Competition](https://competitions.codalab.org/competitions/21238)

# 📝 Publications 
Topics: AI Safety/ Agent / Understanding

(*: indicates equal contribution; ‡: indicates corresponding)

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/paper_imgs/iter_decoding.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Evolutionary Guided Decoding: Iterative Value Refinement for LLMs**

Zhenhua Liu<sup>*</sup>, **Lijun Li**<sup>*</sup>, Ruizhe Chen, Yuxian Jiang, Tong Zhu, Zhaochen Su, Wenliang Chen, Jing Shao<sup>‡</sup>

ACL 2026

[Paper](https://arxiv.org/pdf/2503.02368)

</div>
</div>
<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/paper_imgs/harmrlvr.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**HarmRLVR: Weaponizing Verifiable Rewards for Harmful LLM Alignment**

Yuexiao Liu<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Xingjun Wang, Jing Shao<sup>‡</sup>

ACL 2026

[Paper](https://arxiv.org/pdf/2510.15499) [Code](https://github.com/lyxx2535/HarmRLVR)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/paper_imgs/treeteaming.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**TreeTeaming: Autonomous Red-Teaming of Vision-Language Models via Hierarchical Strategy Exploration**

Chunxiao Li, **Lijun Li**<sup>‡</sup>, Jing Shao<sup>‡</sup>

CVPR 2026

[Paper](https://arxiv.org/pdf/2603.22882)

</div>
</div>
<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/efficient-agent.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


**Toward Efficient Agents: A Survey of Memory, Tool learning, and Planning**

Xiaofang Yang, Lijun Li<sup>‡</sup>, Heng Zhou, Tong Zhu, Xiaoye Qu, Yuchen Fan, Qianshan Wei, Rui Ye, Li Kang, Yiran Qin, Zhiqiang Kou, Daizong Liu, Qi Li, Ning Ding, Siheng Chen, Jing Shao<sup>‡</sup>

Preprint, 2026

[Paper](https://arxiv.org/pdf/2601.14192) [Project](https://efficient-agents.github.io/) [Code](https://github.com/yxf203/Awesome-Efficient-Agents)

</div>
</div>

<!-- ------------------------------------------------------------- -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026 Findings</div><img src='images/paper_imgs/toolsafe.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback**

Yutao Mou, Zhangchi Xue, Lijun Li<sup>‡</sup>, Peiyang Liu, Shikun Zhang, Wei Ye<sup>‡</sup>, Jing Shao<sup>‡</sup>

ACL 2026

[Paper](https://arxiv.org/pdf/2601.10156) [Code](https://github.com/MurrayTom/ToolSafe) [Guard](https://huggingface.co/MurrayTom/TS-Guard)

</div>
</div>

<!-- ------------------------------------------------------------- -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/proguard.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**ProGuard: Towards Proactive Multimodal Safeguard**

Shaohan Yu<sup>*</sup>, Lijun Li<sup>*‡</sup>, Chenyang Si, Lu Sheng, Jing Shao<sup>‡</sup>

Preprint, 2025

[Paper](https://arxiv.org/pdf/2512.23573) [Code](https://github.com/yushaohan/ProGuard) [Guard-3B](https://huggingface.co/yushaohan/ProGuard-3B) [Guard-7B](https://huggingface.co/yushaohan/ProGuard-7B) [Dataset](https://huggingface.co/datasets/yushaohan/ProGuard-data)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/CIA_attack.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Contextual Image Attack: How Visual Context Exposes Multimodal Safety Vulnerabilities**

Yuan Xiong<sup>*</sup>, Ziqi Miao<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Chen Qian, Jie Li, Jing Shao<sup>‡</sup>

Preprint, 2025

[Paper](https://arxiv.org/pdf/2512.02973) [Code](https://github.com/xiongyuaay/Contextual-Image-Attack)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/star-attack.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**STaR-Attack: A Spatio-Temporal and Narrative Reasoning Attack Framework for Unified Multimodal Understanding and Generation Models**

Shaoxiong Guo<sup>*</sup>, Tianyi Du<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Yuyao Wu, Jie Li, Jing Shao<sup>‡</sup>

Preprint, 2025

[Paper](https://arxiv.org/pdf/2509.26473)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/shadow.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Collaborative Shadows: Distributed Backdoor Attacks in LLM-Based Multi-Agent Systems**

Pengyu Zhu<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Yaxing Lyu<sup>*</sup>, Li Sun, Sen Su<sup>‡</sup>, Jing Shao<sup>‡</sup>

Preprint, 2025

[Paper](https://arxiv.org/pdf/2510.11246) [Code](https://github.com/whfeLingYu/Distributed-Backdoor-Attacks-in-MAS)

</div>
</div>

<!-- ------------------------------------------------------------- -->


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/paper_imgs/mis_bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Rethinking bottlenecks in safety fine-tuning of vision language models**

Yi Ding<sup>*</sup>, **Lijun Li**<sup>*</sup>, Bing Cao<sup>‡</sup>, Jing Shao<sup>‡</sup>

ICLR 2026

[Paper](https://arxiv.org/pdf/2501.18533) [Project](https://dripnowhy.github.io/MIS/) [Data](https://huggingface.co/datasets/Tuwhy/MIS_Train) 

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech report</div><img src='images/paper_imgs/safework-r1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SafeWork-R1: Coevolving Safety and Intelligence under the AI-45◦ Law**

Worked as Co-Leads

Tech report, 2025

[Paper](https://arxiv.org/pdf/2507.18576) 

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Findings</div><img src='images/paper_imgs/rms.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Self-adaptive Dataset Construction for Real-World Multimodal Safety Scenarios**

Jingen Qu<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Bo Zhang, Yichen Yan, Jing Shao<sup>‡</sup>

EMNLP 2025 Findings

[Paper](https://arxiv.org/pdf/2509.04403)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/paper_imgs/response_attack.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Response Attack: Exploiting Contextual Priming to Jailbreak Large Language Models**

Ziqi Miao<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Yuan Xiong, Zhenhua Liu, Pengyu Zhu, Jing Shao<sup>‡</sup>

AAAI, 2026

[Paper](https://arxiv.org/pdf/2507.05248) [Data](https://huggingface.co/datasets/miaozq/RA-SFT)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/paper_imgs/LARF.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment**

Hao Li<sup>*</sup>, **Lijun Li**<sup>*‡</sup>, Zhenghao Lu, Xianyi Wei, Rui Li, Jing Shao<sup>‡</sup>, Lei Sha<sup>‡</sup>

EMNLP 2025

[Paper](https://arxiv.org/pdf/2507.18631) [Code](https://github.com/LLLeoLi/LARF)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/paper_imgs/visco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection**

Ziqi Miao<sup>*</sup>, Yi Ding<sup>*</sup>, **Lijun Li**<sup>‡</sup>, Jing Shao<sup>‡</sup>

EMNLP 2025

[Paper](https://arxiv.org/pdf/2507.02844) [Data](https://huggingface.co/datasets/miaozq/Visco-Attack)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_imgs/worldsimbench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Worldsimbench: Towards video generation models as world simulators**

Yiran Qin<sup>*</sup>, Zhelun Shi<sup>*</sup>, Jiwen Yu, Xijun Wang, Enshen Zhou, **Lijun Li**, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao<sup>‡</sup>, Lei Bai<sup>‡</sup>, Wanli Ouyang, Ruimao Zhang<sup>‡</sup>

ICML 2025

[Paper](https://arxiv.org/pdf/2410.18072) [Project](https://iranqin.github.io/WorldSimBench.github.io/)

</div>
</div>


<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/paper_imgs/t2isafety.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**T2isafety: Benchmark for assessing fairness, toxicity, and privacy in image generation**

**Lijun Li**<sup>*</sup>, Zhelun Shi<sup>*</sup>, Xuhao Hu, Bowen Dong, Yiran Qin, Xihui Liu, Lu Sheng, Jing Shao<sup>‡</sup>

CVPR 2025

[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_T2ISafety_Benchmark_for_Assessing_Fairness_Toxicity_and_Privacy_in_Image_CVPR_2025_paper.pdf) [Data](https://huggingface.co/datasets/OpenSafetyLab/t2i_safety_dataset) [ImageGuard](https://huggingface.co/OpenSafetyLab/ImageGuard)

</div>
</div>

<!-- ------------------------------------------------------------- -->


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024 </div><img src='images/paper_imgs/psysafe.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Psysafe: A comprehensive framework for psychological-based attack, defense, and evaluation of multi-agent system safety**

Zaibin Zhang, Yongting Zhang, **Lijun Li**, Hongzhi Gao, Lijun Wang, Huchuan Lu, Feng Zhao, Yu Qiao, Jing Shao

🎖️ACL 2024 Outstanding Paper

[Paper](https://aclanthology.org/2024.acl-long.812.pdf) [Code](https://github.com/AI4Good24/PsySafe)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024 Findings</div><img src='images/paper_imgs/salad-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models**

**Lijun Li**<sup>*</sup>, Bowen Dong<sup>*</sup>, Ruohui Wang<sup>*</sup>, Xuhao Hu<sup>*</sup>, Wangmeng Zuo, Dahua Lin, Yu Qiao, Jing Shao<sup>‡</sup>

ACL 2024 Findings

[Paper](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) [Project](https://adwardlee.github.io/salad_bench/) [Code](https://github.com/OpenSafetyLab/SALAD-BENCH)   [Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)  [MD-Judge](https://huggingface.co/OpenSafetyLab/MD-Judge-v0_2-internlm2_7b) [Leaderboard](https://huggingface.co/spaces/OpenSafetyLab/Salad-Bench-Leaderboard)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/easyjailbreak.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**EasyJailbreak: A Unified Framework for Jailbreaking Large Language Models**

Weikang Zhou, Xiao Wang, Limao Xiong, Han Xia, Yingshuang Gu, Mingxu Chai, Fukang Zhu, Caishuang Huang, Shihan Dou, Zhiheng Xi, Rui Zheng, Songyang Gao, Yicheng Zou, Hang Yan, Yifan Le, Ruohui Wang, **Lijun Li**, Jing Shao, Tao Gui, Qi Zhang, Xuanjing Huang

Preprint, 2024

[Paper](https://arxiv.org/pdf/2403.12171) [Project](http://easyjailbreak.org/) [Code](https://github.com/EasyJailbreak/EasyJailbreak)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/ch3ef.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Assessment of multimodal large language models in alignment with human values**

Zhelun Shi, Zhipin Wang, Hongxing Fan, Zaibin Zhang, **Lijun Li**, Yongting Zhang, Zhenfei Yin, Lu Sheng, Yu Qiao, Jing Shao

Preprint, 2024

[Paper](https://arxiv.org/pdf/2403.17830) [Project](https://openlamm.github.io/ch3ef/) [Code](https://github.com/OpenGVLab/LAMM)

</div>
</div>

<!-- ------------------------------------------------------------- -->


<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2023</div><img src='images/paper_imgs/renderih.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Renderih: A large-scale synthetic dataset for 3d interacting hand pose estimation**

**Lijun Li**<sup>‡</sup>, Linrui Tian, Xindi Zhang, Qi Wang, Bang Zhang, Liefeng Bo, Mengyuan Liu, Chen Chen

ICCV 2023

[Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_RenderIH_A_Large-Scale_Synthetic_Dataset_for_3D_Interacting_Hand_Pose_ICCV_2023_paper.pdf) [Code](https://github.com/adwardlee/RenderIH) [Imgs](https://drive.google.com/file/d/1nl5VZvnKN3SIJnBOis4rfsuG_DT0smLl/view?usp=drive_link) [Annotations](https://drive.google.com/file/d/1wOuZTgWODhyelLXJr7Kv9tuEiFxcWIif/view?usp=drive_link)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper_imgs/action_detection.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**One-stage Action Detection Transformer**

**Lijun Li**, Li'an Zhuo, Bang Zhang

🎖️Winning solution for Action Detection Track of EPIC@CVPR2022

[Paper](https://arxiv.org/pdf/2206.10080)

</div>
</div>

<!-- ------------------------------------------------------------- -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2019</div><img src='images/paper_imgs/nattack.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Nattack: Learning the distributions of adversarial examples for an improved black-box attack on deep neural networks**

Yandong Li<sup>*</sup>, **Lijun Li**<sup>*</sup>, Liqiang Wang, Tong Zhang, Boqing Gong

ICML 2019

[Paper](https://proceedings.mlr.press/v97/li19g/li19g.pdf) [Code](https://github.com/adwardlee/Nattack)

</div>
</div>

<!-- ------------------------------------------------------------- -->

# 🖊️ Research Experiences
- 2023 - Present, Researcher, Shanghai AI Lab, Beijing, China.
- 2021 - 2023, Researcher, DAMO Academy, Alibaba, Beijing, China.

# 🎖 Honors and Awards
- ACL 2024 outstanding paper
- 1st at [Action Detection track on CVPR 2022 EPIC Kitchens](https://epic-kitchens.github.io/2022)
- 2nd at [FreiHand Challenge](https://competitions.codalab.org/competitions/21238#results)
- 9/200 at [AI for prosthetics](https://www.aicrowd.com/challenges/neurips-2018-ai-for-prosthetics-challenge)
- Outstanding Graduate Student 
- National scholarship


# 💬 Invited Talks
- *2024.11*, [ACL2024 Benchmarks Introduction](https://www.bilibili.com/video/BV1KimoYaExY/) hosted by [Opencompass](https://opencompass.org.cn/)
- *2022.06*, [Winner talk of EPIC-KITCHENS 2022 Challenges at CVPR 2022](https://www.youtube.com/watch?v=kLRn-Q48hr0)

# 👨‍🔧 Academic Services
- 2024.07, Workshop Organizer, ICML 2024 workshop on [Trustworthy Multi-modal Foundation Models and AI Agents (TiFA)](https://icml-tifa.github.io/)
- Area Chair for ARR since 2025
- Reviewer for ICLR/ICML/NIPS/CVPR/ICCV/ARR since 2023


<div id="clustrmaps-container" style="width: 250px; height: 250px; overflow: hidden; display: inline-block;">
  <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=iyHOuSXOuyzJU7Wg20gI3dp8vVRLSMxuGfvfe03TqWo"></script>
</div>
<style>
#clustrmaps-container > * {
  transform: scale(1); /* 缩小到50%，可根据需要调整 */
  transform-origin: top left;
  display: block;
}
</style>
