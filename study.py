# import os
# import nibabel as nib
# import matplotlib.pyplot as plt
# import numpy as np
# from monai.apps import download_and_extract

# root = os.path.expanduser(r"E:\3D")
# os.makedirs(root, exist_ok=True)

# # (1) MSD Spleen 데이터 URL
# # url = "https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar"

# # # (2) 최신 방식 (root_dir 대신 output_dir 사용)
# # download_and_extract(url, output_dir=root)

# # (3) 첫 번째 볼륨 로드
# img_path = os.path.join(root, "Task09_Spleen", "imagesTr", "spleen_2.nii.gz")
# img = nib.load(img_path).get_fdata()

# # 2D 슬라이스 보기
# mid = img.shape[2] // 2
# plt.figure(figsize=(6, 6))
# plt.imshow(
#     img[:, :, mid], cmap="gray", origin="upper", interpolation="nearest", aspect="equal"
# )
# plt.title(f"Slice {mid} (raw orientation)")
# plt.axis("off")
# plt.show()

# # ===== 3D 인터랙티브 보기 (napari) =====
# try:
#     import napari

#     nii = nib.load(img_path)
#     vol = nii.get_fdata().astype(np.float32)
#     voxel = nii.header.get_zooms()[:3]  # (sx, sy, sz) 간격

#     viewer = napari.Viewer(ndisplay=3)  # 3D 모드
#     viewer.add_image(
#         vol,
#         name="Spleen",
#         scale=voxel,
#         rendering="mip",  # "mip", "attenuated_mip", "translucent" 등
#         contrast_limits=(float(vol.min()), float(vol.max())),
#     )
#     napari.run()
# except Exception as e:
#     print("napari 3D 뷰어 실행 실패:", e)


import nibabel as nib

epi_img = nib.load(r"E:\3D\Task09_Spleen\imagesTr\spleen_2.nii.gz")
epi_img_data = epi_img.get_fdata()

slice0 = epi_img_data[26, :, :]
slice1 = epi_img_data[:, 30, :]
slice2 = epi_img_data[:, :, 16]

import nibabel as nib
import matplotlib.pyplot as plt

epi_img = nib.load(r"E:\3D\Task09_Spleen\imagesTr\spleen_2.nii.gz")
epi_img_data = epi_img.get_fdata()

# slice0 = epi_img_data[100, :, :]
# slice1 = epi_img_data[:, 100, :]
slice0 = epi_img_data[:, :, 1]
slice1 = epi_img_data[:, :, 20]
slice2 = epi_img_data[:, :, 40]

plt.imshow(slice2, cmap="gray")
plt.title("Axial View")
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(slice0, cmap="gray")
axes[0].set_title("Axial 1 View")

axes[1].imshow(slice1, cmap="gray")
axes[1].set_title("Axial 20 View")

axes[2].imshow(slice2, cmap="gray")
axes[2].set_title("Axial 40 View")

plt.show()
