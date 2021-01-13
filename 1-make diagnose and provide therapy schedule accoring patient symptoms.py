#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 功能：根据患者症状，做出诊断，并统计治疗方案
# 示例：如果只有发热、寒颤，就诊断为感冒；如果只有鼻塞、咳嗽，就诊断为肺炎; 全有的话，可能性各50%
# 来源：

# 定义症状
symptoms = ['fever', 'chill', 'stuffy', 'cough']

# 定义诊断依据，如果只有发热、寒颤，就诊断为感冒；如果只有鼻塞、咳嗽，就诊断为肺炎
diagnoses = {
    'cold': ['fever', 'chill'],
    'pneumonia': ['stuffy', 'cough'],
}

# 定义治疗方案
therapy = {
    'cold': {
        'doctor1': '吃点辣椒',
        'doctor2': '煮点姜汤',
        'docror3': '放点冰块'
    },
    'pneumonia': {
        'doctor1': '多休息',
        'doctor2': '多喝水'
    }
}

# 输入病人症状
string_symptom = str(input('请输入病人症状字符串，长度4位，每位代表是否发烧、寒颤、鼻塞、咳嗽，例如4项症状都有对应的字符串为1111，有发热、有寒颤、无鼻塞、无咳嗽的字符串为1100，依此类推：'))

# 得到病人症状列表
patient_symptoms = [symptoms[i] for i, bit in enumerate(string_symptom) if bit == '1']

# 得到诊断结果列表
result = [diag_name for diag_name, diag_symptoms in  diagnoses.items() if set(diag_symptoms) <= set(patient_symptoms)]

# 输出诊断结果并给出诊断方案。如果只有发热、寒颤，就诊断为感冒；如果只有鼻塞、咳嗽，就诊断为肺炎；如果4项症状全有，可能性各占50%
if len(result) == 1:
    print('诊断结果为：'+result[0]+'，可能性90%，这是各位医生给出的治疗方案：')
    print(therapy[result[0]])

else if len(result) == 2:
    print('诊断结果为: '+result[0]+'可能性50%，'+result[1]+'可能性50%。')
    print('对于'+result[0]+'，这是各位医生给出的治疗方案：')
    print(therapy[result[0]])
    print('对于'+result[1]+'，这是各位医生给出的治疗方案：')
    print(therapy[result[1]])
else:
    print('没有找到对应的诊断结果，请丰富数据库')

#  do some analyze here 此处做一些分析
#  get some result here 此处生成一些结果




