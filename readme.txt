1.创建虚拟环境
  mamba create -n "omni" python==3.10
  conda activate omni

2.使用mamba安装
  mamba install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia

3.安装剩余依赖
  调整依赖文件requirements.txt，移除torch，torchvision
  python -m pip install uv
  uv pip install -r requirements.txt

4.处理报错
  # 在gradio_demo.py中添加
  import os
  os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

5.运行gradio_demo.py
  python gradio_demo.py