# 论文所用数据
## 1. 各模型历史数据
| 模型名称           | Params     | MACs       | PCK   | FPS      |
| ------------------ | ---------- | ---------- | ----- | -------- |
| MobileNetV3-normal | **5.285M** | **3.814G** | 0.65  | **28.5** |
| MobileNetV3-large  | 10.871M    | 4.053G     | 76.43 | 22.7     |
| MFNet-large        | 5.464M     | 8.841G     | 0.76  | 23.8     |

## 2. 各模型关键点数据
| 模型名称    | Head  | Shoulder | Elbow | Wrist | Hip   | Knee  | Ankle | Mean  |
| ----------- | ----- | -------- | ----- | ----- | ----- | ----- | ----- | ----- |
| MFNet-large | 92.91 | 87.89    | 74.72 | 65.16 | 76.07 | 67.49 | 64.55 | 76.43 |
| MFNet       | 0.273 | 0.000    | 0.699 | 0.000 | 1.523 | 0.181 | 0.780 | 0.515 |
## 3. 其他SOTA数据 MPII
| 模型名称                 | Params | MACs   | AP   | FPS      |
| ------------------------ | ------ | ------ | ---- | -------- |
| Simple baseline[256x256] | 34.0M  | --     | 0.65 | **28.5** |
| HRNet[256x256]           | 28.5M  | --     | 90.3 | 22.7     |
| AlphaPose                | 5.464M | 8.841G | 76.7 | 23.8     |

## 4. 大纲
### 1 引言
### 2 相关工作
    简要介绍姿态估计任务，难点与挑战，对近期姿态估计相关技术简要进行综述。
### 3 多尺度空间特征姿态估计
    多尺度特征融合，空间特征利用，深度可分离卷积
### 4 实验
    MPII数据集介绍， 实验结果，消融实验
### 结束语
    总结
### reference