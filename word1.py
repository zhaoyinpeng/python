import docx
doc2 = docx.Document()  # 创建一个Document对象
doc2.add_paragraph('time')  # 增加一个paragraph
# 插入有序列表,段落的前面会有序号123
doc2.add_paragraph('把冰箱门打开', style='List Number')
doc2.add_paragraph('把大象装进去', style='List Number')
doc2.add_paragraph('把冰箱门关上', style='List Number')
# 插入无序列表，段落的前面没有序号
doc2.add_paragraph('把冰箱门打开2', style='List Bullet')
doc2.add_paragraph('把大象装进去2', style='List Bullet')
doc2.add_paragraph('把冰箱门关上', style='List Bullet')
# 插入一个6行6列的表格
table = doc2.add_table(rows=6, cols=6, style='Table Grid')
for i in range(0, 6):
    for j in range(0, 6):
        table.cell(i, j).text = "第{i}行{j}列".format(i=i+1, j=j+1)
for i in range(0, 6):
　　　for j in range(0, 6):
　　　　　　table.cell(i, j).text = "第{i}行{j}列".format(i=i+1, j=j+1)
# 插入照片
# doc2.add_picture('.\\timg(1).jpg', width=docx.shared.Inches(5))
doc2.save('a.docx')  # 保存文档
