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


# omnitool/omnibox
1.启动Docker Desktop
2.运行manage_vm.ps1 create
  到docker desktop查看容器的启动日志，可能会各种原因导致启动失败，比如内存不足，compose.yml文件调整一下,8G改为6G
3.运行manage_vm.ps1 start
4.运行manage_vm.ps1 stop
5.运行manage_vm.ps1 delete


