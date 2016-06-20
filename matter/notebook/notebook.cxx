#encoding "utf8"

NotebookWord -> Word<kwtype="ноутбук_слово"> interp(Notebook.Word);

NotebookVendorRus -> Word<kwtype="ноутбук_производитель_рус">;
NotebookVendorEng -> Word<kwtype="ноутбук_производитель_англ">;
NV -> NotebookVendorRus | NotebookVendorEng;
NotebookVendor -> NV interp(Notebook.Vendor);

NotebookModel -> UnknownPOS* AnyWord<wff=/\w\d.*\s/>;

NotebookUserDefinedName -> AnyWord<kwtype="ноутбук_пользовательское_название"> interp(Notebook.UserDefinedName);

S -> NotebookWord (NotebookVendor) (NotebookModel interp(Notebook.Model));
S -> (NotebookWord) NotebookVendor (NotebookModel interp(Notebook.Model));
S -> NotebookUserDefinedName (NotebookWord);