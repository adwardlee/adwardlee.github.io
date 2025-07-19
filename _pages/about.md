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
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi there! I am now an Researcher at Shanghai AI Lab. Before joining Shanghai AI Lab, I was a Research Engineer at Machine Intelligence Technology Lab, DAMO Academy, Alibaba Group, under the guidance of [Rong Jin](https://scholar.google.com/citations?hl=zh-CN&user=CS5uNscAAAAJ) and [Ping Tan](https://pingtan.people.ust.hk/index.html). I have been engaged in AI research and development since 2019. I am fortunate to have gained industry experience at [Alibaba DAMO Academy](https://damo.alibaba.com/?language=en), [Tencent AI Lab](https://ailab.tencent.com/ailab/en/index/), and Baidu IDL.

_If interested in collaboration or discussion, please email me._

# 🔭 Research Interest

My research interests broadly lie in the areas of AI Safety and vision understanding. My goal is to build Safety capability balanced Artificial General Intelligence. To achieve this goal, my work focuses on first better understanding and then discover the safety vuneralibilities and make Safe AI from the very first begining. .


# 🔥 News
- *2025.05*: 🎉 Our paper [WorldSimBench](https://arxiv.org/pdf/2410.18072) has been accepted by ICML 2025.
- *2025.02*: 🎉 Our paper [T2ISafety](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_T2ISafety_Benchmark_for_Assessing_Fairness_Toxicity_and_Privacy_in_Image_CVPR_2025_paper.pdf) has been accepted by CVPR 2025. 
- *2024.05*: 🎉 Our paper [SALAD-Bench](https://aclanthology.org/2024.findings-acl.235.pdf) and [PsySafe](https://aclanthology.org/2024.acl-long.812.pdf) have been accepted by ACL 2024
- *2023*: 🎉 Our paper [RenderIH](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_RenderIH_A_Large-Scale_Synthetic_Dataset_for_3D_Interacting_Hand_Pose_ICCV_2023_paper.pdf) has been accepted by ICCV 2023.
- *2022.05*: 🎉🎉 We rank 1st at the Action Detection track of [EPIC@CVPR2022 Workshop](https://epic-kitchens.github.io/2022#results)

- *2022.04*：🎉 We rank 2nd at the [FreiHAND Competition](https://competitions.codalab.org/competitions/21238)

# 📝 Publications 
Topics: AI Safety/ Agent / Understanding

(*: indicates equal contribution; ‡: indicates corresponding)

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/t2isafety.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Worldsimbench: Towards video generation models as world simulators**

Yiran Qin<sup>*</sup>, Zhelun Shi<sup>*</sup>, Jiwen Yu, Xijun Wang, Enshen Zhou, **Lijun Li**, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao<sup>‡</sup>, Lei Bai<sup>‡</sup>, Wanli Ouyang, Ruimao Zhang<sup>‡</sup>

ICML 2025

[Paper](https://arxiv.org/pdf/2410.18072) | [Project](https://iranqin.github.io/WorldSimBench.github.io/) | [ImageGuard](https://huggingface.co/OpenSafetyLab/ImageGuard)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/t2isafety.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**T2isafety: Benchmark for assessing fairness, toxicity, and privacy in image generation**

**Lijun Li**<sup>*</sup>, Zhelun Shi<sup>*</sup>, Xuhao Hu, Bowen Dong, Yiran Qin, Xihui Liu, Lu Sheng, Jing Shao<sup>‡</sup>

CVPR 2025

[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_T2ISafety_Benchmark_for_Assessing_Fairness_Toxicity_and_Privacy_in_Image_CVPR_2025_paper.pdf) | [Data](https://huggingface.co/datasets/OpenSafetyLab/t2i_safety_dataset) | [ImageGuard](https://huggingface.co/OpenSafetyLab/ImageGuard)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/mis_bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Rethinking bottlenecks in safety fine-tuning of vision language models**

Yi Ding<sup>*</sup>, **Lijun Li**<sup>*</sup>, Bing Cao<sup>‡</sup>, Jing Shao<sup>‡</sup>

Preprint, 2025

[Paper](https://arxiv.org/pdf/2501.18533) | [Project](https://dripnowhy.github.io/MIS/) | [Data](https://huggingface.co/datasets/Tuwhy/MIS_Train) 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024 Findings</div><img src='images/salad-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models**

**Lijun Li**<sup>*</sup>, Bowen Dong<sup>*</sup>, Ruohui Wang<sup>*</sup>, Xuhao Hu<sup>*</sup>, Wangmeng Zuo, Dahua Lin, Yu Qiao, Jing Shao<sup>‡</sup>

ACL 2024 Findings

[Paper](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) | [Project](https://adwardlee.github.io/salad_bench/) | [Code](https://github.com/OpenSafetyLab/SALAD-BENCH) |   [Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)  | [MD-Judge](https://huggingface.co/OpenSafetyLab/MD-Judge-v0_2-internlm2_7b) | [Leaderboard](https://huggingface.co/spaces/OpenSafetyLab/Salad-Bench-Leaderboard)

</div>
</div>

**Nattack: Learning the distributions of adversarial examples for an improved black-box attack on deep neural networks**

Yandong Li<sup>*</sup>, **Lijun Li**<sup>*</sup>, Liqiang Wang, Tong Zhang, Boqing Gong

ICML 2019

[Paper](https://proceedings.mlr.press/v97/li19g/li19g.pdf) | [Code](https://github.com/adwardlee/Nattack)



# 🖊️ Research Experiences
- 2023 - Present, Researcher, Shanghai AI Lab, Beijing, China.
- 2021 - 2023， Researcher， DAMO Academy， Alibaba， Beijing, China.

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
- Reviewer for ICLR/ICML/NIPS/CVPR/ICCV since 2023