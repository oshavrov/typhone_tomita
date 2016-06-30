#encoding "utf8"

NotebookWord -> Word<kwtype="ноутбук_слово">;

NotebookVendorRus -> Word<kwtype="ноутбук_производитель_рус">;
NotebookVendorEng -> Word<kwtype="ноутбук_производитель_англ">;
NV -> NotebookVendorRus | NotebookVendorEng;
NotebookVendor -> NV;

NotebookModel -> UnknownPOS* AnyWord<wff=/\w\d.*\s/>;

NotebookUserDefinedName -> AnyWord<kwtype="ноутбук_пользовательское_название">;

S -> NotebookWord (NotebookVendor+) (NotebookModel);
S -> (NotebookWord) NotebookVendor (NotebookModel) (NotebookWord);
S -> (NotebookWord) NotebookUserDefinedName (NotebookWord);