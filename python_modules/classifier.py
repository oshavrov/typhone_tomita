
# coding: utf-8

# In[58]:

import pandas as pd
from pandas import DataFrame as df
import xml.etree.ElementTree as ET
import numpy as np
import os
import re
from python_modules.constants import *


# In[ ]:




# In[59]:

DATE_TEMPLATE = re.compile(r'\d{2}.\d{2}.\d{4}')

INPUT_FILE = os.path.normpath(r'IO\output.xml')
PREPROCESSED_INPUT = os.path.normpath(r'IO\preprocessed_input.txt')
OUTPUT_EXCEL = os.path.normpath(r'IO\report.xlsx')
DEBUG_EXCEL = os.path.normpath(r'debug\common_table.xlsx')
SAME_CATEGORY_DELIMITER = r'__'
EMPTY_COLS = ["Комплектация", "Цена клиента", "Наша цена", "Утилизация", "Решение клиента"]


# In[60]:

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
        dict_of_leads[id] = re.sub(r'\.+$', '', text.strip());
    return dict_of_leads

def remove_explicit_from_sentence(xml_sentence):
    
    def remove_target_node(xml_sentence, target_template):
        for node in xml_sentence:
            if re.search(target_template, node.attrib["lemma"]):
                node.text = ''

    # to remove
    phoneno = re.compile(r'\d{9,12}')
    date = DATE_TEMPLATE
    remove_target_node(xml_sentence, date)
    remove_target_node(xml_sentence, phoneno)

    
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


# In[61]:

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
    calls = df()
    
    facts = compare_facts_to_leads()
    leads = make_dict_of_leads()

    for lead in facts:
        try:
            elems = facts[lead]
            one_sentence = leads[lead]
            cols = ["lead_id", "conversation"]
            values = [lead, one_sentence]
            fact_num = 0;
            for fact in elems:
                for fact_field in fact:
                    fact_name = fact.tag + "_" + fact_field.tag
                    if fact_name not in cols:
                        fact_num = 0;
                    else:
                        fact_name += SAME_CATEGORY_DELIMITER + str(fact_num )
                        fact_num += 1
                    cols.append(fact_name)
                    values.append(fact_field.attrib["val"])
            one_row = pd.DataFrame([values], columns=cols)
            calls = calls.append(one_row)
            values = []
            cols = []
        except ValueError as e:
            print(cols, values)
            print("Value Error", e)
            print(e)
            lineno = str(int(lead) + 2)
            строки_с_ошибками[int(lead) + 2] = leads[lead]
            print("Ошибка в строке " + lineno + " исходных данных.\n", leads[lead])
        except AssertionError as e:

            print("Assertion Error", e)
            lineno = str(int(lead) + 2)
            строки_с_ошибками[int(lead) + 2] = leads[lead]
            print("Ошибка в строке " + lineno + " исходных данных.\n", leads[lead])

    calls["lead_id"] = calls["lead_id"].map(int)
    calls = calls.sort_values(by="lead_id")
    calls = calls.set_index("lead_id")
    return calls


# In[ ]:




# In[62]:

def join_cols(source_df, cols):
    to_col = cols[0]
    for c in cols[1:]:
        source_df[to_col].fillna(source_df[c], inplace=True)

