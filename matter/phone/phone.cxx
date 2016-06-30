#encoding "utf8"

Iphones -> AnyWord<wff=/(айфон|iphone)\s?\d\w{0,2}/>;

PhoneWord -> AnyWord<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;

PhoneModel -> UnknownPOS* AnyWord<wff=/(\d{1,5})|(\w\d{1,5})|(\d{1,5}\w)/>;

PhoneUserDefinedName -> AnyWord<kwtype='**телефон_пользовательское_название**'> | Iphones;

S -> PhoneWord (PhoneVendor) (PhoneModel) (PhoneWord);
S -> (PhoneWord) PhoneVendor (PhoneModel) (PhoneWord);
S -> PhoneUserDefinedName (PhoneVendor) (PhoneWord);
S -> (PhoneVendor) PhoneUserDefinedName;
S -> (PhoneWord) (PhoneVendor) (PhoneModel) PhoneUserDefinedName (PhoneWord);
S -> PhoneUserDefinedName;
