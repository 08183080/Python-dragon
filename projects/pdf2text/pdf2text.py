import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(total_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                txt_file.write(text)

    print('PDF转换为文本成功！')

# 调用函数示例
pdf_path = 'D:\\Python-dragon\\Python-dragon\\projects\\pdf2text\\Redis 3.0 中文版 - v1.1.pdf'
txt_path = 'D:\\Python-dragon\\Python-dragon\\projects\\pdf2text\\Redis 3.0 中文版 - v1.1.txt'
pdf_to_txt(pdf_path, txt_path)