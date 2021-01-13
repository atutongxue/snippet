#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 功能：根据患者症状，做出诊断，并统计治疗方案
# 示例：如果只有发热、寒颤，就诊断为感冒；如果只有鼻塞、咳嗽，就诊断为肺炎; 全有的话，可能性各50%
# 来源：https://github.com/atutongxue/snippet/blob/main/python/1-make-diagnose-and-provide-therapy-schedule-according-patient-symptoms.py

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
print('为方便输入，病人症状由4位二进制字符串表示，每位代表是否有发热、寒颤、鼻塞、咳嗽症状，有症状为1，无症状为0。')
print('例如有发热、有寒颤、无鼻塞、无咳嗽，输入1100，4项症状都有，输入1111，依此类推。')
string_symptom = str(input('在这里输入4位二进制字符串：'))

# 得到病人症状列表
patient_symptoms = [symptoms[i] for i, bit in enumerate(string_symptom) if bit == '1']

# 得到诊断结果列表
result = [diag_name for diag_name, diag_symptoms in  diagnoses.items() if set(diag_symptoms) <= set(patient_symptoms)]

# 输出诊断结果并给出诊断方案。如果只有发热、寒颤，就诊断为感冒；如果只有鼻塞、咳嗽，就诊断为肺炎；如果4项症状全有，可能性各占50%
if len(result) == 1:
    print('\n诊断结果为：'+result[0]+'，可能性90%，这是各位医生给出的治疗方案：')
    print(therapy[result[0]])

elif len(result) == 2:
    print('\n诊断结果为: '+result[0]+'可能性50%，'+result[1]+'可能性50%。')
    print('对于'+result[0]+'，这是各位医生给出的治疗方案：')
    print(therapy[result[0]])
    print('对于'+result[1]+'，这是各位医生给出的治疗方案：')
    print(therapy[result[1]])
else:
    print('\n没有找到对应的诊断结果，请丰富数据库')

#  do some analyze here 此处做一些分析
#  get some result here 此处生成一些结果

input("\n程序运行完毕，按[回车键]结束...")
