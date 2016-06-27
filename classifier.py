
# coding: utf-8

# In[28]:

import pandas as pd
from pandas import DataFrame as df
import xml.etree.ElementTree as ET
import numpy as np
import os
import re


# In[ ]:




# In[29]:

DATE_TEMPLATE = re.compile(r'\d{2}\.\d{2}\.\d{4}')

INPUT_FILE = os.path.normpath(r'IO\output.xml')
PREPROCESSED_INPUT = os.path.normpath(r'IO\preprocessed_input.txt')
OUTPUT_EXCEL = os.path.normpath(r'IO\report.xlsx')


# In[30]:

tree = ET.parse(INPUT_FILE)

строки_с_ошибками = dict()

root = tree.getroot()
r = root.findall("Lead")

def make_dict_of_leads(root=root):
    dict_of_leads = dict();
    for lead in root.iter('Lead'):
        id = lead.attrib["id"]

        pulpy = ET.fromstring(lead.attrib["text"])
        source_sentence = pulpy.find("b").find("s")

        remove_explicit_from_sentence(source_sentence)

        text = ''.join(source_sentence.itertext())
        dict_of_leads[id] = re.sub(r'\.$', '', text.strip());
    return dict_of_leads

def remove_explicit_from_sentence(xml_sentence):
    
    def remove_target_node(xml_sentence, target_template):
        for node in xml_sentence:
            if re.search(target_template, node.attrib["lemma"]):
                node.text = ''

    # to remove
    phoneno = re.compile(r'\d{8,12}')
    date = DATE_TEMPLATE

    remove_target_node(xml_sentence, phoneno)
    remove_target_node(xml_sentence, date)
    

"""
   <b>
      <s>
         21.06.2016
         <P n0="" lemma="89140580517">89140580517</P>
         хочет
         <W n1="" lemma="buy">купить</W>
         <W n2="" lemma="ноутбук">ноутбук</W>
         за 17000 руб ездить
         <P n3="" lemma="Якутия">Якутия</P>
         .
      </s>
   </b>
"""


# In[31]:

# todo: помнить о тексте лида. Там выделены факты прямо в разметке - полезно при выводе информации в веб-интерфейсе

def compare_facts_to_leads(root=root):
    facts_grouped_by_lead = dict()

    for i in root.find("document").find('facts'):
        lead_id = i.attrib['LeadID']
        if facts_grouped_by_lead.get(lead_id):
            facts_grouped_by_lead[lead_id].append(i)
        else:
            facts_grouped_by_lead[lead_id] = [i]
    return facts_grouped_by_lead

def make_common_table():
    appendix = [
        "CustomerBuys_Word",
        "CustomerSells_Word",
        "Pawn_Word",
        "Repare_Word",
        "Matter_Notebook",
        "Matter_Phone",
        "Matter_Tablet",
        "Matter_TV",
        "Matter_Other",
        "CustomerPlace_Yakutia",
        "CustomerPlace_Buryatia",
        "Communication_SMS",
        "Communication_WhatsApp",
     ]
    calls = df(columns=appendix)
    
    facts = compare_facts_to_leads()
    leads = make_dict_of_leads()

    for lead in facts:
        try:
            elems = facts[lead]
            one_sentence = leads[lead]
            cols = ["lead_id", "conversation"]
            values = [lead, one_sentence]
            for fact_name in elems:
                for fact_field in fact_name:
                    cols.append(fact_name.tag + "_" + fact_field.tag)
                    values.append(fact_field.attrib["val"])
            one_row = pd.DataFrame([values], columns=cols)
            calls = calls.append(one_row)

            values = []
            cols = []
        except ValueError as e:
            print(e)
            lineno = str(int(lead) + 2)
            строки_с_ошибками[int(lead) + 2] = leads[lead]
            print("Ошибка в строке " + lineno + " исходных данных.\n", leads[lead])
        except AssertionError as e:
            print(e)
            lineno = str(int(lead) + 2)
            строки_с_ошибками[int(lead) + 2] = leads[lead]
            print("Ошибка в строке " + lineno + " исходных данных.\n", leads[lead])

    calls["lead_id"] = calls["lead_id"].map(int)
    calls = calls.sort_values(by="lead_id")
    calls = calls.set_index("lead_id")
    return calls


# In[32]:

calls = make_common_table()


# In[33]:

# Выбираю тут колонки, которые 

cols_for_ykt = [
    # Колонки, полученные из названий фактов
    [
        "CallDate_Date",
        "CustomerPhone_Phone",
        "Matter_Notebook",
        "Matter_Tablet",
        "Matter_Phone",        
        "Matter_TV",
        "Matter_Other",
        "conversation",
        "Комплектация",
        "Цена клиента",
        "Наша цена",
        "Утилизация",
        "Решение клиента",
    ],

    # Колонки, в которые будут переименованы верхние, исходные колонки
    [
        "Дата",
        "Номер телефона",
        "Ноутбук/нетбук",
        "Планшет",
        "Телефон",        
        "Телевизор",
        "Другое",
        "Разговор",
        "Комплектация",
        "Цена клиента",
        "Наша цена",
        "Утилизация",
        "Решение клиента",
    ]
]