def prepare_for_vikup(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    to_handle = to_handle[to_handle["ActionType_Sell"].notnull()]
    cols_to_merge = ["Matter_Other", "Matter_TV"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)

def prepare_for_prodazha(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    to_handle = to_handle[to_handle["ActionType_Buy"].notnull()]
    cols_to_merge = ["Matter_Other", "Matter_TV"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)


def prepare_for_repare(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    to_handle = to_handle[to_handle["ActionType_Repare"].notnull()]
    cols_to_merge = ["Matter_Tablet", "Matter_Phone"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)

def prepare_for_pawn(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    to_handle = to_handle[to_handle["ActionType_Pawn"].notnull()]
    cols_to_merge = ["Matter_Tablet", "Matter_Phone"]
    join_cols(to_handle, cols_to_merge)
    cols_to_merge = ["Matter_Other", "Matter_TV"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)

def prepare_for_buryatia(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    cols_to_merge = ["Matter_Other", "Matter_TV"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)


def prepare_for_smswhatsapp(source_df, cols_to_include):
    to_handle = source_df.copy(deep=True)
    cols_to_merge = ["Matter_Other", "Matter_TV"]
    join_cols(to_handle, cols_to_merge)
    return df(to_handle, columns=cols_to_include)

def prepare_for_unsorted(source_df):
    to_handle = source_df.copy(deep=True)
    actions = [a for a in to_handle.columns if a.startswith("ActionType")]
    not_existing_action = to_handle[actions[0]].isnull()
    for a in actions[1:]:
        not_existing_action &= to_handle[a].isnull();
    return to_handle[not_existing_action].dropna(axis=1, how="all")


# In[ ]:




# In[63]:

colls_for_vikup_and_buryatia = [
        "CallDate_Date", 
        "CustomerPhone_Phone", 
        "Matter_Notebook", 
        "Matter_Tablet", 
        "Matter_Phone",
        "Matter_Other", 
        "conversation", 
    ] + EMPTY_COLS

colls_for_prodazha = [
    "CallDate_Date", 
    "CustomerPhone_Phone", 
    "Matter_Notebook", 
    "Matter_Tablet", 
    "Matter_Phone",
    "Matter_TV",
    "Matter_Other",
    "conversation", 
] + EMPTY_COLS

colls_for_repare = [
    "CallDate_Date", 
    "CustomerPhone_Phone", 
    "Matter_Notebook", 
    "Matter_Tablet", 
    "conversation",
    "Разговор",
    "Цена клиента",
    "Наша цена",
    "Решение клиента"
]

colls_for_pawn = [
    "CallDate_Date", 
    "CustomerPhone_Phone", 
    "Matter_Notebook", 
    "Matter_Tablet",
    "Matter_Other",
    "conversation",
    "Комплектация",
    "Цена клиента",
    "Наша цена",
    "Решение клиента"
]


# In[ ]:




# In[64]:

def make_excel():
    calls = make_common_table()
    calls.to_excel(DEBUG_EXCEL)
    
    
    for_ykt = calls[calls["CustomerPlace_Buryatia"].isnull() &
                      calls["Communication_SMS"].isnull() & 
                      calls["Communication_WhatsApp"].isnull()
                      ]

    for_buryatia = calls[calls["CustomerPlace_Buryatia"].notnull() &
                          calls["Communication_SMS"].isnull() & 
                          calls["Communication_WhatsApp"].isnull()
                          ]

    for_whatsapp = calls[calls["Communication_SMS"].notnull() | 
                          calls["Communication_WhatsApp"].notnull()
                          ]

    writer = pd.ExcelWriter(OUTPUT_EXCEL)

    vikup = prepare_for_vikup(for_ykt, colls_for_vikup_and_buryatia)
    prodazha = prepare_for_prodazha(for_ykt, colls_for_prodazha)
    remont = prepare_for_repare(for_ykt, colls_for_repare)
    lombard = prepare_for_pawn(for_ykt, colls_for_pawn)
    buryatia = prepare_for_buryatia(for_buryatia, colls_for_vikup_and_buryatia)
    smswhatsapp = prepare_for_smswhatsapp(for_whatsapp, colls_for_vikup_and_buryatia)
    without_action = prepare_for_unsorted(calls)
    
    vikup.to_excel(writer, sheet_name = "Выкуп", index=False)
    prodazha.to_excel(writer, sheet_name = "Продажа", index=False)
    remont.to_excel(writer, sheet_name = "Ремонт", index=False)
    lombard.to_excel(writer, sheet_name = "Ломбард", index=False)
    buryatia.to_excel(writer, sheet_name = "Бурятия", index=False)
    smswhatsapp.to_excel(writer, sheet_name = "smswhatsapp", index=False)
    without_action.to_excel(writer, sheet_name = "Действие не определено", index=False)
    writer.save()


# In[65]:

def report():
    num_lines = sum(1 for line in open(PREPROCESSED_INPUT))
    percent_of_handled = len(calls) / num_lines * 100
    print("Процент успешно обработанных данных:", percent_of_handled)
    print("Строки с ошибками (необработано): ", строки_с_ошибками)


# In[66]:

def classify():
    make_excel()
    #report()


# In[67]:

if __name__ == "__main__":
    classify()


# In[ ]:



