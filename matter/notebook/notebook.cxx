#encoding "utf8"

NotebookWord -> Word<kwtype="ноутбук_слово">;

NotebookVendorRus -> Word<kwtype="ноутбук_производитель_рус">;
NotebookVendorEng -> Word<kwtype="ноутбук_производитель_англ">;
NV -> NotebookVendorRus | NotebookVendorEng;
NotebookVendor -> NV;

NotebookModel -> UnknownPOS* AnyWord<wff=/(\w\d.*)/> (AnyWord<wff=/i\d/>);

NotebookUserDefinedName -> AnyWord<kwtype="ноутбук_пользовательское_название">;

NotebookProcessor -> 'i3' | 'i5' | 'i7' | 'pentium' | 'celeron';
NotebookVideo -> AnyWord<wff=/[456789]\d0[mMмМ]?/>;
Specifications -> NotebookProcessor NotebookVideo;

S -> NotebookWord (NotebookVendor+) (NotebookModel);
S -> (NotebookWord) NotebookVendor (NotebookModel) (NotebookWord);
S -> (NotebookWord) NotebookUserDefinedName (NotebookWord);
S -> NotebookVendor Specifications;
S -> NotebookVendor NotebookWord;
S -> NotebookWord NotebookVendor;
S -> NotebookWord NotebookVendor NotebookModel;