# In[34]:

# Подготовка вывода для листа "Бурятия"

# todo действие по умолчанию - купить. Собрать такие графы, в которых нет действия, в таблицу "Купить" - клиент покупает у нас
# todo ремонт только телефонов и ноутбуков - объединить всё, кроме телефонов и ноутбуков в графу "Другое"

def join_other_matters(source_df, cols, new_name):
    matter_other = df(index=source_df.index, columns=[new_name])

    for matter in cols:
        matter_other[new_name] = matter_other[new_name].dropna().append(source_df[matter].dropna())

    source_df = pd.concat([source_df, matter_other], axis=1)
    return source_df

def extract_and_rename(source_df, cols):
    extracted = df(source_df, columns=cols[0])
    extracted.columns=cols[1]
    return extracted

def prepare_for_excel_ykt(source_df, col_name, output_cols):
    yakutia = source_df[source_df.CustomerPlace_Buryatia.isnull()]
    yakutia = yakutia[yakutia.Communication_SMS.isnull() & yakutia.Communication_WhatsApp.isnull()]
    actions = yakutia[yakutia[col_name].notnull()]
    return extract_and_rename(actions, output_cols)

def prepare_for_buryatia(all_calls, cols):
    # Звонки из Бурятии
    calls_from_buryatia = all_calls[all_calls.CustomerPlace_Buryatia.notnull()]
    
    # Группирую все предметы кроме usial_matter в отдельный список для объединения в одной колонке
    usial_matter = ["Matter_Notebook", "Matter_Phone", "Matter_Tablet"]
    matter_except_usial = [col for col in calls_from_buryatia.columns if col.startswith("Matter") and col not in usial_matter]
    
    calls_buryatia_joined = join_other_matters(calls_from_buryatia, matter_except_usial, "Комплектующее")
    if not calls_buryatia_joined.empty:
        return extract_and_rename(calls_buryatia_joined, cols)
    else:
        return calls_from_buryatia

def prepare_for_smswhatsapp(all_calls):
    cols = ["Communication_WhatsApp", "Communication_SMS"]
    all_calls["smswhatsapp"] = all_calls["Communication_WhatsApp"].append(all_calls["Communication_SMS"]).dropna()
    smswhatsapp = all_calls[all_calls["smswhatsapp"].notnull()]
    return extract_and_rename(smswhatsapp, cols_for_buryatia)



# In[35]:

# cols = matter_except_usial
# new_name = "Комплектующее"
# source_df = calls_from_buryatia

# matter_other = df(index=source_df.index, columns=[new_name])

# matter_other[new_name] = matter_other[new_name].dropna().append(source_df["Matter_TV"].dropna())
# matter_other[new_name] = matter_other[new_name].dropna().append(source_df["Matter_Other"].dropna())
# matter_other

# pd.concat([source_df, matter_other], axis=1)


# In[36]:

cols_for_buryatia = [
    [
        "CallDate_Date",
        "CustomerPhone_Phone",
        "Matter_Notebook",
        "Matter_Tablet",
        "Matter_Phone",
        "Комплектующее",
        "conversation",
        "Комплектация",
        "Цена клиента",
        "Наша цена",
        "Утилизация",
        "Решение клиента",
    ],

    [
        "Дата",
        "Номер телефона",
        "Ноутбук/нетбук",
        "Планшет",
        "Телефон",
        "Другое",
        "Разговор",
        "Комплектация",
        "Цена клиента",
        "Наша цена",
        "Утилизация",
        "Решение клиента",
    ]
]


# In[37]:

def make_excel():
    calls = make_common_table()
    
    writer = pd.ExcelWriter(OUTPUT_EXCEL)

    vikup = prepare_for_excel_ykt(calls, "CustomerSells_Word", cols_for_ykt)
    prodazha = prepare_for_excel_ykt(calls, "CustomerBuys_Word", cols_for_ykt)
    remont = prepare_for_excel_ykt(calls, "Repare_Word", cols_for_ykt)
    lombard = prepare_for_excel_ykt(calls, "Pawn_Word", cols_for_ykt)
    buryatia = prepare_for_buryatia(calls, cols_for_buryatia)
    smswhatsapp = prepare_for_smswhatsapp(calls)

    vikup.to_excel(writer, sheet_name = "Выкуп", index=False)
    prodazha.to_excel(writer, sheet_name = "Продажа", index=False)
    remont.to_excel(writer, sheet_name = "Ремонт", index=False)
    lombard.to_excel(writer, sheet_name = "Ломбард", index=False)
    buryatia.to_excel(writer, sheet_name = "Бурятия", index=False)
    smswhatsapp.to_excel(writer, sheet_name = "smswhatsapp", index=False)
    writer.save()


# In[38]:

def report():
    with open(PREPROCESSED_INPUT) as f:
        source_file = f.read().splitlines()

    percent_of_handled = len(calls) / len(source_file) * 100
    print("Процент успешно обработанных данных:", percent_of_handled)
    print("Строки с ошибками (необработано): ", строки_с_ошибками)


# In[39]:

def classify():
    make_excel()
    report()


# In[40]:

if __name__ == "__main__":
    classify()


# In[ ]:



