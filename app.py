import os
from PIL import Image
import streamlit as st
import tempfile

st.set_page_config(page_title="make icon", page_icon="✅")

ICON_SIZES = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]

def convert_to_icon(image_path):
    image = Image.open(image_path)
    image = image.resize((256, 256), resample=Image.BICUBIC)
   
    # 파일명 생성
    file_name, file_ext = os.path.splitext(os.path.basename(image_path))
    icon_path = os.path.join(os.path.dirname(image_path), f"{file_name}.ico") 
    
    # 아이콘 파일 저장
    image.save(icon_path, format="ICO")
    return os.path.splitext(image_path)[0] + ".ico"

def main():
    st.title(":white_check_mark: make icon")

    # 파일 업로드 창 생성
    uploaded_file = st.file_uploader("", type=[".jpg", ".jpeg", ".png", ".bmp", ".gif"])

    if uploaded_file is not None:
        temp_dir = tempfile.TemporaryDirectory()
        # 파일 경로 생성
        temp_filepath = os.path.join(temp_dir.name, uploaded_file.name)
        with open(temp_filepath, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # 아이콘 변환
        icon_path = convert_to_icon(temp_filepath)

        # 다운로드 링크 생성
        st.download_button(
            label="다운로드",
            data=open(icon_path, "rb").read(),
            file_name=uploaded_file.name + ".ico",
            mime="image/x-icon",
        )

        #image
        icon_sizes = [16, 32, 48, 64, 128, 256]
        cols = st.columns([max(48, size) for size in icon_sizes])
        for i, icon_size in enumerate(icon_sizes):
            with cols[i]:
                st.write("{0}X{0}".format(icon_size))
                st.image(icon_path, width=icon_size)
if __name__ == "__main__":
    main()
