#encoding "utf8"

PhoneWord -> AnyWord<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;
PhoneUserDefinedName -> AnyWord<kwtype='**телефон_пользовательское_название**'> | Iphones;

Iphones -> AnyWord<wff=/([Аа]йфон|[Ii]phone)\d?\w?/> (AnyWord<wff=/[4-6]\w?/>);

SamsungGalaxyModels -> AnyWord<wff=/(сгс|sgs|cgc|([галeэ]{1,2}кси))\d?\w*/> (Word<wff=/[м]/>);
SamsungASeriesModels -> AnyWord<wff=/[AaАа]\d/>;
SamsungModels -> SamsungGalaxyModels;
SamsungModels -> SamsungASeriesModels; 
SamsungModels -> AnyWord<kwtype="самсунг_модели_из_файла">;
PhoneModel -> SamsungModels;
PhoneModel -> UnknownPOS* AnyWord<wff=/(\d{1,5})|(\w\d{1,5})/>;

S -> Iphones;
S -> SamsungModels;
S -> PhoneWord (PhoneVendor) (PhoneModel);
S -> (PhoneWord) PhoneVendor (PhoneModel);
S -> (PhoneVendor) (PhoneModel) PhoneWord;
S -> PhoneUserDefinedName (PhoneVendor) (PhoneWord);
S -> (PhoneVendor) PhoneUserDefinedName;
S -> (PhoneWord) (PhoneVendor) (PhoneModel) PhoneUserDefinedName (PhoneWord);
S -> PhoneUserDefinedName;