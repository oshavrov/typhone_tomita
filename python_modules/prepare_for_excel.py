from python_modules.constants import *
from pandas import DataFrame as df

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

def prepare_for_unsorted(source_df, notExistionType):
    to_handle = source_df.copy(deep=True)
    actions = [a for a in to_handle.columns if a.startswith(notExistionType)]
    not_existing_action = to_handle[actions[0]].isnull()
    for a in actions[1:]:
        not_existing_action &= to_handle[a].isnull();
    return to_handle[not_existing_action].dropna(axis=1, how="all")

