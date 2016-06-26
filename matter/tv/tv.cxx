#encoding "utf8"

TVWord -> Word<kwtype="телевизор_слово">;

TVVendorRus -> Word<kwtype="телевизор_производитель_рус">;
TVVendorEng -> Word<kwtype="телевизор_производитель_англ">;
TVVendor -> TVVendorRus | TVVendorEng;

TVModel -> UnknownPOS* AnyWord<wff=/(\d+)|(\w\d)|(\d\w)/>;

TVUserDefinedName -> AnyWord<kwtype='**телевизор_пользовательское_название**'>;

S -> TVWord (TVVendor) (TVModel) (TVWord);
S -> (TVWord) TVVendor (TVModel) (TVWord);
S -> TVUserDefinedName (TVVendor) (TVWord);
S -> TVUserDefinedName;
S -> (TVWord) TVUserDefinedName;
