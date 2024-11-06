import pymupdf
import json
doc = pymupdf.open("test.pdf")
page_no = 0
for page in doc:
	page_no += 1
	word_list = page.get_text("blocks")
	page_list = []
	for i in word_list:
		page_list.append({"bbox": list(i[0:4]), "text": i[4]})
	page_json = json.dump(page_list, open("test_page-000" + str(page_no) + "_words.json", "w"))
