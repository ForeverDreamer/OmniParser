import os

from huggingface_hub import hf_hub_download


def download_omniparser_weights():
    # 创建保存权重的目录
    base_dir = "weights"
    os.makedirs(base_dir, exist_ok=True)

    # 需要下载的文件列表
    icon_detect_files = [
        "icon_detect/train_args.yaml",
        "icon_detect/model.pt",
        "icon_detect/model.yaml",
    ]

    icon_caption_files = [
        "icon_caption/config.json",
        "icon_caption/generation_config.json",
        "icon_caption/model.safetensors",
    ]

    # 下载 icon_detect 文件
    for file in icon_detect_files:
        hf_hub_download(
            repo_id="microsoft/OmniParser-v2.0", filename=file, local_dir=base_dir
        )

    # 下载 icon_caption 文件
    for file in icon_caption_files:
        hf_hub_download(
            repo_id="microsoft/OmniParser-v2.0", filename=file, local_dir=base_dir
        )

    # 重命名 icon_caption 目录
    old_path = os.path.join(base_dir, "icon_caption")
    new_path = os.path.join(base_dir, "icon_caption_florence")
    if os.path.exists(old_path):
        os.rename(old_path, new_path)


if __name__ == "__main__":
    download_omniparser_weights()
