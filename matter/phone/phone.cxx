#encoding "utf8"

PhoneWord -> Word<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;

PhoneModel -> UnknownPOS* AnyWord<wff=/(\d+)|(\w\d)|(\d\w)/>;

PhoneUserDefinedName -> AnyWord<kwtype='**телефон_пользовательское_название**'>;

S -> PhoneWord (PhoneVendor) (PhoneModel) (PhoneWord);
S -> (PhoneWord) PhoneVendor (PhoneModel) (PhoneWord);
S -> PhoneUserDefinedName (PhoneVendor) (PhoneWord);
S -> (PhoneVendor) PhoneUserDefinedName;
S -> PhoneUserDefinedName;